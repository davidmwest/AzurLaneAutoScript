"""
Stages of event_20210624_tw, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

PLAN = ['clear_siren', 'battle_default']
PLAN_2 = [
    'clear_siren',
    'clear_enemy(scale=(1,))',
    "clear_enemy(scale=(2,), genre=['light', 'main', 'enemy', 'carrier'])",
    "clear_enemy(genre=['light', 'main'])",
    'battle_default',
]
PLAN_3 = [
    'clear_siren',
    "clear_enemy(scale=(2,), genre=['light', 'main', 'enemy', 'carrier'])",
    "clear_enemy(scale=(3,), genre=['light', 'main', 'enemy', 'carrier'])",
    'battle_default',
]
PLAN_4 = [
    'clear_enemy(scale=(1,))',
    "clear_enemy(scale=(2,), genre=['light', 'main', 'enemy', 'carrier'])",
    "clear_enemy(genre=['light', 'main'])",
    'battle_default',
]

STAGES = {
    'a1': Stage(
        map=dict(
            name='A1',
            shape='H6',
            camera_data=['D2', 'D4', 'E2', 'E4'],
            camera_data_spawn_point=['D2', 'D4'],
            map_data="""
                Me ME ++ ME ME Me ++ ++
                ME -- ME MS MS -- MB MB
                ++ SP -- ++ __ ME -- MB
                ++ SP -- -- __ ME -- Me
                ME -- ME MS MS -- -- ME
                Me ME ++ ++ ++ Me ME ++
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
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            TRUST_EDGE_LINES=False,
            COINCIDENT_POINT_ENCOURAGE_DISTANCE=1.5,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (100, 231),
                'width': 1,
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (231, 255),
                'prominence': 2,
                'distance': 50,
                'wlen': 1000,
            },
            DETECTION_BACKEND='perspective',
        ),
        battle={
            0: PLAN,
            3: 'clear_boss',
        },
    ),
    'a2': Stage(
        map=dict(
            name='A2',
            shape='I6',
            camera_data=['D2', 'D4', 'F2', 'F4'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- SP -- -- MS -- ME Me ++
                SP -- Me ++ ++ MB -- ME ++
                ++ -- -- MB MB __ Me -- ME
                ++ MS ++ __ MS -- -- -- ME
                ME -- ME -- ++ ++ ME -- ME
                -- ME -- ME ++ ++ -- Me --
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
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'a3': Stage(
        map=dict(
            name='A3',
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- Me ME ++ ++ Me ME ME
                ME -- -- MS -- -- MB --
                ++ ++ -- ME __ Me ++ ++
                ME ME -- ++ -- ME ++ ++
                ME -- -- ++ -- MS MB ME
                SP SP -- -- __ -- ME --
                -- SP Me ++ Me MS -- ME
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
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
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
            shape='F9',
            camera_data=['C2', 'C6', 'C7'],
            camera_data_spawn_point=['C7'],
            map_data="""
                -- ME ++ ++ -- ME
                ME Me ++ ++ ME ME
                ++ -- MB MB -- --
                ME -- ME Me ++ Me
                ME MS __ __ Me ME
                ++ ++ MS -- MS --
                ++ MS -- ME ++ ME
                ME -- SP -- Me --
                ME -- SP SP -- ME
            """,
            weight_data="""
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['LaGalissonniere', 'Algerie'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            TRUST_EDGE_LINES=False,
            COINCIDENT_POINT_ENCOURAGE_DISTANCE=1.5,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (100, 231),
                'width': 1,
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (231, 255),
                'prominence': 2,
                'distance': 50,
                'wlen': 1000,
            },
            DETECTION_BACKEND='perspective',
        ),
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
            camera_data_spawn_point=['H5', 'D5'],
            map_data="""
                -- ME ME ME ++ ME -- -- ME ++ ++
                ME -- -- -- -- -- ++ ++ -- -- Me
                ++ -- Me Me __ ME ++ ++ ME __ --
                ME -- -- MS -- MS MB MB MS -- MS
                -- Me -- -- -- -- MB MB -- -- --
                ++ ++ Me -- SP -- ++ ++ -- SP --
                ++ -- -- -- -- -- ME ME -- -- --
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
            wall_data="""
    ·   · | ·   ·   ·   ·   ·   ·   ·   ·   · ,
          +                                   ,
    ·   ·   ·   ·   ·   ·   ·   ·   ·   · | · ,
          +       +   +               +   +   ,
    ·   · | ·   · | · | ·   ·   ·   · | ·   · ,
          +---+---+   |               |   +   ,
    ·   ·   · | ·   · | ·   ·   ·   · | · | · ,
              +---+   +---+       +---+   +-- ,
    ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   · ,
                                              ,
    ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   · ,
                                              ,
    ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   · ,
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
            MAP_SIREN_TEMPLATE=['Vauquelin', 'Algerie'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_WALL=True,
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'b3': Stage(
        map=dict(
            name='B3',
            shape='N10',
            camera_data=['F2', 'F6', 'F8', 'I2', 'I6', 'I8'],
            camera_data_spawn_point=['F8', 'I8'],
            map_data="""
                -- -- -- -- -- ME -- -- ME -- -- -- -- ++
                -- -- -- ME -- -- MB MB -- -- ME -- -- --
                ++ -- ME -- Me ME -- -- ME Me -- ME -- --
                ++ -- -- ME -- -- __ __ -- -- ME -- -- --
                -- -- -- -- Me MS -- -- MS Me -- -- ++ ++
                -- ++ -- ME ++ ++ -- -- ++ ++ ME -- -- --
                -- ++ -- ME ++ ++ -- -- ++ ++ ME -- -- --
                -- -- -- -- Me MS -- -- MS Me -- -- ++ ++
                ++ -- -- -- -- -- -- -- -- -- -- -- ++ ++
                -- -- -- -- -- -- SP SP -- -- -- -- -- --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50
            """,
            wall_data="""
    ·   ·   ·   ·   · | ·   ·   ·   · | ·   ·   ·   ·   · ,
          +-----------+               +-----------+       ,
    ·   · | ·   ·   · | ·   ·   ·   · | ·   ·   · | ·   · ,
          |           |               |           |       ,
    ·   · | ·   ·   · | ·   ·   ·   · | ·   ·   · | ·   · ,
          +---+       +---+       +----+       +---+       ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |            ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              +-----------+       +-----------+           ,
    ·   ·   ·   ·   ·   · | ·   · | ·   ·   ·   ·   ·   · ,
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
            MAP_SIREN_TEMPLATE=['Vauquelin', 'LaGalissonniere'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_WALL=True,
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
            camera_data_spawn_point=['D2', 'D4'],
            map_data="""
                Me ME ++ ME ME Me ++ ++
                ME -- ME MS MS -- MB MB
                ++ SP -- ++ __ ME -- MB
                ++ SP -- -- __ ME -- Me
                ME -- ME MS MS -- -- ME
                Me ME ++ ++ ++ Me ME ++
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
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            TRUST_EDGE_LINES=False,
            COINCIDENT_POINT_ENCOURAGE_DISTANCE=1.5,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (100, 239),
                'width': 1,
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (239, 255),
                'prominence': 2,
                'distance': 50,
                'wlen': 1000,
            },
            DETECTION_BACKEND='perspective',
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'c2': Stage(
        map=dict(
            name='C2',
            shape='I6',
            camera_data=['D2', 'D4', 'F2', 'F4'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- SP -- -- MS -- ME Me ++
                SP -- Me ++ ++ MB -- ME ++
                ++ -- -- MB MB __ Me -- ME
                ++ MS ++ __ MS -- -- -- ME
                ME -- ME -- ++ ++ ME -- ME
                -- ME -- ME ++ ++ -- Me --
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
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN_2,
            4: 'clear_boss',
        },
    ),
    'c3': Stage(
        map=dict(
            name='C3',
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- Me ME ++ ++ Me ME ME
                ME -- -- MS -- -- MB --
                ++ ++ -- ME __ Me ++ ++
                ME ME -- ++ -- ME ++ ++
                ME -- -- ++ -- MS MB ME
                SP SP -- -- __ -- ME --
                -- SP Me ++ Me MS -- ME
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
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd1': Stage(
        map=dict(
            name='D1',
            shape='F9',
            camera_data=['C2', 'C6', 'C7'],
            camera_data_spawn_point=['C7'],
            map_data="""
                -- ME ++ ++ -- ME
                ME Me ++ ++ ME ME
                ++ -- MB MB -- --
                ME -- ME Me ++ Me
                ME MS __ __ Me ME
                ++ ++ MS -- MS --
                ++ MS -- ME ++ ME
                ME -- SP -- Me --
                ME -- SP SP -- ME
            """,
            weight_data="""
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['LaGalissonniere', 'Algerie'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            TRUST_EDGE_LINES=False,
            COINCIDENT_POINT_ENCOURAGE_DISTANCE=1.5,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (100, 239),
                'width': 1,
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (239, 255),
                'prominence': 2,
                'distance': 50,
                'wlen': 1000,
            },
            DETECTION_BACKEND='perspective',
        ),
        battle={
            0: PLAN_2,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd2': Stage(
        map=dict(
            name='D2',
            shape='K7',
            camera_data=['D2', 'D5', 'H2', 'H5'],
            camera_data_spawn_point=['H5', 'D5'],
            map_data="""
                -- ME ME ME ++ ME -- -- ME ++ ++
                ME -- -- -- -- -- ++ ++ -- -- Me
                ++ -- Me Me __ ME ++ ++ ME __ --
                ME -- -- MS -- MS MB MB MS -- MS
                -- Me -- -- -- -- MB MB -- -- --
                ++ ++ Me -- SP -- ++ ++ -- SP --
                ++ -- -- -- -- -- ME ME -- -- --
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
            wall_data="""
    ·   · | ·   ·   ·   ·   ·   ·   ·   ·   · ,
          +                                   ,
    ·   ·   ·   ·   ·   ·   ·   ·   ·   · | · ,
          +       +   +               +   +   ,
    ·   · | ·   · | · | ·   ·   ·   · | ·   · ,
          +---+---+   |               |   +   ,
    ·   ·   · | ·   · | ·   ·   ·   · | · | · ,
              +---+   +---+       +---+   +-- ,
    ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   · ,
                                              ,
    ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   · ,
                                              ,
    ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   · ,
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
            MAP_SIREN_TEMPLATE=['Vauquelin', 'Algerie'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_WALL=True,
        ),
        battle={
            0: PLAN_3,
            5: PLAN_4,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        map=dict(
            name='D3',
            shape='N10',
            camera_data=['F2', 'F6', 'F8', 'I2', 'I6', 'I8'],
            camera_data_spawn_point=['F8', 'I8'],
            map_data="""
                -- -- -- -- -- ME -- -- ME -- -- -- -- ++
                -- -- -- ME -- -- MB MB -- -- ME -- -- --
                ++ -- ME -- Me ME -- -- ME Me -- ME -- --
                ++ -- -- ME -- -- __ __ -- -- ME -- -- --
                -- -- -- -- Me MS -- -- MS Me -- -- ++ ++
                -- ++ -- ME ++ ++ -- -- ++ ++ ME -- -- --
                -- ++ -- ME ++ ++ -- -- ++ ++ ME -- -- --
                -- -- -- -- Me MS -- -- MS Me -- -- ++ ++
                ++ -- -- -- -- -- -- -- -- -- -- -- ++ ++
                -- -- -- -- -- -- SP SP -- -- -- -- -- --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50
            """,
            wall_data="""
    ·   ·   ·   ·   · | ·   ·   ·   · | ·   ·   ·   ·   · ,
          +-----------+               +-----------+       ,
    ·   · | ·   ·   · | ·   ·   ·   · | ·   ·   · | ·   · ,
          |           |               |           |       ,
    ·   · | ·   ·   · | ·   ·   ·   · | ·   ·   · | ·   · ,
          +---+       +---+       +----+       +---+       ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |            ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              +-----------+       +-----------+           ,
    ·   ·   ·   ·   ·   · | ·   · | ·   ·   ·   ·   ·   · ,
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
            MAP_SIREN_TEMPLATE=['Vauquelin', 'LaGalissonniere'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_WALL=True,
        ),
        battle={
            0: PLAN_3,
            5: PLAN_4,
            6: 'fleet_boss.brute_clear_boss',
        },
    ),
    'sp': Stage(
        map=dict(
            name='SP',
            shape='K9',
            camera_data=['D3', 'D6', 'E3', 'E6'],
            camera_data_spawn_point=['D3', 'D6'],
            map_data="""
                ++ ++ -- -- -- -- -- -- -- ++ --
                -- -- ME ME MS MS ME ME -- ++ --
                -- Me -- -- -- -- -- Me -- -- --
                SP -- -- Me ME -- MB ++ ++ ++ --
                -- ME ++ ++ ++ __ MB ++ ++ ++ --
                SP -- -- Me ME -- MB ++ ++ ++ --
                -- Me -- -- -- -- -- Me -- -- --
                -- -- ME ME MS MS ME ME -- ++ --
                ++ -- -- -- -- -- -- -- -- -- --
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
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Vauquelin', 'LaGalissonniere', 'Algerie'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
        ),
        battle={
            0: PLAN,
            7: 'fleet_boss.clear_boss',
        },
    ),
}
