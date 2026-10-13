"""
Stages of event_20201229_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

PLAN = ['clear_siren', 'battle_default']
PLAN_2 = ['fleet_2_protect', 'clear_siren', 'battle_default']

STAGES = {
    'a1': Stage(
        map=dict(
            name='A1',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D2', 'D5'],
            map_data="""
                ++ -- MS -- ME -- -- ++ ++
                SP -- -- ++ ME -- Me ++ ++
                -- -- -- -- __ -- -- Me --
                SP -- -- MS -- ME -- -- --
                ++ ++ -- ++ ++ ++ -- ++ ++
                ++ ME -- ME MB ME -- ME ++
                -- -- -- -- -- -- -- -- --
            """,
            weight_data="""
                50 50 50 50 50 50 10 90 90
                50 50 50 50 50 50 10 90 90
                50 50 50 50 50 50 10 10 10
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
                {'battle': 4},
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
            MAP_SIREN_TEMPLATE=['DD', 'CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
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
            MAP_SWIPE_MULTIPLY=(1.196, 1.218),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.156, 1.178),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.122, 1.143),
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
            3: 'clear_boss',
        },
    ),
    'a2': Stage(
        map=dict(
            name='A2',
            shape='J6',
            camera_data=['D2', 'D4', 'G2', 'G4'],
            camera_data_spawn_point=['D2'],
            map_data="""
                ++ SP -- SP -- -- ++ -- ++ ++
                ++ -- -- -- -- -- -- ME -- ++
                ME -- MS ++ -- MS -- -- ME --
                ME -- -- -- -- ++ ME __ -- MB
                -- Me ++ ++ Me ++ -- -- ME --
                -- -- ++ ++ -- -- -- ME -- ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 10 10 10 10 50 50 50 50 50
                50 10 90 90 10 50 50 50 50 50
                50 10 90 90 10 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
            spawn_data_loop=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Dorsetshire', 'Rodney', 'ArkRoyal'],
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
            shape='J6',
            camera_data=['D2', 'D4', 'G2', 'G4'],
            camera_data_spawn_point=['D4'],
            map_data="""
                -- -- ME -- ++ ++ -- ++ ++ ++
                -- ++ -- Me ++ ++ Me -- ME ME
                ++ MS -- -- MB MB -- -- -- --
                ++ -- -- -- -- -- __ ++ ++ ME
                SP -- -- MS ME ME -- ME ++ --
                -- SP -- ++ ++ ++ -- -- ME --
            """,
            weight_data="""
                50 50 50 10 90 90 10 50 50 50
                50 50 50 10 90 90 10 50 50 50
                50 50 50 10 10 10 10 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
            spawn_data_loop=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Kongo', 'Yamashiro'],
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
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- -- ++ -- -- ME ++ ++ ++
                -- ++ ++ Me -- -- ME -- --
                ++ ++ ++ -- ++ -- -- -- MB
                -- Me -- Me -- -- ME -- --
                -- -- MS -- __ MS ++ ++ ME
                ++ ++ ++ -- -- -- ++ ME --
                ++ -- SP -- MS -- -- -- ME
                ++ -- SP -- ++ ME -- ME --
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
                {'battle': 0, 'enemy': 4, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
                {'battle': 5, 'enemy': 1},
            ],
            spawn_data_loop=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Z24', 'Nuremberg', 'Carabiniere'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 238),
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
            MAP_SWIPE_MULTIPLY=(1.021, 1.041),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.988, 1.006),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.959, 0.976),
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
            HOMO_EDGE_HOUGHLINES_THRESHOLD=180,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
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
            camera_data=['D3', 'D5', 'H3', 'H5'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- ++ -- ++ ++ ++ MB MB ++ ++ ++
                -- -- -- ++ -- ME -- -- -- ME ++
                SP -- SP ++ ME -- ++ ME -- ME ++
                -- -- -- -- -- __ -- ++ -- -- --
                ++ -- ++ ++ ME -- ME -- -- Me Me
                MS -- MS ++ -- -- -- -- Me ++ ++
                -- MS -- ME -- ME ++ ++ ++ ++ ++
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
                {'battle': 0, 'enemy': 4, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
            spawn_data_loop=[
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
            MAP_SIREN_TEMPLATE=['Z24', 'Carabiniere', 'Kongo', 'Yamashiro'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(1.167, 1.189),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.128, 1.149),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.095, 1.115),
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'b3': Stage(
        map=dict(
            name='B3',
            shape='J10',
            camera_data=['D2', 'D6', 'D8', 'G2', 'G6', 'G8'],
            camera_data_spawn_point=['D8', 'G8'],
            map_data="""
                ++ -- -- ME -- -- ME -- -- ++
                -- -- ++ -- MB MB -- ++ -- --
                ++ -- -- ME -- -- ME -- -- ++
                -- ++ ++ ME -- -- ME ++ ++ --
                ++ ++ MS -- __ __ -- MS ++ ++
                ++ ME -- -- ++ ++ -- -- ME ++
                -- ME -- Me ++ ++ Me -- ME --
                ++ ++ -- -- Me Me -- -- ++ ++
                -- ++ MS -- -- -- -- MS ++ --
                -- ++ ++ ++ SP SP ++ ++ ++ --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 10 10 10 10 50 50 50
                50 50 50 10 90 90 10 50 50 50
                50 50 50 10 90 90 10 50 50 50
                50 50 50 10 10 10 10 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 4, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'enemy': 1, 'boss': 1},
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
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DD', 'CL', 'Intruder'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(0.946, 0.963),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.914, 0.931),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.888, 0.904),
        ),
        battle={
            0: PLAN_2,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c1': Stage(
        map=dict(
            name='C1',
            shape='I7',
            camera_data=['D2', 'D4', 'F2', 'F4'],
            camera_data_spawn_point=['D2', 'D5'],
            map_data="""
                ++ -- MS -- ME -- -- ++ ++
                SP -- -- ++ ME -- Me ++ ++
                -- -- -- -- __ -- -- Me --
                SP -- -- MS -- ME -- -- --
                ++ ++ -- ++ ++ ++ -- ++ ++
                ++ ME -- ME MB ME -- ME ++
                -- -- -- -- -- -- -- -- --
            """,
            weight_data="""
                50 50 50 50 50 50 10 90 90
                50 50 50 50 50 50 10 90 90
                50 50 50 50 50 50 10 10 10
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
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
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 238),
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
            HOMO_EDGE_HOUGHLINES_THRESHOLD=180,
            MAP_SWIPE_MULTIPLY=(1.196, 1.218),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.156, 1.178),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.122, 1.143),
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
        ),
        battle={
            0: PLAN_2,
            4: 'clear_boss',
        },
    ),
    'c2': Stage(
        map=dict(
            name='C2',
            shape='J6',
            camera_data=['D2', 'D4', 'G2', 'G4'],
            camera_data_spawn_point=['D2'],
            map_data="""
                ++ SP -- SP -- -- ++ -- ++ ++
                ++ -- -- -- -- -- -- ME -- ++
                ME -- MS ++ -- MS -- -- ME --
                ME -- -- -- -- ++ ME __ -- MB
                -- Me ++ ++ Me ++ -- -- ME --
                -- -- ++ ++ -- -- -- ME -- ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 10 10 10 10 50 50 50 50 50
                50 10 90 90 10 50 50 50 50 50
                50 10 90 90 10 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
            spawn_data_loop=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Dorsetshire', 'Rodney', 'ArkRoyal'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN_2,
            4: 'clear_boss',
        },
    ),
    'c3': Stage(
        map=dict(
            name='C3',
            shape='J6',
            camera_data=['D2', 'D4', 'G2', 'G4'],
            camera_data_spawn_point=['D4'],
            map_data="""
                -- -- ME -- ++ ++ -- ++ ++ ++
                -- ++ -- Me ++ ++ Me -- ME ME
                ++ MS -- -- MB MB -- -- -- --
                ++ -- -- -- -- -- __ ++ ++ ME
                SP -- -- MS ME ME -- ME ++ --
                -- SP -- ++ ++ ++ -- -- ME --
            """,
            weight_data="""
                50 50 50 10 90 90 10 50 50 50
                50 50 50 10 90 90 10 50 50 50
                50 50 50 10 10 10 10 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
            spawn_data_loop=[
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
            MAP_SIREN_TEMPLATE=['Kongo', 'Yamashiro', 'Shokaku', 'Zuikaku'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN_2,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd1': Stage(
        map=dict(
            name='D1',
            shape='I8',
            camera_data=['D3', 'D6', 'F3', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- -- ++ -- -- ME ++ ++ ++
                -- ++ ++ Me -- -- ME -- --
                ++ ++ ++ -- ++ -- -- -- MB
                -- Me -- Me -- -- ME -- --
                -- -- MS -- __ MS ++ ++ ME
                ++ ++ ++ -- -- -- ++ ME --
                ++ -- SP -- MS -- -- -- ME
                ++ -- SP -- ++ ME -- ME --
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
                {'battle': 0, 'enemy': 4, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'enemy': 1, 'boss': 1},
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
            MAP_SIREN_TEMPLATE=['Z24', 'Nuremberg', 'Carabiniere'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 238),
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
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
            EDGE_LINES_HOUGHLINES_THRESHOLD=40,
            COINCIDENT_POINT_ENCOURAGE_DISTANCE=1.5,
            HOMO_EDGE_HOUGHLINES_THRESHOLD=180,
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
            MAP_SWIPE_MULTIPLY=(1.033, 1.053),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.999, 1.018),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.97, 0.988),
            MAP_ENEMY_TEMPLATE=['LightInvertedOrthant', 'MainInvertedOrthant', 'CarrierInvertedOrthant'],
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
        ),
        battle={
            0: [
                'clear_siren',
                'clear_enemy(scale=(1,))',
                "clear_enemy(scale=(2,), genre=['LightInvertedOrthant', 'MainInvertedOrthant'])",
                "clear_enemy(scale=(3,), genre=['LightInvertedOrthant', 'MainInvertedOrthant'])",
                "clear_enemy(scale=(2,), genre=['Enemy', 'CarrierInvertedOrthant'])",
                "clear_enemy(scale=(3,), genre=['Enemy', 'CarrierInvertedOrthant'])",
                'battle_default',
            ],
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd2': Stage(
        map=dict(
            name='D2',
            shape='K7',
            camera_data=['D3', 'D5', 'H3', 'H5'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- ++ -- ++ ++ ++ MB MB ++ ++ ++
                -- -- -- ++ -- ME -- -- -- ME ++
                SP -- SP ++ ME -- ++ ME -- ME ++
                -- -- -- -- -- __ -- ++ -- -- --
                ++ -- ++ ++ ME -- ME -- -- Me Me
                MS -- MS ++ -- -- -- -- Me ++ ++
                -- MS -- ME -- ME ++ ++ ++ ++ ++
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
                {'battle': 0, 'enemy': 4, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'boss': 1},
            ],
            spawn_data_loop=[
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
            MAP_SIREN_TEMPLATE=['Z24', 'Carabiniere', 'Kongo', 'Yamashiro'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(1.167, 1.189),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.128, 1.149),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.095, 1.115),
        ),
        battle={
            0: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        map=dict(
            name='D3',
            shape='J10',
            camera_data=['D2', 'D6', 'D8', 'G2', 'G6', 'G8'],
            camera_data_spawn_point=['D8', 'G8'],
            map_data="""
                ++ -- -- ME -- -- ME -- -- ++
                -- -- ++ -- MB MB -- ++ -- --
                ++ -- -- ME -- -- ME -- -- ++
                -- ++ ++ ME -- -- ME ++ ++ --
                ++ ++ MS -- __ __ -- MS ++ ++
                ++ ME -- -- ++ ++ -- -- ME ++
                -- ME -- Me ++ ++ Me -- ME --
                ++ ++ -- -- Me Me -- -- ++ ++
                -- ++ MS -- -- -- -- MS ++ --
                -- ++ ++ ++ SP SP ++ ++ ++ --
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
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 4, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'boss': 1},
            ],
            spawn_data_loop=[
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
            MAP_SIREN_TEMPLATE=['BBpurple', 'CVpurple', 'Intruder'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(0.946, 0.963),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.914, 0.931),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.888, 0.904),
            MAP_ENEMY_GENRE_DETECTION_SCALING={'BBpurple': 1.111, 'CVpurple': 1.111},
            MAP_ENEMY_TEMPLATE=['MainPurple', 'CarrierPurple'],
        ),
        battle={
            0: [
                'fleet_2_protect',
                'clear_siren',
                "clear_enemy(scale=(2,), genre=['LightInvertedOrthant', 'MainInvertedOrthant'])",
                "clear_enemy(scale=(3,), genre=['LightInvertedOrthant', 'MainInvertedOrthant'])",
                "clear_enemy(scale=(2,), genre=['Enemy', 'CarrierInvertedOrthant'])",
                "clear_enemy(scale=(3,), genre=['Enemy', 'CarrierInvertedOrthant'])",
                'battle_default',
            ],
            5: [
                'fleet_2_protect',
                'clear_siren',
                'clear_enemy(scale=(1,))',
                "clear_enemy(scale=(2,), genre=['LightInvertedOrthant', 'MainInvertedOrthant'])",
                "clear_enemy(scale=(3,), genre=['LightInvertedOrthant', 'MainInvertedOrthant'])",
                "clear_enemy(scale=(2,), genre=['Enemy', 'CarrierInvertedOrthant'])",
                "clear_enemy(scale=(3,), genre=['Enemy', 'CarrierInvertedOrthant'])",
                'battle_default',
            ],
            6: 'fleet_boss.clear_boss',
        },
    ),
    'sp': Stage(
        map=dict(
            name='SP',
            shape='M10',
            camera_data=['F6', 'I6', 'G8'],
            camera_data_spawn_point=['D8'],
            map_data="""
                -- -- -- -- -- -- -- -- -- -- -- -- --
                -- -- -- -- -- ++ ++ -- -- -- -- -- --
                -- ++ ++ ++ -- -- ++ -- -- ++ ++ ++ --
                -- -- ++ ++ ++ ++ ++ ++ ++ ++ ++ -- --
                -- -- ME -- ++ ++ ++ ++ ++ -- ME -- --
                -- -- -- ME -- -- ++ -- -- ME -- -- --
                -- -- -- -- ME ++ MB ++ ME -- Me Me --
                -- SP -- -- -- MS -- MS -- -- ++ ++ --
                -- -- SP -- -- -- __ -- -- -- ++ ++ --
                -- -- -- -- -- MS -- MS -- -- -- -- --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'enemy': 1},
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Z24', 'Nuremberg', 'PeterStrasser'],
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
                'height': (150, 238),
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
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
            EDGE_LINES_HOUGHLINES_THRESHOLD=40,
            COINCIDENT_POINT_ENCOURAGE_DISTANCE=1.5,
            HOMO_EDGE_HOUGHLINES_THRESHOLD=180,
            MAP_SWIPE_MULTIPLY=(0.946, 0.963),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.914, 0.931),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.888, 0.904),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
        ),
        battle={
            0: PLAN,
            7: 'fleet_boss.clear_boss',
        },
    ),
}
