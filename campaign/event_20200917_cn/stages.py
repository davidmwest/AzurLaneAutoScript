"""
Stages of event_20200917_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
PLAN = ['clear_siren', 'battle_default']
PLAN_2 = ['fleet_2_protect', 'clear_siren', 'battle_default']
PLAN_3 = [
    'clear_siren',
    ('when', 'map_is_clear_mode', ['clear_enemy(scale=(2,))', 'clear_enemy(scale=(1,))']),
    'battle_default',
]
PLAN_4 = ['clear_siren', 'clear_enemy(scale=(2,))', 'clear_enemy(scale=(1,))', 'battle_default']
PLAN_5 = ['clear_enemy(scale=(1,))', 'clear_enemy(scale=(2,))', 'battle_default']

STAGES = {
    'ht1': Stage(
        base=BASE,
        map=dict(
            name='HT1',
            shape='K7',
            camera_data=['D3', 'D5', 'H3', 'H5'],
            camera_data_spawn_point=['H5', 'D5'],
            map_data="""
                -- -- ++ -- -- MB -- -- ++ -- --
                -- ++ ++ ++ Me -- Me ++ ++ ++ --
                ++ Me -- ++ ++ -- ++ ++ -- Me ++
                ME -- ME ++ ++ -- ++ ++ ME -- ME
                -- -- -- ME MS -- MS ME -- -- --
                ME -- MS -- -- __ -- -- MS -- ME
                ++ Me -- -- SP -- SP -- -- Me ++
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
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'SS'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            STAGE_ENTRANCE=['blue'],
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 238),
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
            MAP_WALK_USE_CURRENT_FLEET=True,
        ),
        battle={
            0: PLAN_2,
            4: 'clear_boss',
        },
    ),
    'ht2': Stage(
        base=BASE,
        map=dict(
            name='HT2',
            shape='H7',
            camera_data=['D3', 'D5', 'E3', 'E5'],
            camera_data_spawn_point=['E5'],
            portal_data=[('E5', 'E1'), ('E1', 'E5')],
            map_data="""
                -- ++ -- ME -- ME ++ ++
                ME -- Me __ -- -- MB ++
                -- -- -- -- ME -- ++ ME
                ++ ME ++ ++ ++ ++ MS --
                -- ++ Me Me -- Me -- ME
                MS -- -- -- -- -- -- ++
                -- ME ++ ++ SP SP -- MS
            """,
            map_data_loop="""
                -- ++ -- ME -- ME ++ ++
                ME -- Me __ -- -- MB ++
                -- -- -- -- ME -- ++ ME
                ++ ME ++ -- -- -- MS --
                -- ++ Me Me -- Me -- ME
                MS -- -- -- -- -- -- ++
                -- ME ++ ++ SP SP -- MS
            """,
            weight_data="""
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 10 20 50 50
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
        config_base='ht1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CAred'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_PORTAL=True,
        ),
        battle={
            0: PLAN_2,
            4: 'clear_boss',
        },
    ),
    'ht3': Stage(
        base=BASE,
        map=dict(
            name='HT3',
            shape='I9',
            camera_data=['D3', 'D5', 'D7', 'F3', 'F5', 'F7'],
            camera_data_spawn_point=['D5'],
            portal_data=[('I2', 'A1'), ('A1', 'I2'), ('I9', 'H1'), ('H1', 'I9')],
            map_data="""
                -- -- -- ++ ME -- ME -- ++
                -- -- MB ++ -- -- -- -- --
                ++ ++ ++ ++ -- ++ ++ -- ME
                -- MS -- Me -- Me ++ -- --
                ME -- ++ -- __ -- -- -- ME
                -- -- SP -- -- Me ++ ++ ++
                Me -- -- SP ++ -- ++ MB --
                -- MS -- -- -- MS ++ -- --
                ++ -- Me -- ME -- ++ -- --
            """,
            map_data_loop="""
                -- -- -- -- ME -- ME -- ++
                -- -- MB -- -- -- -- -- --
                ++ ++ ++ -- -- ++ ++ -- ME
                -- MS -- Me -- Me ++ -- --
                ME -- ++ -- __ -- -- -- ME
                -- -- SP -- -- Me -- -- --
                Me -- -- SP ++ -- ++ MB --
                -- MS -- -- -- MS ++ -- --
                ++ -- Me -- ME -- ++ -- --
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
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='ht1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CAred'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_PORTAL=True,
        ),
        battle={
            0: PLAN_2,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'ht4': Stage(
        base=BASE,
        map=dict(
            name='HT4',
            shape='K9',
            camera_data=['D2', 'D5', 'D7', 'H2', 'H5', 'H7'],
            camera_data_spawn_point=['D2', 'D7'],
            portal_data=[('I5', 'C5'), ('C5', 'I5'), ('E5', 'E3'), ('E3', 'E5'), ('G5', 'G7'), ('G7', 'G5')],
            map_data="""
                Me -- -- ++ Me -- ME -- ME ++ ++
                -- MS -- ++ -- SP -- __ -- MS --
                -- -- Me ++ -- -- -- ME -- -- --
                ME -- ++ ++ ++ ++ ++ ++ ++ -- ME
                -- -- -- ++ -- MB -- ++ -- -- --
                ME -- ++ ++ ++ ++ ++ ++ ++ -- ME
                -- -- -- ME -- -- -- ++ Me -- --
                -- MS -- __ -- SP -- ++ -- MS --
                ++ ++ ME -- ME -- Me ++ -- -- Me
            """,
            map_data_loop="""
                Me -- -- ++ Me -- ME -- ME ++ ++
                -- MS -- -- -- SP -- __ -- MS --
                -- -- Me ++ -- -- -- ME -- -- --
                ME -- ++ ++ -- ++ -- ++ ++ -- ME
                -- -- -- ++ -- MB -- ++ -- -- --
                ME -- ++ ++ -- ++ -- ++ ++ -- ME
                -- -- -- ME -- -- -- ++ Me -- --
                -- MS -- __ -- SP -- -- -- MS --
                ++ ++ ME -- ME -- Me ++ -- -- Me
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 10 50 50 50 50 50
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
        config_base='ht1',
        config=dict(
            MAP_SIREN_TEMPLATE=['BB', 'SS'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_PORTAL=True,
            MAP_SWIPE_MULTIPLY=(1.23, 1.253),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.19, 1.212),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.155, 1.176),
        ),
        battle={
            0: [
                ('when', 'config.MAP_HAS_MOVABLE_ENEMY', [('do', 'fleet_2_push_forward')]),
                'clear_siren',
                ('when', 'map_is_clear_mode', ['clear_enemy(scale=(2,))', 'clear_enemy(scale=(1,))']),
                'battle_default',
            ],
            2: PLAN_3,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'ht5': Stage(
        base=BASE,
        map=dict(
            name='HT5',
            shape='I9',
            camera_data=['D3', 'D5', 'D7', 'F3', 'F5', 'F7'],
            camera_data_spawn_point=['F7', 'D3'],
            portal_data=[('D3', 'F3'), ('G4', 'G6'), ('F7', 'D7'), ('C6', 'C4')],
            map_data="""
                ++ -- -- -- ++ -- MB -- ++
                -- ME -- ME ++ MS -- MS --
                Me -- SP -- ++ -- __ -- --
                -- ME -- Me ++ Me -- ME --
                ++ ++ ++ ++ -- ++ ++ ++ ++
                -- ME -- Me ++ Me -- ME --
                -- -- __ -- ++ -- SP -- Me
                -- MS -- MS ++ ME -- ME --
                ++ -- MB -- ++ -- -- -- ++
            """,
            map_data_loop="""
                ++ -- -- -- ++ -- MB -- ++
                -- ME -- ME ++ MS -- MS --
                Me -- SP -- -- -- __ -- --
                -- ME -- Me ++ Me -- ME --
                ++ ++ -- ++ -- ++ -- ++ ++
                -- ME -- Me ++ Me -- ME --
                -- -- __ -- -- -- SP -- Me
                -- MS -- MS ++ ME -- ME --
                ++ -- MB -- ++ -- -- -- ++
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
        config_base='ht1',
        config=dict(
            MAP_SIREN_TEMPLATE=['BB', 'CV'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_PORTAL=True,
        ),
        battle={
            0: PLAN_3,
            5: PLAN_5,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'ht6': Stage(
        base=BASE,
        map=dict(
            name='HT6',
            shape='K10',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['D6', 'G6'],
            map_data="""
                -- -- -- ME -- Me -- ME -- -- --
                -- ++ ++ -- MS -- MS -- ++ ++ --
                -- ++ ME -- -- __ -- -- ME ++ --
                Me -- -- ++ ++ -- ++ ++ -- -- Me
                ++ ME -- ++ MS -- MS ++ -- ME ++
                ++ ME -- -- -- MB -- -- -- ME ++
                -- -- ++ Me -- -- -- Me ++ -- --
                -- ++ ++ ++ SP -- SP ++ ++ ++ --
                ++ -- -- ++ ++ -- ++ ++ -- -- ++
                -- -- -- ++ ++ -- ++ ++ -- -- --
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
        config_base='ht1',
        config=dict(
            MAP_SIREN_TEMPLATE=['BB', 'CV', 'SS'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(0.978, 0.997),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.946, 0.964),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.919, 0.935),
        ),
        battle={
            0: [
                'fleet_2_protect',
                'clear_siren',
                'clear_enemy(scale=(2,))',
                'clear_enemy(scale=(1,))',
                'battle_default',
            ],
            2: PLAN_4,
            5: PLAN_5,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'sp': Stage(
        base=BASE,
        map=dict(
            name='SP',
            shape='K9',
            camera_data=['F2', 'F4', 'F7'],
            camera_data_spawn_point=['F2'],
            portal_data=[('E1', 'K1'), ('K1', 'E1'), ('A1', 'G1'), ('G1', 'A1')],
            map_data="""
                -- -- MS ++ -- -- -- ++ MS -- --
                -- -- -- ++ -- __ -- ++ -- -- --
                ++ -- Me ++ SP -- SP ++ Me -- ++
                -- ++ ++ ++ ++ -- ++ ++ ++ ++ --
                -- -- ++ ME -- -- -- ME ++ -- --
                -- -- ++ -- -- MS -- -- ++ -- --
                -- ++ ++ ++ ++ -- ++ ++ ++ ++ --
                ++ -- -- -- ++ -- ++ -- -- -- ++
                -- -- -- -- ++ MB ++ -- -- -- --
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
                {'battle': 1},
                {'battle': 2},
                {'battle': 3},
                {'battle': 4, 'enemy': 2, 'siren': 1},
                {'battle': 5},
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_PORTAL=True,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            STAGE_ENTRANCE=['blue'],
            MAP_SIREN_TEMPLATE=['CV', 'BB'],
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 231),
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
            HOMO_EDGE_COLOR_RANGE=(0, 24),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
            MAP_SWIPE_MULTIPLY=(1.23, 1.253),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.19, 1.212),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.155, 1.176),
            MAP_WALK_USE_CURRENT_FLEET=True,
        ),
        battle={
            0: PLAN,
            7: 'fleet_boss.clear_boss',
        },
    ),
    't1': Stage(
        base=BASE,
        map=dict(
            name='T1',
            shape='K7',
            camera_data=['D3', 'D5', 'H3', 'H5'],
            camera_data_spawn_point=['H5', 'D5'],
            map_data="""
                -- -- ++ -- -- MB -- -- ++ -- --
                -- ++ ++ ++ Me -- Me ++ ++ ++ --
                ++ Me -- ++ ++ -- ++ ++ -- Me ++
                ME -- ME ++ ++ -- ++ ++ ME -- ME
                -- -- -- ME MS -- MS ME -- -- --
                ME -- MS -- -- __ -- -- MS -- ME
                ++ Me -- -- SP -- SP -- -- Me ++
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
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1, 'boss': 1},
                {'battle': 4, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['DD', 'SS'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            STAGE_ENTRANCE=['blue'],
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 238),
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
            MAP_WALK_USE_CURRENT_FLEET=True,
        ),
        battle={
            0: PLAN,
            3: 'clear_boss',
        },
    ),
    't2': Stage(
        base=BASE,
        map=dict(
            name='T2',
            shape='H7',
            camera_data=['D3', 'D5', 'E3', 'E5'],
            camera_data_spawn_point=['E5'],
            portal_data=[('E5', 'E1'), ('E1', 'E5')],
            map_data="""
                -- ++ -- ME -- ME ++ ++
                ME -- Me __ -- -- MB ++
                -- -- -- -- ME -- ++ ME
                ++ ME ++ ++ ++ ++ MS --
                -- ++ Me Me -- Me -- ME
                MS -- -- -- -- -- -- ++
                -- ME ++ ++ SP SP -- MS
            """,
            map_data_loop="""
                -- ++ -- ME -- ME ++ ++
                ME -- Me __ -- -- MB ++
                -- -- -- -- ME -- ++ ME
                ++ ME ++ -- -- -- MS --
                -- ++ Me Me -- Me -- ME
                MS -- -- -- -- -- -- ++
                -- ME ++ ++ SP SP -- MS
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
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_PORTAL=True,
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
            HOMO_EDGE_COLOR_RANGE=(0, 33),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    't3': Stage(
        base=BASE,
        map=dict(
            name='T3',
            shape='I9',
            camera_data=['D3', 'D5', 'D7', 'F3', 'F5', 'F7'],
            camera_data_spawn_point=['D5'],
            portal_data=[('I2', 'A1'), ('A1', 'I2'), ('I9', 'H1'), ('H1', 'I9')],
            map_data="""
                -- -- -- ++ ME -- ME -- ++
                -- -- MB ++ -- -- -- -- --
                ++ ++ ++ ++ -- ++ ++ -- ME
                -- MS -- Me -- Me ++ -- --
                ME -- ++ -- __ -- -- -- ME
                -- -- SP -- -- Me ++ ++ ++
                Me -- -- SP ++ -- ++ MB --
                -- MS -- -- -- MS ++ -- --
                ++ -- Me -- ME -- ++ -- --
            """,
            map_data_loop="""
                -- -- -- -- ME -- ME -- ++
                -- -- MB -- -- -- -- -- --
                ++ ++ ++ -- -- ++ ++ -- ME
                -- MS -- Me -- Me ++ -- --
                ME -- ++ -- __ -- -- -- ME
                -- -- SP -- -- Me -- -- --
                Me -- -- SP ++ -- ++ MB --
                -- MS -- -- -- MS ++ -- --
                ++ -- Me -- ME -- ++ -- --
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
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CAred'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_PORTAL=True,
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
            HOMO_EDGE_COLOR_RANGE=(0, 33),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    't4': Stage(
        base=BASE,
        map=dict(
            name='T4',
            shape='K9',
            camera_data=['D2', 'D5', 'D7', 'H2', 'H5', 'H7'],
            camera_data_spawn_point=['D2', 'D7'],
            portal_data=[('I5', 'C5'), ('C5', 'I5'), ('E5', 'E3'), ('E3', 'E5'), ('G5', 'G7'), ('G7', 'G5')],
            map_data="""
                Me -- -- ++ Me -- ME -- ME ++ ++
                -- MS -- ++ -- SP -- __ -- MS --
                -- -- Me ++ -- -- -- ME -- -- --
                ME -- ++ ++ ++ ++ ++ ++ ++ -- ME
                -- -- -- ++ -- MB -- ++ -- -- --
                ME -- ++ ++ ++ ++ ++ ++ ++ -- ME
                -- -- -- ME -- -- -- ++ Me -- --
                -- MS -- __ -- SP -- ++ -- MS --
                ++ ++ ME -- ME -- Me ++ -- -- Me
            """,
            map_data_loop="""
                Me -- -- ++ Me -- ME -- ME ++ ++
                -- MS -- -- -- SP -- __ -- MS --
                -- -- Me ++ -- -- -- ME -- -- --
                ME -- ++ ++ -- ++ -- ++ ++ -- ME
                -- -- -- ++ -- MB -- ++ -- -- --
                ME -- ++ ++ -- ++ -- ++ ++ -- ME
                -- -- -- ME -- -- -- ++ Me -- --
                -- MS -- __ -- SP -- -- -- MS --
                ++ ++ ME -- ME -- Me ++ -- -- Me
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 10 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
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
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'SS'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_PORTAL=True,
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
            HOMO_EDGE_COLOR_RANGE=(0, 33),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(1.23, 1.253),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.19, 1.212),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.155, 1.176),
        ),
        battle={
            0: [
                ('when', 'config.MAP_HAS_MOVABLE_ENEMY', [('do', 'fleet_2_push_forward')]),
                'clear_siren',
                'battle_default',
            ],
            4: 'clear_boss',
        },
    ),
    't5': Stage(
        base=BASE,
        map=dict(
            name='T5',
            shape='I9',
            camera_data=['D3', 'D5', 'D7', 'F3', 'F5', 'F7'],
            camera_data_spawn_point=['F7', 'D3'],
            portal_data=[('D3', 'F3'), ('G4', 'G6'), ('F7', 'D7'), ('C6', 'C4')],
            map_data="""
                ++ -- -- -- ++ -- MB -- ++
                -- ME -- ME ++ MS -- MS --
                Me -- SP -- ++ -- __ -- --
                -- ME -- Me ++ Me -- ME --
                ++ ++ ++ ++ -- ++ ++ ++ ++
                -- ME -- Me ++ Me -- ME --
                -- -- __ -- ++ -- SP -- Me
                -- MS -- MS ++ ME -- ME --
                ++ -- MB -- ++ -- -- -- ++
            """,
            map_data_loop="""
                ++ -- -- -- ++ -- MB -- ++
                -- ME -- ME ++ MS -- MS --
                Me -- SP -- -- -- __ -- --
                -- ME -- Me ++ Me -- ME --
                ++ ++ -- ++ -- ++ -- ++ ++
                -- ME -- Me ++ Me -- ME --
                -- -- __ -- -- -- SP -- Me
                -- MS -- MS ++ ME -- ME --
                ++ -- MB -- ++ -- -- -- ++
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
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CAred'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_PORTAL=True,
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
            HOMO_EDGE_COLOR_RANGE=(0, 33),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    't6': Stage(
        base=BASE,
        map=dict(
            name='T6',
            shape='K10',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['D6', 'G6'],
            map_data="""
                -- -- -- ME -- Me -- ME -- -- --
                -- ++ ++ -- MS -- MS -- ++ ++ --
                -- ++ ME -- -- __ -- -- ME ++ --
                Me -- -- ++ ++ -- ++ ++ -- -- Me
                ++ ME -- ++ MS -- MS ++ -- ME ++
                ++ ME -- -- -- MB -- -- -- ME ++
                -- -- ++ Me -- -- -- Me ++ -- --
                -- ++ ++ ++ SP -- SP ++ ++ ++ --
                ++ -- -- ++ ++ -- ++ ++ -- -- ++
                -- -- -- ++ ++ -- ++ ++ -- -- --
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
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CA', 'SS'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 238),
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
            MAP_SWIPE_MULTIPLY=(0.978, 0.997),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.946, 0.964),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.919, 0.935),
        ),
        battle={
            0: PLAN_4,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
