"""
Stages of event_20210624_cn, see module/campaign/stage.py
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
PLAN_3 = ['clear_siren', 'clear_enemy(scale=(2,))', 'clear_enemy(scale=(3,))', 'battle_default']
PLAN_4 = [
    'clear_siren',
    'clear_enemy(scale=(1,))',
    "clear_enemy(scale=(2,), genre=['light', 'main', 'enemy'])",
    "clear_enemy(genre=['light', 'main'])",
    'clear_enemy(scale=[2, 3])',
    'battle_default',
]

STAGES = {
    'a1': Stage(
        map=dict(
            name='A1',
            shape='H6',
            camera_data=['D2', 'D4', 'E2', 'E4'],
            camera_data_spawn_point=['D4'],
            map_data="""
                -- ++ ME ME -- -- ME --
                Me ++ -- ME -- Me ME ++
                ME -- __ ++ ++ -- -- MB
                -- Me -- ME ++ -- MS MB
                SP -- ME -- ME -- -- MB
                SP SP -- -- -- -- ME ++
            """,
            weight_data="""
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
                {'battle': 3, 'enemy': 1, 'boss': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Kasumi'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(0.948, 0.966),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.917, 0.934),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.89, 0.906),
        ),
        battle={
            0: PLAN_4,
            3: 'clear_boss',
        },
    ),
    'a2': Stage(
        map=dict(
            name='A2',
            shape='G7',
            camera_data=['D2', 'D5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- ME MS MS -- -- --
                ME ++ MB -- ME ME --
                MB MB -- MS -- ++ ++
                -- -- ME ++ ME ++ ++
                Me __ ME ++ Me -- MS
                Me -- -- -- -- ++ ++
                ME -- SP SP -- ME --
            """,
            weight_data="""
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 10 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
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
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Hibiki'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(0.948, 0.966),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.917, 0.934),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.89, 0.906),
        ),
        battle={
            0: PLAN_4,
            4: 'clear_boss',
        },
    ),
    'a3': Stage(
        map=dict(
            name='A3',
            shape='I6',
            camera_data=['D2', 'D4', 'F2', 'F4'],
            camera_data_spawn_point=['D4', 'F4'],
            map_data="""
                Me -- ++ MB ++ ++ ME -- --
                -- ME ME MB ++ ++ ME ME --
                -- -- -- -- MB -- -- MS ME
                ME MS __ -- -- -- ++ ++ ++
                -- ME ++ MS -- -- -- Me MS
                -- ME ++ -- SP SP Me -- --
            """,
            weight_data="""
                50 50 50 50 50 50 90 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 90 50 50 50 50 50 50 50
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
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Kinu'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(0.948, 0.966),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.917, 0.934),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.89, 0.906),
        ),
        battle={
            0: PLAN_4,
            4: 'clear_boss',
        },
    ),
    'b1': Stage(
        map=dict(
            name='B1',
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- -- -- ++ ++ -- ME --
                -- ME Me ++ ++ MB -- ++
                ++ -- -- MB MB -- MS ++
                MS ME -- __ -- ME -- Me
                -- ME MS -- ME -- ME --
                ME ME -- -- -- ++ ++ ++
                -- -- SP SP -- -- Me --
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
                {'battle': 5, 'enemy': 1},
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
            MAP_SWIPE_MULTIPLY=(0.985, 1.003),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.952, 0.97),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.925, 0.941),
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b2': Stage(
        map=dict(
            name='B2',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['F2', 'D2'],
            map_data="""
                -- ++ -- -- SP SP ME -- --
                -- -- MS Me -- -- -- ME --
                ME ++ ++ ++ -- -- MS ++ ME
                -- ME ME -- -- MS -- ++ --
                -- -- Me __ ++ -- -- ME ME
                ++ ME ME -- -- -- Me -- ME
                ++ -- -- MB MB MB -- Me --
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
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DD', 'CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(1.132, 1.153),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.095, 1.115),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.063, 1.082),
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'b3': Stage(
        map=dict(
            name='B3',
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['D2', 'D5'],
            map_data="""
                ME -- MS -- ME -- ++ --
                -- Me ++ MS -- Me ME ME
                SP -- ME -- Me ++ ++ ++
                -- -- -- __ -- MB MB MB
                SP -- Me -- -- ++ ++ ++
                -- ++ ++ -- ME -- ME ME
                Me ++ ++ ME ME MS -- --
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
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DD', 'CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(1.002, 1.021),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.969, 0.987),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.941, 0.958),
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c1': Stage(
        map=dict(
            name='C1',
            shape='H6',
            camera_data=['D2', 'D4', 'E2', 'E4'],
            camera_data_spawn_point=['D4'],
            map_data="""
                -- ++ ME ME -- -- ME --
                Me ++ -- ME -- Me ME ++
                ME -- __ ++ ++ -- -- MB
                -- Me -- ME ++ -- MS MB
                SP -- ME -- ME -- -- MB
                SP SP -- -- -- -- ME ++
            """,
            weight_data="""
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
                {'battle': 4, 'enemy': 2, 'boss': 1},
                {'battle': 5, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Kinu', 'Maya'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(0.948, 0.966),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.917, 0.934),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.89, 0.906),
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'c2': Stage(
        map=dict(
            name='C2',
            shape='G7',
            camera_data=['D2', 'D5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- ME MS MS -- -- --
                ME ++ MB -- ME ME --
                MB MB -- MS -- ++ ++
                -- -- ME ++ ME ++ ++
                Me __ ME ++ Me -- MS
                Me -- -- -- -- ++ ++
                ME -- SP SP -- ME --
            """,
            weight_data="""
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 10 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
                {'battle': 5, 'enemy': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Kinu', 'Maya', 'Ise'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(0.948, 0.966),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.917, 0.934),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.89, 0.906),
        ),
        battle={
            0: [
                'clear_siren',
                'clear_enemy(scale=(1,))',
                "clear_enemy(scale=(2,), genre=['light', 'main', 'enemy', 'carrier'])",
                "clear_enemy(genre=['light', 'main'])",
                'battle_default',
            ],
            4: 'clear_boss',
        },
    ),
    'c3': Stage(
        map=dict(
            name='C3',
            shape='I6',
            camera_data=['D2', 'D4', 'F2', 'F4'],
            camera_data_spawn_point=['D4', 'F4'],
            map_data="""
                Me -- ++ MB ++ ++ ME -- --
                -- ME ME MB ++ ++ ME ME --
                -- -- -- -- MB -- -- MS ME
                ME MS __ -- -- -- ++ ++ ++
                -- ME ++ MS -- -- -- Me MS
                -- ME ++ -- SP SP Me -- --
            """,
            weight_data="""
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
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Kinu', 'Maya', 'Ise'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(0.948, 0.966),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.917, 0.934),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.89, 0.906),
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd1': Stage(
        map=dict(
            name='D1',
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- -- -- ++ ++ -- ME --
                -- ME Me ++ ++ MB -- ++
                ++ -- -- MB MB -- MS ++
                MS ME -- __ -- ME -- Me
                -- ME MS -- ME -- ME --
                ME ME -- -- -- ++ ++ ++
                -- -- SP SP -- -- Me --
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
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA', 'BB'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(0.985, 1.003),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.952, 0.97),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.925, 0.941),
        ),
        battle={
            0: PLAN_2,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd2': Stage(
        map=dict(
            name='D2',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['F2', 'D2'],
            map_data="""
                -- ++ -- -- SP SP ME -- --
                -- -- MS Me -- -- -- ME --
                ME ++ ++ ++ -- -- MS ++ ME
                -- ME ME -- -- MS -- ++ --
                -- -- Me __ ++ -- -- ME ME
                ++ ME ME -- -- -- Me -- ME
                ++ -- -- MB MB MB -- Me --
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
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA', 'BB'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(1.132, 1.153),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.095, 1.115),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.063, 1.082),
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
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['D2', 'D5'],
            map_data="""
                ME -- MS -- ME -- ++ --
                -- Me ++ MS -- Me ME ME
                SP -- ME -- Me ++ ++ ++
                -- -- -- __ -- MB MB MB
                SP -- Me -- -- ++ ++ ++
                -- ++ ++ -- ME -- ME ME
                Me ++ ++ ME ME MS -- --
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
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA', 'BB', 'CV'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(1.002, 1.021),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.969, 0.987),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.941, 0.958),
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
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D2', 'D5'],
            map_data="""
                -- MS ++ -- MS ME -- ++ --
                -- -- Me -- ++ -- ME ++ ++
                SP -- -- -- Me -- -- -- MB
                -- -- Me -- __ ME -- MB MB
                SP -- -- MS -- ME -- ++ ++
                -- Me ++ ++ ++ Me ME ++ ++
                -- -- Me -- ME -- -- ME --
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
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Kinu', 'Maya', 'Ise', 'Junyo'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_SWIPE_MULTIPLY=(1.002, 1.021),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.969, 0.987),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.941, 0.958),
        ),
        battle={
            0: PLAN_3,
            5: PLAN_2,
            7: 'fleet_boss.clear_boss',
        },
    ),
}
