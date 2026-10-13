"""
Stages of war_archives_20240725_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from campaign.event_20240725_cn.stages import STAGES as ARCHIVED
from module.campaign.stage import borrowed


STAGES = {
    **borrowed(ARCHIVED, ['ht1', 'ht2', 'ht3', 't1', 't2', 't3']),
}
