"""
Stages of event_20240815_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']

STAGES = {
    'a1': Stage(
        base=BASE,
        map=dict(
            name='A1',
            shape='I8',
            camera_data=['E2', 'E5'],
            camera_data_spawn_point=['E2'],
            map_data="""
                -- -- -- SP -- SP -- -- --
                -- ME -- -- MB -- -- ME --
                -- ++ Me -- -- -- ++ ++ --
                ++ ME -- MS -- MS ++ ++ --
                -- ME -- -- __ -- -- ME --
                -- -- ME -- Me -- -- ME --
                -- -- ++ ME -- ++ Me -- --
                -- -- ++ -- -- -- -- -- --
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
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
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
            MAP_SWIPE_MULTIPLY=(1.194, 1.217),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.155, 1.176),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.121, 1.142),
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
            camera_data_spawn_point=['D2', 'D6'],
            map_data="""
                -- -- -- ME -- -- -- ++ ++
                ++ ++ Me -- Me ++ -- ++ ++
                ++ ++ -- -- -- ME -- ME --
                SP -- -- MS -- -- ME -- --
                -- -- Me __ ++ ++ ++ -- MB
                SP -- -- MS -- -- -- -- --
                ++ -- -- -- -- ME -- ME --
                ++ -- -- ME ++ -- ME -- --
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
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.103, 1.124),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.067, 1.087),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.036, 1.055),
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
            shape='O5',
            camera_data=['F2', 'F3', 'J2', 'J3'],
            camera_data_spawn_point=['J2'],
            map_data="""
                -- -- ++ ++ ++ ME -- ++ ++ SP -- SP -- ++ --
                -- -- -- ++ ME -- ME ++ ++ -- -- -- -- ++ ++
                -- -- MB -- -- __ -- ME -- -- MS -- MS ++ ++
                -- -- -- ++ ME -- -- -- -- Me -- ++ -- -- --
                -- -- ++ ++ ++ ME ME ++ Me -- Me ++ -- -- --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
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
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.24, 1.263),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.199, 1.221),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.164, 1.185),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b3': Stage(
        base=BASE,
        map=dict(
            name='B3',
            shape='K9',
            camera_data=['D3', 'D7', 'H3', 'H7'],
            camera_data_spawn_point=['D3'],
            map_data="""
                -- -- ++ -- -- -- -- -- ++ ++ --
                ++ ++ ++ -- -- ++ -- ME ++ ++ --
                ++ ++ ++ -- Me ++ ME -- ME ME --
                ++ ++ ++ -- -- Me -- __ -- -- MB
                SP -- SP -- -- -- -- ME -- -- MB
                -- -- -- ++ ++ ME -- ++ ME ME --
                -- MS -- -- ++ Me -- ++ ++ ++ ++
                MS -- MS -- Me -- -- -- ME -- --
                ++ ++ ++ -- -- -- ++ ME -- -- --
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
            MAP_SIREN_TEMPLATE=['AmagiMasked'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_MOVABLE_NORMAL_ENEMY=True,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=False,
            MAP_SWIPE_MULTIPLY=(1.108, 1.129),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.072, 1.092),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.041, 1.059),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c1': Stage(
        base=BASE,
        map=dict(
            name='C1',
            shape='I8',
            camera_data=['E2', 'E5'],
            camera_data_spawn_point=['E2'],
            map_data="""
                -- -- -- SP -- SP -- -- --
                -- ME -- -- MB -- -- ME --
                -- ++ Me -- -- -- ++ ++ --
                ++ ME -- MS -- MS ++ ++ --
                -- ME -- -- __ -- -- ME --
                -- -- ME -- Me -- -- ME --
                -- -- ++ ME -- ++ Me -- --
                -- -- ++ -- -- -- -- -- --
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
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
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
            MAP_SWIPE_MULTIPLY=(1.194, 1.217),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.155, 1.176),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.121, 1.142),
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
            camera_data_spawn_point=['D2', 'D6'],
            map_data="""
                -- -- -- ME -- -- -- ++ ++
                ++ ++ Me -- Me ++ -- ++ ++
                ++ ++ -- -- -- ME -- ME --
                SP -- -- MS -- -- ME -- --
                -- -- Me __ ++ ++ ++ -- MB
                SP -- -- MS -- -- -- -- --
                ++ -- -- -- -- ME -- ME --
                ++ -- -- ME ++ -- ME -- --
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
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.103, 1.124),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.067, 1.087),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.036, 1.055),
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
            shape='O5',
            camera_data=['F2', 'F3', 'J2', 'J3'],
            camera_data_spawn_point=['J2'],
            map_data="""
                -- -- ++ ++ ++ ME -- ++ ++ SP -- SP -- ++ --
                -- -- -- ++ ME -- ME ++ ++ -- -- -- -- ++ ++
                -- -- MB -- -- __ -- ME -- -- MS -- MS ++ ++
                -- -- -- ++ ME -- -- -- -- Me -- ++ -- -- --
                -- -- ++ ++ ++ ME ME ++ Me -- Me ++ -- -- --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50 50 50
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
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.24, 1.263),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.199, 1.221),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.164, 1.185),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        base=BASE,
        map=dict(
            name='D3',
            shape='K9',
            camera_data=['D3', 'D7', 'H3', 'H7'],
            camera_data_spawn_point=['D3'],
            map_data="""
                -- -- ++ -- -- -- -- -- ++ ++ --
                ++ ++ ++ -- -- ++ -- ME ++ ++ --
                ++ ++ ++ -- Me ++ ME -- ME ME --
                ++ ++ ++ -- -- Me -- __ -- -- MB
                SP -- SP -- -- -- -- ME -- -- MB
                -- -- -- ++ ++ ME -- ++ ME ME --
                -- MS -- -- ++ Me -- ++ ++ ++ ++
                MS -- MS -- Me -- -- -- ME -- --
                ++ ++ ++ -- -- -- ++ ME -- -- --
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
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_SIREN_TEMPLATE=['AmagiMasked'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_MOVABLE_NORMAL_ENEMY=True,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=False,
            MAP_SWIPE_MULTIPLY=(1.108, 1.129),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.072, 1.092),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.041, 1.059),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default'],
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
}
