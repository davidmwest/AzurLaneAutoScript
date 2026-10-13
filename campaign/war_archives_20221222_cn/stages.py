"""
Stages of war_archives_20221222_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from campaign.event_20221222_cn.stages import STAGES as ARCHIVED
from module.campaign.stage import borrowed


STAGES = {
    **borrowed(ARCHIVED, ['a1', 'a2', 'a3', 'b2']),
    **borrowed(ARCHIVED, ['c1', 'c2', 'c3', 'd2'], base='..campaign_war_archives.campaign_base:CampaignBase'),
}
