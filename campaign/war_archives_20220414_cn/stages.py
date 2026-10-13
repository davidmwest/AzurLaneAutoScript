"""
Stages of war_archives_20220414_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from campaign.event_20220414_cn.stages import STAGES as ARCHIVED
from module.campaign.stage import borrowed


STAGES = {
    **borrowed(ARCHIVED, ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3', 'd1', 'd2', 'd3'], base='..campaign_war_archives.campaign_base:CampaignBase'),
}
