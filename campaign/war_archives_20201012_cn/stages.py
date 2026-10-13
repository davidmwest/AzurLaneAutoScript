"""
Stages of war_archives_20201012_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '..campaign_war_archives.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']

STAGES = {
    'sp1': Stage(
        base=BASE,
        map=dict(
            name='SP1',
            shape='I6',
            camera_data=['D2', 'D4', 'F2', 'F4'],
            camera_data_spawn_point=['D4'],
            map_data="""
                ++ ++ ME -- -- -- ME ++ --
                ++ ++ Me -- ME MB -- -- Me
                -- -- -- -- __ ++ ME -- ME
                SP -- -- ME MB ++ ME -- --
                -- -- ME ++ -- -- -- -- Me
                SP -- -- -- -- Me ++ ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 231),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (231, 255),
                'prominence': 10,
                'distance': 50,
                'width': (0, 10),
                'wlen': 1000,
            },
            MAP_SWIPE_MULTIPLY=(1.16, 1.182),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.122, 1.143),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.089, 1.109),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'sp2': Stage(
        base=BASE,
        map=dict(
            name='SP2',
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['D2', 'E2'],
            map_data="""
                -- ME -- SP SP -- -- ME
                ME ++ -- -- -- -- Me --
                -- -- -- -- ++ ++ ++ --
                -- -- Me -- -- -- ME --
                Me -- ++ ++ ME __ -- MB
                ME -- -- ++ ME -- Me ++
                ++ ME -- ME -- MB -- ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 4},
                {'battle': 1, 'enemy': 3},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'sp3': Stage(
        base=BASE,
        map=dict(
            name='SP3',
            shape='I6',
            camera_data=['D2', 'D4', 'F2', 'F4'],
            camera_data_spawn_point=['F2', 'D2'],
            map_data="""
                ++ ++ Me ++ ++ ++ ME Me ME
                ++ ++ -- -- MB -- -- -- --
                -- ME -- SP MB SP -- ++ ME
                -- Me -- -- __ -- -- ME --
                ++ ME -- Me ++ Me -- ++ ++
                ++ ME -- ME -- ME -- Me ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 4},
                {'battle': 1, 'enemy': 3},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
