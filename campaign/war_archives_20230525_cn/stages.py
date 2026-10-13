"""
Stages of war_archives_20230525_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from campaign.event_20230525_cn.stages import STAGES as ARCHIVED
from module.campaign.stage import borrowed


STAGES = {
    **borrowed(ARCHIVED, ['ht2', 'ht4', 'ht5', 'hts1', 'hts2', 't2', 't4', 't5', 'ts1', 'ts2']),
}
