"""
Stages of event_20220428_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']

STAGES = {
    'a1': Stage(
        base=BASE,
        map=dict(
            name='A1',
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- ++ ++ ++ -- MB MB MB
                ME -- -- MS -- Me -- ++
                -- ME ++ -- __ -- ME ++
                -- -- -- Me ME ME -- --
                ++ SP -- ME -- ++ -- --
                ++ SP -- -- Me -- MS ME
                ++ ++ Me -- ME -- Me --
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
                {'battle': 0, 'enemy': 4, 'siren': 1},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 2, 'boss': 1},
                {'battle': 4, 'enemy': 2},
            ],
            spawn_data_loop=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1, 'boss': 1},
                {'battle': 4, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Z2'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_DECOY_ENEMY=True,
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
            HOMO_CANNY_THRESHOLD=(50, 75),
            HOMO_EDGE_COLOR_RANGE=(0, 49),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=300,
            MAP_SWIPE_MULTIPLY=(1.131, 1.152),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.094, 1.114),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.062, 1.081),
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
            shape='H8',
            camera_data=['C2', 'C6', 'E2', 'E6'],
            camera_data_spawn_point=['C2'],
            map_data="""
                ++ ME ME -- -- Me ++ ++
                Me -- -- -- MS -- -- ++
                SP -- ++ -- -- ME ME --
                SP -- ++ ME -- -- -- --
                -- -- -- ME Me ++ __ --
                -- -- Me -- -- MS -- MB
                Me ++ MS -- ME -- -- MB
                -- -- ME -- ++ ++ ++ --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_DECOY_ENEMY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 222),
                'width': (0.9, 10),
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
            HOMO_EDGE_HOUGHLINES_THRESHOLD=300,
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
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
    'a3': Stage(
        base=BASE,
        map=dict(
            name='A3',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ ++ -- ME -- -- -- ++ ++ ++
                ++ ++ MS ME -- -- -- -- ME ME
                ME -- -- __ -- MB MB -- -- --
                -- -- Me -- MS ++ ++ -- -- ME
                ++ SP -- ++ ++ ++ ME -- Me --
                ++ SP -- Me -- Me -- -- -- --
                -- ME -- -- ME -- -- MS ++ ++
                ME -- ++ ME -- ME -- -- -- ++
            """,
            map_data_loop="""
                ++ ++ -- ME -- -- -- ++ ++ ++
                ++ ++ MS ME -- Me -- -- ME ME
                ME -- -- __ -- MB MB -- -- --
                -- -- Me -- MS ++ ++ -- -- ME
                ++ SP -- ++ ++ ++ ME -- Me --
                ++ SP -- -- -- Me -- -- -- --
                -- ME -- -- ME -- -- MS ++ ++
                ME -- ++ ME -- ME -- -- -- ++
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
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_DECOY_ENEMY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 222),
                'width': (0.9, 10),
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
            HOMO_EDGE_HOUGHLINES_THRESHOLD=300,
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
            MAP_SWIPE_MULTIPLY=(0.984, 1.003),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.952, 0.969),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.924, 0.941),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b1': Stage(
        map=dict(
            name='B1',
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                ++ ++ ++ ME ME Me -- ++
                MB MB ++ -- -- ME -- ++
                -- -- -- -- MS -- MS ++
                -- -- Me -- -- -- -- ME
                ME __ -- Me -- ++ -- --
                Me MS ME -- MS -- Me ME
                ++ ++ -- Me ++ ME -- --
                ++ ++ ME -- ME -- SP SP
            """,
            map_data_loop="""
                ++ ++ ++ ME -- Me -- ++
                MB MB ++ -- -- ME -- ++
                -- -- -- -- MS -- MS ++
                ME -- Me -- ME -- -- ME
                -- __ -- Me -- ++ -- --
                Me MS ME -- MS -- -- ME
                ++ ++ -- -- ++ ME -- --
                ++ ++ ME -- ME -- SP SP
            """,
            weight_data="""
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 4, 'siren': 1},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 4},
                {'battle': 3, 'enemy': 2},
                {'battle': 4, 'enemy': 4, 'boss': 1},
                {'battle': 5, 'enemy': 2},
            ],
            spawn_data_loop=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
                {'battle': 5, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Z2', 'Leipzig'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_DECOY_ENEMY=True,
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
            HOMO_CANNY_THRESHOLD=(50, 75),
            HOMO_EDGE_COLOR_RANGE=(0, 49),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=300,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom-right',
            MAP_SWIPE_MULTIPLY=(0.985, 1.004),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.953, 0.971),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.925, 0.942),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b2': Stage(
        map=dict(
            name='B2',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['F2'],
            map_data="""
                ME -- ME -- ME ++ -- SP SP
                ME -- ME -- -- ++ ME -- --
                ++ ME -- Me -- ++ Me -- ME
                ++ ++ ++ MS -- MS -- -- --
                -- -- __ -- -- -- -- ME --
                -- Me -- MS ME MS Me ++ ++
                MB -- -- ++ ME -- -- ++ ++
            """,
            map_data_loop="""
                ME -- ME -- ME ++ -- SP SP
                ME -- ME -- -- ++ ME -- --
                ++ ME -- Me -- ++ Me -- ME
                ++ ++ ++ MS -- MS -- -- --
                -- -- __ -- -- -- -- ME --
                MB Me -- MS ME MS Me ++ ++
                MB MB -- ++ ME -- -- ++ ++
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CAlightning', 'SS'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_ENEMY_GENRE_DETECTION_SCALING={'CAlightning': 1.111, 'BBlightning': 1.111, 'SS': 1.111},
            MAP_HAS_DECOY_ENEMY=False,
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom-right',
            MAP_SWIPE_MULTIPLY=(1.115, 1.136),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.078, 1.098),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.047, 1.066),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'b3': Stage(
        map=dict(
            name='B3',
            shape='I9',
            camera_data=['D4', 'D7', 'F4', 'F7'],
            camera_data_spawn_point=['F7', 'D7'],
            map_data="""
                ++ ++ ++ ++ ++ ++ ++ ++ ++
                ++ ++ ++ ++ ++ ++ ++ ++ ++
                ME -- ++ ++ MB ++ ++ -- ME
                -- Me MS ++ -- ++ MS Me --
                ME -- __ -- MS -- __ -- ME
                -- ++ ++ Me ++ Me ++ ++ --
                -- -- ME -- ++ -- ME -- --
                -- -- -- -- -- -- -- -- --
                ME -- ME SP -- SP ME -- ME
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
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Compiler'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_DECOY_ENEMY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (120, 242),
                'width': (1.5, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (242, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=35,
            EDGE_LINES_HOUGHLINES_THRESHOLD=35,
            HOMO_CANNY_THRESHOLD=(50, 100),
            HOMO_EDGE_COLOR_RANGE=(0, 13),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=300,
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(0.983, 1.001),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.951, 0.968),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.923, 0.939),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c1': Stage(
        map=dict(
            name='C1',
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- ++ ++ ++ -- MB MB MB
                ME -- -- MS -- Me -- ++
                -- ME ++ -- __ -- ME ++
                -- -- -- Me ME ME -- --
                ++ SP -- ME -- ++ -- --
                ++ SP -- -- Me -- MS ME
                ++ ++ Me -- ME -- Me --
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
                {'battle': 0, 'enemy': 4, 'siren': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 4},
                {'battle': 3, 'enemy': 2},
                {'battle': 4, 'enemy': 2, 'boss': 1},
            ],
            spawn_data_loop=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Z2', 'Leipzig'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_DECOY_ENEMY=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 222),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (222, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_CANNY_THRESHOLD=(50, 75),
            HOMO_EDGE_COLOR_RANGE=(0, 33),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=300,
            MAP_SWIPE_MULTIPLY=(1.131, 1.152),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.094, 1.114),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.062, 1.081),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'c2': Stage(
        map=dict(
            name='C2',
            shape='H8',
            camera_data=['C2', 'C6', 'E2', 'E6'],
            camera_data_spawn_point=['C2'],
            map_data="""
                ++ ME ME -- -- Me ++ ++
                Me -- -- -- MS -- -- ++
                SP -- ++ -- -- ME ME --
                SP -- ++ ME -- -- -- --
                -- -- -- ME Me ++ __ --
                -- -- Me -- -- MS -- MB
                Me ++ MS -- ME -- -- MB
                -- -- ME -- ++ ++ ++ --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_DECOY_ENEMY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 231),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (231, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_EDGE_COLOR_RANGE=(0, 24),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=300,
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
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
    'c3': Stage(
        map=dict(
            name='C3',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ ++ -- ME -- -- -- ++ ++ ++
                ++ ++ MS ME -- -- -- -- ME ME
                ME -- -- __ -- MB MB -- -- --
                -- -- Me -- MS ++ ++ -- -- ME
                ++ SP -- ++ ++ ++ ME -- Me --
                ++ SP -- Me -- Me -- -- -- --
                -- ME -- -- ME -- -- MS ++ ++
                ME -- ++ ME -- ME -- -- -- ++
            """,
            map_data_loop="""
                ++ ++ -- ME -- -- -- ++ ++ ++
                ++ ++ MS ME -- Me -- -- ME ME
                ME -- -- __ -- MB MB -- -- --
                -- -- Me -- MS ++ ++ -- -- ME
                ++ SP -- ++ ++ ++ ME -- Me --
                ++ SP -- -- -- Me -- -- -- --
                -- ME -- -- ME -- -- MS ++ ++
                ME -- ++ ME -- ME -- -- -- ++
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
            MAP_SIREN_TEMPLATE=['CL', 'CA', 'BB'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_DECOY_ENEMY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 231),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (231, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_EDGE_COLOR_RANGE=(0, 24),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=300,
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
            MAP_SWIPE_MULTIPLY=(0.984, 1.003),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.952, 0.969),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.924, 0.941),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd1': Stage(
        map=dict(
            name='D1',
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                ++ ++ ++ ME ME Me -- ++
                MB MB ++ -- -- ME -- ++
                -- -- -- -- MS -- MS ++
                -- -- Me -- -- -- -- ME
                ME __ -- Me -- ++ -- --
                Me MS ME -- MS -- Me ME
                ++ ++ -- Me ++ ME -- --
                ++ ++ ME -- ME -- SP SP
            """,
            map_data_loop="""
                ++ ++ ++ ME -- Me -- ++
                MB MB ++ -- -- ME -- ++
                -- -- -- -- MS -- MS ++
                ME -- Me -- ME -- -- ME
                -- __ -- Me -- ++ -- --
                Me MS ME -- MS -- -- ME
                ++ ++ -- -- ++ ME -- --
                ++ ++ ME -- ME -- SP SP
            """,
            weight_data="""
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 4, 'siren': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 4},
                {'battle': 3, 'enemy': 2},
                {'battle': 4, 'enemy': 4},
                {'battle': 5, 'enemy': 2, 'boss': 1},
            ],
            spawn_data_loop=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Z2', 'Leipzig', 'PrinzEugen'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_DECOY_ENEMY=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (120, 222),
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
            HOMO_CANNY_THRESHOLD=(50, 75),
            HOMO_EDGE_COLOR_RANGE=(0, 33),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=300,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom-right',
            MAP_SWIPE_MULTIPLY=(0.985, 1.004),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.953, 0.971),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.925, 0.942),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd2': Stage(
        map=dict(
            name='D2',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['F2'],
            map_data="""
                ME -- ME -- ME ++ -- SP SP
                ME -- ME -- -- ++ ME -- --
                ++ ME -- Me -- ++ Me -- ME
                ++ ++ ++ MS -- MS -- -- --
                -- -- __ -- -- -- -- ME --
                -- Me -- MS ME MS Me ++ ++
                MB -- -- ++ ME -- -- ++ ++
            """,
            map_data_loop="""
                ME -- ME -- ME ++ -- SP SP
                ME -- ME -- -- ++ ME -- --
                ++ ME -- Me -- ++ Me -- ME
                ++ ++ ++ MS -- MS -- -- --
                -- -- __ -- -- -- -- ME --
                MB Me -- MS ME MS Me ++ ++
                MB MB -- ++ ME -- -- ++ ++
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
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_SIREN_TEMPLATE=['SS', 'CAlightning', 'BBlightning'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (120, 238),
                'width': (1.5, 10),
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
            HOMO_EDGE_HOUGHLINES_THRESHOLD=300,
            MAP_ENEMY_GENRE_DETECTION_SCALING={'CAlightning': 1.111, 'BBlightning': 1.111, 'SS': 1.111},
            MAP_HAS_DECOY_ENEMY=False,
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom-right',
            MAP_SWIPE_MULTIPLY=(1.115, 1.136),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.078, 1.098),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.047, 1.066),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        map=dict(
            name='D3',
            shape='I9',
            camera_data=['D4', 'D7', 'F4', 'F7'],
            camera_data_spawn_point=['F7', 'D7'],
            map_data="""
                ++ ++ ++ ++ ++ ++ ++ ++ ++
                ++ ++ ++ ++ ++ ++ ++ ++ ++
                ME -- ++ ++ MB ++ ++ -- ME
                -- Me MS ++ -- ++ MS Me --
                ME -- __ -- MS -- __ -- ME
                -- ++ ++ Me ++ Me ++ ++ --
                -- -- ME -- ++ -- ME -- --
                -- -- -- -- -- -- -- -- --
                ME -- ME SP -- SP ME -- ME
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
            MAP_SIREN_TEMPLATE=['Compiler'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_DECOY_ENEMY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (120, 242),
                'width': (1.5, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (242, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=35,
            EDGE_LINES_HOUGHLINES_THRESHOLD=35,
            HOMO_CANNY_THRESHOLD=(50, 100),
            HOMO_EDGE_COLOR_RANGE=(0, 13),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=300,
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(0.983, 1.001),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.951, 0.968),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.923, 0.939),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'sp': Stage(
        map=dict(
            name='SP',
            shape='I8',
            camera_data=['D3', 'D5', 'F3', 'F5'],
            camera_data_spawn_point=['F5', 'F3'],
            map_data="""
                ++ ++ -- ++ ++ ++ -- ++ ++
                ++ ++ Me -- ME -- Me ++ ++
                -- Me ++ MS -- MS ++ ME --
                MB -- -- __ ++ -- ME -- SP
                MB -- ME -- ++ -- -- -- SP
                -- Me ++ MS -- MS ++ ME --
                ++ ++ Me -- ME -- Me ++ ++
                ++ ++ -- ++ ++ ++ -- ++ ++
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
                {'battle': 0, 'enemy': 1, 'siren': 4},
                {'battle': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Roon', 'Odin', 'Mainz', 'August'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (120, 222),
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
            HOMO_CANNY_THRESHOLD=(50, 75),
            HOMO_EDGE_COLOR_RANGE=(0, 33),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=300,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=2)', 'battle_default'],
            5: PLAN,
            7: 'fleet_boss.clear_boss',
        },
    ),
}
