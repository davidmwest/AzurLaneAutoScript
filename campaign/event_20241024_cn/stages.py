"""
Stages of event_20241024_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']

STAGES = {
    't2': Stage(
        base=BASE,
        map=dict(
            name='T2',
            shape='I8',
            camera_data=['D3', 'D6', 'F3', 'F6'],
            camera_data_spawn_point=['F2'],
            map_data="""
                -- ++ ++ ++ ++ ++ SP -- SP
                -- ME -- ++ ++ ++ -- -- --
                -- -- ME ++ ++ ++ -- MS --
                ME -- -- -- MB -- MS ++ MS
                ++ ++ ++ -- -- -- -- Me --
                -- -- ME -- -- ++ Me __ Me
                -- ++ ++ ME -- -- -- -- --
                -- -- ME -- -- ME ++ ME --
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
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['MaryCeleste', 'Amity', 'Portsmouth'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.246, 1.269),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.205, 1.227),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.17, 1.191),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    't6': Stage(
        base=BASE,
        map=dict(
            name='T6',
            shape='K10',
            camera_data=['E3', 'G3'],
            camera_data_spawn_point=['F4'],
            map_data="""
                ++ ++ -- -- ++ ++ ++ -- -- ++ ++
                ++ -- -- ME -- MB -- ME -- -- ++
                -- -- ME -- MS -- MS -- ME -- --
                -- ME -- ME -- MS -- ME -- ME --
                -- -- ME -- -- __ -- -- ME -- --
                ++ -- -- -- SP -- SP -- -- -- ++
                -- ++ ++ ++ ++ -- ++ ++ ++ ++ --
                -- ++ ++ ++ ++ ++ ++ ++ ++ ++ --
                -- ++ ++ ++ ++ -- ++ ++ ++ ++ --
                -- -- -- ++ -- -- -- ++ -- -- --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 10, 'siren': 3},
                {'battle': 1},
                {'battle': 2},
                {'battle': 3},
                {'battle': 4},
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='t4',
        config=dict(
            MAP_SIREN_TEMPLATE=['fengfanhaigu03'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='top',
            MAP_SWIPE_MULTIPLY=(1.124, 1.145),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.087, 1.107),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.055, 1.074),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default'],
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
}
