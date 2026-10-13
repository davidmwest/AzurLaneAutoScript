"""
Stages of event_20240829_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']

STAGES = {
    'sp': Stage(
        base=BASE,
        map=dict(
            name='SP',
            shape='I9',
            camera_data=['E5', 'E7'],
            camera_data_spawn_point=['E5'],
            map_data="""
                -- -- -- ++ ++ ++ -- -- --
                -- -- -- ++ ++ ++ -- -- --
                -- -- -- ++ ++ ++ -- -- --
                -- -- ++ SP -- SP ++ -- --
                -- ++ ME -- -- -- ME ++ --
                ++ ME -- -- __ -- -- ME ++
                ++ -- ME -- MS -- ME -- ++
                -- ++ ++ MS -- MS ++ ++ --
                -- ++ ++ -- MB -- ++ ++ --
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
                {'battle': 0, 'enemy': 6, 'siren': 3},
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
            MOVABLE_ENEMY_TURN=(0,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=False,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
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
            MAP_IS_ONE_TIME_STAGE=True,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(1.167, 1.189),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.129, 1.15),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.096, 1.116),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=2)', 'battle_default'],
            5: PLAN,
            7: 'fleet_boss.clear_boss',
        },
    ),
    't1': Stage(
        base=BASE,
        map=dict(
            name='T1',
            shape='I7',
            camera_data=['D2', 'D5', 'F5'],
            camera_data_spawn_point=['F2'],
            map_data="""
                -- -- ME -- -- ME ++ ++ ++
                -- ME ++ ME -- -- -- -- SP
                ME -- ++ Me -- MS -- -- SP
                -- -- -- -- MB -- ME ++ ++
                ++ ++ ++ -- __ -- -- Me ++
                -- ME -- -- Me -- ME -- --
                -- -- ME -- ++ -- -- ME --
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
                {'battle': 4, 'boss': 1},
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
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
            MAP_SWIPE_MULTIPLY=(1.237, 1.26),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.196, 1.218),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.161, 1.182),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    't2': Stage(
        base=BASE,
        map=dict(
            name='T2',
            shape='J7',
            camera_data=['D3', 'D5', 'G5'],
            camera_data_spawn_point=['G3'],
            map_data="""
                -- -- -- -- -- ++ -- -- -- --
                ME ++ Me ++ ME ++ SP -- SP ++
                -- ME -- ME -- -- -- -- -- --
                -- -- -- -- -- Me -- __ -- Me
                -- ++ ++ ++ -- -- MS -- MS --
                -- ME -- ME -- ++ ++ MB ++ ++
                ME -- -- -- Me ++ ++ ++ ++ ++
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
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.23, 1.254),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.19, 1.212),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.155, 1.176),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    't3': Stage(
        base=BASE,
        map=dict(
            name='T3',
            shape='I10',
            camera_data=['D5', 'D8', 'F5'],
            camera_data_spawn_point=['D8'],
            map_data="""
                -- -- -- ++ ++ ++ -- -- --
                -- -- -- ++ ++ ++ -- -- --
                ++ ++ ++ ++ ++ ++ ++ ++ ++
                ME -- ME -- MB -- ME -- ME
                -- ME -- -- __ -- -- ME --
                -- -- -- -- Me -- -- -- --
                ++ Me -- MS ++ MS ++ ++ ++
                ME -- -- -- MS -- Me -- --
                -- Me ++ -- -- -- ++ ++ --
                -- -- ++ SP -- SP ++ ++ --
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
                50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 2, 'siren': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['AmagiMasked'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(1.325, 1.349),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.281, 1.305),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.244, 1.266),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
