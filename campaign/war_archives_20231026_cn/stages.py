"""
Stages of war_archives_20231026_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from campaign.event_20231026_cn.stages import STAGES as ARCHIVED
from module.campaign.stage import borrowed


STAGES = {
    **borrowed(ARCHIVED, ['t1', 't2', 't3', 't4', 't5', 't6']),
}
