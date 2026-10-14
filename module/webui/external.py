"""
Show a scheduler that was started outside the GUI, from a terminal or a script:
its status, and its log by following its log file.
"""
import os
import re

from rich.rule import Rule
from rich.text import Text

# Status of a scheduler, as in AlasGUI.set_status()
STATUS_RUNNING = 1
STATUS_INACTIVE = 2
STATUS_RUNNING_OUTSIDE = 5
STATUS_PAUSED = 6
STATUS_PAUSING = 7


def scheduler_status(alive, scheduler, pause_requested):
    """
    Args:
        alive (bool): If the GUI runs a scheduler of this config.
        scheduler (dict): What the running scheduler of this config tells, wherever it was started from,
            None if none tells anything. See module/config/scheduler_state.py
        pause_requested (bool): If the pause file exists.

    Returns:
        int: A status, or None if no scheduler is running.
    """
    if not alive and scheduler is None:
        return None
    if pause_requested:
        # Only the scheduler knows if it holds already or still finishes a task
        if scheduler is not None and scheduler.get('paused'):
            return STATUS_PAUSED
        return STATUS_PAUSING
    if alive:
        return STATUS_RUNNING
    return STATUS_RUNNING_OUTSIDE


def latest_log_file(config_name, folder='./log'):
    """
    The scheduler names its log file after the day it started, ./log/<date>_<config_name>.txt,
    and keeps writing it after midnight.

    Returns:
        str: Path to the log file of a config written last, None if there is none.
    """
    suffix = f'_{config_name}.txt'
    try:
        files = [os.path.join(folder, f) for f in os.listdir(folder)
                 if f.endswith(suffix) and re.match(r'^\d{4}-\d{2}-\d{2}_', f)]
    except FileNotFoundError:
        return None
    if not files:
        return None
    return max(files, key=lambda f: (os.path.getmtime(f), f))


class LogFileFollower:
    """
    Read the end of a log file, then the lines written to it after that, like `tail -f`.
    """

    def __init__(self, file, tail=200, tail_bytes=65536):
        """
        Args:
            file (str):
            tail (int): Number of lines already in the file to show at first.
            tail_bytes (int): Bytes to read from the end of the file at most to find them.
        """
        self.file = file
        self.tail = tail
        self.tail_bytes = tail_bytes
        # Byte offset where the next read starts, None before the first read
        self.position = None
        # A line still being written
        self.partial = b''

    def read(self):
        """
        Returns:
            list[str]: Lines written since the last read, the last lines of the file at the first read.
        """
        try:
            with open(self.file, 'rb') as f:
                f.seek(0, os.SEEK_END)
                size = f.tell()
                if self.position is None:
                    start = max(size - self.tail_bytes, 0)
                    f.seek(start)
                    data = f.read()
                    if start > 0:
                        # Drop the line cut in the middle
                        data = data[data.find(b'\n') + 1:]
                    self.position = size
                    lines = self._split(data)
                    return lines[-self.tail:]
                if size < self.position:
                    # Truncated or replaced, read it again from the beginning
                    self.position = 0
                    self.partial = b''
                f.seek(self.position)
                data = f.read()
                self.position += len(data)
                return self._split(data)
        except FileNotFoundError:
            return []

    def _split(self, data):
        data = self.partial + data
        lines = data.split(b'\n')
        self.partial = lines.pop()
        return [line.decode('utf-8', errors='replace').rstrip('\r') for line in lines]


# 2026-10-14 05:49:34.954 | INFO | BATTLE_0
LOG_LINE = re.compile(r'^\d{4}-\d{2}-\d{2} (\d{2}:\d{2}:\d{2}\.\d{3}) \| (\w+) \| (.*)$')
# ──────── BATTLE_0 ────────, or a rule without a title
RULE_LINE = re.compile(r'^([─═])\1+(?: (.*?) \1+)?$')
# The title between two rules of a task, centered in the file
TITLE_LINE = re.compile(r'^ {30,}(\S.*)$')
LEVEL_STYLE = {
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold red',
}


def log_line_renderable(line):
    """
    Turn a line of the log file into something like what the GUI shows for its own scheduler.

    Args:
        line (str):

    Returns:
        str, Text, Rule:
    """
    line = line.rstrip()
    rule = RULE_LINE.match(line)
    if rule:
        character, title = rule.groups()
        return Rule(title or '', characters=character)
    log = LOG_LINE.match(line)
    if log:
        time, level, message = log.groups()
        style = LEVEL_STYLE.get(level)
        if style:
            return Text(f'{time} │ {message}', style=style)
        return f'{time} │ {message}'
    title = TITLE_LINE.match(line)
    if title:
        return Text(title.group(1), style='bold', justify='center')
    return line
