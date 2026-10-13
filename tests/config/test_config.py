import json
from datetime import datetime, timedelta
from types import SimpleNamespace

import pytest

from module.config.config import AzurLaneConfig

DAILIES = ['Commission', 'Research', 'Reward']


def make_config(enabled):
    now = datetime.now().replace(microsecond=0)
    data = {task: {'Scheduler': {'Enable': enabled, 'NextRun': now}} for task in DAILIES}
    config = SimpleNamespace(data=data, modified={}, overridden={}, args={task: {} for task in DAILIES})
    config.is_task_enabled = lambda task: data[task]['Scheduler']['Enable']
    return config


def test_override_leaves_disabled_dailies_disabled():
    config = make_config(enabled=False)

    AzurLaneConfig.override(config)

    assert config.modified == {}
    assert [config.is_task_enabled(task) for task in DAILIES] == [False, False, False]


def test_override_still_pulls_in_a_run_scheduled_too_far_ahead():
    config = make_config(enabled=True)
    config.data['Commission']['Scheduler']['NextRun'] = datetime.now() + timedelta(days=3)

    AzurLaneConfig.override(config)

    assert config.data['Commission']['Scheduler']['NextRun'] <= datetime.now()


@pytest.mark.parametrize('task', DAILIES)
def test_dailies_can_be_switched_off(task):
    with open('./module/config/argument/args.json', encoding='utf-8') as f:
        enable = json.load(f)[task]['Scheduler']['Enable']

    assert enable['type'] == 'checkbox'
    assert enable['value'] is True
    assert False in enable['option']
