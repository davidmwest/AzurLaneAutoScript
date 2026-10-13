"""
Stages of event_20231123_cn, see module/campaign/stage.py
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
            camera_data=['D4', 'D6', 'F4', 'F6'],
            camera_data_spawn_point=['F6', 'D6'],
            map_data="""
                ++ ++ ++ ++ ++ ++ ++ ++ ++
                ++ MS -- -- MS -- -- MS ++
                ++ -- Me -- -- -- Me -- ++
                ME -- -- ++ -- ++ -- -- ME
                -- ME -- -- MB -- -- ME --
                ME -- -- ++ -- ++ -- -- ME
                ++ -- Me -- __ -- Me -- ++
                ++ ME -- SP -- SP -- ME ++
                ++ ++ ++ ++ -- ++ ++ ++ ++
            """,
            map_data_loop="""
                ++ ++ ++ ++ ++ ++ ++ ++ ++
                ++ -- -- -- -- -- -- -- ++
                ++ -- Me -- -- -- Me -- ++
                ME -- -- ++ MS ++ -- -- ME
                -- ME -- MS MB MS -- ME --
                ME -- -- ++ -- ++ -- -- ME
                ++ -- Me -- __ -- Me -- ++
                ++ -- -- SP -- SP -- -- ++
                ++ ++ ++ ++ -- ++ ++ ++ ++
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
                {'battle': 0, 'enemy': 10, 'siren': 3},
                {'battle': 1},
                {'battle': 2},
                {'battle': 3},
                {'battle': 4},
                {'battle': 5},
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
            spawn_data_loop=[
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
            MAP_SIREN_TEMPLATE=['SK_BB', 'SK_CV'],
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
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 222),
                'width': (1.5, 10),
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
            MAP_SWIPE_MULTIPLY=(1.038, 1.058),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.004, 1.023),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.975, 0.992),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_IS_ONE_TIME_STAGE=True,
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
            shape='I8',
            camera_data=['E3', 'E6'],
            camera_data_spawn_point=['E3'],
            map_data="""
                -- -- -- -- -- -- -- -- --
                -- -- SP -- SP -- ME ++ --
                -- ++ -- -- -- -- -- -- --
                -- ME -- -- -- ++ ME -- ME
                -- -- Me -- Me ++ -- __ --
                -- ME -- MS -- -- -- ME --
                ++ ++ Me -- Me -- ME -- ME
                ++ ++ -- MB -- ++ ++ ++ --
            """,
            map_data_loop="""
                -- -- -- -- -- -- -- -- --
                -- -- SP -- SP -- ME ++ --
                -- ++ -- -- -- -- -- -- --
                -- ME -- MS -- ++ ME -- ME
                -- -- Me -- Me ++ -- __ --
                -- ME -- -- -- -- -- ME --
                ++ ++ Me -- Me -- ME -- ME
                ++ ++ -- MB -- ++ ++ ++ --
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
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
            spawn_data_loop=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['SK_DD'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 222),
                'width': (1.5, 10),
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
            MAP_SWIPE_MULTIPLY=(1.187, 1.209),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.148, 1.169),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.115, 1.135),
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
            camera_data=['D3', 'D5', 'F3', 'F5'],
            camera_data_spawn_point=['D3'],
            map_data="""
                -- ++ ++ ++ MS ++ ++ ++ --
                -- -- -- -- __ -- -- Me --
                SP -- -- ME -- ME -- -- ME
                SP -- ++ -- MB -- ++ ME --
                -- -- -- ME -- ME -- -- ME
                ++ Me -- -- ++ -- -- Me ++
                ++ -- ME -- -- -- ME -- ++
            """,
            map_data_loop="""
                -- ++ ++ ++ -- ++ ++ ++ --
                -- -- MS -- __ -- -- Me --
                SP -- -- ME -- ME -- -- ME
                SP -- ++ -- MB -- ++ ME --
                -- -- -- ME -- ME -- -- ME
                ++ Me -- -- ++ -- -- Me ++
                ++ -- ME -- -- -- ME -- ++
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
            spawn_data_loop=[
                {'battle': 0, 'enemy': 3, 'siren': 1},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['SK_DD', 'SK_CL'],
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
    't3': Stage(
        base=BASE,
        map=dict(
            name='T3',
            shape='I8',
            camera_data=['D3', 'D6', 'F3', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- -- -- -- -- -- -- -- --
                -- ++ ++ -- MB -- ++ ME --
                -- ++ ++ ME -- ME ++ -- ME
                -- Me -- ME -- ME -- Me --
                Me -- -- -- __ -- -- -- --
                ++ -- -- MS -- MS -- -- ME
                -- -- -- ++ ++ ++ -- MS --
                -- SP SP ++ ++ -- ME -- ++
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
            spawn_data_loop=[
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
            MAP_SIREN_TEMPLATE=['SK_CL', 'SK_CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.078, 1.099),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.043, 1.062),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.013, 1.031),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    't4': Stage(
        base=BASE,
        map=dict(
            name='T4',
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['F6', 'D6'],
            map_data="""
                ++ ++ ++ ME -- MB -- ME ++
                ++ MS -- -- ME -- ME -- --
                ME -- -- ++ -- __ -- -- ++
                -- ME -- -- -- Me -- -- ++
                ++ ++ -- MS -- ++ -- MS --
                ++ ++ -- -- Me ++ Me -- --
                -- -- ME -- -- -- -- -- ME
                -- ME -- -- SP -- SP ++ --
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
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
            spawn_data_loop=[
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['SK_CL', 'SK_CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.08, 1.1),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.044, 1.063),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.014, 1.032),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    't5': Stage(
        base=BASE,
        map=dict(
            name='T5',
            shape='I10',
            camera_data=['D2', 'D6', 'D7', 'F2', 'F6', 'F7'],
            camera_data_spawn_point=['F7', 'D7'],
            map_data="""
                ++ ++ -- ME -- ME -- ++ ++
                ++ ++ ME -- MB -- ME ++ ++
                -- ME -- -- -- -- -- ME --
                ME -- -- ME -- ME -- -- ME
                ++ ME -- ++ ++ ++ -- ME ++
                ++ -- -- Me MS Me -- -- ++
                -- MS -- -- __ -- -- MS --
                -- ++ -- SP -- SP -- ++ --
                -- -- Me -- MS -- Me -- --
                ++ ++ ++ -- -- -- ++ ++ ++
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
                {'battle': 0, 'enemy': 3, 'siren': 3},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
            spawn_data_loop=[
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2, 'siren': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['SK_BB', 'SK_CV'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(0.978, 0.997),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.946, 0.963),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.918, 0.935),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default'],
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'tsk1': Stage(
        base=BASE,
        map=dict(
            name='TSK1',
            shape='E5',
            camera_data=['D3'],
            camera_data_spawn_point=['D3'],
            map_data="""
                -- ++ ++ ++ --
                -- -- ++ -- --
                -- SP -- MB --
                ++ -- -- -- ++
                -- ++ ++ ++ --
            """,
            weight_data="""
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
            """,
            spawn_data=[{'battle': 0, 'boss': 1}],
        ),
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 222),
                'width': (1.5, 10),
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
            MAP_SWIPE_MULTIPLY=(1.187, 1.209),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.148, 1.169),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.115, 1.135),
            MAP_IS_ONE_TIME_STAGE=True,
            FLEET_2=0,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: 'clear_boss',
        },
    ),
    'tsk2': Stage(
        base=BASE,
        map=dict(
            name='TSK2',
            shape='E5',
            camera_data=['D3'],
            camera_data_spawn_point=['D3'],
            map_data="""
                -- ++ ++ ++ --
                -- -- ++ -- --
                -- SP -- MB --
                ++ -- -- -- ++
                -- ++ ++ ++ --
            """,
            weight_data="""
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
            """,
            spawn_data=[{'battle': 0, 'boss': 1}],
        ),
        config_base='tsk1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: 'clear_boss',
        },
    ),
    'tsk3': Stage(
        base=BASE,
        map=dict(
            name='TSK3',
            shape='E5',
            camera_data=['D3'],
            camera_data_spawn_point=['D3'],
            map_data="""
                -- ++ ++ ++ --
                -- -- ++ -- --
                -- SP -- MB --
                ++ -- -- -- ++
                -- ++ ++ ++ --
            """,
            weight_data="""
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
            """,
            spawn_data=[{'battle': 0, 'boss': 1}],
        ),
        config_base='tsk1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: 'clear_boss',
        },
    ),
    'tsk4': Stage(
        base=BASE,
        map=dict(
            name='TSK4',
            shape='E5',
            camera_data=['D3'],
            camera_data_spawn_point=['D3'],
            map_data="""
                -- ++ ++ ++ --
                -- -- ++ -- --
                -- SP -- MB --
                ++ -- -- -- ++
                -- ++ ++ ++ --
            """,
            weight_data="""
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
            """,
            spawn_data=[{'battle': 0, 'boss': 1}],
        ),
        config_base='tsk1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: 'clear_boss',
        },
    ),
    'tsk5': Stage(
        base=BASE,
        map=dict(
            name='TSK5',
            shape='E5',
            camera_data=['D3'],
            camera_data_spawn_point=['D3'],
            map_data="""
                -- ++ ++ ++ --
                -- -- ++ -- --
                -- SP -- MB --
                ++ -- -- -- ++
                -- ++ ++ ++ --
            """,
            weight_data="""
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
            """,
            spawn_data=[{'battle': 0, 'boss': 1}],
        ),
        config_base='tsk1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: 'clear_boss',
        },
    ),
}
