"""
Stages of event_20220414_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']
PLAN_2 = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default']

STAGES = {
    'a1': Stage(
        map=dict(
            name='A1',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D2', 'D5'],
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
                {'battle': 3, 'enemy': 1, 'boss': 1},
                {'battle': 4},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['U81', 'U101', 'U522'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            DETECTION_BACKEND='homography',
            HOMO_STORAGE=((7, 6), [(263.285, 83.378), (1045.503, 83.378), (149.679, 616.57), (1168.955, 616.57)]),
            HOMO_EDGE_COLOR_RANGE=(0, 13),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=350,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(1.105, 1.126),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.069, 1.089),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.038, 1.056),
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
            shape='J6',
            camera_data=['D2', 'D4', 'G2', 'G4'],
            camera_data_spawn_point=['D2', 'D4'],
            map_data="""
                -- ++ ME MS ++ MB MB MB ++ --
                Me -- ME -- ++ -- -- -- ME ME
                -- SP -- -- -- -- Me -- -- --
                -- SP -- -- MS ++ ++ __ ME --
                Me -- ME -- -- ++ ME -- -- ME
                -- ++ ++ MS -- Me -- -- ME ++
            """,
            weight_data="""
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Scharnhorst', 'Deutschland', 'Spee', 'Gneisenau', 'Tirpitz'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.143, 1.165),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.106, 1.126),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.073, 1.093),
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
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['E6', 'D6'],
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DDpurple', 'CLpurple'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.034, 1.053),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.0, 1.018),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.971, 0.988),
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
            MAP_SIREN_TEMPLATE=['U73', 'U101', 'U522'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            DETECTION_BACKEND='homography',
            HOMO_STORAGE=((9, 5), [(239.4, 150.511), (1280.977, 150.511), (142.318, 609.21), (1439.411, 609.21)]),
            HOMO_EDGE_COLOR_RANGE=(0, 13),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=350,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(1.167, 1.189),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.128, 1.149),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.095, 1.115),
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
            shape='K7',
            camera_data=['D2', 'D5', 'H2', 'H5'],
            camera_data_spawn_point=['H5', 'H2'],
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
            MAP_SIREN_TEMPLATE=['Scharnhorst', 'Deutschland', 'Spee', 'Gneisenau', 'Tirpitz'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.107, 1.128),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.071, 1.091),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.04, 1.058),
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
            MAP_SIREN_TEMPLATE=['ELpurple', 'CLpurple', 'CApurple'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MID_DIFF_RANGE_H=(141, 147),
            MID_DIFF_RANGE_V=(141, 147),
            DETECTION_BACKEND='homography',
            HOMO_STORAGE=((8, 5), [(200.097, 82.51), (1200.298, 82.51), (95.065, 506.098), (1335.813, 506.098)]),
            HOMO_TILE=(168, 140),
            HOMO_CENTER_OFFSET=(62, 48),
            GRID_IMAGE_A_MULTIPLY=0.8333333333333334,
            MAP_SWIPE_MULTIPLY=(0.967, 0.985),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.935, 0.953),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.908, 0.924),
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
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D2', 'D5'],
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
            MAP_SIREN_TEMPLATE=['U81', 'U101', 'U522'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            DETECTION_BACKEND='homography',
            HOMO_STORAGE=((7, 6), [(263.285, 83.378), (1045.503, 83.378), (149.679, 616.57), (1168.955, 616.57)]),
            HOMO_EDGE_COLOR_RANGE=(0, 13),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=350,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(1.105, 1.126),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.069, 1.089),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.038, 1.056),
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
            shape='J6',
            camera_data=['D2', 'D4', 'G2', 'G4'],
            camera_data_spawn_point=['D2', 'D4'],
            map_data="""
                -- ++ ME MS ++ MB MB MB ++ --
                Me -- ME -- ++ -- -- -- ME ME
                -- SP -- -- -- -- Me -- -- --
                -- SP -- -- MS ++ ++ __ ME --
                Me -- ME -- -- ++ ME -- -- ME
                -- ++ ++ MS -- Me -- -- ME ++
            """,
            weight_data="""
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
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Scharnhorst', 'Deutschland', 'Spee', 'Gneisenau', 'Tirpitz'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.143, 1.165),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.106, 1.126),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.073, 1.093),
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
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['E6', 'D6'],
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
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CLpurple', 'BBpurple'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.034, 1.053),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.0, 1.018),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.971, 0.988),
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
            MAP_SIREN_TEMPLATE=['U73', 'U101', 'U522'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            DETECTION_BACKEND='homography',
            HOMO_STORAGE=((9, 5), [(239.4, 150.511), (1280.977, 150.511), (142.318, 609.21), (1439.411, 609.21)]),
            HOMO_EDGE_COLOR_RANGE=(0, 13),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=350,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(1.167, 1.189),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.128, 1.149),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.095, 1.115),
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
            shape='K7',
            camera_data=['D2', 'D5', 'H2', 'H5'],
            camera_data_spawn_point=['H5', 'H2'],
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
            MAP_SIREN_TEMPLATE=['Scharnhorst', 'Deutschland', 'Spee', 'Gneisenau', 'Tirpitz'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.107, 1.128),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.071, 1.091),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.04, 1.058),
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
            shape='I10',
            camera_data=['D2', 'D6', 'D7', 'F2', 'F6', 'F7'],
            camera_data_spawn_point=['F7', 'D7'],
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
            MAP_SIREN_TEMPLATE=['ELpurple', 'CVpurple', 'BBpurple'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MID_DIFF_RANGE_H=(141, 147),
            MID_DIFF_RANGE_V=(141, 147),
            DETECTION_BACKEND='homography',
            HOMO_STORAGE=((8, 5), [(200.097, 82.51), (1200.298, 82.51), (95.065, 506.098), (1335.813, 506.098)]),
            HOMO_TILE=(168, 140),
            HOMO_CENTER_OFFSET=(62, 48),
            GRID_IMAGE_A_MULTIPLY=0.8333333333333334,
            MAP_SWIPE_MULTIPLY=(0.967, 0.985),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.935, 0.953),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.908, 0.924),
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
            shape='M10',
            camera_data=['D5', 'D8', 'J5', 'J8'],
            camera_data_spawn_point=['D8', 'J8'],
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
            MAP_SIREN_TEMPLATE=['Scharnhorst', 'Deutschland', 'Spee', 'Gneisenau', 'Tirpitz'],
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
            DETECTION_BACKEND='homography',
            HOMO_STORAGE=((10, 6), [(172.714, 96.467), (1291.455, 96.467), (27.369, 639.803), (1491.921, 639.803)]),
            HOMO_EDGE_COLOR_RANGE=(0, 13),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=350,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(0.963, 0.981),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.932, 0.949),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.904, 0.921),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=2)', 'battle_default'],
            5: PLAN,
            7: 'fleet_boss.clear_boss',
        },
    ),
}
