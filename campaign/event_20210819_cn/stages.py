"""
Stages of event_20210819_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

PLAN = ['clear_siren', 'battle_default']
PLAN_2 = ['clear_siren', 'clear_enemy(scale=(2,))', 'clear_enemy(scale=(3,))', 'battle_default']

STAGES = {
    'a1': Stage(
        map=dict(
            name='A1',
            shape='F7',
            camera_data=['C2', 'C5'],
            camera_data_spawn_point=['C5', 'C2'],
            map_data="""
                -- -- ME -- -- ++
                ME ++ ++ ME -- ME
                -- ++ MS -- SP --
                MB MB __ -- -- ME
                ME MB MS -- SP --
                -- ++ ME ME -- --
                Me ++ Me Me ++ Me
            """,
            weight_data="""
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
            DETECTION_BACKEND='perspective',
            COINCIDENT_POINT_ENCOURAGE_DISTANCE=5,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (50, 175),
                'width': (0, 7),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (175, 255),
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
            shape='F8',
            camera_data=['C2', 'C6'],
            camera_data_spawn_point=['C2'],
            map_data="""
                -- ME -- ME Me ME
                -- ME -- -- MS --
                ++ ++ ++ ME -- --
                SP -- -- -- -- SP
                ME -- -- -- ++ ++
                -- MS ME __ ++ ++
                Me -- ++ -- -- MB
                -- Me -- ME MB MB
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
            shape='G7',
            camera_data=['D2', 'D5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                ++ ++ ME Me ME ++ --
                ++ MS -- ME -- MS ++
                ME -- -- __ -- -- ME
                Me -- SP MB SP -- Me
                ME -- -- MB -- -- ME
                -- MS -- MB ++ ++ ++
                ++ -- ME -- ME -- --
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
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['E2'],
            map_data="""
                -- Me -- ME ++ ++ SP SP
                Me -- MS -- ME -- -- SP
                ++ ME -- -- -- -- -- --
                ++ ME -- -- MS -- ME ++
                Me -- __ ME ++ -- -- --
                MB -- -- MS ++ -- ME ME
                MB MB Me -- ME -- ME --
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
            MAP_SIREN_TEMPLATE=['SS', 'CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            DETECTION_BACKEND='perspective',
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
            EDGE_LINES_HOUGHLINES_THRESHOLD=40,
            COINCIDENT_POINT_ENCOURAGE_DISTANCE=5,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (50, 175),
                'width': (0, 7),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (175, 255),
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
            shape='F9',
            camera_data=['C2', 'C6', 'C7'],
            camera_data_spawn_point=['C2'],
            map_data="""
                Me ME MS MS ME Me
                ME -- -- -- -- ME
                ++ ++ -- -- ++ ++
                ++ ++ SP SP Me ++
                MS -- -- -- -- MS
                ME -- MB MB __ ME
                -- ME ++ ++ -- ME
                -- Me ++ Me -- ME
                -- -- ME -- -- Me
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
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['SS', 'CL'],
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
    'b3': Stage(
        map=dict(
            name='B3',
            shape='G9',
            camera_data=['D2', 'D6', 'D7'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ME -- ME -- ME -- ME
                ++ -- -- Me -- -- ++
                ++ -- ++ ++ ++ -- ++
                MS -- MB MB MB -- MS
                Me ME -- __ -- ME Me
                ++ ++ SP -- SP ++ ++
                ++ ME -- -- -- ME ++
                Me -- -- ME -- -- Me
                -- MS ME -- ME MS --
            """,
            weight_data="""
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
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
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['SS', 'CA'],
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
    'c1': Stage(
        map=dict(
            name='C1',
            shape='F7',
            camera_data=['C2', 'C5'],
            camera_data_spawn_point=['C5', 'C2'],
            map_data="""
                -- -- ME -- -- ++
                ME ++ ++ ME -- ME
                -- ++ MS -- SP --
                MB MB __ -- -- ME
                ME MB MS -- SP --
                -- ++ ME ME -- --
                Me ++ Me Me ++ Me
            """,
            weight_data="""
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
            DETECTION_BACKEND='perspective',
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
            EDGE_LINES_HOUGHLINES_THRESHOLD=40,
            COINCIDENT_POINT_ENCOURAGE_DISTANCE=5,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (100, 195),
                'width': (0, 7),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (195, 255),
                'prominence': 2,
                'distance': 50,
                'wlen': 1000,
            },
        ),
        battle={
            0: PLAN_2,
            4: 'clear_boss',
        },
    ),
    'c2': Stage(
        map=dict(
            name='C2',
            shape='F8',
            camera_data=['C2', 'C6'],
            camera_data_spawn_point=['C2'],
            map_data="""
                -- ME -- ME Me ME
                -- ME -- -- MS --
                ++ ++ ++ ME -- --
                SP -- -- -- -- SP
                ME -- -- -- ++ ++
                -- MS ME __ ++ ++
                Me -- ++ -- -- MB
                -- Me -- ME MB MB
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
            shape='G7',
            camera_data=['D2', 'D5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                ++ ++ ME Me ME ++ --
                ++ MS -- ME -- MS ++
                ME -- -- __ -- -- ME
                Me -- SP MB SP -- Me
                ME -- -- MB -- -- ME
                -- MS -- MB ++ ++ ++
                ++ -- ME -- ME -- --
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
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CLpurple', 'CApurple', 'BBpurple'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN_2,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'sp': Stage(
        map=dict(
            name='SP',
            shape='G7',
            camera_data=['D2', 'D5'],
            camera_data_spawn_point=['D2', 'D5'],
            map_data="""
                Me ++ ME ME -- MS ME
                MS ++ -- -- -- ++ ++
                -- -- SP MB Me -- ME
                ME -- MB __ MB -- ME
                ME -- Me MB SP -- --
                ++ ++ -- -- -- ++ MS
                ME MS -- ME ME ++ ME
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
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['SS', 'BB', 'CV'],
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
