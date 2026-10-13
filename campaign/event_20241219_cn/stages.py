"""
Stages of event_20241219_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']
PLAN_2 = ['clear_siren', "clear_enemy(sort=('weight', 'cost_2', 'cost_1'))", 'battle_default']

STAGES = {
    'a1': Stage(
        base=BASE,
        map=dict(
            name='A1',
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- -- ME ++ ++ ++ -- ++ ++
                ++ ME -- MS -- MS -- ++ ++
                -- -- -- -- MB -- -- Me ++
                -- ME -- -- __ -- -- Me --
                ME -- ++ SP -- SP ++ ++ ++
                -- ME ++ -- -- -- -- ME --
                -- -- Me -- Me ++ -- -- ME
                ++ -- -- -- -- ++ -- ME --
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
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1, 'boss': 1},
                {'battle': 4, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_CHAPTER_SWITCH_20241219=True,
            MAP_HAS_MODE_SWITCH=True,
            MAP_HAS_MOVABLE_NORMAL_ENEMY=True,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
            MOVABLE_NORMAL_ENEMY_TURN=(2,),
            MAP_SIREN_MOVE_WAIT=0.7,
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
            MAP_SWIPE_MULTIPLY=(1.127, 1.148),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.09, 1.11),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.058, 1.077),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            3: 'clear_boss',
        },
    ),
    'a2': Stage(
        base=BASE,
        map=dict(
            name='A2',
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ME -- -- ME -- -- ME -- --
                -- -- ME -- ++ ME -- ME --
                ME -- -- ME -- -- -- ++ ++
                ++ -- Me ++ ++ ++ -- Me ++
                ++ -- -- MS MB MS -- -- --
                -- -- -- -- MS -- -- -- ME
                -- ++ Me -- __ -- Me ++ --
                ++ ME -- SP -- SP -- ME ++
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
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.108, 1.129),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.072, 1.092),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.041, 1.059),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'a3': Stage(
        base=BASE,
        map=dict(
            name='A3',
            shape='K9',
            camera_data=['D2', 'D5', 'D7', 'H2', 'H5', 'H7'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ME -- -- -- ME -- -- -- ME ++ ++
                -- -- ++ -- -- -- ME -- -- ++ --
                ME -- ME ++ ++ ++ ++ ++ -- ME --
                ++ -- -- ++ ++ ++ MB ++ -- -- ME
                ++ -- Me ++ ++ ++ -- Me -- -- --
                Me -- -- SP -- SP -- -- -- ME ME
                -- -- -- -- __ -- -- Me ++ -- --
                ++ ++ MS -- MS -- MS -- ME ++ ++
                -- ++ -- ME -- ME -- ++ -- ++ ++
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
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.127, 1.148),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.09, 1.11),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.058, 1.077),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b1': Stage(
        base=BASE,
        map=dict(
            name='B1',
            shape='K8',
            camera_data=['D2', 'D6', 'H2', 'H6'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- -- -- ++ SP -- SP ++ ++ ++ MB
                -- ME ++ ++ -- __ -- -- Me -- --
                ME -- Me -- -- MS -- -- -- -- ME
                -- -- -- -- MS -- MS Me -- ++ --
                -- ME ++ Me -- -- ++ ++ -- ME --
                -- -- ++ -- Me ++ ++ ++ -- -- --
                ++ -- ME -- -- ME -- ME -- -- ME
                -- -- -- -- ++ -- ME -- -- ME ++
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_CHAPTER_SWITCH_20241219=True,
            MAP_HAS_MODE_SWITCH=True,
            MAP_HAS_MOVABLE_NORMAL_ENEMY=True,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
            MOVABLE_NORMAL_ENEMY_TURN=(2,),
            MAP_SIREN_MOVE_WAIT=0.7,
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
            MAP_SWIPE_MULTIPLY=(1.254, 1.278),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.213, 1.235),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.178, 1.199),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b2': Stage(
        base=BASE,
        map=dict(
            name='B2',
            shape='K8',
            camera_data=['D2', 'D5', 'H2', 'H5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- -- ME ++ ++ MB ++ ++ -- -- --
                -- ME -- ++ MS -- MS ++ Me ++ ++
                ME -- -- Me -- MS -- Me -- ++ ++
                ++ -- Me -- -- __ -- -- -- ME ME
                ++ -- -- -- SP -- SP -- -- -- --
                ME -- ME -- ++ ++ ++ Me -- ++ --
                -- ++ ++ ME ++ -- ++ -- ME -- ME
                -- -- ++ -- -- ++ -- -- ++ ++ ++
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.168, 1.19),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.13, 1.151),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.097, 1.117),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'b3': Stage(
        base=BASE,
        map=dict(
            name='B3',
            shape='K9',
            camera_data=['D2', 'D5', 'D7', 'H2', 'H5', 'H7'],
            camera_data_spawn_point=['D6'],
            map_covered=['I3', 'I4'],
            map_data="""
                ME -- -- -- ME -- -- -- ME ++ ++
                -- -- ++ -- -- -- ME -- -- ++ --
                ME -- ME ++ ++ ++ ++ ++ -- ME --
                ++ -- -- ++ ++ ++ MB ++ -- -- ME
                ++ -- Me ++ ++ ++ -- Me -- -- --
                Me -- -- SP -- SP -- -- -- ME ME
                -- -- -- -- __ -- -- Me ++ -- --
                ++ ++ MS -- MS -- MS -- ME ++ ++
                -- ++ -- ME -- ME -- ++ -- ++ ++
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.135, 1.157),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.098, 1.118),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.066, 1.085),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c1': Stage(
        base=BASE,
        map=dict(
            name='C1',
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- -- ME ++ ++ ++ -- ++ ++
                ++ ME -- MS -- MS -- ++ ++
                -- -- -- -- MB -- -- Me ++
                -- ME -- -- __ -- -- Me --
                ME -- ++ SP -- SP ++ ++ ++
                -- ME ++ -- -- -- -- ME --
                -- -- Me -- Me ++ -- -- ME
                ++ -- -- -- -- ++ -- ME --
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
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_CHAPTER_SWITCH_20241219=True,
            MAP_HAS_MODE_SWITCH=True,
            MAP_HAS_MOVABLE_NORMAL_ENEMY=True,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
            MOVABLE_NORMAL_ENEMY_TURN=(2,),
            MAP_SIREN_MOVE_WAIT=0.7,
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
            MAP_SWIPE_MULTIPLY=(1.127, 1.148),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.09, 1.11),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.058, 1.077),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'c2': Stage(
        base=BASE,
        map=dict(
            name='C2',
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ME -- -- ME -- -- ME -- --
                -- -- ME -- ++ ME -- ME --
                ME -- -- ME -- -- -- ++ ++
                ++ -- Me ++ ++ ++ -- Me ++
                ++ -- -- MS MB MS -- -- --
                -- -- -- -- MS -- -- -- ME
                -- ++ Me -- __ -- Me ++ --
                ++ ME -- SP -- SP -- ME ++
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
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.108, 1.129),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.072, 1.092),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.041, 1.059),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'c3': Stage(
        base=BASE,
        map=dict(
            name='C3',
            shape='K9',
            camera_data=['D2', 'D5', 'D7', 'H2', 'H5', 'H7'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ME -- -- -- ME -- -- -- ME ++ ++
                -- -- ++ -- -- -- ME -- -- ++ --
                ME -- ME ++ ++ ++ ++ ++ -- ME --
                ++ -- -- ++ ++ ++ MB ++ -- -- ME
                ++ -- Me ++ ++ ++ -- Me -- -- --
                Me -- -- SP -- SP -- -- -- ME ME
                -- -- -- -- __ -- -- Me ++ -- --
                ++ ++ MS -- MS -- MS -- ME ++ ++
                -- ++ -- ME -- ME -- ++ -- ++ ++
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.127, 1.148),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.09, 1.11),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.058, 1.077),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd1': Stage(
        base=BASE,
        map=dict(
            name='D1',
            shape='K8',
            camera_data=['D2', 'D6', 'H2', 'H6'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- -- -- ++ SP -- SP ++ ++ ++ MB
                -- ME ++ ++ -- __ -- -- Me -- --
                ME -- Me -- -- MS -- -- -- -- ME
                -- -- -- -- MS -- MS Me -- ++ --
                -- ME ++ Me -- -- ++ ++ -- ME --
                -- -- ++ -- Me ++ ++ ++ -- -- --
                ++ -- ME -- -- ME -- ME -- -- ME
                -- -- -- -- ++ -- ME -- -- ME ++
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_CHAPTER_SWITCH_20241219=True,
            MAP_HAS_MODE_SWITCH=True,
            MAP_HAS_MOVABLE_NORMAL_ENEMY=True,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
            MOVABLE_NORMAL_ENEMY_TURN=(2,),
            MAP_SIREN_MOVE_WAIT=0.7,
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
            MAP_SWIPE_MULTIPLY=(1.254, 1.278),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.213, 1.235),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.178, 1.199),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd2': Stage(
        base=BASE,
        map=dict(
            name='D2',
            shape='K8',
            camera_data=['D2', 'D5', 'H2', 'H5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- -- ME ++ ++ MB ++ ++ -- -- --
                -- ME -- ++ MS -- MS ++ Me ++ ++
                ME -- -- Me -- MS -- Me -- ++ ++
                ++ -- Me -- -- __ -- -- -- ME ME
                ++ -- -- -- SP -- SP -- -- -- --
                ME -- ME -- ++ ++ ++ Me -- ++ --
                -- ++ ++ ME ++ -- ++ -- ME -- ME
                -- -- ++ -- -- ++ -- -- ++ ++ ++
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.168, 1.19),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.13, 1.151),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.097, 1.117),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default'],
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        base=BASE,
        map=dict(
            name='D3',
            shape='K9',
            camera_data=['D2', 'D5', 'D7', 'H2', 'H5', 'H7'],
            camera_data_spawn_point=['D6'],
            map_covered=['I3', 'I4'],
            map_data="""
                ME -- -- -- ME -- -- -- ME ++ ++
                -- -- ++ -- -- -- ME -- -- ++ --
                ME -- ME ++ ++ ++ ++ ++ -- ME --
                ++ -- -- ++ ++ ++ MB ++ -- -- ME
                ++ -- Me ++ ++ ++ -- Me -- -- --
                Me -- -- SP -- SP -- -- -- ME ME
                -- -- -- -- __ -- -- Me ++ -- --
                ++ ++ MS -- MS -- MS -- ME ++ ++
                -- ++ -- ME -- ME -- ++ -- ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 10 50 50 50 50 50 50 50 50
                50 50 10 10 10 10 10 50 50 50 50
                50 50 10 10 10 10 10 50 50 50 50
                50 50 10 10 10 10 10 50 50 50 50
                50 50 10 10 10 10 10 50 50 50 50
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.135, 1.157),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.098, 1.118),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.066, 1.085),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN_2,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'sp': Stage(
        base=BASE,
        map=dict(
            name='SP',
            shape='I9',
            camera_data=['D2', 'D5', 'D7', 'F2', 'F5', 'F7'],
            camera_data_spawn_point=['F6'],
            map_data="""
                ++ -- ME ++ ++ ++ ME -- ++
                -- ME -- -- MB -- -- -- ME
                -- -- -- -- -- -- ME -- ++
                ++ ME ++ ++ ++ ++ ++ -- --
                ++ -- ++ ++ ++ ++ ++ ME --
                -- -- ++ ++ ++ SP SP -- --
                ME -- -- -- -- __ __ -- MS
                -- ME -- ++ ME -- ME MS --
                ++ -- ME ++ -- MS ++ -- ++
            """,
            weight_data="""
                50 50 50 50 10 10 10 10 10
                50 50 50 50 10 10 10 10 10
                50 50 50 50 10 10 10 10 10
                50 50 50 50 50 50 50 10 10
                50 50 50 50 50 50 50 10 10
                50 50 50 50 50 10 10 10 10
                50 50 50 50 10 10 10 10 10
                50 50 50 50 10 10 10 10 10
                50 50 50 50 10 10 10 10 10
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
            spawn_data_loop=[
                {'battle': 0, 'enemy': 12, 'siren': 3},
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_CHAPTER_SWITCH_20241219=True,
            MAP_HAS_MODE_SWITCH=False,
            MAP_HAS_MOVABLE_NORMAL_ENEMY=True,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
            MOVABLE_NORMAL_ENEMY_TURN=(2,),
            MAP_SIREN_MOVE_WAIT=0.7,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 238),
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
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(1.09, 1.11),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.054, 1.073),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.023, 1.042),
            MAP_IS_ONE_TIME_STAGE=True,
            MAP_WALK_USE_CURRENT_FLEET=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: ['clear_siren', "clear_enemy(sort=('weight', 'cost_1'))", 'battle_default'],
            7: 'fleet_boss.clear_boss',
        },
    ),
}
