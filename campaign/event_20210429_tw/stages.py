"""
Stages of event_20210429_tw, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

PLAN = ['clear_siren', 'battle_default']

STAGES = {
    'a1': Stage(
        map=dict(
            name='A1',
            shape='I6',
            camera_data=['D2', 'D4', 'F2', 'F4'],
            camera_data_spawn_point=['D4'],
            map_data="""
                Me -- -- ME -- -- ME -- Me
                -- -- __ -- -- __ -- -- MB
                ME -- ME ++ ++ ME -- -- --
                -- -- ++ ++ ++ -- -- ME Me
                SP -- ++ ++ -- MS -- ++ ++
                SP SP -- -- -- ME MB ++ ++
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
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1, 'boss': 1},
                {'battle': 4, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['DD'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN,
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
                ++ ++ ME -- Me -- MB
                ++ ++ -- __ -- -- --
                ++ ++ ME -- ME -- Me
                ME -- ME MS -- -- --
                -- ME __ -- -- Me MB
                SP -- -- ME -- ++ ++
                SP SP -- -- ME ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['DD', 'CL'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
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
            shape='H8',
            camera_data=['D3', 'D6', 'E3', 'E6'],
            camera_data_spawn_point=['D3'],
            map_data="""
                -- -- ++ ++ ++ ++ ++ --
                -- SP ++ ++ ++ ++ ++ --
                SP -- -- ME -- ME -- MB
                -- ME -- -- -- -- -- --
                -- -- Me -- ME Me -- MB
                ME -- ME __ -- __ ++ ++
                ++ ++ -- -- MS -- ++ ++
                ++ ++ -- ME -- -- -- MB
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
            MAP_SIREN_TEMPLATE=['DD', 'CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'a4': Stage(
        map=dict(
            name='A4',
            shape='I7',
            camera_data=['D3', 'D5', 'F3', 'F5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                ++ ++ ++ ++ ++ -- -- ++ ++
                ++ ++ ++ ++ ++ MB MB ++ ++
                -- ME Me ME -- -- -- ++ ++
                MS -- __ -- -- MS -- Me --
                ++ ++ ME -- ME -- ME __ ME
                ++ ++ -- -- -- ME -- ME --
                ++ ++ SP SP SP ++ ++ -- MS
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
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DD'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
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
            shape='J7',
            camera_data=['E2', 'E5', 'G2', 'G5'],
            camera_data_spawn_point=['G5'],
            map_data="""
                ++ ++ ++ MS -- ME ++ ++ ++ ++
                ++ ++ ++ -- ME __ -- ++ ++ ++
                ++ ++ ++ __ -- ME -- -- ++ ++
                ++ ++ ++ Me ++ ++ ME -- ++ ++
                -- MB -- -- ME ME -- ME -- SP
                -- -- Me -- -- -- -- __ -- SP
                ++ ++ -- Me MS ME Me ++ ME --
            """,
            weight_data="""
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
        config=dict(
            MAP_SIREN_TEMPLATE=['DD', 'CL'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'b2': Stage(
        map=dict(
            name='B2',
            shape='J8',
            camera_data=['D3', 'D6', 'G3', 'G6'],
            camera_data_spawn_point=['G6'],
            map_data="""
                -- -- ++ ++ ++ ++ -- -- ++ ++
                MS -- MB ++ ++ ++ ME -- ++ ++
                -- Me -- -- ++ ++ MS __ -- --
                -- ++ ++ __ ++ ++ ME -- ME --
                Me -- ME -- -- ME -- -- -- SP
                MB -- -- -- -- __ -- ME -- SP
                Me -- ME Me ME -- -- ++ -- SP
                -- Me -- ++ ++ MS ME -- -- --
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
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DD', 'CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c1': Stage(
        map=dict(
            name='C1',
            shape='I6',
            camera_data=['D2', 'D4', 'F2', 'F4'],
            camera_data_spawn_point=['D4'],
            map_data="""
                Me -- -- ME -- -- ME -- Me
                -- -- __ -- -- __ -- -- MB
                ME -- ME ++ ++ ME -- -- --
                -- -- ++ ++ ++ -- -- ME Me
                SP -- ++ ++ -- MS -- ++ ++
                SP SP -- -- -- ME MB ++ ++
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
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(3,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
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
                ++ ++ ME -- Me -- MB
                ++ ++ -- __ -- -- --
                ++ ++ ME -- ME -- Me
                ME -- ME MS -- -- --
                -- ME __ -- -- Me MB
                SP -- -- ME -- ++ ++
                SP SP -- -- ME ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['CL', 'CA', 'BB'],
            MOVABLE_ENEMY_TURN=(3,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'c3': Stage(
        map=dict(
            name='C3',
            shape='H8',
            camera_data=['D3', 'D6', 'E3', 'E6'],
            camera_data_spawn_point=['D3'],
            map_data="""
                -- -- ++ ++ ++ ++ ++ --
                -- SP ++ ++ ++ ++ ++ --
                SP -- -- ME -- ME -- MB
                -- ME -- -- -- -- -- --
                -- -- Me -- ME Me -- MB
                ME -- ME __ -- __ ++ ++
                ++ ++ -- -- MS -- ++ ++
                ++ ++ -- ME -- -- -- MB
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
            MAP_SIREN_TEMPLATE=['CL', 'CA', 'BB', 'CV'],
            MOVABLE_ENEMY_TURN=(3,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c4': Stage(
        map=dict(
            name='C4',
            shape='I7',
            camera_data=['D3', 'D5', 'F3', 'F5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                ++ ++ ++ ++ ++ -- -- ++ ++
                ++ ++ ++ ++ ++ MB MB ++ ++
                -- ME Me ME -- -- -- ++ ++
                MS -- __ -- -- MS -- Me --
                ++ ++ ME -- ME -- ME __ ME
                ++ ++ -- -- -- ME -- ME --
                ++ ++ SP SP SP ++ ++ -- MS
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
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(3,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd1': Stage(
        map=dict(
            name='D1',
            shape='J7',
            camera_data=['E2', 'E5', 'G2', 'G5'],
            camera_data_spawn_point=['G5'],
            map_data="""
                ++ ++ ++ MS -- ME ++ ++ ++ ++
                ++ ++ ++ -- ME __ -- ++ ++ ++
                ++ ++ ++ __ -- ME -- -- ++ ++
                ++ ++ ++ Me ++ ++ ME -- ++ ++
                -- MB -- -- ME ME -- ME -- SP
                -- -- Me -- -- -- -- __ -- SP
                ++ ++ -- Me MS ME Me ++ ME --
            """,
            weight_data="""
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
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA', 'BB'],
            MOVABLE_ENEMY_TURN=(3,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd2': Stage(
        map=dict(
            name='D2',
            shape='J8',
            camera_data=['D3', 'D6', 'G3', 'G6'],
            camera_data_spawn_point=['G6'],
            map_data="""
                -- -- ++ ++ ++ ++ -- -- ++ ++
                MS -- MB ++ ++ ++ ME -- ++ ++
                -- Me -- -- ++ ++ MS __ -- --
                -- ++ ++ __ ++ ++ ME -- ME --
                Me -- ME -- -- ME -- -- -- SP
                MB -- -- -- -- __ -- ME -- SP
                Me -- ME Me ME -- -- ++ -- SP
                -- Me -- ++ ++ MS ME -- -- --
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
            MAP_SIREN_TEMPLATE=['CL', 'CA', 'BB', 'CV'],
            MOVABLE_ENEMY_TURN=(3,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
}
