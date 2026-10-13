from types import SimpleNamespace

import pytest

from module.handler.fast_forward import FastForwardHandler


def make_handler(stage_increase_ab, event='event_20250912_cn'):
    config = SimpleNamespace(STAGE_INCREASE_AB=stage_increase_ab, STAGE_INCREASE_CUSTOM=None, Campaign_Event=event)
    return SimpleNamespace(config=config, STAGE_INCREASE=FastForwardHandler.STAGE_INCREASE)


@pytest.mark.parametrize('stage, following', [
    ('A3', 'B1'),
    ('B3', 'B3'),
    ('C1', 'C2'),
    ('C3', 'D1'),
    ('D2', 'D3'),
    ('D3', 'D3'),
])
def test_stage_increase_continues_into_the_second_part(stage, following):
    handler = make_handler(stage_increase_ab=True)

    assert FastForwardHandler.campaign_name_increase(handler, stage) == following


@pytest.mark.parametrize('stage, following', [
    ('A3', 'A3'),
    ('C2', 'C3'),
    ('C3', 'C3'),
])
def test_stage_increase_stays_in_its_chapter_without_the_ab_chain(stage, following):
    handler = make_handler(stage_increase_ab=False)

    assert FastForwardHandler.campaign_name_increase(handler, stage) == following
