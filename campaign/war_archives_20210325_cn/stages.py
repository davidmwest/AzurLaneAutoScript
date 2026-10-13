"""
Stages of war_archives_20210325_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from campaign.event_20210325_cn.stages import STAGES as ARCHIVED
from module.campaign.stage import borrowed


STAGES = {
    **borrowed(ARCHIVED, [
        'a1',
        'a2',
        'a3',
        'as1',
        'as2',
        'b1',
        'b2',
        'b3',
        'bs1',
        'bs2',
        'c1',
        'c2',
        'c3',
        'cs1',
        'cs2',
        'd1',
        'd2',
        'd3',
        'ds1',
        'ds2',
    ]),
}
