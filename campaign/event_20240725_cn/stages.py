"""
Stages of event_20240725_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']
PLAN_2 = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default']

STAGES = {
    'ht1': Stage(
        base=BASE,
        map=dict(
            name='HT1',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['F2', 'D2'],
            map_data="""
                ++ ++ -- -- SP -- SP -- --
                MB ++ ME -- -- -- -- -- ++
                -- ME -- -- -- MS -- -- ME
                -- -- __ -- Me ++ Me -- --
                -- ME -- -- -- ++ -- -- ME
                ++ ++ -- Me -- MS -- Me --
                ++ ++ ME -- ME -- ME -- ++
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
            MAP_SIREN_TEMPLATE=['Sirius', 'Dido'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_HAS_MODE_SWITCH=True,
            MAP_SWIPE_MULTIPLY=(1.236, 1.259),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.195, 1.217),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.16, 1.181),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'ht2': Stage(
        base=BASE,
        map=dict(
            name='HT2',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['F2'],
            map_data="""
                -- ++ -- Me -- MS ++ ++ ++
                ME ++ Me -- -- -- -- SP --
                -- -- -- -- -- MS -- -- SP
                ME -- ME -- Me ++ ++ -- --
                -- ++ -- __ -- ++ ++ MS Me
                ++ ME -- ME -- ME ME -- ++
                MB -- -- ++ Me -- -- ME --
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
            MAP_SIREN_TEMPLATE=['Z23_g', 'Leipzig_g'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_HAS_MODE_SWITCH=True,
            MAP_SWIPE_MULTIPLY=(1.189, 1.211),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.15, 1.171),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.116, 1.137),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'ht3': Stage(
        base=BASE,
        map=dict(
            name='HT3',
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ ++ Me -- MB -- ++ -- --
                ++ ++ -- ME -- ME ++ Me ME
                -- ME -- -- __ -- Me -- --
                -- ME -- ++ -- -- -- -- ME
                -- ++ MS ++ MS ++ -- -- ME
                -- Me -- -- -- MS -- Me --
                ME -- -- -- -- -- -- ++ ++
                ++ ++ ++ SP SP ++ ME -- ++
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
            MAP_SIREN_TEMPLATE=['PompeoMagno', 'AlfredoOriani'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_HAS_MODE_SWITCH=True,
            MAP_SWIPE_MULTIPLY=(1.089, 1.109),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.053, 1.072),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.022, 1.041),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'sp': Stage(
        base=BASE,
        map=dict(
            name='SP',
            shape='I9',
            camera_data=['E5', 'E7'],
            camera_data_spawn_point=['E5'],
            map_data="""
                ++ ++ ++ ++ ++ ++ ++ ++ ++
                -- -- -- ++ ++ ++ -- -- --
                -- -- -- ++ ++ ++ -- -- --
                ++ -- -- SP -- SP -- -- ++
                -- -- ME -- MS -- ME -- --
                -- ME -- MS __ MS -- ME --
                -- -- ME -- MB -- ME -- --
                ++ ++ -- ME -- ME -- ++ ++
                ++ ++ -- -- ME -- -- ++ ++
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
                {'battle': 0, 'enemy': 9, 'siren': 3},
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
            MAP_SIREN_TEMPLATE=['LAudacieux', 'Dupleix'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=False,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_IS_ONE_TIME_STAGE=True,
            MAP_SWIPE_MULTIPLY=(1.073, 1.093),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.038, 1.057),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.008, 1.026),
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
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['F2', 'D2'],
            map_data="""
                ++ ++ -- -- SP -- SP -- --
                MB ++ ME -- -- -- -- -- ++
                -- ME -- -- -- MS -- -- ME
                -- -- __ -- Me ++ Me -- --
                -- ME -- -- -- ++ -- -- ME
                ++ ++ -- Me -- MS -- Me --
                ++ ++ ME -- ME -- ME -- ++
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
            MAP_SIREN_TEMPLATE=['Sirius', 'Dido'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_HAS_MODE_SWITCH=True,
            MAP_SWIPE_MULTIPLY=(1.236, 1.259),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.195, 1.217),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.16, 1.181),
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
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['F2'],
            map_data="""
                -- ++ -- Me -- MS ++ ++ ++
                ME ++ Me -- -- -- -- SP --
                -- -- -- -- -- MS -- -- SP
                ME -- ME -- Me ++ ++ -- --
                -- ++ -- __ -- ++ ++ MS Me
                ++ ME -- ME -- ME ME -- ++
                MB -- -- ++ Me -- -- ME --
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
            MAP_SIREN_TEMPLATE=['Z23_g', 'Leipzig_g'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_HAS_MODE_SWITCH=True,
            MAP_SWIPE_MULTIPLY=(1.189, 1.211),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.15, 1.171),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.116, 1.137),
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
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ ++ Me -- MB -- ++ -- --
                ++ ++ -- ME -- ME ++ Me ME
                -- ME -- -- __ -- Me -- --
                -- ME -- ++ -- -- -- -- ME
                -- ++ MS ++ MS ++ -- -- ME
                -- Me -- -- -- MS -- Me --
                ME -- -- -- -- -- -- ++ ++
                ++ ++ ++ SP SP ++ ME -- ++
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
            MAP_SIREN_TEMPLATE=['PompeoMagno', 'AlfredoOriani'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_HAS_MODE_SWITCH=True,
            MAP_SWIPE_MULTIPLY=(1.089, 1.109),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.053, 1.072),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.022, 1.041),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
