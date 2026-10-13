"""
Stages of event_20210527_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

PLAN = ['clear_siren', 'battle_default']
PLAN_2 = [
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
            camera_data_spawn_point=['F2'],
            map_data="""
                ++ ++ -- ME -- Me ++ -- --
                ++ ++ Me -- -- -- -- -- SP
                ME -- -- -- ++ MS -- ME SP
                -- -- ME -- ++ __ ME -- ++
                MB -- ++ MS -- ME -- -- --
                -- -- -- -- ME -- Me ++ ME
                -- ++ -- ME -- -- -- ++ --
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
            MAP_SIREN_TEMPLATE=['Dewey'],
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
            0: PLAN,
            3: 'clear_boss',
        },
    ),
    'a2': Stage(
        map=dict(
            name='A2',
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['E6', 'D6'],
            map_data="""
                -- ++ ++ ++ -- MB -- ++
                -- ME -- ME -- ME -- --
                ++ -- MS -- ME ++ Me --
                -- Me ++ -- Me -- -- --
                ME -- ++ ME -- __ ME MS
                -- MS -- Me -- ++ -- --
                ++ -- ME -- -- -- ME ++
                ++ -- -- SP SP -- ++ ++
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
            MAP_SWIPE_MULTIPLY=(0.989, 1.008),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.957, 0.975),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.929, 0.946),
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'a3': Stage(
        map=dict(
            name='A3',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['G6', 'D6'],
            map_data="""
                ++ ++ -- ++ ++ -- -- ME ++ ++
                -- -- MB -- ME -- MS -- ++ ++
                -- ME -- ME MS Me -- ME -- --
                -- ++ -- ++ -- __ -- Me -- MS
                ME ++ -- ++ ME Me ++ -- ME --
                -- -- -- Me -- -- ME -- -- --
                -- ME -- -- SP ++ -- ++ SP ++
                -- ++ ++ ++ -- SP -- SP -- ++
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
            MAP_SIREN_TEMPLATE=['CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(0.989, 1.008),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.957, 0.975),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.929, 0.946),
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b1': Stage(
        map=dict(
            name='B1',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['D2', 'D6'],
            map_data="""
                -- ME -- ME -- -- -- -- ++ ++
                ++ -- MS -- -- Me -- -- MB ++
                ++ -- -- MS Me ++ -- Me -- --
                SP -- ME -- ME -- ME ++ -- ++
                SP -- ++ ++ -- __ -- ++ -- ME
                -- -- ++ ++ Me ME -- ME -- --
                ME -- MS -- -- -- Me -- ++ ++
                -- ++ -- ME -- MS -- ++ ++ ++
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
            MAP_SIREN_TEMPLATE=['Hammann', 'CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
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
    'b2': Stage(
        map=dict(
            name='B2',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['G6'],
            map_data="""
                ++ ++ -- ME -- -- MS ++ ++ ++
                ++ ++ -- ++ ++ -- -- -- -- ME
                -- Me -- -- ME -- Me -- ++ --
                ME ++ MS MB -- -- ME -- ++ --
                -- ++ -- -- ME __ -- MS ++ ME
                -- ++ -- Me -- -- Me -- -- --
                ME -- ME -- -- ++ ++ -- -- SP
                ++ ++ ++ MS -- ME -- -- SP ++
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
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Atlanta', 'CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(0.997, 1.015),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.964, 0.982),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.936, 0.953),
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'b3': Stage(
        map=dict(
            name='B3',
            shape='I9',
            camera_data=['D2', 'D6', 'D7', 'F2', 'F6', 'F7'],
            camera_data_spawn_point=['F7', 'D7'],
            map_data="""
                ++ -- ME -- -- -- ME -- ++
                ++ ++ ++ -- MB -- ++ ++ ++
                ME -- -- -- ++ -- -- -- ME
                -- ME Me -- Me -- Me ME --
                -- ++ ++ -- __ -- ++ ++ --
                MS ++ ++ -- Me -- ++ ++ MS
                -- ME MS -- -- -- MS ME --
                ME Me -- ++ -- ++ -- Me ME
                ++ -- -- SP -- SP -- -- ++
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
            MAP_SIREN_TEMPLATE=['Dewey', 'Northampton', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(0.966, 0.985),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.935, 0.952),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.907, 0.924),
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
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
            camera_data_spawn_point=['F2'],
            map_data="""
                ++ ++ -- ME -- Me ++ -- --
                ++ ++ Me -- -- -- -- -- SP
                ME -- -- -- ++ MS -- ME SP
                -- -- ME -- ++ __ ME -- ++
                MB -- ++ MS -- ME -- -- --
                -- -- -- -- ME -- Me ++ ME
                -- ++ -- ME -- -- -- ++ --
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
            MAP_SIREN_TEMPLATE=['Dewey', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(1.163, 1.185),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.125, 1.146),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.092, 1.112),
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
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['E6', 'D6'],
            map_data="""
                -- ++ ++ ++ -- MB -- ++
                -- ME -- ME -- ME -- --
                ++ -- MS -- ME ++ Me --
                -- Me ++ -- Me -- -- --
                ME -- ++ ME -- __ ME MS
                -- MS -- Me -- ++ -- --
                ++ -- ME -- -- -- ME ++
                ++ -- -- SP SP -- ++ ++
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
            MAP_SIREN_TEMPLATE=['Atlanta', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(0.989, 1.008),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.957, 0.975),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.929, 0.946),
        ),
        battle={
            0: PLAN_2,
            4: 'clear_boss',
        },
    ),
    'c3': Stage(
        map=dict(
            name='C3',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['G6', 'D6'],
            map_data="""
                ++ ++ -- ++ ++ -- -- ME ++ ++
                -- -- MB -- ME -- MS -- ++ ++
                -- ME -- ME MS Me -- ME -- --
                -- ++ -- ++ -- __ -- Me -- MS
                ME ++ -- ++ ME Me ++ -- ME --
                -- -- -- Me -- -- ME -- -- --
                -- ME -- -- SP ++ -- ++ SP ++
                -- ++ ++ ++ -- SP -- SP -- ++
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
            MAP_SIREN_TEMPLATE=['Northampton', 'CA', 'BB'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(0.989, 1.008),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.957, 0.975),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.929, 0.946),
        ),
        battle={
            0: PLAN_2,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd1': Stage(
        map=dict(
            name='D1',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['D2', 'D6'],
            map_data="""
                -- ME -- ME -- -- -- -- ++ ++
                ++ -- MS -- -- Me -- -- MB ++
                ++ -- -- MS Me ++ -- Me -- --
                SP -- ME -- ME -- ME ++ -- ++
                SP -- ++ ++ -- __ -- ++ -- ME
                -- -- ++ ++ Me ME -- ME -- --
                ME -- MS -- -- -- Me -- ++ ++
                -- ++ -- ME -- MS -- ++ ++ ++
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
            MAP_SIREN_TEMPLATE=['Hammann', 'Atlanta', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
        ),
        battle={
            0: PLAN_2,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd2': Stage(
        map=dict(
            name='D2',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['G6'],
            map_data="""
                ++ ++ -- ME -- -- MS ++ ++ ++
                ++ ++ -- ++ ++ -- -- -- -- ME
                -- Me -- -- ME -- Me -- ++ --
                ME ++ MS MB -- -- ME -- ++ --
                -- ++ -- -- ME __ -- MS ++ ME
                -- ++ -- Me -- -- Me -- -- --
                ME -- ME -- -- ++ ++ -- -- SP
                ++ ++ ++ MS -- ME -- -- SP ++
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
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Dewey', 'Northampton', 'BB'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(0.997, 1.015),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.964, 0.982),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.936, 0.953),
        ),
        battle={
            0: ['clear_siren', 'clear_enemy(scale=(2,))', 'clear_enemy(scale=(3,))', 'battle_default'],
            5: PLAN_2,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        map=dict(
            name='D3',
            shape='I9',
            camera_data=['D2', 'D6', 'D7', 'F2', 'F6', 'F7'],
            camera_data_spawn_point=['F7', 'D7'],
            map_data="""
                ++ -- ME -- -- -- ME -- ++
                ++ ++ ++ -- MB -- ++ ++ ++
                ME -- -- -- ++ -- -- -- ME
                -- ME Me -- Me -- Me ME --
                -- ++ ++ -- __ -- ++ ++ --
                MS ++ ++ -- Me -- ++ ++ MS
                -- ME MS -- -- -- MS ME --
                ME Me -- ++ -- ++ -- Me ME
                ++ -- -- SP -- SP -- -- ++
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
            MAP_SIREN_TEMPLATE=['Atlanta', 'Northampton', 'CV'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(0.966, 0.985),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.935, 0.952),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.907, 0.924),
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
        ),
        battle={
            0: [
                'fleet_2_protect',
                'clear_siren',
                'clear_enemy(scale=(2,))',
                'clear_enemy(scale=(3,))',
                'battle_default',
            ],
            5: PLAN_2,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'sp': Stage(
        map=dict(
            name='SP',
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['F6', 'D6'],
            map_data="""
                ++ ++ ++ -- MB -- ++ ++ ++
                ME ++ -- -- -- -- -- ++ ME
                -- -- MS ++ -- ++ MS -- --
                -- -- ++ ++ MS ++ ++ -- --
                ++ -- ++ ++ -- ++ ++ -- ++
                ME -- -- ++ -- ++ -- -- ME
                ++ ++ -- -- __ -- -- ++ ++
                ++ ++ ++ SP ++ SP ++ ++ ++
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
                {'battle': 0, 'enemy': 4, 'siren': 3},
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
            MAP_SIREN_TEMPLATE=['Hammann', 'Northampton', 'CV'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_SWIPE_MULTIPLY=(0.997, 1.015),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.964, 0.982),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.936, 0.953),
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
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
            7: 'fleet_boss.clear_boss',
        },
    ),
}
