"""
Stages of event_20250227_cn, see module/campaign/stage.py
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
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['F2'],
            map_data="""
                ++ -- ME -- -- SP SP ++ MB
                -- ME -- ME -- -- -- -- --
                ME -- ++ ++ Me -- -- __ Me
                -- -- ++ ++ -- MS MS -- --
                -- ME -- -- ME -- -- ++ --
                -- -- ME -- -- -- Me ++ --
                ME -- -- -- Me -- -- Me --
                -- -- ME ++ ++ ++ -- -- --
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
            MAP_SIREN_TEMPLATE=[],
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
            STAGE_INCREASE_AB=True,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
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
            MAP_SWIPE_MULTIPLY=(1.227, 1.25),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.187, 1.209),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.152, 1.173),
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
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['F2', 'D2'],
            map_data="""
                -- -- ME -- -- ME -- ++ --
                ME ++ -- ME -- -- -- -- ME
                -- -- ME ++ ++ ++ -- Me --
                -- ME -- SP -- SP -- -- --
                -- -- -- -- -- -- -- -- ME
                -- ME -- -- __ -- -- Me --
                ME ++ -- MS -- MS -- ++ ++
                -- ++ Me -- MB -- Me ++ ++
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.128, 1.149),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.091, 1.111),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.059, 1.078),
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
            camera_data=['D3', 'D6', 'G3', 'G6'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- SP -- -- -- ++ -- ++ ++ --
                SP -- -- MS -- -- Me ++ ++ --
                ++ ++ ++ -- MS -- -- -- ME --
                -- -- -- __ -- -- Me -- -- ME
                -- ME -- -- Me ++ Me -- ME ++
                ME -- MB -- -- ++ Me -- -- ME
                ++ ++ -- ME -- -- -- -- ME --
                ++ ++ ME -- -- ++ -- ME -- ++
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
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
    'b1': Stage(
        map=dict(
            name='B1',
            shape='K8',
            camera_data=['D2', 'D6', 'H2', 'H6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ ME -- -- -- ME -- ++ -- ME --
                ME -- ++ -- ++ -- ME ++ ME -- ME
                -- -- -- MB -- -- -- -- -- -- --
                -- Me ++ -- ++ Me -- ++ ++ ++ --
                -- -- MS __ MS -- -- -- ME -- --
                Me -- -- MS -- -- Me -- -- ME --
                ++ ++ -- -- -- ++ ++ Me ME -- ++
                ++ ++ SP -- SP ++ ++ -- -- -- ++
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
            MAP_SIREN_TEMPLATE=['TrentoAlter', 'BolzanoAlter', 'CesareAlter'],
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
            STAGE_INCREASE_AB=True,
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
    'b2': Stage(
        map=dict(
            name='B2',
            shape='K8',
            camera_data=['E2', 'E6', 'G2', 'G6'],
            camera_data_spawn_point=['G2', 'E2'],
            map_data="""
                -- -- ++ ++ SP -- SP ++ ++ -- --
                -- -- ++ ++ -- -- -- ++ ++ -- --
                -- -- Me -- -- MS -- -- Me -- --
                ++ ME -- -- MS -- MS -- -- ME ++
                ++ -- -- ME -- MB -- ME -- -- ++
                -- -- Me -- -- __ -- -- Me -- --
                -- ++ -- ME -- Me -- ME -- ++ --
                -- -- -- -- ME -- ME -- -- -- --
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
            MAP_SIREN_TEMPLATE=['SirenBoss26'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.258, 1.282),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.217, 1.239),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.182, 1.203),
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
            shape='K9',
            camera_data=['E3', 'E6', 'G3', 'G6'],
            camera_data_spawn_point=['E6', 'G6'],
            map_data="""
                -- ++ ++ -- -- -- -- -- ++ ++ --
                -- ++ ++ -- -- MB -- -- ++ ++ --
                -- -- ++ ++ ++ -- ++ ++ ++ -- --
                -- ++ -- Me -- __ -- Me -- ++ --
                -- ME Me -- MS -- MS -- Me ME --
                -- ME -- -- -- MS -- -- -- ME --
                -- ME -- ME -- -- -- ME -- ME --
                -- ++ ME ++ SP -- SP ++ ME ++ --
                -- -- -- ++ -- -- -- ++ -- -- --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 10 10 10 50 50 50 50
                50 50 50 50 10 10 10 50 50 50 50
                50 50 50 50 10 10 10 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['SirenBoss26', 'SirenBoss25'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.063, 1.083),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.028, 1.047),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.998, 1.016),
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
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['F2'],
            map_data="""
                ++ -- ME -- -- SP SP ++ MB
                -- ME -- ME -- -- -- -- --
                ME -- ++ ++ Me -- -- __ Me
                -- -- ++ ++ -- MS MS -- --
                -- ME -- -- ME -- -- ++ --
                -- -- ME -- -- -- Me ++ --
                ME -- -- -- Me -- -- Me --
                -- -- ME ++ ++ ++ -- -- --
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
            MAP_SIREN_TEMPLATE=[],
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
            STAGE_INCREASE_AB=True,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
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
            MAP_SWIPE_MULTIPLY=(1.227, 1.25),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.187, 1.209),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.152, 1.173),
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
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['F2', 'D2'],
            map_data="""
                -- -- ME -- -- ME -- ++ --
                ME ++ -- ME -- -- -- -- ME
                -- -- ME ++ ++ ++ -- Me --
                -- ME -- SP -- SP -- -- --
                -- -- -- -- -- -- -- -- ME
                -- ME -- -- __ -- -- Me --
                ME ++ -- MS -- MS -- ++ ++
                -- ++ Me -- MB -- Me ++ ++
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.128, 1.149),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.091, 1.111),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.059, 1.078),
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
            camera_data_spawn_point=['D2'],
            map_data="""
                -- SP -- -- -- ++ -- ++ ++ --
                SP -- -- MS -- -- Me ++ ++ --
                ++ ++ ++ -- MS -- -- -- ME --
                -- -- -- __ -- -- Me -- -- ME
                -- ME -- -- Me ++ Me -- ME ++
                ME -- MB -- -- ++ Me -- -- ME
                ++ ++ -- ME -- -- -- -- ME --
                ++ ++ ME -- -- ++ -- ME -- ++
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
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
    'd1': Stage(
        map=dict(
            name='D1',
            shape='K8',
            camera_data=['D2', 'D6', 'H2', 'H6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ ME -- -- -- ME -- ++ -- ME --
                ME -- ++ -- ++ -- ME ++ ME -- ME
                -- -- -- MB -- -- -- -- -- -- --
                -- Me ++ -- ++ Me -- ++ ++ ++ --
                -- -- MS __ MS -- -- -- ME -- --
                Me -- -- MS -- -- Me -- -- ME --
                ++ ++ -- -- -- ++ ++ Me ME -- ++
                ++ ++ SP -- SP ++ ++ -- -- -- ++
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
            MAP_SIREN_TEMPLATE=['TrentoAlter', 'BolzanoAlter', 'CesareAlter'],
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
            STAGE_INCREASE_AB=True,
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
            MAP_SWIPE_MULTIPLY=(1.131, 1.152),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.094, 1.114),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.062, 1.081),
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
            shape='K8',
            camera_data=['E2', 'E6', 'G2', 'G6'],
            camera_data_spawn_point=['G2', 'E2'],
            map_data="""
                -- -- ++ ++ SP -- SP ++ ++ -- --
                -- -- ++ ++ -- -- -- ++ ++ -- --
                -- -- Me -- -- MS -- -- Me -- --
                ++ ME -- -- MS -- MS -- -- ME ++
                ++ -- -- ME -- MB -- ME -- -- ++
                -- -- Me -- -- __ -- -- Me -- --
                -- ++ -- ME -- Me -- ME -- ++ --
                -- -- -- -- ME -- ME -- -- -- --
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
            MAP_SIREN_TEMPLATE=['SirenBoss26'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.258, 1.282),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.217, 1.239),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.182, 1.203),
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
            camera_data_spawn_point=['E6', 'G6'],
            map_data="""
                -- ++ ++ -- -- -- -- -- ++ ++ --
                -- ++ ++ -- -- MB -- -- ++ ++ --
                -- -- ++ ++ ++ -- ++ ++ ++ -- --
                -- ++ -- Me -- __ -- Me -- ++ --
                -- ME Me -- MS -- MS -- Me ME --
                -- ME -- -- -- MS -- -- -- ME --
                -- ME -- ME -- -- -- ME -- ME --
                -- ++ ME ++ SP -- SP ++ ME ++ --
                -- -- -- ++ -- -- -- ++ -- -- --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 10 10 10 50 50 50 50
                50 50 50 50 10 10 10 50 50 50 50
                50 50 50 50 10 10 10 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['SirenBoss26', 'SirenBoss25'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.063, 1.083),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.028, 1.047),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.998, 1.016),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
}
