"""
Stages of war_archives_20200603_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from campaign.event_20200603_cn.stages import STAGES as ARCHIVED
from module.campaign.stage import borrowed


STAGES = {
    **borrowed(ARCHIVED, ['sp1', 'sp2', 'sp3'], base='..campaign_war_archives.campaign_base:CampaignBase'),
}
