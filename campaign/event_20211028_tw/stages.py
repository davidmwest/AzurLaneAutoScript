"""
Stages of event_20211028_tw, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

PLAN = ['clear_siren', 'battle_default']
PLAN_2 = ['clear_siren', 'clear_enemy(scale=(2, 3))', 'battle_default']
PLAN_3 = ['clear_enemy(scale=(1,))', 'clear_enemy(scale=(2,))', 'battle_default']

STAGES = {
    'a1': Stage(
        map=dict(
            name='A1',
            shape='I5',
            camera_data=['D2', 'D3', 'F2', 'F3'],
            camera_data_spawn_point=['D3', 'D2'],
            map_data="""
                SP -- ++ ME -- ME ++ ++ --
                -- ME -- -- ME -- Me ++ Me
                -- -- MS -- -- -- __ -- --
                -- ME -- -- ++ Me -- ME --
                SP -- -- Me ++ -- Me -- MB
            """,
            weight_data="""
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
            spawn_data_loop=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
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
            TRUST_EDGE_LINES=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 215),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (215, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
        ),
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
                SP -- ME -- ME -- -- -- Me MB
                -- -- -- -- -- -- ++ -- -- --
                ++ ++ ++ ME MS -- ++ __ Me ++
                SP -- -- -- ME -- Me -- -- Me
                -- -- ME -- -- -- -- Me -- --
                ++ ME ME -- ++ ME MM -- -- MB
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
                {'battle': 1, 'enemy': 1, 'mystery': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
            spawn_data_loop=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1, 'mystery': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
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
            shape='K7',
            camera_data=['D2', 'D5', 'H2', 'H5'],
            camera_data_spawn_point=['D2', 'D5'],
            map_data="""
                SP ++ ++ ++ ME -- -- -- Me -- MM
                -- -- -- -- -- -- Me -- -- -- --
                ME -- ++ ME -- -- -- -- ++ ++ --
                ME -- -- -- MS ++ __ -- MB ++ --
                -- -- ME -- -- -- -- -- -- -- --
                -- -- ++ ++ ME Me -- Me ++ ++ ++
                SP -- ++ ++ ME -- -- -- -- Me MM
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
                {'battle': 2, 'enemy': 1, 'mystery': 1},
                {'battle': 3, 'enemy': 1, 'mystery': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
            spawn_data_loop=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2, 'mystery': 1},
                {'battle': 3, 'enemy': 1, 'mystery': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
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
    'b1': Stage(
        map=dict(
            name='B1',
            shape='H6',
            camera_data=['D2', 'D4', 'E2', 'E4'],
            camera_data_spawn_point=['D4'],
            map_data="""
                ++ ++ ++ -- -- -- -- MB
                -- -- -- -- __ Me Me --
                ME -- ME ++ ++ ME -- --
                SP -- ME ++ ++ MS ME --
                ME -- -- -- -- -- -- --
                SP -- -- ME -- Me -- MB
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
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            TRUST_EDGE_LINES=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 215),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (215, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
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
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D2', 'D5'],
            map_data="""
                SP -- -- -- -- -- Me ++ MB
                -- Me -- -- ME -- -- ++ --
                -- -- Me ++ ++ ++ -- -- --
                ME __ -- ME Me ME -- MS --
                ME MS -- ++ ++ ++ -- -- --
                -- ME -- ME -- -- -- ++ --
                SP -- -- -- -- ME -- ++ MB
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
                {'battle': 1, 'enemy': 1, 'mystery': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'boss': 1},
            ],
            spawn_data_loop=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1, 'mystery': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA', 'BB'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN_2,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'b3': Stage(
        map=dict(
            name='B3',
            shape='I9',
            camera_data=['D2', 'D6', 'D7', 'E2', 'E6', 'E7'],
            camera_data_spawn_point=['D2', 'D7'],
            map_data="""
                SP -- ++ ++ -- -- -- ME --
                -- ME ++ ++ -- Me -- -- --
                -- -- -- -- -- -- Me Me --
                ME -- ME Me -- ME ++ ++ ++
                -- -- ++ __ -- -- -- MB ++
                -- ME ++ -- -- ME ++ ++ ++
                -- -- MS -- ++ Me -- ME --
                SP -- -- -- ++ -- -- ME --
                SP -- MS -- -- ME -- -- --
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
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='b1',
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
    'c2': Stage(
        map=dict(
            name='C2',
            shape='J6',
            camera_data=['D2', 'D4', 'G2', 'G4'],
            camera_data_spawn_point=['D2', 'D4'],
            map_data="""
                SP -- ME MS ME -- -- -- Me MB
                -- -- -- -- -- -- ++ -- -- --
                ++ ++ ++ ME MS -- ++ __ Me ++
                SP -- -- -- ME -- Me -- -- Me
                -- -- ME -- -- -- -- Me -- --
                ++ ME ME -- ++ ME MM -- -- MB
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
                {'battle': 1, 'enemy': 1, 'mystery': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
            spawn_data_loop=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1, 'mystery': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DD', 'CL'],
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
    'd2': Stage(
        map=dict(
            name='D2',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D2', 'D5'],
            map_data="""
                SP -- -- -- -- -- Me ++ MB
                -- Me -- MS ME -- -- ++ --
                -- -- ME ++ ++ ++ -- -- --
                ME __ -- ME ME ME -- MS --
                ME MS -- ++ ++ ++ -- -- --
                -- ME -- ME -- -- -- ++ --
                SP -- -- -- -- ME -- ++ MB
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
                {'battle': 1, 'enemy': 1, 'mystery': 1},
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA', 'BB'],
            MOVABLE_ENEMY_TURN=(3,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 231),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
        ),
        battle={
            0: PLAN_2,
            5: PLAN_3,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        map=dict(
            name='D3',
            shape='I9',
            camera_data=['D2', 'D6', 'D7', 'E2', 'E6', 'E7'],
            camera_data_spawn_point=['D2', 'D7'],
            map_data="""
                SP -- ++ ++ -- MS -- ME --
                -- ME ++ ++ -- Me -- -- --
                -- -- -- -- -- -- Me Me --
                ME -- Me ME -- Me ++ ++ ++
                -- -- ++ __ -- -- -- MB ++
                -- ME ++ -- -- ME ++ ++ ++
                -- -- MS -- ++ Me -- ME --
                SP -- -- -- ++ -- -- ME --
                SP -- MS -- -- ME -- -- --
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
                {'battle': 5},
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
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 215),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
                'wlen': 100,
            },
        ),
        battle={
            0: PLAN_2,
            5: PLAN_3,
            6: 'fleet_boss.clear_boss',
        },
    ),
}
