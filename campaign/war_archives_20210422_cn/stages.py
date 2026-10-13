"""
Stages of war_archives_20210422_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '..campaign_war_archives.campaign_base:CampaignBase'
PLAN = ['clear_siren', 'battle_default']

STAGES = {
    'a1': Stage(
        base=BASE,
        map=dict(
            name='A1',
            shape='I7',
            camera_data=['D3', 'D5', 'F3', 'F5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- -- ++ -- -- -- ++ -- --
                -- -- MS ME -- ME ++ ME --
                ++ ++ -- -- ME -- Me -- ME
                -- -- __ -- -- -- -- ++ --
                SP -- -- MS -- Me -- -- ME
                SP -- -- Me ++ ++ ME -- ME
                -- -- ME -- ++ ++ -- MB --
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
            MAP_SIREN_TEMPLATE=['DD'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
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
            MAP_SWIPE_MULTIPLY=(1.097, 1.117),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.061, 1.08),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.03, 1.048),
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
            3: 'clear_boss',
        },
    ),
    'a2': Stage(
        base=BASE,
        map=dict(
            name='A2',
            shape='I7',
            camera_data=['D3', 'D5', 'F3', 'F5'],
            camera_data_spawn_point=['D3'],
            map_data="""
                ++ -- -- -- ++ ++ -- -- ++
                ++ SP -- SP ++ ++ -- ME ME
                ME -- -- -- -- -- Me -- --
                ++ MS -- MS ++ -- -- -- MB
                ME -- __ -- Me -- Me -- --
                -- Me MS -- -- ME ++ ME ME
                ++ ++ -- ME ME -- ++ ++ --
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
        base=BASE,
        map=dict(
            name='A3',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['D2', 'D6'],
            map_data="""
                ++ ++ ME -- ++ ++ -- -- ++ ++
                ++ ++ -- ME ++ -- ME ME -- ++
                SP -- -- Me ++ Me -- -- Me ++
                -- SP -- -- MS -- -- -- -- ME
                -- SP -- -- -- __ -- MB ++ --
                SP -- -- -- MS -- -- -- -- ME
                ++ ++ ME MS ++ ++ Me -- ME ++
                ++ ++ -- -- -- ME -- -- ME --
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
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b1': Stage(
        base=BASE,
        map=dict(
            name='B1',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['G2', 'D2'],
            map_data="""
                -- MS ++ SP MB SP ++ MS ME --
                ME -- -- -- __ -- -- -- -- ME
                Me -- ++ MS -- MS ++ Me -- ++
                ++ -- ++ ++ -- ++ ++ ++ -- ++
                ME -- -- -- -- -- -- -- -- --
                -- Me -- ++ ++ ++ -- ++ ++ --
                ME -- -- ++ -- ME -- ME Me --
                ++ ME -- -- ME -- Me -- -- ME
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
            maze_data=[('D5', 'I4', 'J6'), ('B4', 'E4', 'D8'), ('C2', 'G2', 'G6')],
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
            MAP_SIREN_TEMPLATE=['Gloucester', 'York'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
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
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_HAS_MAZE=True,
            MAP_SWIPE_MULTIPLY=(1.207, 1.229),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.167, 1.189),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.133, 1.153),
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b2': Stage(
        base=BASE,
        map=dict(
            name='B2',
            shape='I9',
            camera_data=['D3', 'D5', 'D7', 'F3', 'D5', 'F7'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- SP -- -- -- MS -- ME --
                SP -- -- ++ MS -- ++ -- ME
                -- -- __ -- ++ -- -- ++ --
                -- ++ Me -- Me ++ -- -- ME
                -- MS ++ -- -- -- ++ ME --
                MS -- -- ++ Me -- Me ++ --
                -- ++ -- -- ++ -- -- -- --
                ME -- ++ -- ME ++ -- MB ME
                -- ME -- ME -- -- -- ME --
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
            maze_data=[('A4', 'I6'), ('F9', 'D1', 'E5'), ('A7', 'C9', 'G1', 'I3')],
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
            MAP_SIREN_TEMPLATE=['Gloucester', 'York'],
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
        base=BASE,
        map=dict(
            name='B3',
            shape='I9',
            camera_data=['D2', 'D5', 'D7', 'F2', 'F5', 'F7'],
            camera_data_spawn_point=['F7', 'D7'],
            map_data="""
                -- ME -- -- Me -- -- ME --
                ME -- ++ ++ -- ++ ++ -- ME
                -- ++ ++ MS -- MS ++ ++ --
                -- ++ Me -- -- -- Me ++ --
                ME -- -- -- MB -- -- -- ME
                -- ++ MS -- __ -- MS ++ --
                -- ++ ++ Me -- Me ++ ++ --
                ME -- ++ ++ -- ++ ++ -- ME
                -- ME -- SP -- SP -- ME --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 10 10 10 50 50 50
                50 50 10 10 10 10 10 50 50
                50 50 10 10 10 10 10 50 50
                50 50 10 10 50 10 10 50 50
                50 50 50 10 10 10 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
            """,
            maze_data=[('A3', 'I3', 'C9', 'G9'), ('E2', 'B5', 'H5', 'E8'), ('C1', 'G1', 'A7', 'I7')],
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
            MAP_SIREN_TEMPLATE=['Gloucester', 'York', 'Warspite'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(1.002, 1.021),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.97, 0.987),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.941, 0.958),
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c1': Stage(
        base=BASE,
        map=dict(
            name='C1',
            shape='I7',
            camera_data=['D3', 'D5', 'F3', 'F5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- -- ++ -- -- -- ++ -- --
                -- -- MS ME -- ME ++ ME --
                ++ ++ -- -- ME -- Me -- ME
                -- -- __ -- -- -- -- ++ --
                SP -- -- MS -- Me -- -- ME
                SP -- -- Me ++ ++ ME -- ME
                -- -- ME -- ++ ++ -- MB --
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
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(1.097, 1.117),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.061, 1.08),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.03, 1.048),
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
        base=BASE,
        map=dict(
            name='C2',
            shape='I7',
            camera_data=['D3', 'D5', 'F3', 'F5'],
            camera_data_spawn_point=['D3'],
            map_data="""
                ++ -- -- -- ++ ++ -- -- ++
                ++ SP -- SP ++ ++ -- ME ME
                ME -- -- -- -- -- Me -- --
                ++ MS -- MS ++ -- -- -- MB
                ME -- __ -- Me -- Me -- --
                -- Me MS -- -- ME ++ ME ME
                ++ ++ -- ME ME -- ++ ++ --
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
                'clear_enemy(scale=(2,))',
                'clear_enemy(scale=(3,))',
                'battle_default',
            ],
            4: 'clear_boss',
        },
    ),
    'c3': Stage(
        base=BASE,
        map=dict(
            name='C3',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['D2', 'D6'],
            map_data="""
                ++ ++ ME -- ++ ++ -- -- ++ ++
                ++ ++ -- ME ++ -- ME ME -- ++
                SP -- -- Me ++ Me -- -- Me ++
                -- SP -- -- MS -- -- -- -- ME
                -- SP -- -- -- __ -- MB ++ --
                SP -- -- -- MS -- -- -- -- ME
                ++ ++ ME MS ++ ++ Me -- ME ++
                ++ ++ -- -- -- ME -- -- ME --
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
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        base=BASE,
        map=dict(
            name='D3',
            shape='I9',
            camera_data=['D2', 'D5', 'D7', 'F2', 'F5', 'F7'],
            camera_data_spawn_point=['F7', 'D7'],
            map_data="""
                -- ME -- -- Me -- -- ME --
                ME -- ++ ++ -- ++ ++ -- ME
                -- ++ ++ MS -- MS ++ ++ --
                -- ++ Me -- -- -- Me ++ --
                ME -- -- -- MB -- -- -- ME
                -- ++ MS -- __ -- MS ++ --
                -- ++ ++ Me -- Me ++ ++ --
                ME -- ++ ++ -- ++ ++ -- ME
                -- ME -- SP -- SP -- ME --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 10 10 10 50 50 50
                50 50 10 10 10 10 10 50 50
                50 50 10 10 10 10 10 50 50
                50 50 10 10 50 10 10 50 50
                50 50 50 10 10 10 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
            """,
            maze_data=[('A3', 'I3', 'C9', 'G9'), ('E2', 'B5', 'H5', 'E8'), ('C1', 'G1', 'A7', 'I7')],
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
            MAP_SIREN_TEMPLATE=['Warspite', 'Formidable', 'Illustrious'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(1.002, 1.021),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.97, 0.987),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.941, 0.958),
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
        ),
        battle={
            0: ['clear_siren', 'clear_enemy(scale=(2,))', 'clear_enemy(scale=(3,))', 'battle_default'],
            5: [
                'clear_enemy(scale=(1,))',
                'clear_enemy(scale=(2,))',
                'clear_enemy(scale=(3,))',
                'battle_default',
            ],
            6: 'fleet_boss.clear_boss',
        },
    ),
}
