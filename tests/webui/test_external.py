import os

import pytest
from rich.rule import Rule
from rich.text import Text

from module.webui.external import LogFileFollower, STATUS_PAUSED, STATUS_PAUSING, STATUS_RUNNING, \
    STATUS_RUNNING_OUTSIDE, latest_log_file, log_line_renderable, scheduler_status

RUNNING = {'pid': 1234, 'task': 'Event2', 'paused': False}
HOLDING = {'pid': 1234, 'task': None, 'paused': True}


@pytest.mark.parametrize('alive, scheduler, pause_requested, status', [
    # Nothing runs
    (False, None, False, None),
    (False, None, True, None),
    # Started from the GUI
    (True, None, False, STATUS_RUNNING),
    (True, RUNNING, False, STATUS_RUNNING),
    (True, RUNNING, True, STATUS_PAUSING),
    (True, HOLDING, True, STATUS_PAUSED),
    # Started from a terminal or a script
    (False, RUNNING, False, STATUS_RUNNING_OUTSIDE),
    (False, RUNNING, True, STATUS_PAUSING),
    (False, HOLDING, True, STATUS_PAUSED),
])
def test_scheduler_status(alive, scheduler, pause_requested, status):
    assert scheduler_status(alive, scheduler, pause_requested) == status


def test_latest_log_file_of_a_config(tmp_path):
    for second, name in enumerate(['2026-10-12_alas.txt', '2026-10-14_alas.txt', '2026-10-13_alas.txt',
                                   '2026-10-15_alas2.txt', '2026-10-16_gui.txt', 'notes_alas.txt']):
        file = tmp_path / name
        file.write_text('')
        os.utime(str(file), (1000 + second, 1000 + second))

    # A scheduler started on the 13th and still running writes the file of the 13th
    assert latest_log_file('alas', folder=str(tmp_path)) == str(tmp_path / '2026-10-13_alas.txt')
    assert latest_log_file('alas3', folder=str(tmp_path)) is None
    assert latest_log_file('alas', folder=str(tmp_path / 'missing')) is None


def write(file, text):
    with open(file, 'ab') as f:
        f.write(text.encode('utf-8'))


def test_follower_shows_the_end_of_the_file_then_new_lines(tmp_path):
    file = tmp_path / 'log.txt'
    write(file, ''.join(f'line {i}\n' for i in range(10)))
    follower = LogFileFollower(str(file), tail=3)

    assert follower.read() == ['line 7', 'line 8', 'line 9']
    assert follower.read() == []

    write(file, 'line 10\nline 1')
    assert follower.read() == ['line 10']
    # The rest of a line being written
    write(file, '1\n')
    assert follower.read() == ['line 11']


def test_follower_skips_a_line_cut_by_the_tail(tmp_path):
    file = tmp_path / 'log.txt'
    write(file, 'a long first line\nsecond\nthird\n')

    # Starts in "a long first line"
    assert LogFileFollower(str(file), tail_bytes=15).read() == ['second', 'third']
    # Starts in "second"
    assert LogFileFollower(str(file), tail_bytes=10).read() == ['third']


def test_follower_reads_a_file_written_again_from_the_beginning(tmp_path):
    file = tmp_path / 'log.txt'
    write(file, 'old line one\nold line two\n')
    follower = LogFileFollower(str(file))
    follower.read()

    file.write_bytes('new\n'.encode('utf-8'))
    assert follower.read() == ['new']


def test_follower_of_a_missing_file(tmp_path):
    assert LogFileFollower(str(tmp_path / 'missing.txt')).read() == []


def test_follower_keeps_windows_line_endings_and_utf8(tmp_path):
    file = tmp_path / 'log.txt'
    write(file, 'Waiting for ★\r\n')

    assert LogFileFollower(str(file)).read() == ['Waiting for ★']


def test_log_line_of_info():
    line = '2026-10-14 05:49:34.954 | INFO | Auto search combat loading                            '

    assert log_line_renderable(line) == '05:49:34.954 │ Auto search combat loading'


def test_log_line_of_warning_is_colored():
    renderable = log_line_renderable('2026-10-14 05:42:21.411 | WARNING | Wait too long')

    assert isinstance(renderable, Text)
    assert renderable.plain == '05:42:21.411 │ Wait too long'
    assert renderable.style == 'yellow'


def test_log_line_of_a_rule_with_title():
    renderable = log_line_renderable('─' * 54 + ' BATTLE_0 ' + '─' * 55)

    assert isinstance(renderable, Rule)
    assert renderable.title == 'BATTLE_0'
    assert renderable.characters == '─'


def test_log_line_of_a_task_title():
    rule = log_line_renderable('═' * 119)
    title = log_line_renderable(' ' * 56 + 'EVENTA')

    assert isinstance(rule, Rule)
    assert rule.title == ''
    assert rule.characters == '═'
    assert isinstance(title, Text)
    assert title.plain == 'EVENTA'


def test_log_line_of_a_wrapped_message_is_kept():
    line = "'AUTO_SEARCH_MAP_OPTION_OFF', 'STORY_SKIP_3', 'POPUP_CANCEL', 'NEW_SHIP'"
    trace = '              alas.py L714 <module>'

    assert log_line_renderable(line) == line
    assert log_line_renderable(trace) == trace
