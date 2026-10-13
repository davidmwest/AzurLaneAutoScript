"""
Stages of event_20240912_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']
PLAN_2 = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default']

STAGES = {
    'a1': Stage(
        base=BASE,
        map=dict(
            name='A1',
            shape='I7',
            camera_data=['D5', 'F2', 'F5'],
            camera_data_spawn_point=['D1'],
            map_data="""
                SP -- SP ++ ++ -- ME -- --
                -- -- -- ++ ++ ME -- MB --
                -- MS -- -- Me -- -- -- ME
                ++ -- MS -- -- -- ME -- --
                -- -- -- -- __ -- ++ ME --
                ME -- Me -- Me -- -- -- Me
                -- ME ++ ++ ++ ME -- ME --
            """,
            weight_data="""
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
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1, 'boss': 1},
                {'battle': 4, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['AmagiMasked'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_CHAPTER_SWITCH_20241219=True,
            MAP_HAS_MODE_SWITCH=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (120, 206),
                'width': (1.5, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (206, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_CANNY_THRESHOLD=(75, 100),
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_SWIPE_MULTIPLY=(1.234, 1.257),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.193, 1.215),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.158, 1.179),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            3: 'clear_boss',
        },
    ),
    'a2': Stage(
        base=BASE,
        map=dict(
            name='A2',
            shape='I8',
            camera_data=['D3', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['F6'],
            map_data="""
                -- -- -- ++ -- -- -- -- --
                ++ ME -- -- ME -- ME ++ --
                ++ -- ME -- -- -- -- -- ME
                -- ME -- -- Me Me -- Me --
                -- -- -- ME ++ ++ -- __ ME
                -- ME -- -- SP ++ MS -- --
                -- ++ Me -- -- -- -- MS --
                MB ++ -- -- SP ++ MS -- ++
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
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=['AmagiMasked'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.07, 1.09),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.035, 1.054),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.005, 1.023),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'a3': Stage(
        base=BASE,
        map=dict(
            name='A3',
            shape='I7',
            camera_data=['E2', 'E5'],
            camera_data_spawn_point=['F3'],
            map_data="""
                -- -- -- -- Me ++ ++ -- --
                ++ ++ ++ ME -- ME ++ Me --
                -- -- ME -- -- MS -- -- SP
                -- MB -- -- ME __ MS -- --
                -- -- ME -- -- MS -- -- SP
                ++ ++ ++ ME -- ME ++ Me --
                -- -- -- -- Me ++ ++ -- --
            """,
            weight_data="""
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
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=['AmagiMasked'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.176, 1.198),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.137, 1.158),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.104, 1.124),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b1': Stage(
        base=BASE,
        map=dict(
            name='B1',
            shape='K8',
            camera_data=['D3', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['E2'],
            map_data="""
                -- ++ ++ ++ SP -- SP ++ -- -- --
                ME -- Me -- -- __ -- -- -- MB --
                -- -- -- -- -- MS -- ++ -- -- --
                ME -- Me ++ MS -- MS ++ ++ ++ ++
                ++ -- -- ++ ++ ME -- -- -- -- --
                ME -- ME -- ME -- -- Me ++ ++ --
                -- -- -- -- -- -- -- Me ++ ++ --
                -- ME -- ME ++ ME -- -- -- -- --
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
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
                {'battle': 5, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Fox'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_CHAPTER_SWITCH_20241219=True,
            MAP_HAS_MODE_SWITCH=True,
            STAGE_ENTRANCE=['half', '20240725'],
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
            MAP_SWIPE_MULTIPLY=(1.222, 1.245),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.182, 1.204),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.148, 1.168),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b2': Stage(
        base=BASE,
        map=dict(
            name='B2',
            shape='K8',
            camera_data=['E2', 'E6', 'H2', 'H6'],
            camera_data_spawn_point=['E2'],
            map_data="""
                -- -- -- ++ SP -- SP ++ ME -- ME
                -- MB -- -- -- __ -- -- -- ME --
                -- -- -- ++ -- MS -- ++ ME -- --
                ++ ++ ++ ++ MS ++ MS ++ ++ ++ --
                -- -- -- -- -- Me -- -- -- -- --
                -- ++ ++ Me -- -- -- ME -- ME --
                -- ++ ++ Me -- Me ++ ++ ME -- ME
                -- -- -- -- ME -- -- ++ -- ++ --
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
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Fox'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.215, 1.238),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.175, 1.197),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.141, 1.161),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'b3': Stage(
        base=BASE,
        map=dict(
            name='B3',
            shape='I9',
            camera_data=['E2', 'E5'],
            camera_data_spawn_point=['E7'],
            map_data="""
                ++ ME -- ME -- ME -- ME ++
                -- -- ME -- MB -- ME -- --
                -- ME -- ME -- ME -- ME --
                -- ++ ++ ++ MS ++ ++ ++ --
                -- Me -- MS __ MS -- Me --
                -- -- -- Me -- Me -- -- --
                ++ ++ -- ++ ++ ++ -- ++ ++
                ++ ++ -- -- -- -- -- ++ ++
                -- -- -- SP -- SP -- -- --
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
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Fox'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.035, 1.055),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.001, 1.019),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.972, 0.989),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c1': Stage(
        base=BASE,
        map=dict(
            name='C1',
            shape='I7',
            camera_data=['D5', 'F2', 'F5'],
            camera_data_spawn_point=['D1'],
            map_data="""
                SP -- SP ++ ++ -- ME -- --
                -- -- -- ++ ++ ME -- MB --
                -- MS -- -- Me -- -- -- ME
                ++ -- MS -- -- -- ME -- --
                -- -- -- -- __ -- ++ ME --
                ME -- Me -- Me -- -- -- Me
                -- ME ++ ++ ++ ME -- ME --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['AmagiMasked'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_CHAPTER_SWITCH_20241219=True,
            MAP_HAS_MODE_SWITCH=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (120, 206),
                'width': (1.5, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (206, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_CANNY_THRESHOLD=(75, 100),
            STAGE_ENTRANCE=['half', '20240725'],
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
    'c2': Stage(
        base=BASE,
        map=dict(
            name='C2',
            shape='I8',
            camera_data=['D3', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['F6'],
            map_data="""
                -- -- -- ++ -- -- -- -- --
                ++ ME -- -- ME -- ME ++ --
                ++ -- ME -- -- -- -- -- ME
                -- ME -- -- Me Me -- Me --
                -- -- -- ME ++ ++ -- __ ME
                -- ME -- -- SP ++ MS -- --
                -- ++ Me -- -- -- -- MS --
                MB ++ -- -- SP ++ MS -- ++
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
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['AmagiMasked'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.062, 1.082),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.027, 1.046),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.997, 1.015),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'c3': Stage(
        base=BASE,
        map=dict(
            name='C3',
            shape='I7',
            camera_data=['E2', 'E5'],
            camera_data_spawn_point=['F3'],
            map_data="""
                -- -- -- -- Me ++ ++ -- --
                ++ ++ ++ ME -- ME ++ Me --
                -- -- ME -- -- MS -- -- SP
                -- MB -- -- ME __ MS -- --
                -- -- ME -- -- MS -- -- SP
                ++ ++ ++ ME -- ME ++ Me --
                -- -- -- -- Me ++ ++ -- --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['AmagiMasked'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.186, 1.208),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.147, 1.168),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.114, 1.134),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd1': Stage(
        base=BASE,
        map=dict(
            name='D1',
            shape='K8',
            camera_data=['D3', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['E2'],
            map_data="""
                -- ++ ++ ++ SP -- SP ++ -- -- --
                ME -- Me -- -- __ -- -- -- MB --
                -- -- -- -- -- MS -- ++ -- -- --
                ME -- Me ++ MS -- MS ++ ++ ++ ++
                ++ -- -- ++ ++ ME -- -- -- -- --
                ME -- ME -- ME -- -- Me ++ ++ --
                -- -- -- -- -- -- -- Me ++ ++ --
                -- ME -- ME ++ ME -- -- -- -- --
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
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Fox'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_CHAPTER_SWITCH_20241219=True,
            MAP_HAS_MODE_SWITCH=True,
            STAGE_ENTRANCE=['half', '20240725'],
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
            MAP_SWIPE_MULTIPLY=(1.222, 1.245),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.182, 1.204),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.148, 1.168),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd2': Stage(
        base=BASE,
        map=dict(
            name='D2',
            shape='K8',
            camera_data=['E2', 'E6', 'H2', 'H6'],
            camera_data_spawn_point=['E2'],
            map_data="""
                -- -- -- ++ SP -- SP ++ ME -- ME
                -- MB -- -- -- __ -- -- -- ME --
                -- -- -- ++ -- MS -- ++ ME -- --
                ++ ++ ++ ++ MS ++ MS ++ ++ ++ --
                -- -- -- -- -- Me -- -- -- -- --
                -- ++ ++ Me -- -- -- ME -- ME --
                -- ++ ++ Me -- Me ++ ++ ME -- ME
                -- -- -- -- ME -- -- ++ -- ++ --
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
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Fox'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.215, 1.238),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.175, 1.197),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.141, 1.161),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        base=BASE,
        map=dict(
            name='D3',
            shape='I9',
            camera_data=['E2', 'E5'],
            camera_data_spawn_point=['E7'],
            map_data="""
                ++ ME -- ME -- ME -- ME ++
                -- -- ME -- MB -- ME -- --
                -- ME -- ME -- ME -- ME --
                -- ++ ++ ++ MS ++ ++ ++ --
                -- Me -- MS __ MS -- Me --
                -- -- -- Me -- Me -- -- --
                ++ ++ -- ++ ++ ++ -- ++ ++
                ++ ++ -- -- -- -- -- ++ ++
                -- -- -- SP -- SP -- -- --
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
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Fox'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.035, 1.055),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.001, 1.019),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.972, 0.989),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'sp': Stage(
        base=BASE,
        map=dict(
            name='SP',
            shape='K5',
            camera_data=['D3', 'F3'],
            camera_data_spawn_point=['I2'],
            map_data="""
                ++ -- ME -- ++ -- ME -- ++ ++ ++
                -- -- -- ME ++ ME -- MS -- -- SP
                -- MB -- -- -- -- MS -- __ -- --
                -- -- -- ME ++ ME -- MS -- -- SP
                ++ -- ME -- ++ -- ME -- ++ ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 8, 'siren': 3},
                {'battle': 1},
                {'battle': 2},
                {'battle': 3},
                {'battle': 4},
                {'battle': 5},
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Fox'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_CHAPTER_SWITCH_20241219=True,
            MAP_IS_ONE_TIME_STAGE=True,
            STAGE_ENTRANCE=['half', '20240725'],
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (120, 206),
                'width': (1.5, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (206, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_CANNY_THRESHOLD=(75, 100),
            MAP_SWIPE_MULTIPLY=(1.194, 1.217),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.155, 1.176),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.121, 1.142),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=2)', 'battle_default'],
            5: PLAN,
            7: 'fleet_boss.clear_boss',
        },
    ),
}
