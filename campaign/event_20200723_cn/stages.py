"""
Stages of event_20200723_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

PLAN = ['clear_siren', 'battle_default']
PLAN_2 = [
    'clear_siren',
    'clear_enemy(scale=(1,))',
    "clear_enemy(scale=(2,), genre=['light', 'main', 'enemy', 'carrier'])",
    "clear_enemy(genre=['light', 'main', 'enemy'])",
    'battle_default',
]
PLAN_3 = [
    'clear_enemy(scale=(1,))',
    "clear_enemy(scale=(2,), genre=['light', 'main', 'enemy', 'carrier'])",
    "clear_enemy(genre=['light', 'main', 'enemy'])",
    'battle_default',
]

STAGES = {
    'a1': Stage(
        map=dict(
            name='A1',
            shape='I7',
            camera_data=['D3', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D3'],
            map_data="""
                ++ ++ MS ME Me ++ ME -- --
                ++ ME -- -- -- -- -- Me --
                SP -- Me ++ ++ ++ -- -- ME
                -- -- -- MB -- MB -- ++ ++
                SP -- -- -- __ -- MS ++ ++
                -- ++ Me MS ++ ++ -- ME --
                ME -- ME -- -- ME -- ME --
            """,
            weight_data="""
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            SUBMARINE=0,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_SIREN=True,
            MAP_HAS_DYNAMIC_RED_BORDER=False,
            MAP_HAS_MAP_STORY=True,
            MAP_SIREN_COUNT=1,
            HOMO_EDGE_HOUGHLINES_THRESHOLD=280,
            MAP_SIREN_TEMPLATE=['U73', 'U81', 'U552'],
            MAP_SWIPE_MULTIPLY=(1.191, 1.213),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.152, 1.173),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.118, 1.138),
        ),
        battle={
            0: PLAN,
            3: 'fleet_1.clear_boss',
        },
    ),
    'a2': Stage(
        map=dict(
            name='A2',
            shape='J6',
            camera_data=['D2', 'D4', 'G2', 'G4'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- ++ ME MS ++ MB MB MB ++ --
                Me -- ME -- ++ -- -- -- ME ME
                -- SP -- -- -- -- Me -- -- --
                -- SP -- -- MS ++ ++ __ ME --
                Me -- ME -- -- ++ ME -- -- ME
                -- ++ ++ MS -- Me -- -- ME ++
            """,
            weight_data="""
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Deutschland', 'Tirpitz', 'Gneisenau', 'Scharnhorst', 'Spee'],
        ),
        battle={
            0: PLAN,
            4: 'fleet_boss.clear_boss',
        },
    ),
    'a3': Stage(
        map=dict(
            name='A3',
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ME ++ ++ ++ ME -- -- --
                -- -- Me ME -- ++ ++ ME
                -- ME ++ Me -- ME -- --
                -- Me __ MB MB __ -- ++
                -- MS -- MB MB -- MS --
                ++ ++ Me -- -- Me ++ ME
                ++ ME -- -- -- -- ME --
                MS -- -- SP SP -- -- MS
            """,
            weight_data="""
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DDpurple', 'CLpurple'],
        ),
        battle={
            0: PLAN,
            4: 'fleet_boss.clear_boss',
        },
    ),
    'b1': Stage(
        map=dict(
            name='B1',
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['D2'],
            map_data="""
                ++ ++ ++ ME -- ME -- ++ --
                SP -- Me -- -- -- Me -- ME
                SP -- -- ++ MS -- -- -- --
                SP -- -- -- __ -- MS ++ ++
                ++ ++ Me -- -- -- Me ++ --
                ++ ++ -- -- MS -- -- ME --
                -- ME -- MB ++ MB -- -- ME
                -- ME -- ME ++ -- ME -- ++
            """,
            weight_data="""
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
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
            SUBMARINE=0,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_SIREN=True,
            MAP_HAS_DYNAMIC_RED_BORDER=False,
            MAP_HAS_MAP_STORY=True,
            MAP_SIREN_COUNT=1,
            DETECTION_BACKEND='homography',
            HOMO_STORAGE=((9, 5), [(239.4, 150.511), (1280.977, 150.511), (142.318, 609.21), (1439.411, 609.21)]),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=280,
            MAP_SIREN_TEMPLATE=['U101', 'U73', 'U552'],
            MAP_SWIPE_MULTIPLY=(1.191, 1.213),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.152, 1.173),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.118, 1.138),
        ),
        battle={
            0: PLAN,
            4: 'fleet_1.clear_boss',
        },
    ),
    'b2': Stage(
        map=dict(
            name='B2',
            shape='K7',
            camera_data=['D2', 'D5', 'H2', 'H5'],
            camera_data_spawn_point=['H2', 'H5'],
            map_data="""
                -- ME -- -- MS -- ++ ++ ++ -- --
                ME ++ MS -- -- Me -- -- -- Me --
                -- ME -- ME __ -- -- SP -- -- --
                -- -- ME ++ ++ Me -- -- -- -- MB
                ME -- -- ++ MS -- -- SP -- -- --
                -- ME -- -- -- Me -- -- -- Me --
                ++ -- ME -- MS -- ++ ++ ++ -- --
            """,
            weight_data="""
                10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10
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
            MAP_SIREN_TEMPLATE=['Deutschland', 'Tirpitz', 'Gneisenau', 'Scharnhorst', 'Spee'],
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'b3': Stage(
        map=dict(
            name='B3',
            in_map_swipe_preset_data=(1, 1),
            shape='I10',
            camera_data=['E3', 'E5', 'C6', 'F6'],
            camera_data_spawn_point=['E7'],
            map_data="""
                ++ ++ -- -- Me -- -- ++ ++
                ++ -- -- ME __ ME -- -- ++
                -- -- Me -- MS -- Me -- --
                -- ME -- ++ -- ++ -- ME --
                -- -- MS -- MB -- MS -- --
                -- ME -- ++ -- ++ -- ME --
                -- -- Me -- MS -- Me -- --
                ME -- -- -- -- -- -- -- ME
                ++ ++ -- SP -- SP -- ++ ++
                ++ ++ -- -- -- -- -- ++ ++
            """,
            weight_data="""
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
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
            MAP_SIREN_TEMPLATE=['ELpurple', 'CLpurple', 'CApurple'],
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 215),
                'width': (0.9, 50),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (231, 255),
                'prominence': 2,
                'distance': 50,
                'wlen': 1000,
            },
            MID_DIFF_RANGE_H=(141, 147),
            MID_DIFF_RANGE_V=(141, 147),
            DETECTION_BACKEND='homography',
            HOMO_STORAGE=((7, 5), [(198.047, 82.241), (1078.103, 82.241), (93.21, 506.071), (1183.061, 506.071)]),
            HOMO_TILE=(168, 140),
            HOMO_CENTER_OFFSET=(62, 48),
            GRID_IMAGE_A_MULTIPLY=0.8333333333333334,
            MAP_SWIPE_MULTIPLY=(1.006, 1.025),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.973, 0.991),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.944, 0.961),
        ),
        battle={
            0: PLAN,
            5: 'fleet_1.clear_boss',
        },
    ),
    'c1': Stage(
        map=dict(
            name='C1',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D3'],
            map_data="""
                ++ ++ MS ME Me ++ ME -- --
                ++ ME -- -- -- -- -- Me --
                SP -- Me ++ ++ ++ -- -- ME
                -- -- -- MB -- MB -- ++ ++
                SP -- -- -- __ -- MS ++ ++
                -- ++ Me MS ++ ++ -- ME --
                ME -- ME -- -- ME -- ME --
            """,
            weight_data="""
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
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
            SUBMARINE=0,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_SIREN=True,
            MAP_HAS_DYNAMIC_RED_BORDER=False,
            MAP_HAS_MAP_STORY=True,
            MAP_SIREN_COUNT=2,
            HOMO_EDGE_HOUGHLINES_THRESHOLD=280,
            MAP_SIREN_TEMPLATE=['U73', 'U81', 'U552'],
            MAP_SWIPE_MULTIPLY=(1.191, 1.213),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.152, 1.173),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.118, 1.138),
        ),
        battle={
            0: PLAN,
            4: 'fleet_1.clear_boss',
        },
    ),
    'c2': Stage(
        map=dict(
            name='C2',
            shape='J6',
            camera_data=['D2', 'D4', 'G2', 'G4'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- ++ ME MS ++ MB MB MB ++ --
                Me -- ME -- ++ -- -- -- ME ME
                -- SP -- -- -- -- Me -- -- --
                -- SP -- -- MS ++ ++ __ ME --
                Me -- ME -- -- ++ ME -- -- ME
                -- ++ ++ MS -- Me -- -- ME ++
            """,
            weight_data="""
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
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
            MAP_SIREN_TEMPLATE=['Deutschland', 'Tirpitz', 'Gneisenau', 'Scharnhorst', 'Spee'],
        ),
        battle={
            0: PLAN_2,
            4: 'fleet_boss.clear_boss',
        },
    ),
    'c3': Stage(
        map=dict(
            name='C3',
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ME ++ ++ ++ ME -- -- --
                -- -- Me ME -- ++ ++ ME
                -- ME ++ Me -- ME -- --
                -- Me __ MB MB __ -- ++
                -- MS -- MB MB -- MS --
                ++ ++ Me -- -- Me ++ ME
                ++ ME -- -- -- -- ME --
                MS -- -- SP SP -- -- MS
            """,
            weight_data="""
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
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
            MAP_SIREN_TEMPLATE=['CLpurple', 'BBpurple'],
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
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['D2'],
            map_data="""
                ++ ++ ++ ME -- ME -- ++ --
                SP -- Me -- -- -- Me -- ME
                SP -- -- ++ MS -- -- -- --
                SP -- -- -- __ -- MS ++ ++
                ++ ++ Me -- -- -- Me ++ --
                ++ ++ -- -- MS -- -- ME --
                -- ME -- MB ++ MB -- -- ME
                -- ME -- ME ++ -- ME -- ++
            """,
            weight_data="""
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
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
            SUBMARINE=0,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_SIREN=True,
            MAP_HAS_DYNAMIC_RED_BORDER=False,
            MAP_HAS_MAP_STORY=True,
            MAP_SIREN_COUNT=2,
            DETECTION_BACKEND='homography',
            HOMO_STORAGE=((6, 6), [(583.092, 82.574), (1247.528, 82.574), (564.74, 614.947), (1434.046, 614.947)]),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=350,
            MAP_SIREN_TEMPLATE=['U101', 'U73', 'U552'],
            MAP_SWIPE_MULTIPLY=(1.191, 1.213),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.152, 1.173),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.118, 1.138),
        ),
        battle={
            0: PLAN_2,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd2': Stage(
        map=dict(
            name='D2',
            shape='K7',
            camera_data=['D2', 'D5', 'H2', 'H5'],
            camera_data_spawn_point=['H2', 'H5'],
            map_data="""
                -- ME -- -- MS -- ++ ++ ++ -- --
                ME ++ MS -- -- Me -- -- -- Me --
                -- ME -- ME __ -- -- SP -- -- --
                -- -- ME ++ ++ Me -- -- -- -- MB
                ME -- -- ++ MS -- -- SP -- -- --
                -- ME -- -- -- Me -- -- -- Me --
                ++ -- ME -- MS -- ++ ++ ++ -- --
            """,
            weight_data="""
                10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10
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
            MAP_SIREN_TEMPLATE=['Deutschland', 'Tirpitz', 'Gneisenau', 'Scharnhorst', 'Spee'],
        ),
        battle={
            0: [
                'clear_siren',
                "clear_enemy(scale=(2,), genre=['light', 'main', 'enemy', 'carrier'])",
                "clear_enemy(genre=['light', 'main', 'enemy'])",
                'battle_default',
            ],
            5: PLAN_3,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        map=dict(
            name='D3',
            in_map_swipe_preset_data=(1, 1),
            shape='I10',
            camera_data=['E3', 'E5', 'C6', 'F6'],
            camera_data_spawn_point=['E7'],
            map_data="""
                ++ ++ -- -- Me -- -- ++ ++
                ++ -- -- ME __ ME -- -- ++
                -- -- Me -- MS -- Me -- --
                -- ME -- ++ -- ++ -- ME --
                -- -- MS -- MB -- MS -- --
                -- ME -- ++ -- ++ -- ME --
                -- -- Me -- MS -- Me -- --
                ME -- -- -- -- -- -- -- ME
                ++ ++ -- SP -- SP -- ++ ++
                ++ ++ -- -- -- -- -- ++ ++
            """,
            weight_data="""
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
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
            MAP_SIREN_TEMPLATE=['ELpurple', 'CVpurple', 'BBpurple'],
            DETECTION_BACKEND='perspective',
            HOMO_STORAGE=((8, 5), [(200.097, 82.51), (1200.298, 82.51), (95.065, 506.098), (1335.813, 506.098)]),
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 215),
                'width': (0.9, 50),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (231, 255),
                'prominence': 2,
                'distance': 50,
                'wlen': 1000,
            },
            MID_DIFF_RANGE_H=(141, 147),
            MID_DIFF_RANGE_V=(141, 147),
            HOMO_TILE=(168, 140),
            HOMO_CENTER_OFFSET=(62, 48),
            GRID_IMAGE_A_MULTIPLY=0.8333333333333334,
            MAP_SWIPE_MULTIPLY=(1.006, 1.025),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.973, 0.991),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.944, 0.961),
        ),
        battle={
            0: [
                'clear_siren',
                "clear_enemy(scale=(2,), genre=['light', 'main', 'enemy', 'carrier'])",
                "clear_enemy(scale=(3,), genre=['light', 'main', 'enemy'])",
                'battle_default',
            ],
            5: PLAN_3,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'sp': Stage(
        map=dict(
            name='SP',
            shape='M10',
            camera_data=['D5', 'E8', 'J6', 'I8', 'G8'],
            camera_data_spawn_point=['G8'],
            map_data="""
                -- -- -- -- -- -- -- -- -- -- -- -- --
                -- -- -- -- -- ++ ++ -- -- -- -- -- --
                -- ++ ++ ++ -- -- ++ -- -- ++ ++ ++ --
                -- ME ++ ++ ++ ++ ++ ++ ++ ++ ++ Me --
                Me -- Me -- ++ ++ ++ ++ ++ -- Me -- Me
                -- -- -- MS Me -- ++ -- Me MS -- -- --
                -- ME -- -- -- ++ MB ++ -- -- -- ME --
                ME -- ME -- -- MS -- MS -- -- ME -- ME
                -- ME -- -- -- -- __ -- -- -- -- ME --
                -- -- -- SP -- -- -- -- -- SP -- -- --
            """,
            weight_data="""
                10 10 10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10 10 10
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
        ),
        config=dict(
            SUBMARINE=0,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_SIREN=True,
            MAP_HAS_DYNAMIC_RED_BORDER=False,
            MAP_SIREN_COUNT=3,
            STAR_REQUIRE_3=0,
            DETECTION_BACKEND='homography',
            HOMO_STORAGE=((10, 6), [(172.714, 96.467), (1291.455, 96.467), (27.369, 639.803), (1491.921, 639.803)]),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=280,
            MAP_SIREN_TEMPLATE=['Deutschland', 'Tirpitz', 'Gneisenau', 'Scharnhorst', 'Spee'],
            MAP_SWIPE_MULTIPLY=(1.006, 1.025),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.973, 0.991),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.944, 0.961),
        ),
        battle={
            0: ['clear_siren', 'clear_enemy(scale=(2,))', 'clear_enemy(scale=(3,))', 'battle_default'],
            5: ['clear_enemy(scale=(1,))', 'clear_enemy(scale=(2,))', 'battle_default'],
            7: 'fleet_boss.clear_boss',
        },
    ),
}
