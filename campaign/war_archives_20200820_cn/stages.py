"""
Stages of war_archives_20200820_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '..campaign_war_archives.campaign_base:CampaignBase'
PLAN = ['clear_siren', 'battle_default']
PLAN_2 = [
    'clear_enemy(scale=(1,))',
    "clear_enemy(scale=(2,), genre=['light', 'main', 'enemy', 'carrier'])",
    "clear_enemy(genre=['light', 'main', 'enemy'])",
    'battle_default',
]

STAGES = {
    'a1': Stage(
        base=BASE,
        map=dict(
            name='A1',
            shape='H6',
            camera_data=['D2', 'D4', 'E2', 'E4'],
            camera_data_spawn_point=['D4'],
            map_data="""
                -- ++ -- ME -- -- ME --
                Me ++ -- MB -- Me ++ --
                -- -- __ ++ ++ -- -- ME
                -- Me -- ++ ++ -- -- ME
                SP -- ME ME -- MS -- --
                SP SP -- -- -- ME MB --
            """,
            weight_data="""
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
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1, 'boss': 1},
                {'battle': 4, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Arethusa'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_SWIPE_MULTIPLY=(1.154, 1.176),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.116, 1.137),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.084, 1.103),
        ),
        battle={
            0: PLAN,
            3: 'fleet_1.clear_boss',
        },
    ),
    'a2': Stage(
        base=BASE,
        map=dict(
            name='A2',
            shape='G7',
            camera_data=['D3', 'D5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- -- -- -- -- -- MB
                ME -- -- ++ ++ ++ --
                -- ME __ -- ME Me --
                ME -- -- ME -- -- --
                ++ ME -- -- -- Me --
                -- -- -- MS -- ++ --
                SP SP -- ME -- ++ MB
            """,
            weight_data="""
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
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
            MAP_SIREN_TEMPLATE=['Arethusa', 'Sheffield'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
        ),
        battle={
            0: PLAN,
            4: 'fleet_1.clear_boss',
        },
    ),
    'a3': Stage(
        base=BASE,
        map=dict(
            name='A3',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D2'],
            map_data="""
                SP SP -- MS -- -- Me -- --
                SP -- -- -- ++ MS -- -- --
                -- ME -- ME ++ -- -- ME --
                -- -- -- __ -- Me -- -- MB
                ME -- ++ ++ -- -- ++ ++ ++
                -- -- ++ ++ -- ME -- -- --
                -- ME -- -- MB -- -- -- --
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
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Arethusa', 'Sheffield', 'Dorsetshire'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
        ),
        battle={
            0: PLAN,
            4: 'fleet_1.clear_boss',
        },
    ),
    'b1': Stage(
        base=BASE,
        map=dict(
            name='B1',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D5'],
            map_covered=['D1'],
            map_data="""
                MB -- -- MS -- -- -- -- --
                -- ME -- ++ ++ ME ++ ++ --
                -- -- __ ++ ++ -- MB ++ --
                MS ME -- -- -- -- -- Me --
                -- -- MS -- ME Me -- -- ME
                -- ++ -- -- -- -- ME ++ --
                -- ++ SP SP -- ME -- ++ --
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
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
                {'battle': 5, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_SWIPE_MULTIPLY=(1.108, 1.129),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.072, 1.092),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.041, 1.06),
        ),
        battle={
            0: PLAN,
            4: 'fleet_1.clear_boss',
        },
    ),
    'b2': Stage(
        base=BASE,
        map=dict(
            name='B2',
            shape='J7',
            camera_data=['D2', 'D5', 'G2', 'G5'],
            camera_data_spawn_point=['E2'],
            map_data="""
                -- ++ -- -- SP SP -- -- -- --
                MS ++ -- MB -- -- -- ME -- --
                -- -- -- ++ ++ ++ -- -- ME --
                ME -- -- -- -- -- Me -- -- ME
                -- -- -- MS Me __ -- ME ME --
                -- ME ME -- ++ Me -- -- -- ++
                -- -- -- MB ++ -- -- Me -- --
            """,
            weight_data="""
                10 10 10 10 10 10 10 10 10 10
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
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'b3': Stage(
        base=BASE,
        map=dict(
            name='B3',
            shape='I7',
            camera_data=['D2', 'D5', 'F3', 'F5'],
            camera_data_spawn_point=['D2', 'D5'],
            map_data="""
                MS -- -- ++ ++ -- -- -- --
                -- Me ME MS ++ -- ME -- --
                SP -- -- -- -- ME ++ ++ ++
                -- Me -- ++ -- -- -- -- MB
                SP -- ME __ -- ME ++ ++ ++
                Me -- ++ Me ME -- -- -- --
                -- Me ++ -- ME MS ME -- --
            """,
            weight_data="""
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                05 04 10 10 10 10 10 10 10
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
            MAP_SIREN_TEMPLATE=['CL', 'CA', 'BB'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
        ),
        battle={
            0: [
                ('when', 'config.MAP_HAS_MOVABLE_ENEMY', [('do', 'fleet_2_push_forward')]),
                'clear_siren',
                'battle_default',
            ],
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c1': Stage(
        base=BASE,
        map=dict(
            name='C1',
            shape='H6',
            camera_data=['D2', 'D4', 'E2', 'E4'],
            camera_data_spawn_point=['D4'],
            map_data="""
                -- ++ -- ME -- -- ME --
                Me ++ -- MB -- Me ++ --
                -- -- __ ++ ++ -- -- ME
                -- Me -- ++ ++ -- -- ME
                SP -- ME ME -- MS -- --
                SP SP -- -- -- ME MB --
            """,
            weight_data="""
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
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Sheffield', 'Dorsetshire'],
            MOVABLE_ENEMY_TURN=(3,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MOVABLE_ENEMY=True,
        ),
        battle={
            0: PLAN,
            4: 'fleet_1.clear_boss',
        },
    ),
    'c2': Stage(
        base=BASE,
        map=dict(
            name='C2',
            shape='G7',
            camera_data=['D3', 'D5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- -- -- -- -- -- MB
                ME -- -- ++ ++ ++ --
                -- ME __ -- ME Me --
                ME -- -- ME -- -- --
                ++ ME -- -- -- Me --
                -- -- -- MS -- ++ --
                SP SP -- ME -- ++ MB
            """,
            weight_data="""
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Sheffield', 'Dorsetshire', 'Renown'],
            MOVABLE_ENEMY_TURN=(3,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
        ),
        battle={
            0: PLAN,
            4: 'fleet_boss.clear_boss',
        },
    ),
    'c3': Stage(
        base=BASE,
        map=dict(
            name='C3',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D2'],
            map_data="""
                SP SP -- MS -- -- Me -- --
                SP -- -- -- ++ MS -- -- --
                -- ME -- ME ++ -- -- ME --
                -- -- -- __ -- Me -- -- MB
                ME -- ++ ++ -- -- ++ ++ ++
                -- -- ++ ++ -- ME -- -- --
                -- ME -- -- MB -- -- -- --
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
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Sheffield', 'Dorsetshire', 'Renown', 'PrinceOfWales'],
            MOVABLE_ENEMY_TURN=(3,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd1': Stage(
        base=BASE,
        map=dict(
            name='D1',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D5'],
            map_covered=['D1'],
            map_data="""
                MB -- -- MS -- -- -- -- --
                -- ME -- ++ ++ ME ++ ++ --
                -- -- __ ++ ++ -- MB ++ --
                MS ME -- -- -- -- -- Me --
                -- -- MS -- ME Me -- -- ME
                -- ++ -- -- -- -- ME ++ --
                -- ++ SP SP -- ME -- ++ --
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
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(3,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_SWIPE_MULTIPLY=(1.108, 1.129),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.072, 1.092),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.041, 1.06),
        ),
        battle={
            0: [
                'clear_siren',
                'clear_enemy(scale=(1,))',
                "clear_enemy(scale=(2,), genre=['light', 'main', 'enemy', 'carrier'])",
                "clear_enemy(genre=['light', 'main', 'enemy'])",
                'battle_default',
            ],
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd2': Stage(
        base=BASE,
        map=dict(
            name='D2',
            shape='J7',
            camera_data=['D2', 'D5', 'G2', 'G5'],
            camera_data_spawn_point=['E2'],
            map_data="""
                -- ++ -- -- SP SP -- -- -- --
                MS ++ -- MB -- -- -- ME -- --
                -- -- -- ++ ++ ++ -- -- ME --
                ME -- -- -- -- -- Me -- -- ME
                -- -- -- MS Me __ -- ME ME --
                -- ME ME -- ++ Me -- -- -- ++
                -- -- -- MB ++ -- -- Me -- --
            """,
            weight_data="""
                10 10 10 10 10 10 10 10 10 10
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
            MOVABLE_ENEMY_TURN=(3,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
        ),
        battle={
            0: [
                'clear_siren',
                "clear_enemy(scale=(3,), genre=['light', 'main', 'enemy', 'carrier'])",
                'battle_default',
            ],
            5: PLAN_2,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        base=BASE,
        map=dict(
            name='D3',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D2', 'D5'],
            map_data="""
                MS -- -- ++ ++ -- -- -- --
                -- Me ME MS ++ -- ME -- --
                SP -- -- -- -- ME ++ ++ ++
                -- Me -- ++ -- -- -- -- MB
                SP -- ME __ -- ME ++ ++ ++
                Me -- ++ Me ME -- -- -- --
                -- Me ++ -- ME MS ME -- --
            """,
            weight_data="""
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                05 04 10 10 10 10 10 10 10
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
            MAP_SIREN_TEMPLATE=['CL', 'CA', 'BB', 'CV'],
            MOVABLE_ENEMY_TURN=(3,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
        ),
        battle={
            0: [
                ('when', 'config.MAP_HAS_MOVABLE_ENEMY', [('do', 'fleet_2_push_forward')]),
                'clear_siren',
                "clear_enemy(scale=(3,), genre=['light', 'main', 'enemy', 'carrier'])",
                'battle_default',
            ],
            5: PLAN_2,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'sp': Stage(
        base=BASE,
        map=dict(
            name='SP',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- MS ++ SP -- SP -- -- ME
                -- -- Me -- -- -- ME -- --
                ++ ++ -- MS Me -- ++ ++ --
                ++ ++ Me -- __ -- ME ++ MS
                -- -- ME -- -- ME -- ME --
                -- Me -- ++ -- ++ ME -- --
                -- -- Me ++ MB ++ -- ME --
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
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA', 'BB', 'CV'],
            MOVABLE_ENEMY_TURN=(3,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_SWIPE_MULTIPLY=(1.175, 1.197),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.137, 1.158),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.103, 1.123),
            STAR_REQUIRE_3=0,
        ),
        battle={
            0: ['fleet_2_protect', 'clear_siren', 'clear_enemy(scale=(3,))', 'battle_default'],
            5: ['clear_enemy(scale=(1,))', 'clear_enemy(scale=(2,))', 'battle_default'],
            7: 'fleet_boss.clear_boss',
        },
    ),
}
