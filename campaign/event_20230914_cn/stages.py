"""
Stages of event_20230914_cn, see module/campaign/stage.py
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
            shape='I8',
            camera_data=['D3', 'D6', 'F3', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- -- -- -- -- ++ ++ -- --
                ME ME ++ MS MB ++ ++ ME --
                -- -- ++ -- -- MS -- -- ME
                ME -- -- MS ++ ++ ++ -- ++
                ++ ME -- -- Me Me -- -- ME
                -- Me -- __ -- -- -- ME --
                ME -- SP -- SP -- Me ++ ++
                -- ME ++ ++ ++ ME -- -- ++
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
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SIREN_HAS_BOSS_ICON=True,
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
            HOMO_EDGE_COLOR_RANGE=(0, 17),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(1.074, 1.095),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.039, 1.058),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.009, 1.027),
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
            shape='K5',
            camera_data=['D3', 'F3', 'H3'],
            camera_data_spawn_point=['D2'],
            map_data="""
                ++ SP -- SP ++ ++ -- ME ME ++ --
                Me -- -- -- Me ++ ME -- -- ME ++
                -- -- MS -- -- __ -- -- -- -- MB
                Me MS ++ MS Me -- ME -- -- ME ++
                -- -- ++ -- -- ++ -- ME ME -- ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['Kawakaze', 'Sakawa'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_ENEMY_GENRE_DETECTION_SCALING={'Kawakaze': 0.78, 'Sakawa': 0.78},
            MAP_SWIPE_MULTIPLY=(1.269, 1.293),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.227, 1.25),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.191, 1.213),
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
            shape='H8',
            camera_data=['D3', 'D6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- ++ ++ -- ME ME -- ++
                ME ++ ++ ME -- -- MB --
                -- Me Me -- -- ME -- ME
                -- -- -- -- __ -- -- ME
                -- MS ++ ++ -- -- ME --
                -- -- MS ++ -- Me ++ ++
                SP -- -- MS -- Me ++ ++
                ++ SP -- -- -- -- ME --
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
            MAP_SIREN_TEMPLATE=['Asanagi', 'Hatsuzuki'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.091, 1.111),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.055, 1.074),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.024, 1.043),
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
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['F5', 'D5'],
            map_data="""
                -- ME -- ++ ++ ++ -- ME --
                ME -- MS -- MS -- MS -- ME
                -- ME -- -- __ -- -- ME ++
                ME ++ -- SP MB SP -- -- ME
                -- ++ Me -- -- -- -- ME --
                ME -- -- -- Me -- Me ++ ++
                -- ME Me ++ ++ ++ -- ++ ++
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
                {'battle': 4, 'enemy': 2, 'boss': 1},
                {'battle': 5, 'enemy': 1},
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
            MAP_SIREN_HAS_BOSS_ICON=True,
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
            HOMO_EDGE_COLOR_RANGE=(0, 17),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(1.146, 1.167),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.108, 1.128),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.076, 1.095),
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
            camera_data_spawn_point=['F2', 'D2'],
            map_data="""
                -- ME ++ ++ SP -- SP ++ --
                -- -- Me ++ -- -- -- -- Me
                ME -- -- MS -- MS -- MS --
                ++ ME -- __ -- MS -- Me --
                ++ ME -- ME Me ++ ++ ++ --
                -- ME -- -- -- -- ME -- --
                -- ++ -- ME -- MB -- ++ ++
                -- -- ME ++ ME -- -- ++ ++
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.266, 1.289),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.224, 1.247),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.188, 1.21),
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
            camera_data=['D3', 'D6', 'H2', 'H5', 'H7'],
            camera_data_spawn_point=['H5'],
            map_data="""
                -- -- ++ -- -- ME -- ME -- ++ --
                -- ++ ++ ME -- ++ ++ ++ -- -- ++
                ++ ++ ++ ME -- -- Me -- MS -- ++
                -- -- ME -- -- Me ++ MS -- -- SP
                MB -- -- -- -- -- -- -- -- __ --
                -- -- ME -- -- Me ++ MS -- -- SP
                ++ ++ ++ ME -- -- Me -- MS -- ++
                -- ++ ++ ME -- ++ ++ ++ -- -- ++
                -- -- ++ -- -- ME -- ME -- ++ --
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.102, 1.123),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.066, 1.086),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.035, 1.054),
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
            camera_data=['D3', 'D6', 'F3', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- -- -- -- -- ++ ++ -- --
                ME ME ++ MS MB ++ ++ ME --
                -- -- ++ -- -- MS -- -- ME
                ME -- -- MS ++ ++ ++ -- ++
                ++ ME -- -- Me Me -- -- ME
                -- Me -- __ -- -- -- ME --
                ME -- SP -- SP -- Me ++ ++
                -- ME ++ ++ ++ ME -- -- ++
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
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SIREN_HAS_BOSS_ICON=True,
            MAP_SWIPE_MULTIPLY=(1.074, 1.095),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.039, 1.058),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.009, 1.027),
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
            shape='K5',
            camera_data=['D3', 'F3', 'H3'],
            camera_data_spawn_point=['D2'],
            map_data="""
                ++ SP -- SP ++ ++ -- ME ME ++ --
                Me -- -- -- Me ++ ME -- -- ME ++
                -- -- MS -- -- __ -- -- -- -- MB
                Me MS ++ MS Me -- ME -- -- ME ++
                -- -- ++ -- -- ++ -- ME ME -- ++
            """,
            weight_data="""
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
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Kawakaze', 'Sakawa'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_ENEMY_GENRE_DETECTION_SCALING={'Kawakaze': 0.78, 'Sakawa': 0.78},
            MAP_SWIPE_MULTIPLY=(1.269, 1.293),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.227, 1.25),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.191, 1.213),
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
            camera_data=['D3', 'D6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- ++ ++ -- ME ME -- ++
                ME ++ ++ ME -- -- MB --
                -- Me Me -- -- ME -- ME
                -- -- -- -- __ -- -- ME
                -- MS ++ ++ -- -- ME --
                -- -- MS ++ -- Me ++ ++
                SP -- -- MS -- Me ++ ++
                ++ SP -- -- -- -- ME --
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
            MAP_SIREN_TEMPLATE=['Hatsuzuki', 'Zuiho'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.091, 1.111),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.055, 1.074),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.024, 1.043),
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
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['F5', 'D5'],
            map_data="""
                -- ME -- ++ ++ ++ -- ME --
                ME -- MS -- MS -- MS -- ME
                -- ME -- -- __ -- -- ME ++
                ME ++ -- SP MB SP -- -- ME
                -- ++ Me -- -- -- -- ME --
                ME -- -- -- Me -- Me ++ ++
                -- ME Me ++ ++ ++ -- ++ ++
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
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
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
            MAP_SIREN_HAS_BOSS_ICON=True,
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
            HOMO_EDGE_COLOR_RANGE=(0, 17),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(1.146, 1.167),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.108, 1.128),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.076, 1.095),
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
            camera_data_spawn_point=['F2', 'D2'],
            map_data="""
                -- ME ++ ++ SP -- SP ++ --
                -- -- Me ++ -- -- -- -- Me
                ME -- -- MS -- MS -- MS --
                ++ ME -- __ -- MS -- Me --
                ++ ME -- ME Me ++ ++ ++ --
                -- ME -- -- -- -- ME -- --
                -- ++ -- ME -- MB -- ++ ++
                -- -- ME ++ ME -- -- ++ ++
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.266, 1.289),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.224, 1.247),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.188, 1.21),
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
            camera_data=['D3', 'D6', 'H2', 'H5', 'H7'],
            camera_data_spawn_point=['H5'],
            map_data="""
                -- -- ++ -- -- ME -- ME -- ++ --
                -- ++ ++ ME -- ++ ++ ++ -- -- ++
                ++ ++ ++ ME -- -- Me -- MS -- ++
                -- -- ME -- -- Me ++ MS -- -- SP
                MB -- -- -- -- -- -- -- -- __ --
                -- -- ME -- -- Me ++ MS -- -- SP
                ++ ++ ++ ME -- -- Me -- MS -- ++
                -- ++ ++ ME -- ++ ++ ++ -- -- ++
                -- -- ++ -- -- ME -- ME -- ++ --
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.102, 1.123),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.066, 1.086),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.035, 1.054),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
}
