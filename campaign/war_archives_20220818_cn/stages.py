"""
Stages of war_archives_20220818_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from campaign.event_20220818_cn.stages import STAGES as ARCHIVED
from module.campaign.stage import borrowed


STAGES = {
    **borrowed(ARCHIVED, ['sp1', 'sp2', 'sp3', 'sp4']),
}
