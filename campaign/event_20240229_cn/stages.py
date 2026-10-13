"""
Stages of event_20240229_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']
PLAN_2 = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default']

STAGES = {
    'a1': Stage(
        map=dict(
            name='A1',
            shape='I8',
            camera_data=['E3', 'D6', 'E6'],
            camera_data_spawn_point=['D2'],
            map_data="""
                ++ SP -- SP ++ ME -- -- --
                ++ -- -- -- Me -- ME -- --
                -- -- MS -- -- -- ++ ++ ++
                -- ++ ++ MS -- -- -- -- ME
                -- ME ++ Me -- Me -- ME --
                ME -- -- -- __ ++ __ -- ME
                -- ME -- Me -- MB -- Me ++
                ++ ++ ++ -- ME -- ME -- ++
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
                {'battle': 3, 'enemy': 1, 'boss': 1},
                {'battle': 4, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['DD', 'CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
                'CAlightning': 1.111,
                'BBlightning': 1.111,
            },
            MAP_SWIPE_MULTIPLY=(1.232, 1.255),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.191, 1.213),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.156, 1.177),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            3: 'clear_boss',
        },
    ),
    'a2': Stage(
        map=dict(
            name='A2',
            shape='I8',
            camera_data=['D3', 'D6', 'F3', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- -- -- -- ++ -- -- ++ ++
                ME -- ME ++ ++ ME ME ++ ++
                -- Me -- -- -- -- -- ME --
                -- -- -- ME -- -- ME -- --
                -- MS ++ ++ Me -- -- ++ --
                -- -- MB ++ -- -- -- Me --
                SP __ -- MS -- ++ -- -- ME
                -- SP -- -- -- Me -- ME --
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
            MAP_SIREN_TEMPLATE=['DD', 'CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
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
    'a3': Stage(
        map=dict(
            name='A3',
            shape='G10',
            camera_data=['D5', 'D8'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- -- SP -- SP -- --
                -- ++ -- -- -- ++ --
                -- Me -- MS -- Me --
                ++ -- MS -- MS -- ++
                ++ Me -- ++ -- Me ++
                ME -- -- Me -- -- ME
                -- ME -- __ -- ME --
                ME -- -- ++ -- -- ME
                -- ME -- MB -- ME --
                ++ -- ME -- ME -- ++
            """,
            weight_data="""
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['CL', 'CAlightning'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.233, 1.256),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.192, 1.214),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.157, 1.178),
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
            shape='I8',
            camera_data=['D3', 'D5', 'F3', 'F5'],
            camera_data_spawn_point=['D2'],
            map_covered=['G5'],
            map_data="""
                ++ -- -- SP -- SP -- ++ ++
                ++ Me -- -- -- -- -- Me ++
                -- -- Me -- MS -- Me -- --
                ++ ++ ++ MS -- MS ++ ++ ++
                -- ME ME -- __ -- ME ME --
                ME -- -- ++ MB ++ -- -- ME
                -- ME ME ++ ++ ++ ME ME --
                -- ++ -- ++ ++ ++ -- ++ --
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
                {'battle': 5, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.24, 1.263),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.199, 1.221),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.164, 1.185),
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
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['F2'],
            map_data="""
                -- ME -- Me -- Me ++ ++ ++
                ++ ++ -- -- -- -- -- -- SP
                MB ++ ME -- ++ MS -- -- SP
                -- __ -- -- ++ Me MS -- ++
                ME ++ ME -- -- -- -- MS ME
                -- ME -- -- ME ME -- -- --
                -- -- -- Me ++ ++ -- Me --
                ME -- ME -- ++ ++ ME -- ME
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Dilloy'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.192, 1.215),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.153, 1.174),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.119, 1.14),
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
            shape='K9',
            camera_data=['E3', 'E6', 'G3', 'G6'],
            camera_data_spawn_point=['E3', 'G3'],
            map_data="""
                ++ -- -- -- ++ ++ ++ -- -- -- ++
                -- -- ME -- ++ ++ ++ -- ME -- --
                -- ME -- -- SP -- SP -- -- ME --
                ++ ++ ME -- -- -- -- -- ME ++ ++
                ++ ++ -- Me -- MB -- Me -- -- ++
                -- -- ME -- MS __ MS -- ME -- --
                -- -- -- Me -- MS -- Me -- ++ --
                -- ++ ++ -- ME -- ME -- ++ ++ --
                -- -- ++ -- ++ ++ ++ -- -- -- --
            """,
            map_data_loop="""
                ++ -- -- -- ++ ++ ++ -- -- -- ++
                -- -- ME -- -- -- -- -- ME -- --
                -- ME -- -- SP -- SP -- -- ME --
                ++ ++ ME -- -- -- -- -- ME ++ ++
                ++ ++ -- Me -- MB -- Me -- -- ++
                -- -- ME -- MS __ MS -- ME -- --
                -- -- -- Me -- MS -- Me -- ++ --
                -- ++ ++ -- ME -- ME -- ++ ++ --
                -- -- ++ -- ++ ++ ++ -- -- -- --
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
            MAP_SIREN_TEMPLATE=['Dilloy'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 222),
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
            MAP_SWIPE_MULTIPLY=(1.109, 1.13),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.073, 1.093),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.042, 1.06),
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
            shape='I8',
            camera_data=['E3', 'D6', 'E6'],
            camera_data_spawn_point=['D2'],
            map_data="""
                ++ SP -- SP ++ ME -- -- --
                ++ -- -- -- Me -- ME -- --
                -- -- MS -- -- -- ++ ++ ++
                -- ++ ++ MS -- -- -- -- ME
                -- ME ++ Me -- Me -- ME --
                ME -- -- -- __ ++ __ -- ME
                -- ME -- Me -- MB -- Me ++
                ++ ++ ++ -- ME -- ME -- ++
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
        config=dict(
            MAP_SIREN_TEMPLATE=['DD', 'CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
                'CAlightning': 1.111,
                'BBlightning': 1.111,
            },
            MAP_SWIPE_MULTIPLY=(1.232, 1.255),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.191, 1.213),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.156, 1.177),
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
            shape='I8',
            camera_data=['D3', 'D6', 'F3', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- -- -- -- ++ -- -- ++ ++
                ME -- ME ++ ++ ME ME ++ ++
                -- Me -- -- -- -- -- ME --
                -- -- -- ME -- -- ME -- --
                -- MS ++ ++ Me -- -- ++ --
                -- -- MB ++ -- -- -- Me --
                SP __ -- MS -- ++ -- -- ME
                -- SP -- -- -- Me -- ME --
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
            MAP_SIREN_TEMPLATE=['CL', 'CAlightning'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
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
    'c3': Stage(
        map=dict(
            name='C3',
            shape='G10',
            camera_data=['D5', 'D8'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- -- SP -- SP -- --
                -- ++ -- -- -- ++ --
                -- Me -- MS -- Me --
                ++ -- MS -- MS -- ++
                ++ Me -- ++ -- Me ++
                ME -- -- Me -- -- ME
                -- ME -- __ -- ME --
                ME -- -- ++ -- -- ME
                -- ME -- MB -- ME --
                ++ -- ME -- ME -- ++
            """,
            weight_data="""
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['CAlightning', 'BBlightning'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
                'CAlightning': 1.111,
                'BBlightning': 1.111,
            },
            MAP_SWIPE_MULTIPLY=(1.233, 1.256),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.192, 1.214),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.157, 1.178),
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
            shape='I8',
            camera_data=['D3', 'D5', 'F3', 'F5'],
            camera_data_spawn_point=['D2'],
            map_data="""
                ++ -- -- SP -- SP -- ++ ++
                ++ Me -- -- -- -- -- Me ++
                -- -- Me -- MS -- Me -- --
                ++ ++ ++ MS -- MS ++ ++ ++
                -- ME ME -- __ -- ME ME --
                ME -- -- ++ MB ++ -- -- ME
                -- ME ME ++ ++ ++ ME ME --
                -- ++ -- ++ ++ ++ -- ++ --
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
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.24, 1.263),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.199, 1.221),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.164, 1.185),
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
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['F2'],
            map_data="""
                -- ME -- Me -- Me ++ ++ ++
                ++ ++ -- -- -- -- -- -- SP
                MB ++ ME -- ++ MS -- -- SP
                -- __ -- -- ++ Me MS -- ++
                ME ++ ME -- -- -- -- MS ME
                -- ME -- -- ME ME -- -- --
                -- -- -- Me ++ ++ -- Me --
                ME -- ME -- ++ ++ ME -- ME
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
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Dilloy'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.192, 1.215),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.153, 1.174),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.119, 1.14),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        map=dict(
            name='D3',
            shape='K9',
            camera_data=['E3', 'E6', 'G3', 'G6'],
            camera_data_spawn_point=['E3', 'G3'],
            map_data="""
                ++ -- -- -- ++ ++ ++ -- -- -- ++
                -- -- ME -- ++ ++ ++ -- ME -- --
                -- ME -- -- SP -- SP -- -- ME --
                ++ ++ ME -- -- -- -- -- ME ++ ++
                ++ ++ -- Me -- MB -- Me -- -- ++
                -- -- ME -- MS __ MS -- ME -- --
                -- -- -- Me -- MS -- Me -- ++ --
                -- ++ ++ -- ME -- ME -- ++ ++ --
                -- -- ++ -- ++ ++ ++ -- -- -- --
            """,
            map_data_loop="""
                ++ -- -- -- ++ ++ ++ -- -- -- ++
                -- -- ME -- -- -- -- -- ME -- --
                -- ME -- -- SP -- SP -- -- ME --
                ++ ++ ME -- -- -- -- -- ME ++ ++
                ++ ++ -- Me -- MB -- Me -- -- ++
                -- -- ME -- MS __ MS -- ME -- --
                -- -- -- Me -- MS -- Me -- ++ --
                -- ++ ++ -- ME -- ME -- ++ ++ --
                -- -- ++ -- ++ ++ ++ -- -- -- --
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
            MAP_SIREN_TEMPLATE=['Dilloy'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 222),
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
            MAP_SWIPE_MULTIPLY=(1.109, 1.13),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.073, 1.093),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.042, 1.06),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'sp': Stage(
        map=dict(
            name='SP',
            shape='T10',
            camera_data=['B3', 'B6'],
            camera_data_spawn_point=['B6'],
            map_data="""
                -- ++ ++ ++ -- -- -- -- ++ ++ -- -- -- -- -- -- -- -- -- --
                ME -- MB -- ME -- -- -- ++ ++ ++ -- ++ -- -- -- ++ ++ ++ --
                -- ME __ ME -- -- ++ -- -- -- ++ -- -- -- ++ -- -- -- -- --
                ME -- MS -- ME -- -- -- -- -- -- -- -- -- ++ -- -- -- -- ++
                -- ME -- ME -- -- -- -- -- ++ ++ ++ -- -- -- -- ++ -- -- --
                MS -- -- -- MS -- ++ -- -- -- -- -- -- ++ ++ -- -- -- -- --
                -- -- -- -- -- -- -- -- ++ -- -- -- -- -- ++ -- -- ++ ++ --
                ++ SP -- SP ++ ++ -- -- -- -- ++ ++ -- -- -- -- -- ++ ++ --
                -- -- -- -- -- ++ -- ++ ++ -- -- ++ -- ++ ++ ++ -- -- -- --
                ++ ++ ++ -- -- -- -- -- -- -- -- -- -- -- ++ -- -- -- ++ --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['shuguangjixie_shanliu', 'shuguangjixie_huixing'],
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
            MAP_IS_ONE_TIME_STAGE=True,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom-left',
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 222),
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
            MAP_SWIPE_MULTIPLY=(0.996, 1.014),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.963, 0.981),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.935, 0.952),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=2)', 'battle_default'],
            5: PLAN,
            7: 'fleet_boss.clear_boss',
        },
    ),
}
