import os
import time

import psutil
import pytest

import module.config.scheduler_state as scheduler_state
from module.config.scheduler_state import is_process_alive, read_scheduler_state, remove_scheduler_state, \
    write_scheduler_state


@pytest.fixture
def state_file(tmp_path, monkeypatch):
    file = tmp_path / 'alas.running'
    monkeypatch.setattr(scheduler_state, 'filepath_running', lambda config_name: str(file))
    return file


def test_running_scheduler_tells_its_task(state_file):
    write_scheduler_state('alas', task='Event2')

    assert read_scheduler_state('alas') == {'pid': os.getpid(), 'task': 'Event2', 'paused': False}


def test_paused_scheduler_tells_it_holds(state_file):
    write_scheduler_state('alas', paused=True)

    assert read_scheduler_state('alas') == {'pid': os.getpid(), 'task': None, 'paused': True}


def test_no_scheduler_once_the_state_is_removed(state_file):
    write_scheduler_state('alas', task='Event2')
    remove_scheduler_state('alas')

    assert not state_file.exists()
    assert read_scheduler_state('alas') is None
    # Removing twice is fine
    remove_scheduler_state('alas')


def test_state_of_a_killed_scheduler_is_ignored(state_file):
    state_file.write_text('{"pid": 99999999, "task": "Event2", "paused": false}')

    assert read_scheduler_state('alas') is None


@pytest.mark.parametrize('content', ['', 'not json', '{"task": "Event2"}', '{"pid": "abc"}'])
def test_invalid_state_is_ignored(state_file, content):
    state_file.write_text(content)

    assert read_scheduler_state('alas') is None


def test_writing_never_stops_the_scheduler(state_file, monkeypatch):
    def atomic_write(file, data):
        raise PermissionError('Access is denied')

    monkeypatch.setattr(scheduler_state, 'atomic_write', atomic_write)

    write_scheduler_state('alas', task='Event2')

    assert read_scheduler_state('alas') is None


def test_process_alive():
    assert is_process_alive(os.getpid(), started_before=time.time()) is True
    assert is_process_alive(99999999, started_before=time.time()) is False


def test_process_with_the_pid_of_a_gone_scheduler_is_another_one():
    created = psutil.Process(os.getpid()).create_time()

    # The state was written long before this process started
    assert is_process_alive(os.getpid(), started_before=created - 60) is False
