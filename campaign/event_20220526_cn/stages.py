"""
Stages of event_20220526_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']

STAGES = {
    'a1': Stage(
        map=dict(
            name='A1',
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['E5', 'D5'],
            map_data="""
                ++ ME -- -- -- -- ++ --
                -- -- -- ME ME -- -- ME
                ME -- Me ++ ++ ME -- --
                -- -- -- MB ++ -- Me --
                ME ++ MS __ __ MS -- --
                -- Me -- -- -- -- Me --
                ++ ++ ++ SP SP ++ ++ ++
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
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1, 'boss': 1},
                {'battle': 4, 'enemy': 1},
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
            MAP_SIREN_HAS_BOSS_ICON=True,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
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
            HOMO_EDGE_COLOR_RANGE=(0, 49),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(1.084, 1.104),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.048, 1.067),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.017, 1.036),
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
            shape='H8',
            camera_data=['D3', 'D6'],
            camera_data_spawn_point=['D3', 'D6'],
            map_data="""
                ++ ++ -- -- -- -- -- --
                ++ ++ ME ME ME -- ++ --
                -- Me -- -- -- MS ++ --
                ME -- -- SP -- -- Me --
                ++ Me -- -- SP -- ME --
                -- ++ MS -- -- -- Me --
                MB -- __ -- ++ ++ -- --
                -- ME ME ME -- ++ -- --
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
            MAP_SIREN_TEMPLATE=['DD'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SIREN_HAS_BOSS_ICON=False,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (120, 231),
                'width': (1.5, 10),
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
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(1.064, 1.084),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.029, 1.048),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.999, 1.017),
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
            shape='J8',
            camera_data=['E2', 'E5', 'G2', 'G5'],
            camera_data_spawn_point=['E6'],
            map_data="""
                ++ ++ -- -- -- -- -- ME -- MB
                ++ ++ ME -- ME -- ME ++ -- --
                -- -- -- -- -- Me -- -- ME --
                -- ME -- Me ++ ++ ME -- -- --
                -- ME -- -- __ ++ -- -- Me ++
                -- ME ++ MS -- Me MS -- -- ++
                -- -- Me -- -- -- -- -- ME --
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
            MAP_SIREN_HAS_BOSS_ICON=False,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=False,
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
            HOMO_EDGE_COLOR_RANGE=(0, 33),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CAred': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
            MAP_SWIPE_MULTIPLY=(1.064, 1.084),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.029, 1.048),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.999, 1.017),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b3': Stage(
        map=dict(
            name='B3',
            shape='I9',
            camera_data=['D3', 'D5', 'D7', 'F3', 'F5', 'F7'],
            camera_data_spawn_point=['F7', 'D7'],
            map_data="""
                -- ++ ++ -- MB -- ++ ++ --
                -- ++ ++ Me -- Me ++ ++ --
                ME -- -- -- -- -- -- -- ME
                -- ME ME Me -- Me ME ME --
                -- ++ ++ ++ -- ++ ++ ++ --
                -- Me ME MS -- MS ME Me --
                ME -- -- -- __ -- -- -- ME
                ++ MS -- -- -- -- -- MS ++
                ++ -- ++ SP -- SP ++ -- ++
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
            MAP_SIREN_TEMPLATE=['CA', 'BB', 'Bellona', 'Revenge'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
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
            HOMO_EDGE_COLOR_RANGE=(0, 33),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_SWIPE_MULTIPLY=(0.993, 1.011),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.96, 0.978),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.932, 0.949),
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
            camera_data_spawn_point=['E5', 'D5'],
            map_data="""
                ++ ME -- -- -- -- ++ --
                -- -- -- ME ME -- -- ME
                ME -- Me ++ ++ ME -- --
                -- -- -- MB ++ -- Me --
                ME ++ MS __ __ MS -- --
                -- Me -- -- -- -- Me --
                ++ ++ ++ SP SP ++ ++ ++
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
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
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
            MAP_SIREN_HAS_BOSS_ICON=True,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(1.084, 1.104),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.048, 1.067),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.017, 1.036),
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
            camera_data=['D3', 'D6'],
            camera_data_spawn_point=['D3', 'D6'],
            map_data="""
                ++ ++ -- -- -- -- -- --
                ++ ++ ME ME ME -- ++ --
                -- Me -- -- -- MS ++ --
                ME -- -- SP -- -- Me --
                ++ Me -- -- SP -- ME --
                -- ++ MS -- -- -- Me --
                MB -- __ -- ++ ++ -- --
                -- ME ME ME -- ++ -- --
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
            MAP_SIREN_TEMPLATE=['CL', 'CAred'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SIREN_HAS_BOSS_ICON=False,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=False,
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
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CAred': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
            MAP_SWIPE_MULTIPLY=(1.225, 1.248),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.185, 1.207),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.15, 1.171),
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
            camera_data=['E2', 'E5', 'G2', 'G5'],
            camera_data_spawn_point=['E6'],
            map_data="""
                ++ ++ -- -- -- -- -- ME -- MB
                ++ ++ ME -- ME -- ME ++ -- --
                -- -- -- -- -- Me -- -- ME --
                -- ME -- Me ++ ++ ME -- -- --
                -- ME -- -- __ ++ -- -- Me ++
                -- ME ++ MS -- Me MS -- -- ++
                -- -- Me -- -- -- -- -- ME --
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
            MAP_SIREN_HAS_BOSS_ICON=False,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=False,
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
            HOMO_EDGE_COLOR_RANGE=(0, 33),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CAred': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
            MAP_SWIPE_MULTIPLY=(1.076, 1.097),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.041, 1.06),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.011, 1.029),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        map=dict(
            name='D3',
            shape='I9',
            camera_data=['D3', 'D5', 'D7', 'F3', 'F5', 'F7'],
            camera_data_spawn_point=['F7', 'D7'],
            map_data="""
                -- ++ ++ -- MB -- ++ ++ --
                -- ++ ++ Me -- Me ++ ++ --
                ME -- -- -- -- -- -- -- ME
                -- ME ME Me -- Me ME ME --
                -- ++ ++ ++ -- ++ ++ ++ --
                -- Me ME MS -- MS ME Me --
                ME -- -- -- __ -- -- -- ME
                ++ MS -- -- -- -- -- MS ++
                ++ -- ++ SP -- SP ++ -- ++
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
            MAP_SIREN_TEMPLATE=['CA', 'BB', 'Bellona', 'Revenge'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
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
            HOMO_EDGE_COLOR_RANGE=(0, 33),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_SWIPE_MULTIPLY=(1.084, 1.105),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.049, 1.068),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.018, 1.036),
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
            camera_data=['E3', 'D6', 'F6'],
            camera_data_spawn_point=['F6', 'D6'],
            map_data="""
                -- -- ++ ++ MB ++ ++ -- --
                -- -- ++ ++ -- ++ ++ -- --
                -- -- ++ MS -- MS ++ -- --
                -- ++ MS -- -- -- MS ++ --
                -- ++ -- -- __ -- -- ++ --
                ++ Me -- SP -- SP -- Me ++
                ME -- ME -- -- -- ME -- ME
                ++ ++ ++ Me -- Me ++ ++ ++
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
                {'battle': 0, 'enemy': 2, 'siren': 4},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5},
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['DukeOfYork', 'Howe', 'KingGeorgeV', 'PrinceOfWales'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (120, 225),
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
            HOMO_EDGE_HOUGHLINES_THRESHOLD=300,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_ENEMY_GENRE_SIMILARITY=0.75,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: PLAN,
            7: 'fleet_boss.clear_boss',
        },
    ),
}
