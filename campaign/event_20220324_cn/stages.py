"""
Stages of event_20220324_cn, see module/campaign/stage.py
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
            shape='K8',
            camera_data=['D4', 'D6', 'H4', 'H6'],
            camera_data_spawn_point=['H6', 'D6'],
            map_data="""
                -- -- -- -- ++ ++ ++ -- -- -- --
                -- -- -- -- ++ ++ ++ -- ++ ++ --
                -- ++ ++ Me -- MB -- Me ++ ++ --
                ME -- ME -- -- -- -- -- ME -- ME
                -- -- ++ ++ -- MS -- ++ ++ -- --
                -- ME ++ ++ MS __ MS ++ ++ ME --
                ME -- Me -- -- -- -- -- Me -- ME
                -- ME -- -- SP -- SP -- -- ME --
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
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2, 'siren': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4},
                {'battle': 5},
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['BB', 'CV'],
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
            DETECTION_BACKEND='perspective',
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
            EDGE_LINES_HOUGHLINES_THRESHOLD=75,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 245),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (245, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_CANNY_THRESHOLD=(75, 150),
            HOMO_EDGE_COLOR_RANGE=(0, 10),
            MAP_SWIPE_MULTIPLY=(1.037, 1.056),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.002, 1.021),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.973, 0.991),
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=2)', 'battle_default'],
            5: PLAN,
            7: 'fleet_boss.clear_boss',
        },
    ),
    'sp1': Stage(
        base=BASE,
        map=dict(
            name='SP1',
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['D2'],
            map_data="""
                SP SP -- -- -- -- -- --
                -- -- -- ++ ++ -- -- --
                ME -- -- MB MB -- -- ME
                -- -- MS -- -- MS -- --
                Me ++ ++ __ __ ++ ++ Me
                -- ME ++ ME ME ++ ME --
                ME -- Me -- -- Me -- ME
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
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 245),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (245, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_CANNY_THRESHOLD=(75, 150),
            HOMO_EDGE_COLOR_RANGE=(0, 10),
            MAP_SWIPE_MULTIPLY=(1.245, 1.268),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.204, 1.226),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.169, 1.19),
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'sp2': Stage(
        base=BASE,
        map=dict(
            name='SP2',
            shape='H8',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- ME ++ MB MB ++ ME --
                SP -- -- __ __ -- -- ME
                SP -- MS ME ME MS -- ME
                -- Me -- ++ ++ -- Me --
                -- Me -- ++ ++ -- Me --
                -- -- Me -- -- Me -- --
                ++ -- -- ME ME -- -- ++
                -- -- -- ++ ++ -- -- --
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
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.21, 1.233),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.17, 1.192),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.136, 1.156),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'sp3': Stage(
        base=BASE,
        map=dict(
            name='SP3',
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- -- ME -- -- -- ME --
                -- Me ++ ME -- ME -- --
                Me -- ++ Me -- ++ ++ --
                ++ -- -- __ -- -- ++ --
                SP -- MS -- Me -- ME --
                SP -- -- ++ ++ ME -- ME
                -- -- MS ++ ++ -- ME ++
                ++ ME -- MB MB -- -- --
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
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CA', 'BB'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.037, 1.056),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.002, 1.021),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.973, 0.991),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'sp4': Stage(
        base=BASE,
        map=dict(
            name='SP4',
            shape='H8',
            camera_data=['D3', 'D6', 'E3', 'E6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ -- -- -- -- ++ -- --
                -- Me ++ ++ ME ++ ME --
                ME -- ++ ++ -- ME -- ++
                Me -- MB MB -- -- -- ME
                ++ MS -- __ -- MS -- --
                SP -- -- Me ++ ++ -- ME
                SP -- -- Me -- ++ ME --
                ++ -- MS -- ME -- -- --
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
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2, 'siren': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['BB', 'CV'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.037, 1.056),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.002, 1.021),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.973, 0.991),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
