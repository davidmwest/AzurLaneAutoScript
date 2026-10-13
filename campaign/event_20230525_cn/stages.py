"""
Stages of event_20230525_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = [
    ('when', 'map_is_clear_mode', ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)'], ["clear_any_enemy(sort=('cost_2',))"]),
    'battle_default',
]
PLAN_2 = [
    ('when', 'map_is_clear_mode', ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)'], ['clear_siren', "clear_any_enemy(sort=('cost_2',))"]),
    'battle_default',
]
PLAN_3 = ['clear_siren', "clear_any_enemy(sort=('cost_2',))", 'battle_default']
PLAN_4 = ["clear_any_enemy(sort=('cost_2',))", 'battle_default']

STAGES = {
    'ht2': Stage(
        base=BASE,
        map=dict(
            name='HT2',
            shape='J8',
            camera_data=['D3', 'D6', 'G3', 'G6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ ++ ++ -- -- -- -- -- ++ ++
                -- ME -- ME -- -- ME -- -- ++
                ME -- -- -- ++ ++ -- -- ME --
                -- MS ++ Me ++ ++ Me -- -- ME
                ME -- ++ -- MB MB -- __ -- ME
                -- -- SP -- -- -- -- -- Me --
                Me -- -- SP -- ++ ++ Me ++ --
                ++ MS -- -- -- MS -- -- ++ --
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
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='ht1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            4: 'clear_boss',
        },
    ),
    'ht4': Stage(
        base=BASE,
        map=dict(
            name='HT4',
            shape='J8',
            camera_data=['E2', 'E6', 'G2', 'G6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                ++ -- ME Me -- -- ME ME -- ++
                -- ME -- -- -- -- -- -- ME --
                -- -- ++ -- ++ ++ Me -- -- ME
                -- -- Me -- ++ ++ -- ++ -- --
                ++ Me -- -- SP SP -- ++ Me --
                -- -- MS __ -- -- __ MS -- --
                -- ME -- MS -- -- MS -- ME --
                ++ -- ME -- MB MB -- ME -- ++
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
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='ht1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'ht5': Stage(
        base=BASE,
        map=dict(
            name='HT5',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- SP SP -- -- -- -- ME -- --
                -- -- -- -- -- ++ ++ ++ MB --
                MS ++ -- MS ++ ++ -- ME -- MB
                -- ++ MS -- ++ ++ Me -- -- ME
                -- Me __ -- -- -- -- -- -- ++
                Me -- -- -- Me -- Me -- ME ++
                -- ME ME -- -- ++ -- -- ME --
                ++ -- -- Me ME -- ME -- -- ME
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
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='ht1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CAred', 'BBred'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.256, 1.28),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.215, 1.237),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.18, 1.201),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: [
                ('when', 'map_is_clear_mode', ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)'], ["clear_any_enemy(sort=('cost_2',))"]),
                'battle_default',
            ],
            5: PLAN_2,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'hts1': Stage(
        base=BASE,
        map=dict(
            name='HTS1',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['G6', 'D6'],
            map_data="""
                MB -- -- ++ ME ME -- -- ++ ++
                -- -- Me -- -- -- Me -- -- --
                ++ -- -- MS ++ ++ -- -- ME --
                -- MS __ -- ++ ++ -- ME -- ME
                ME -- __ -- SP SP -- -- ME --
                -- Me MS -- -- -- -- ++ ++ Me
                -- ++ ME -- Me -- -- ++ ++ --
                -- ++ -- ME ++ ME -- Me -- --
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
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='.config_base:ConfigBase',
        config=dict(
            MAP_SIREN_TEMPLATE=['AbyssalBoss4'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_IS_ONE_TIME_STAGE=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_3,
            4: 'clear_boss',
        },
    ),
    'hts2': Stage(
        base=BASE,
        map=dict(
            name='HTS2',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['G6', 'D6'],
            map_data="""
                -- ME -- ME Me ME -- ME -- --
                ++ ++ -- -- -- -- -- ++ ++ --
                ++ ++ ME Me ++ ++ -- ME ++ --
                -- Me -- -- ++ ++ -- -- Me --
                ME -- -- -- SP SP -- -- -- Me
                -- -- -- __ -- -- -- ++ -- ++
                ME ++ MS -- -- -- -- MS MB --
                -- ME -- MS -- MS -- ++ -- ++
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
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='hts1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CAred', 'BBred'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_IS_ONE_TIME_STAGE=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_3,
            5: PLAN_4,
            6: 'fleet_boss.clear_boss',
        },
    ),
    't2': Stage(
        base=BASE,
        map=dict(
            name='T2',
            shape='J8',
            camera_data=['D3', 'D6', 'G3', 'G6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ ++ ++ -- -- -- -- -- ++ ++
                -- ME -- ME -- -- ME -- -- ++
                ME -- -- -- ++ ++ -- -- ME --
                -- MS ++ Me ++ ++ Me -- -- ME
                ME -- ++ -- MB MB -- __ -- ME
                -- -- SP -- -- -- -- -- Me --
                Me -- -- SP -- ++ ++ Me ++ --
                ++ MS -- -- -- MS -- -- ++ --
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
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    't4': Stage(
        base=BASE,
        map=dict(
            name='T4',
            shape='J8',
            camera_data=['E2', 'E6', 'G2', 'G6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                ++ -- ME Me -- -- ME ME -- ++
                -- ME -- -- -- -- -- -- ME --
                -- -- ++ -- ++ ++ Me -- -- ME
                -- -- Me -- ++ ++ -- ++ -- --
                ++ Me -- -- SP SP -- ++ Me --
                -- -- MS __ -- -- __ MS -- --
                -- ME -- MS -- -- MS -- ME --
                ++ -- ME -- MB MB -- ME -- ++
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
                {'battle': 5, 'enemy': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    't5': Stage(
        base=BASE,
        map=dict(
            name='T5',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- SP SP -- -- -- -- ME -- --
                -- -- -- -- -- ++ ++ ++ MB --
                MS ++ -- MS ++ ++ -- ME -- MB
                -- ++ MS -- ++ ++ Me -- -- ME
                -- Me __ -- -- -- -- -- -- ++
                Me -- -- -- Me -- Me -- ME ++
                -- ME ME -- -- ++ -- -- ME --
                ++ -- -- Me ME -- ME -- -- ME
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CAred', 'BBred'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.256, 1.28),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.215, 1.237),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.18, 1.201),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'ts1': Stage(
        base=BASE,
        map=dict(
            name='TS1',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['G6', 'D6'],
            map_data="""
                MB -- -- ++ ME ME -- -- ++ ++
                -- -- Me -- -- -- Me -- -- --
                ++ -- -- MS ++ ++ -- -- ME --
                -- MS __ -- ++ ++ -- ME -- ME
                ME -- __ -- SP SP -- -- ME --
                -- Me MS -- -- -- -- ++ ++ Me
                -- ++ ME -- Me -- -- ++ ++ --
                -- ++ -- ME ++ ME -- Me -- --
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
        config_base='.config_base:ConfigBase',
        config=dict(
            MAP_SIREN_TEMPLATE=['AbyssalBoss4'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_IS_ONE_TIME_STAGE=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_4,
            4: 'clear_boss',
        },
    ),
    'ts2': Stage(
        base=BASE,
        map=dict(
            name='TS2',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['G6', 'D6'],
            map_data="""
                -- ME -- ME Me ME -- ME -- --
                ++ ++ -- -- -- -- -- ++ ++ --
                ++ ++ ME Me ++ ++ -- ME ++ --
                -- Me -- -- ++ ++ -- -- Me --
                ME -- -- -- SP SP -- -- -- Me
                -- -- -- __ -- -- -- ++ -- ++
                ME ++ MS -- -- -- -- MS MB --
                -- ME -- MS -- MS -- ++ -- ++
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='ts1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CAred', 'BBred'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_IS_ONE_TIME_STAGE=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
