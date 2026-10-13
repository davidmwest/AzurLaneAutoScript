"""
Stages of event_20220728_cn, see module/campaign/stage.py
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
            shape='H8',
            camera_data=['D3', 'D6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ -- -- -- -- ME -- --
                ++ -- ++ ++ Me -- ME --
                -- ME ++ ++ -- -- -- ++
                ME -- -- MB -- Me -- ME
                -- -- MS -- -- MS -- --
                ME ++ ++ __ __ ++ ++ --
                -- -- Me -- -- Me -- --
                -- ME -- SP SP -- ME --
            """,
            map_data_loop="""
                ++ -- -- -- -- ME -- --
                ++ -- ++ ++ Me -- ME --
                -- ME ++ ++ -- -- -- ++
                ME -- -- MB -- Me -- ME
                -- -- MS -- -- MS -- --
                ME ++ -- __ __ ++ ++ ++
                -- -- Me -- -- Me -- --
                -- ME -- SP SP -- ME --
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
                {'battle': 3, 'enemy': 1, 'boss': 1},
                {'battle': 4, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['DD', 'Juno_ghost'],
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
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
            MAP_ENEMY_TEMPLATE=['Light', 'Main', 'Carrier', 'Treasure', 'Vestal_ghost'],
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
            shape='L7',
            camera_data=['D3', 'F5', 'H5'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- SP -- ++ ++ ++ Me -- -- -- -- --
                SP -- -- -- -- MS -- ++ ++ -- ++ ++
                -- -- Me MS -- -- -- ++ ++ ME ++ ++
                Me -- -- -- ++ ++ -- -- ME -- -- MB
                -- ++ ++ Me ++ ++ Me -- __ -- ME --
                -- ++ ++ -- -- ME -- -- -- -- ME ++
                -- -- ME -- -- -- -- ME ++ ME -- --
            """,
            map_data_loop="""
                -- SP -- ++ ++ ++ Me -- -- -- -- --
                SP -- -- -- -- MS -- -- ++ -- ++ ++
                -- -- Me MS -- -- -- -- ++ ME -- ++
                Me -- -- -- ++ ++ ++ -- ME -- -- MB
                -- ++ ++ Me -- -- Me -- __ -- ME --
                -- ++ ++ -- -- ME -- -- -- -- ME ++
                -- -- ME -- -- -- -- ME ++ ME -- --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['CL', 'Juno_ghost'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.226, 1.249),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.186, 1.208),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.151, 1.172),
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
            shape='I8',
            camera_data=['D3', 'E6'],
            camera_data_spawn_point=['E2'],
            map_data="""
                -- -- -- -- SP SP -- -- --
                -- ME ++ ++ -- -- ++ ++ --
                ME -- -- MS -- ME ++ ++ --
                -- ++ ++ Me -- MS ME Me --
                -- ++ ++ -- __ -- -- -- ME
                -- -- Me -- ME Me ME ME --
                -- ++ ++ -- -- -- ME -- --
                -- -- ++ -- MB -- ++ ++ ++
            """,
            map_data_loop="""
                -- -- -- -- SP SP -- -- --
                -- ME ++ -- -- -- ++ ++ --
                ME -- -- MS -- ME ++ ++ --
                -- -- ++ Me -- MS ME Me --
                -- -- ++ -- __ -- -- -- ME
                -- -- Me -- ME Me ME ME --
                -- ++ ++ -- -- -- ME -- --
                -- -- ++ -- MB -- ++ ++ ++
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
            MAP_SIREN_TEMPLATE=['CA', 'Neptune_ghost'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.226, 1.249),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.186, 1.208),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.151, 1.172),
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
            shape='J8',
            camera_data=['E2', 'E6', 'G4'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- -- ME -- -- Me -- -- ++ ++
                -- -- ++ MS -- -- Me -- MB ++
                SP -- -- -- MS ++ ++ -- -- ME
                SP -- -- -- MS ++ ++ ME -- --
                -- -- ++ MS __ ME Me -- -- ME
                -- Me ++ Me -- -- -- -- ME --
                -- -- -- -- -- ME -- ME -- --
                -- ME -- ME -- -- ++ ++ ++ --
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
                {'battle': 5, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Neptune_ghost', 'LeMars_ghost'],
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
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
            MAP_ENEMY_TEMPLATE=['Light', 'Main', 'Carrier', 'Treasure', 'Vestal_ghost'],
            MAP_SWIPE_MULTIPLY=(1.141, 1.163),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.104, 1.124),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.071, 1.091),
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
            camera_data=['D2', 'D3', 'E3', 'E6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                -- ME -- -- -- ME -- ME --
                ++ -- -- ME -- -- ++ -- ME
                ++ ME Me ++ Me -- -- -- Me
                -- -- -- ME -- -- -- MS --
                MB -- __ -- -- MS -- -- ++
                -- -- -- Me -- ++ Me -- --
                ++ ++ ME -- MS -- -- -- SP
                ++ ++ -- ME -- ME -- SP --
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
            MAP_SIREN_TEMPLATE=['Neptune_ghost', 'LeMars_ghost'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.038, 1.058),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.004, 1.023),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.975, 0.993),
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
            camera_data=['D3', 'D5', 'F3', 'F5'],
            camera_data_spawn_point=['E7'],
            map_data="""
                -- ++ ++ ++ -- ++ ++ ++ --
                -- ME -- -- ME -- -- ME --
                ME -- -- ME -- ME -- -- ME
                ++ -- Me ++ -- ++ Me -- ++
                ME -- -- -- MB -- -- -- ME
                -- -- Me ++ MS ++ Me -- --
                ME -- MS -- __ -- MS -- ME
                ++ ++ -- -- -- -- -- ++ ++
                ++ ++ -- SP -- SP -- ++ ++
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
            MAP_SIREN_TEMPLATE=['LeMars_ghost', 'Hermes_ghost'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(0.994, 1.013),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.961, 0.979),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.933, 0.95),
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
            shape='H8',
            camera_data=['D3', 'D6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ -- -- -- -- ME -- --
                ++ -- ++ ++ Me -- ME --
                -- ME ++ ++ -- -- -- ++
                ME -- -- MB -- Me -- ME
                -- -- MS -- -- MS -- --
                ME ++ ++ __ __ ++ ++ --
                -- -- Me -- -- Me -- --
                -- ME -- SP SP -- ME --
            """,
            map_data_loop="""
                ++ -- -- -- -- ME -- --
                ++ -- ++ ++ Me -- ME --
                -- ME ++ ++ -- -- -- ++
                ME -- -- MB -- Me -- ME
                -- -- MS -- -- MS -- --
                ME ++ -- __ __ ++ ++ ++
                -- -- Me -- -- Me -- --
                -- ME -- SP SP -- ME --
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
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA', 'Juno_ghost', 'Neptune_ghost'],
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
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
            MAP_ENEMY_TEMPLATE=['Light', 'Main', 'Carrier', 'Treasure', 'Vestal_ghost'],
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
            shape='L7',
            camera_data=['D3', 'F5', 'H5'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- SP -- ++ ++ ++ Me -- -- -- -- --
                SP -- -- -- -- MS -- ++ ++ -- ++ ++
                -- -- Me MS -- -- -- ++ ++ ME ++ ++
                Me -- -- -- ++ ++ -- -- ME -- -- MB
                -- ++ ++ Me ++ ++ Me -- __ -- ME --
                -- ++ ++ -- -- ME -- -- -- -- ME ++
                -- -- ME -- -- -- -- ME ++ ME -- --
            """,
            map_data_loop="""
                -- SP -- ++ ++ ++ Me -- -- -- -- --
                SP -- -- -- -- MS -- -- ++ -- ++ ++
                -- -- Me MS -- -- -- -- ++ ME -- ++
                Me -- -- -- ++ ++ ++ -- ME -- -- MB
                -- ++ ++ Me -- -- Me -- __ -- ME --
                -- ++ ++ -- -- ME -- -- -- -- ME ++
                -- -- ME -- -- -- -- ME ++ ME -- --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['CA', 'BB', 'Juno_ghost', 'Neptune_ghost'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.226, 1.249),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.186, 1.208),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.151, 1.172),
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
            shape='I8',
            camera_data=['D3', 'E6'],
            camera_data_spawn_point=['E2'],
            map_data="""
                -- -- -- -- SP SP -- -- --
                -- ME ++ ++ -- -- ++ ++ --
                ME -- -- MS -- ME ++ ++ --
                -- ++ ++ Me -- MS ME Me --
                -- ++ ++ -- __ -- -- -- ME
                -- -- Me -- ME Me ME ME --
                -- ++ ++ -- -- -- ME -- --
                -- -- ++ -- MB -- ++ ++ ++
            """,
            map_data_loop="""
                -- -- -- -- SP SP -- -- --
                -- ME ++ -- -- -- ++ ++ --
                ME -- -- MS -- ME ++ ++ --
                -- -- ++ Me -- MS ME Me --
                -- -- ++ -- __ -- -- -- ME
                -- -- Me -- ME Me ME ME --
                -- ++ ++ -- -- -- ME -- --
                -- -- ++ -- MB -- ++ ++ ++
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
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CA', 'BB', 'Juno_ghost', 'Neptune_ghost'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.226, 1.249),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.186, 1.208),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.151, 1.172),
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
            shape='J8',
            camera_data=['E2', 'E6', 'G4'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- -- ME -- -- Me -- -- ++ ++
                -- -- ++ MS -- -- Me -- MB ++
                SP -- -- -- MS ++ ++ -- -- ME
                SP -- -- -- MS ++ ++ ME -- --
                -- -- ++ MS __ ME Me -- -- ME
                -- Me ++ Me -- -- -- -- ME --
                -- -- -- -- -- ME -- ME -- --
                -- ME -- ME -- -- ++ ++ ++ --
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
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Neptune_ghost', 'LeMars_ghost'],
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
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
            MAP_ENEMY_TEMPLATE=['Light', 'Main', 'Carrier', 'Treasure', 'Vestal_ghost'],
            MAP_SWIPE_MULTIPLY=(1.141, 1.163),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.104, 1.124),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.071, 1.091),
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
            camera_data=['D2', 'D3', 'E3', 'E6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                -- ME -- -- -- ME -- ME --
                ++ -- -- ME -- -- ++ -- ME
                ++ ME Me ++ Me -- -- -- Me
                -- -- -- ME -- -- -- MS --
                MB -- __ -- -- MS -- -- ++
                -- -- -- Me -- ++ Me -- --
                ++ ++ ME -- MS -- -- -- SP
                ++ ++ -- ME -- ME -- SP --
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
            MAP_SIREN_TEMPLATE=['LeMars_ghost', 'Hermes_ghost'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.038, 1.058),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.004, 1.023),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.975, 0.993),
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
            shape='I9',
            camera_data=['D3', 'D5', 'F3', 'F5'],
            camera_data_spawn_point=['E7'],
            map_data="""
                -- ++ ++ ++ -- ++ ++ ++ --
                -- ME -- -- ME -- -- ME --
                ME -- -- ME -- ME -- -- ME
                ++ -- Me ++ -- ++ Me -- ++
                ME -- -- -- MB -- -- -- ME
                -- -- Me ++ MS ++ Me -- --
                ME -- MS -- __ -- MS -- ME
                ++ ++ -- -- -- -- -- ++ ++
                ++ ++ -- SP -- SP -- ++ ++
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
            MAP_SIREN_TEMPLATE=['LeMars_ghost', 'Hermes_ghost'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(0.994, 1.013),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.961, 0.979),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.933, 0.95),
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
            shape='S9',
            camera_data=['G6', 'I6', 'K6', 'K7'],
            camera_data_spawn_point=['K7'],
            map_data="""
                -- -- -- -- -- -- -- -- -- -- -- -- -- -- ++ ++ -- ++ ++
                -- -- -- -- -- -- -- -- -- -- -- ++ ++ -- ++ ++ -- ++ ++
                -- -- ++ ++ -- ++ ++ ME ++ ++ ME ++ ++ -- -- -- -- -- --
                -- -- -- -- ME ++ ++ -- ++ ++ -- Me -- MS -- -- -- -- --
                -- ++ ++ ME -- -- -- -- -- Me -- -- ME -- -- -- -- -- --
                -- ++ ++ -- -- MB ++ ++ -- -- __ MS -- -- SP -- -- -- --
                -- -- -- ME -- MB ++ ++ -- Me -- MS -- -- SP -- -- -- --
                -- -- -- -- ME -- -- ME -- -- -- -- -- -- -- -- -- -- --
                -- -- -- -- -- ++ ++ -- ++ ++ Me -- ME MS -- -- -- -- --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['Neptune_ghost', 'Jupiter_ghost', 'Juno_ghost'],
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
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
            MAP_ENEMY_TEMPLATE=['Light', 'Main', 'Carrier', 'Treasure', 'Vestal_ghost'],
            MAP_SWIPE_MULTIPLY=(0.992, 1.011),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.959, 0.977),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.931, 0.948),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=2)', 'battle_default'],
            5: PLAN,
            7: 'fleet_boss.clear_boss',
        },
    ),
}
