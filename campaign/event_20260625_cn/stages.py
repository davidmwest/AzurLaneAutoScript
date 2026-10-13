"""
Stages of event_20260625_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']
PLAN_2 = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default']

STAGES = {
    'ht1': Stage(
        map=dict(
            name='HT1',
            shape='I7',
            camera_data=['F2', 'F5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- -- ME -- ME -- -- ++ MB
                -- -- ++ ME -- ME ++ ME --
                SP -- -- MS -- -- Me -- --
                -- -- __ -- ++ -- -- -- ME
                SP -- -- MS ++ Me -- ++ ++
                -- -- -- -- -- -- -- ++ ++
                ++ ++ ++ Me -- ME -- ME --
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
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['MeowfficerBust_Studying', 'MeowfficerBust_Playtime'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_CHAPTER_SWITCH_20241219_SP=True,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_HAS_MODE_SWITCH=True,
            MAP_SWIPE_MULTIPLY=(1.144, 1.165),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.106, 1.126),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.074, 1.093),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'ht2': Stage(
        map=dict(
            name='HT2',
            shape='I7',
            camera_data=['D2', 'D5', 'F5'],
            camera_data_spawn_point=['F2'],
            map_data="""
                ME -- ME ++ ME -- -- ++ ++
                -- -- -- -- -- -- SP -- ++
                -- Me ++ ++ ++ -- -- SP --
                -- -- -- Me -- MS -- -- --
                ME -- ME ++ -- MS MS ++ Me
                -- MB -- ++ __ -- -- ++ --
                ME -- ME -- -- ME -- Me --
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
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2, 'siren': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='ht1',
        config=dict(
            MAP_SIREN_TEMPLATE=['MeowfficerBust_Studying', 'MeowfficerBust_Playtime'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.224, 1.247),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.184, 1.206),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.149, 1.17),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'ht3': Stage(
        map=dict(
            name='HT3',
            shape='I8',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['F5'],
            map_data="""
                ++ ++ ++ ++ MB ++ ++ ++ ++
                ++ -- Me Me -- Me Me -- ++
                -- ME -- -- __ -- -- ME --
                ME -- -- SP ++ SP -- -- ME
                -- ME -- -- -- -- -- ME --
                ++ ++ ME -- MS -- ME ++ ++
                ++ ++ -- MS -- MS -- ++ ++
                -- -- ++ ++ ++ ++ ++ -- --
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
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2, 'siren': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='ht1',
        config=dict(
            MAP_SIREN_TEMPLATE=['MeowfficerBust_Studying', 'MeowfficerBust_Playtime'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.115, 1.136),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.078, 1.098),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.047, 1.065),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'sp': Stage(
        map=dict(
            name='SP',
            shape='G10',
            camera_data=['D3', 'D7', 'D8'],
            camera_data_spawn_point=['D8'],
            map_data="""
                -- -- ++ -- ++ ++ --
                ++ ++ ++ MB ++ ++ ++
                ++ ME -- -- -- ME --
                -- -- -- ME -- -- ME
                ME -- ME ++ ++ -- --
                ++ -- -- -- ++ -- ME
                ++ -- MS __ MS -- ++
                ME -- -- MS -- -- ME
                ++ ++ -- -- -- ME --
                ++ ++ SP -- SP ++ --
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
                50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 10, 'siren': 3},
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
            MAP_SIREN_TEMPLATE=['MeowfficerBust_Studying', 'MeowfficerBust_Playtime'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_IS_ONE_TIME_STAGE=True,
            MAP_CHAPTER_SWITCH_20241219_SP=True,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_HAS_MODE_SWITCH=False,
            HOMO_STORAGE=((8, 6), [(137.405, 104.804), (1046.044, 104.804), (-12.171, 652.093), (1166.717, 652.093)]),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(1.005, 1.024),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.972, 0.99),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.944, 0.961),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=2)', 'battle_default'],
            5: PLAN,
            7: 'fleet_boss.clear_boss',
        },
    ),
    't1': Stage(
        map=dict(
            name='T1',
            shape='I7',
            camera_data=['F2', 'F5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- -- ME -- ME -- -- ++ MB
                -- -- ++ ME -- ME ++ ME --
                SP -- -- MS -- -- Me -- --
                -- -- __ -- ++ -- -- -- ME
                SP -- -- MS ++ Me -- ++ ++
                -- -- -- -- -- -- -- ++ ++
                ++ ++ ++ Me -- ME -- ME --
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
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['MeowfficerBust_Hobbies'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_CHAPTER_SWITCH_20241219_SP=True,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_HAS_MODE_SWITCH=True,
            MAP_SWIPE_MULTIPLY=(1.144, 1.165),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.106, 1.126),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.074, 1.093),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    't2': Stage(
        map=dict(
            name='T2',
            shape='I7',
            camera_data=['D2', 'D5', 'F5'],
            camera_data_spawn_point=['F2'],
            map_data="""
                ME -- ME ++ ME -- -- ++ ++
                -- -- -- -- -- -- SP -- ++
                -- Me ++ ++ ++ -- -- SP --
                -- -- -- Me -- MS -- -- --
                ME -- ME ++ -- MS MS ++ Me
                -- MB -- ++ __ -- -- ++ --
                ME -- ME -- -- ME -- Me --
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
                {'battle': 0, 'enemy': 3, 'siren': 1},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['MeowfficerBust_Hobbies'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.224, 1.247),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.184, 1.206),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.149, 1.17),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    't3': Stage(
        map=dict(
            name='T3',
            shape='I8',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['F5'],
            map_data="""
                ++ ++ ++ ++ MB ++ ++ ++ ++
                ++ -- Me Me -- Me Me -- ++
                -- ME -- -- __ -- -- ME --
                ME -- -- SP ++ SP -- -- ME
                -- ME -- -- -- -- -- ME --
                ++ ++ ME -- MS -- ME ++ ++
                ++ ++ -- MS -- MS -- ++ ++
                -- -- ++ ++ ++ ++ ++ -- --
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
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['MeowfficerBust_Hobbies'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.115, 1.136),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.078, 1.098),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.047, 1.065),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
