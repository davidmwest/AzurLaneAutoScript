"""
Stages of event_20231026_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']
PLAN_2 = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default']

STAGES = {
    't1': Stage(
        base=BASE,
        map=dict(
            name='T1',
            shape='I8',
            camera_data=['E2', 'E5'],
            camera_data_spawn_point=['E5'],
            map_data="""
                ++ -- -- -- -- -- -- ++ MB
                -- ME -- -- ME -- ME -- --
                -- -- ME ++ ++ -- -- -- --
                -- -- -- Me ++ Me -- ME ++
                -- ME -- -- MS -- -- -- ++
                -- ++ ++ -- __ -- Me -- --
                -- ME -- SP -- SP -- ++ --
                -- -- -- -- -- -- -- -- --
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
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['DD'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 222),
                'width': (1.5, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (222, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_EDGE_COLOR_RANGE=(0, 33),
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
            MAP_SWIPE_MULTIPLY=(1.067, 1.087),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.032, 1.051),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.002, 1.02),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    't2': Stage(
        base=BASE,
        map=dict(
            name='T2',
            shape='I8',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['F2'],
            map_data="""
                -- -- -- ++ ++ -- -- SP --
                -- ME -- ++ ++ MS -- -- SP
                ME -- ME -- MB -- __ -- --
                ++ -- ++ Me -- Me -- MS --
                ME -- -- -- -- ++ ++ ++ --
                -- ME -- ME -- -- Me -- --
                -- ++ ++ -- -- ME ++ ME --
                -- -- -- -- -- -- -- -- --
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
            MAP_SWIPE_MULTIPLY=(1.223, 1.246),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.183, 1.205),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.149, 1.169),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    't3': Stage(
        base=BASE,
        map=dict(
            name='T3',
            shape='J8',
            camera_data=['D3', 'D6', 'G3', 'G6'],
            camera_data_spawn_point=['D3'],
            map_data="""
                ++ ++ -- -- -- -- ++ ++ -- --
                MB ++ -- SP -- -- -- -- ME --
                -- -- SP -- -- MS ++ -- -- ME
                Me -- -- -- MS -- Me -- ME --
                -- Me ++ ++ -- ++ ++ -- -- ++
                ME -- -- Me __ Me -- -- Me --
                ++ ME -- -- -- -- -- ME ++ ++
                -- -- ME ++ ++ ++ ME -- ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.218, 1.241),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.178, 1.2),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.144, 1.164),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    't4': Stage(
        base=BASE,
        map=dict(
            name='T4',
            shape='J8',
            camera_data=['D3', 'G3', 'G6'],
            camera_data_spawn_point=['G3'],
            map_data="""
                ++ ++ -- -- -- -- -- -- ++ ++
                -- ME -- Me ++ -- -- SP MB ++
                ME -- -- -- -- MS -- -- SP --
                -- ME -- ME ME -- __ -- -- --
                -- -- ++ ++ -- Me -- MS -- Me
                ++ ++ ++ -- ME -- -- -- ++ --
                ++ ++ ++ ++ ME -- ME -- Me --
                ++ ++ ++ ++ -- ME -- ++ ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
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
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.205, 1.227),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.165, 1.187),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.131, 1.151),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    't5': Stage(
        base=BASE,
        map=dict(
            name='T5',
            shape='I10',
            camera_data=['D3', 'D5', 'D7', 'F3', 'F5', 'F7'],
            camera_data_spawn_point=['E8'],
            map_data="""
                ++ ++ ++ ++ ++ ++ ++ ++ ++
                -- ME -- ++ ++ ++ -- ME --
                -- -- ME ++ ++ ++ ME -- --
                ME -- -- ++ MB ++ -- -- ME
                -- ME -- -- -- -- -- ME --
                ++ -- ME Me -- Me ME -- ++
                -- Me ++ ++ MS ++ ++ Me --
                ME -- MS -- __ -- MS -- ME
                -- Me -- -- -- -- -- Me --
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
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2, 'siren': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
            MAP_SWIPE_MULTIPLY=(0.991, 1.009),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.958, 0.976),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.93, 0.947),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    't6': Stage(
        base=BASE,
        map=dict(
            name='T6',
            shape='I10',
            camera_data=['E5', 'E8'],
            camera_data_spawn_point=['E8'],
            map_data="""
                -- -- -- -- -- -- -- -- --
                -- -- -- -- -- -- -- -- --
                -- -- ++ ++ ++ ++ ++ -- --
                -- -- ++ MS -- MS ++ -- --
                -- -- ++ -- MB -- ++ -- --
                -- -- ++ -- MS -- ++ -- --
                -- -- ++ ++ -- ++ ++ -- --
                -- ME -- SP -- SP -- ME --
                -- Me -- -- __ -- -- Me --
                -- -- ME ME -- ME ME -- --
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
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 8, 'siren': 3},
                {'battle': 1},
                {'battle': 2},
                {'battle': 3},
                {'battle': 4},
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['BB', 'CV'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 238),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (238, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_EDGE_COLOR_RANGE=(0, 17),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=280,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(0.987, 1.006),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.955, 0.973),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.927, 0.944),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
}
