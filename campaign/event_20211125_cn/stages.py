"""
Stages of event_20211125_cn, see module/campaign/stage.py
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
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                ++ MB -- ++ ++ -- Me --
                ++ -- -- -- Me -- -- --
                ME ++ MS __ -- -- ++ ++
                -- -- -- ++ ++ MS -- ME
                Me -- MS ++ ++ -- -- --
                ++ ++ -- -- __ MS ++ ME
                -- -- -- Me -- -- -- ++
                -- Me -- ++ ++ SP SP ++
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
            spawn_data=[
                {'battle': 0, 'siren': 2},
                {'battle': 1, 'enemy': 1, 'siren': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 2},
                {'battle': 4},
                {'battle': 5},
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['GridmanCL', 'GridmanCA'],
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
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 231),
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
            HOMO_EDGE_HOUGHLINES_THRESHOLD=180,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom-left',
            MAP_SWIPE_MULTIPLY=(0.976, 0.995),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.944, 0.962),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.917, 0.933),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=2)', 'battle_default'],
            5: PLAN,
            7: 'fleet_boss.clear_boss',
        },
    ),
    't2': Stage(
        base=BASE,
        map=dict(
            name='T2',
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                -- MB -- -- -- ++ -- ME
                Me -- -- ME -- -- -- --
                ME -- ++ ++ Me -- ME ME
                -- ME ++ ++ -- -- ++ --
                -- -- -- MS __ -- ++ Me
                ME -- ME -- ME -- -- MS
                -- ++ ++ -- -- -- ME --
                -- ME Me -- SP SP ++ ++
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
            MAP_SIREN_TEMPLATE=['GridmanCL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(0.958, 0.976),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.926, 0.944),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.899, 0.916),
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
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['E6', 'E2'],
            map_data="""
                ++ -- ME -- -- MS -- ++
                ++ ME -- -- Me -- -- ME
                MB -- -- ME ++ ++ -- --
                -- -- Me ME ++ ++ -- SP
                -- ME -- -- -- Me -- SP
                ME ++ ++ ME __ MS -- --
                -- Me ++ -- ME -- ME --
                ME -- -- ME ++ ME ++ MS
            """,
            weight_data="""
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                90 90 90 50 50 50 50 50
                90 90 90 50 50 50 50 50
                90 90 90 90 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['GridmanCL', 'GridmanCA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.064, 1.084),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.029, 1.048),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.999, 1.017),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'tss1': Stage(
        base=BASE,
        map=dict(
            name='TSS1',
            shape='E7',
            camera_data=['C3'],
            camera_data_spawn_point=['C3'],
            map_data="""
                -- ++ -- ++ --
                -- -- -- -- --
                ++ ++ MB ++ ++
                ++ ++ -- ++ ++
                -- -- SP -- --
                ++ -- -- -- ++
                -- -- -- -- --
            """,
            weight_data="""
                50 50 50 50 50
                50 50 50 50 50
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
            MAP_IS_ONE_TIME_STAGE=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: 'clear_boss',
        },
    ),
    'tss2': Stage(
        base=BASE,
        map=dict(
            name='TSS2',
            shape='E5',
            camera_data=['C2'],
            camera_data_spawn_point=['C2'],
            map_data="""
                ++ -- -- ++ ++
                -- -- -- MB ++
                -- -- SP -- --
                ++ ++ -- -- --
                ++ ++ -- -- ++
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
        config_base='tss1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_IS_ONE_TIME_STAGE=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: 'clear_boss',
        },
    ),
    'tss3': Stage(
        base=BASE,
        map=dict(
            name='TSS3',
            shape='E5',
            camera_data=['C3'],
            camera_data_spawn_point=['C3'],
            map_data="""
                -- ++ -- ++ --
                -- ++ ++ ++ --
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
        config_base='tss1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_IS_ONE_TIME_STAGE=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: 'clear_boss',
        },
    ),
    'tss4': Stage(
        base=BASE,
        map=dict(
            name='TSS4',
            shape='E7',
            camera_data=['C3'],
            camera_data_spawn_point=['C3'],
            map_data="""
                -- -- -- -- --
                -- ++ ++ ++ --
                -- ++ SP ++ --
                -- ++ -- ++ --
                -- ++ MB ++ --
                -- ++ ++ ++ --
                -- -- -- -- --
            """,
            weight_data="""
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
            """,
            spawn_data=[{'battle': 0, 'boss': 1}],
        ),
        config_base='tss1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_IS_ONE_TIME_STAGE=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: 'clear_boss',
        },
    ),
    'tss5': Stage(
        base=BASE,
        map=dict(
            name='TSS5',
            shape='E7',
            camera_data=['C3'],
            camera_data_spawn_point=['C3'],
            map_data="""
                ++ ++ ++ ++ ++
                ++ ++ ++ ++ ++
                ++ ++ MB ++ ++
                -- ++ -- ++ --
                ++ ++ SP ++ ++
                ++ ++ -- ++ ++
                -- ++ -- ++ --
            """,
            weight_data="""
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
            """,
            spawn_data=[{'battle': 0, 'boss': 1}],
        ),
        config_base='tss1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_IS_ONE_TIME_STAGE=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: 'clear_boss',
        },
    ),
}
