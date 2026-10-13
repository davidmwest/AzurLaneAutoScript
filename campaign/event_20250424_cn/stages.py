"""
Stages of event_20250424_cn, see module/campaign/stage.py
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
            camera_data=['D2', 'F2', 'F5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                Me -- Me -- -- -- ++ ++ ++
                -- Me -- ++ ME -- ME -- --
                -- ++ -- -- -- -- -- ME --
                -- ++ MS -- ME -- ME ++ ++
                -- -- __ MS -- -- -- -- ++
                SP -- -- ++ ++ ME -- -- ME
                -- SP -- MB ++ -- ME ME --
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
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_CHAPTER_SWITCH_20241219_SP=True,
            MAP_HAS_MODE_SWITCH=True,
            STAGE_ENTRANCE=['half', '20240725'],
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
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
            MAP_SWIPE_MULTIPLY=(1.124, 1.145),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.087, 1.107),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.055, 1.074),
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
            camera_data_spawn_point=['F2', 'D2'],
            map_data="""
                ++ ++ ++ SP -- SP ++ ++ --
                Me -- Me -- -- -- ++ ++ ME
                -- -- -- -- MS -- -- Me --
                -- ME ++ MS __ MS -- -- --
                -- -- -- -- ++ -- -- Me --
                ME ME ++ -- MB -- ME -- ME
                -- -- ++ ME -- ME ++ ++ ++
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
            MAP_SIREN_TEMPLATE=['BB', 'CV'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.246, 1.269),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.205, 1.227),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.17, 1.191),
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
            camera_data=['E3', 'F3', 'F6'],
            camera_data_spawn_point=['F6'],
            map_data="""
                ++ ++ -- -- ++ -- -- ++ ++
                ++ ++ ME -- ++ -- ME -- ++
                -- ME -- Me ME Me -- ME --
                -- ME -- -- -- -- -- ME --
                ++ ++ ++ Me -- Me ++ ++ ++
                -- -- ++ -- -- MS -- -- SP
                -- -- MB -- __ -- MS -- --
                -- -- ++ -- -- MS -- -- SP
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
            MAP_SIREN_TEMPLATE=['Intruder'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            HOMO_EDGE_COLOR_RANGE=(0, 17),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=300,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(1.077, 1.098),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.042, 1.061),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.012, 1.03),
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
            shape='M5',
            camera_data=['F3', 'H3'],
            camera_data_spawn_point=['F3'],
            map_data="""
                ++ ++ ++ ++ ++ ++ ++ ++ ME -- ME ++ ++
                -- -- ++ SP -- -- MS ME -- Me -- ++ ++
                -- -- MB -- __ MS -- -- -- -- -- ++ --
                -- -- ++ SP -- -- MS ME -- Me -- ++ ++
                ++ ++ ++ ++ ++ ++ ++ ++ ME -- ME ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 8, 'siren': 3},
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
            MAP_SIREN_TEMPLATE=['Intruder'],
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
            MAP_CHAPTER_SWITCH_20241219_SP=True,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_IS_ONE_TIME_STAGE=True,
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
            HOMO_EDGE_COLOR_RANGE=(0, 17),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=300,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom-right',
            MAP_SWIPE_MULTIPLY=(1.206, 1.228),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.166, 1.188),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.132, 1.152),
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
            camera_data=['D2', 'F2', 'F5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                Me -- Me -- -- -- ++ ++ ++
                -- Me -- ++ ME -- ME -- --
                -- ++ -- -- -- -- -- ME --
                -- ++ MS -- ME -- ME ++ ++
                -- -- __ MS -- -- -- -- ++
                SP -- -- ++ ++ ME -- -- ME
                -- SP -- MB ++ -- ME ME --
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
            MAP_SIREN_TEMPLATE=['DD', 'CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_CHAPTER_SWITCH_20241219_SP=True,
            MAP_HAS_MODE_SWITCH=True,
            STAGE_ENTRANCE=['half', '20240725'],
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
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
            MAP_SWIPE_MULTIPLY=(1.124, 1.145),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.087, 1.107),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.055, 1.074),
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
            camera_data_spawn_point=['F2', 'D2'],
            map_data="""
                ++ ++ ++ SP -- SP ++ ++ --
                Me -- Me -- -- -- ++ ++ ME
                -- -- -- -- MS -- -- Me --
                -- ME ++ MS __ MS -- -- --
                -- -- -- -- ++ -- -- Me --
                ME ME ++ -- MB -- ME -- ME
                -- -- ++ ME -- ME ++ ++ ++
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
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.246, 1.269),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.205, 1.227),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.17, 1.191),
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
            camera_data=['E3', 'F3', 'F6'],
            camera_data_spawn_point=['F6'],
            map_data="""
                ++ ++ -- -- ++ -- -- ++ ++
                ++ ++ ME -- ++ -- ME -- ++
                -- ME -- Me ME Me -- ME --
                -- ME -- -- -- -- -- ME --
                ++ ++ ++ Me -- Me ++ ++ ++
                -- -- ++ -- -- MS -- -- SP
                -- -- MB -- __ -- MS -- --
                -- -- ++ -- -- MS -- -- SP
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
            MAP_SIREN_TEMPLATE=['Intruder'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            HOMO_EDGE_COLOR_RANGE=(0, 17),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=300,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(1.077, 1.098),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.042, 1.061),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.012, 1.03),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
