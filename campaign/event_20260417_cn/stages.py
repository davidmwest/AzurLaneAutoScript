"""
Stages of event_20260417_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']

STAGES = {
    'sp2': Stage(
        base=BASE,
        map=dict(
            name='SP2',
            shape='I8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['D2', 'E2'],
            map_data="""
                ++ -- SP -- SP -- ++ -- --
                ME -- -- -- -- -- -- ME --
                -- ME -- MS __ -- -- -- ++
                ME -- Me ++ -- Me -- ME --
                ++ -- ++ ++ -- ++ ++ -- --
                ME -- -- Me -- ++ ++ ME --
                -- MB -- -- -- -- -- -- --
                MB -- -- ++ ++ ++ -- ME --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 1},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['FuShunG'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.234, 1.257),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.193, 1.215),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.158, 1.179),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'sp4': Stage(
        base=BASE,
        map=dict(
            name='SP4',
            shape='I8',
            camera_data=['D3', 'D6', 'F3', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- -- -- ++ ++ ++ -- -- --
                -- ++ ME -- MB -- ME ++ --
                -- ME -- -- -- -- -- ME --
                -- ++ ++ Me -- Me ++ ++ --
                -- ++ ++ MS -- MS ++ ++ --
                -- ME Me -- __ -- Me ME --
                ME -- -- -- -- -- -- -- ME
                ++ ++ ++ SP -- SP ++ ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Cheshire', 'Nakhimov'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.084, 1.104),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.048, 1.067),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.017, 1.036),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
