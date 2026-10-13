"""
Stages of war_archives_20210916_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
PLAN = ['clear_siren', 'battle_default']
PLAN_2 = ['clear_siren', 'fleet_boss.clear_boss']
PLAN_3 = [
    'clear_siren',
    'clear_enemy(scale=(1,))',
    "clear_enemy(scale=(2,), genre=['light', 'main', 'enemy'])",
    "clear_enemy(genre=['light', 'main'])",
    'clear_enemy(scale=[2, 3])',
    'battle_default',
]

STAGES = {
    'a2': Stage(
        base=BASE,
        map=dict(
            name='A2',
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ -- -- ME ++ -- -- MB
                -- -- ME -- ++ ME -- ++
                ME ++ ++ Me -- -- -- --
                -- ++ ++ __ -- MS -- Me
                ME -- MS -- Me -- ++ --
                -- ME -- -- -- Me ++ --
                -- -- -- ME MS -- -- ME
                SP SP ++ ++ ++ -- ME ++
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
            fortress_data=['F5', 'G1'],
            spawn_data=[
                {'battle': 0, 'enemy': 1, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
            spawn_data_loop=[
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
            MAP_HAS_MYSTERY=False,
            MAP_HAS_FORTRESS=True,
        ),
        battle={
            0: PLAN_3,
            4: 'clear_boss',
        },
    ),
    'b3': Stage(
        base=BASE,
        map=dict(
            name='B3',
            shape='I9',
            camera_data=['D2', 'D5', 'F3', 'F5', 'F7'],
            camera_data_spawn_point=['D7'],
            map_data="""
                ++ ME ++ ++ ++ ++ ++ -- ++
                ME -- -- ++ -- ++ -- MB --
                ++ -- MS -- -- -- -- -- ++
                ++ ++ -- Me ME Me -- ++ ++
                ++ -- __ ME ME ME -- -- ++
                ++ ++ -- Me ME Me -- ++ ++
                ++ -- MS -- __ -- MS -- ++
                -- -- -- ++ -- ++ -- -- ME
                SP SP ++ ++ ++ ++ ++ ME ++
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
            fortress_data=[('B5', 'E2', 'H5', 'E8'), 'G3'],
            spawn_data=[
                {'battle': 0, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
            spawn_data_loop=[
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
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_FORTRESS=True,
            MAP_SWIPE_MULTIPLY=(0.961, 0.979),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.93, 0.947),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.903, 0.919),
        ),
        battle={
            0: PLAN,
            5: PLAN_2,
        },
    ),
    'c1': Stage(
        base=BASE,
        map=dict(
            name='C1',
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['E5'],
            map_data="""
                -- MB -- ++ ++ ++ -- ME
                ME -- -- ME -- -- Me --
                ++ -- Me -- Me ++ -- ME
                ++ -- __ -- -- -- MS --
                ME -- -- ++ -- ME -- ++
                -- ME -- ME -- -- -- ++
                ++ -- MS -- -- SP SP --
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
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
            spawn_data_loop=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['DD', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_PREDICT=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (120, 215),
                'width': (1.5, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (215, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_CANNY_THRESHOLD=(50, 50),
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': (1, 1.111),
                'CA': (1, 1.111),
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
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ -- -- ME ++ -- -- MB
                -- -- ME -- ++ ME -- ++
                ME ++ ++ Me -- -- -- --
                -- ++ ++ __ -- MS -- Me
                ME -- MS -- Me -- ++ --
                -- ME -- -- -- Me ++ --
                -- -- -- ME MS -- -- ME
                SP SP ++ ++ ++ -- ME ++
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
            fortress_data=['F5', 'G1'],
            spawn_data=[
                {'battle': 0, 'enemy': 1, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
            spawn_data_loop=[
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
            MAP_HAS_MYSTERY=False,
            MAP_HAS_FORTRESS=True,
        ),
        battle={
            0: PLAN_3,
            4: 'clear_boss',
        },
    ),
    'c3': Stage(
        base=BASE,
        map=dict(
            name='C3',
            shape='I9',
            camera_data=['E2', 'E5', 'E7', 'D5'],
            camera_data_spawn_point=['F5'],
            map_data="""
                -- ME ME ++ ++ ++ ME ME ++
                ++ ++ -- -- -- MS -- -- ++
                ++ ++ -- Me ++ Me -- ME --
                ++ -- -- ++ -- ++ -- -- SP
                MB -- MS -- -- __ MS -- --
                ++ -- -- ++ -- ++ -- -- SP
                ++ ++ -- Me ++ Me -- ME --
                ++ ++ -- -- -- MS -- -- ++
                -- ME ME ++ ++ ++ ME ME ++
            """,
            weight_data="""
                50 60 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 60 50 50 50 50 50 50 50
            """,
            fortress_data=['E5', 'B5'],
            spawn_data=[
                {'battle': 0, 'enemy': 1, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
            spawn_data_loop=[
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
            MAP_HAS_MYSTERY=False,
            MAP_HAS_FORTRESS=True,
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
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['D2'],
            map_data="""
                ++ ++ ++ -- ME -- -- ME -- --
                ++ ME -- MS -- -- Me -- ++ --
                SP -- -- ++ Me ME -- ++ ++ ME
                SP -- ME -- __ -- -- Me ++ --
                -- -- -- MS -- MS -- ME -- --
                ME -- Me ++ ++ -- -- -- -- --
                -- ME -- ++ ++ ME -- Me ++ MB
                ++ -- MS -- -- -- -- ++ ++ ++
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
            fortress_data=['G3', 'C7'],
            spawn_data=[
                {'battle': 0, 'enemy': 1, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
            spawn_data_loop=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['DD', 'CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_FORTRESS=True,
            MAP_SWIPE_PREDICT=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 215),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (231, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_CANNY_THRESHOLD=(60, 60),
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': (1, 1.111),
                'CA': (1, 1.111),
                'CV': 1.111,
                'BB': 1.111,
            },
            MAP_SWIPE_MULTIPLY=(1.146, 1.168),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.109, 1.129),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.076, 1.096),
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd2': Stage(
        base=BASE,
        map=dict(
            name='D2',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['G2'],
            map_data="""
                -- ME ++ ++ ++ -- Me ++ SP --
                ++ -- Me ++ ME -- -- -- -- SP
                ++ ME -- MS -- MS -- ME -- --
                ME -- ++ -- __ -- ++ ++ -- --
                -- -- -- ME -- Me ++ ++ -- ME
                ++ ++ ME -- -- MS -- -- MS --
                ++ MB -- -- ++ ME -- -- -- ++
                ++ ++ ME -- -- -- -- Me ++ ++
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
            fortress_data=['I7', 'C7'],
            spawn_data=[
                {'battle': 0, 'enemy': 1, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'boss': 1},
            ],
            spawn_data_loop=[
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
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_FORTRESS=True,
            MAP_SWIPE_MULTIPLY=(1.174, 1.196),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.135, 1.156),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.102, 1.122),
        ),
        battle={
            0: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        base=BASE,
        map=dict(
            name='D3',
            shape='I9',
            camera_data=['D2', 'D5', 'F3', 'F5', 'F7'],
            camera_data_spawn_point=['D7'],
            map_data="""
                ++ ME ++ ++ ++ ++ ++ -- ++
                ME -- -- ++ -- ++ -- MB --
                ++ -- MS -- -- -- -- -- ++
                ++ ++ -- Me ME Me -- ++ ++
                ++ -- __ ME ME ME -- -- ++
                ++ ++ -- Me ME Me -- ++ ++
                ++ -- MS -- __ -- MS -- ++
                -- -- -- ++ -- ++ -- -- ME
                SP SP ++ ++ ++ ++ ++ ME ++
            """,
            weight_data="""
                50 60 50 50 50 50 50 50 50
                60 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 30 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 60
                50 50 50 50 50 50 50 60 50
            """,
            fortress_data=[('B5', 'E2', 'H5', 'E8'), 'G3'],
            spawn_data=[
                {'battle': 0, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'boss': 1},
            ],
            spawn_data_loop=[
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
            MAP_SIREN_TEMPLATE=['CA', 'CV', 'BB'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_FORTRESS=True,
            MAP_SWIPE_MULTIPLY=(0.961, 0.979),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.93, 0.947),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.903, 0.919),
        ),
        battle={
            0: PLAN,
            6: PLAN_2,
        },
    ),
}
