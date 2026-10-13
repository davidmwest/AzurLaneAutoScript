"""
Stages of event_20210225_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

PLAN = ['clear_siren', 'battle_default']
PLAN_2 = ['clear_enemy(scale=(1,))', 'clear_enemy(scale=(2,))', 'clear_enemy(scale=(3,))', 'battle_default']
PLAN_3 = ['clear_siren', 'clear_enemy(scale=(2,))', 'clear_enemy(scale=(3,))', 'battle_default']
PLAN_4 = [
    'clear_siren',
    'clear_enemy(scale=(1,))',
    'clear_enemy(scale=(2,))',
    'clear_enemy(scale=(3,))',
    'battle_default',
]

STAGES = {
    'a1': Stage(
        map=dict(
            name='A1',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                ++ ME -- -- -- -- -- -- --
                ME -- ME ++ ME -- Me ++ ++
                -- -- -- Me -- -- ME ++ ++
                -- MS -- ++ ++ -- -- ME --
                Me -- -- ME ++ MS __ -- MB
                ++ -- -- -- -- -- -- ME --
                ++ SP -- SP ++ ++ ++ -- --
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
            MAP_SIREN_TEMPLATE=['DD'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
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
                'wlen': 1000,
            },
            MAP_ENEMY_GENRE_DETECTION_SCALING={'DD': 1.111, 'CL': 1.111},
        ),
        battle={
            0: PLAN,
            3: 'clear_boss',
        },
    ),
    'a2': Stage(
        map=dict(
            name='A2',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- Me ++ ++ ++ MB ++ ++ ++
                ME -- ME ++ ME -- ME ++ --
                -- -- -- -- -- -- -- ME --
                MS ++ -- ++ Me __ -- -- Me
                -- -- -- ++ -- -- -- ME --
                SP -- -- MS ME -- ME ++ ++
                -- SP -- ++ -- Me -- ++ ++
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
            MAP_SIREN_TEMPLATE=['CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'a3': Stage(
        map=dict(
            name='A3',
            shape='I10',
            camera_data=['E3', 'E6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                -- ++ ++ ++ ++ ++ ++ ++ --
                ++ -- -- -- Me -- -- -- ++
                ++ -- ++ ME -- ME ++ -- ++
                -- -- ME -- MS -- ME -- --
                -- Me -- MS MB MS -- Me --
                -- -- ME -- MS -- ME -- --
                ++ -- ++ -- __ -- ++ -- ++
                ++ ME -- SP -- SP -- ME ++
                -- ++ ++ ++ -- ++ ++ ++ --
                -- -- ++ -- -- -- ++ -- --
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
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b1': Stage(
        map=dict(
            name='B1',
            shape='I8',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['D2', 'E2'],
            map_data="""
                -- ++ ++ ++ MB ++ ++ ++ --
                -- ME ++ SP -- SP ++ -- --
                Me -- -- -- -- -- -- ME ++
                ++ ME ++ -- __ -- MS Me ++
                -- ME ++ MS -- MS -- ME --
                Me -- -- -- -- -- ++ ++ ++
                -- ME ++ ME Me ME ++ ++ --
                -- ++ ++ ++ ++ -- ++ -- --
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
            MAP_SIREN_TEMPLATE=['CL', 'CAred'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
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
                'wlen': 1000,
            },
            MAP_ENEMY_GENRE_DETECTION_SCALING={'CL': 1.111, 'CAred': 1.111, 'BBred': 1.111},
            MAP_SWIPE_MULTIPLY=(1.159, 1.181),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.121, 1.141),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.088, 1.108),
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b2': Stage(
        map=dict(
            name='B2',
            shape='K7',
            camera_data=['D2', 'D4', 'H2', 'H4'],
            camera_data_spawn_point=['H4'],
            map_data="""
                -- -- -- -- -- -- -- ME ME -- ++
                ++ -- ME -- ++ ++ ME -- -- ME ++
                -- ME -- ME ++ ++ ++ -- MS ++ ++
                ++ ++ -- -- Me __ MS -- -- -- SP
                -- ++ Me -- -- -- -- -- -- -- SP
                MB -- -- -- Me -- ++ ME MS Me ++
                -- ++ ++ ++ ++ -- ++ -- ++ -- ++
            """,
            weight_data="""
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
            MAP_SIREN_TEMPLATE=['CL', 'CAred'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'b3': Stage(
        map=dict(
            name='B3',
            shape='I10',
            camera_data=['D4', 'D8', 'F4', 'F8'],
            camera_data_spawn_point=['D4', 'F4'],
            map_data="""
                -- ++ ++ ++ ++ ++ ++ ++ --
                ++ -- -- -- -- -- -- -- ++
                ++ ME ++ SP -- SP ++ ME ++
                ME -- -- -- -- -- -- -- ME
                -- Me MS -- __ -- MS Me --
                ME -- -- -- -- -- -- -- ME
                ++ ME ++ -- MS -- ++ ME ++
                ++ -- Me -- -- -- Me -- ++
                -- ++ ++ ++ -- ++ ++ ++ --
                -- -- ++ -- MB -- ++ -- --
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
            MAP_SIREN_TEMPLATE=['CL', 'CAred', 'BBred'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c1': Stage(
        map=dict(
            name='C1',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                ++ ME -- -- -- -- -- -- --
                ME -- ME ++ ME -- Me ++ ++
                -- -- -- Me -- -- ME ++ ++
                -- MS -- ++ ++ -- -- ME --
                Me -- -- ME ++ MS __ -- MB
                ++ -- -- -- -- -- -- ME --
                ++ SP -- SP ++ ++ ++ -- --
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
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
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
                'wlen': 1000,
            },
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'c2': Stage(
        map=dict(
            name='C2',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- Me ++ ++ ++ MB ++ ++ ++
                ME -- ME ++ ME -- ME ++ --
                -- -- -- -- -- -- -- ME --
                MS ++ -- ++ Me __ -- -- Me
                -- -- -- ++ -- -- -- ME --
                SP -- -- MS ME -- ME ++ ++
                -- SP -- ++ -- Me -- ++ ++
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
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN_4,
            4: 'clear_boss',
        },
    ),
    'c3': Stage(
        map=dict(
            name='C3',
            shape='I10',
            camera_data=['E3', 'E6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                -- ++ ++ ++ ++ ++ ++ ++ --
                ++ -- -- -- Me -- -- -- ++
                ++ -- ++ ME -- ME ++ -- ++
                -- -- ME -- MS -- ME -- --
                -- Me -- MS MB MS -- Me --
                -- -- ME -- MS -- ME -- --
                ++ -- ++ -- __ -- ++ -- ++
                ++ ME -- SP -- SP -- ME ++
                -- ++ ++ ++ -- ++ ++ ++ --
                -- -- ++ -- -- -- ++ -- --
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
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd1': Stage(
        map=dict(
            name='D1',
            shape='I8',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['D2', 'E2'],
            map_data="""
                -- ++ ++ ++ MB ++ ++ ++ --
                -- ME ++ SP -- SP ++ -- --
                Me -- -- -- -- -- -- ME ++
                ++ ME ++ -- __ -- MS Me ++
                -- ME ++ MS -- MS -- ME --
                Me -- -- -- -- -- ++ ++ ++
                -- ME ++ ME Me ME ++ ++ --
                -- ++ ++ ++ ++ -- ++ -- --
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
            MAP_SIREN_TEMPLATE=['CAred', 'BBred'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
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
                'wlen': 1000,
            },
            MAP_ENEMY_GENRE_DETECTION_SCALING={'CL': 1.111, 'CAred': 1.111, 'BBred': 1.111, 'CV': 1.111},
            MAP_SWIPE_MULTIPLY=(1.193, 1.215),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.154, 1.175),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.12, 1.14),
        ),
        battle={
            0: PLAN_4,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd2': Stage(
        map=dict(
            name='D2',
            shape='K7',
            camera_data=['D2', 'D4', 'H2', 'H4'],
            camera_data_spawn_point=['H4'],
            map_data="""
                -- -- -- -- -- -- -- ME ME -- ++
                ++ -- ME -- ++ ++ ME -- -- ME ++
                -- ME -- ME ++ ++ ++ -- MS ++ ++
                ++ ++ -- -- Me __ MS -- -- -- SP
                -- ++ Me -- -- -- -- -- -- -- SP
                MB -- -- -- Me -- ++ ME MS Me ++
                -- ++ ++ ++ ++ -- ++ -- ++ -- ++
            """,
            weight_data="""
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
            MAP_SIREN_TEMPLATE=['CAred', 'CV'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(1.084, 1.105),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.049, 1.068),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.018, 1.036),
        ),
        battle={
            0: PLAN_3,
            5: PLAN_2,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        map=dict(
            name='D3',
            shape='I10',
            camera_data=['D4', 'D8', 'F4', 'F8'],
            camera_data_spawn_point=['D4', 'F4'],
            map_data="""
                -- ++ ++ ++ ++ ++ ++ ++ --
                ++ -- -- -- -- -- -- -- ++
                ++ ME ++ SP -- SP ++ ME ++
                ME -- -- -- -- -- -- -- ME
                -- Me MS -- __ -- MS Me --
                ME -- -- -- -- -- -- -- ME
                ++ ME ++ -- MS -- ++ ME ++
                ++ -- Me -- -- -- Me -- ++
                -- ++ ++ ++ -- ++ ++ ++ --
                -- -- ++ -- MB -- ++ -- --
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
            MAP_SIREN_TEMPLATE=['CAred', 'BBred', 'CV'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(1.163, 1.185),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.125, 1.146),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.092, 1.112),
        ),
        battle={
            0: PLAN_3,
            5: PLAN_2,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'sp': Stage(
        map=dict(
            name='SP',
            shape='G10',
            camera_data=['D2', 'D6', 'D7'],
            camera_data_spawn_point=['D7'],
            map_data="""
                -- -- ++ MB ++ -- --
                ++ ++ ++ -- ++ ++ ++
                ++ ME -- -- -- ME ++
                ++ -- -- ++ -- -- ++
                ++ ME -- -- -- ME ++
                ++ ++ ++ MS ++ ++ ++
                ++ -- -- -- -- -- ++
                MS -- -- __ -- -- MS
                ++ -- SP -- SP -- ++
                ++ ++ ++ -- ++ ++ ++
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
                {'battle': 0, 'siren': 3},
                {'battle': 1},
                {'battle': 2},
                {'battle': 3, 'enemy': 4},
                {'battle': 4},
                {'battle': 5},
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['BBred', 'CV'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
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
                'wlen': 1000,
            },
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
            EDGE_LINES_HOUGHLINES_THRESHOLD=40,
            MAP_ENEMY_GENRE_DETECTION_SCALING={'BBred': 1.111, 'CV': 1.111},
            MAP_SWIPE_MULTIPLY=(0.976, 0.995),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.944, 0.962),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.917, 0.933),
        ),
        battle={
            0: ['clear_siren', 'clear_enemy(scale=(3,))', 'clear_enemy(scale=(2,))', 'battle_default'],
            5: PLAN_2,
            7: 'fleet_boss.clear_boss',
        },
    ),
}
