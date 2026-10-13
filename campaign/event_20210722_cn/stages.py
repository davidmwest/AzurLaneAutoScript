"""
Stages of event_20210722_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
PLAN = [
    'clear_siren',
    'clear_enemy(scale=(1,))',
    'clear_enemy(scale=(2,))',
    'clear_enemy(scale=(3,))',
    'battle_default',
]

STAGES = {
    'sp': Stage(
        base=BASE,
        map=dict(
            name='VSP',
            shape='G8',
            camera_data=['D2', 'D6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ ++ ++ MB ++ ++ ++
                ME -- MS -- MS -- ME
                ++ ++ -- MS -- ++ ++
                ++ ME -- ++ -- ME ++
                ++ ++ -- ++ -- ++ ++
                ++ ++ -- __ -- ++ ++
                ME -- -- -- -- -- ME
                ++ ++ SP -- SP ++ ++
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
            """,
            spawn_data=[
                {'battle': 0, 'siren': 3},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 2},
                {'battle': 4},
                {'battle': 5},
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_HAS_SIREN=True,
            MAP_SIREN_TEMPLATE=['AzusaMiura', 'ChihayaKisaragi', 'IoriMinase'],
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            HOMO_EDGE_COLOR_RANGE=(0, 12),
        ),
        battle={
            0: ['clear_siren', 'battle_default'],
            7: 'fleet_boss.clear_boss',
        },
    ),
    'sp1': Stage(
        base=BASE,
        map=dict(
            name='SP1',
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['E5'],
            map_data="""
                -- ME -- ME ++ ME -- --
                -- ++ MB -- ME -- Me --
                ME ++ -- -- -- ++ ++ MS
                -- ME -- ME -- Me ++ --
                -- Me ++ -- __ -- ME --
                -- -- -- ME MS -- -- SP
                ME -- Me ++ -- -- SP ++
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
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            HOMO_EDGE_COLOR_RANGE=(0, 12),
        ),
        battle={
            0: [
                'clear_enemy(scale=(1,))',
                'clear_enemy(scale=(2,))',
                'clear_enemy(scale=(3,))',
                'battle_default',
            ],
            4: 'clear_boss',
        },
    ),
    'sp2': Stage(
        base=BASE,
        map=dict(
            name='SP2',
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['D2'],
            map_data="""
                ++ ME -- -- ME ++ ++ ++
                ++ -- MS ME -- ME -- --
                SP -- -- -- Me -- ++ ME
                SP -- Me -- __ -- -- --
                -- -- -- -- ++ Me -- MB
                ++ -- ME MS ++ -- ME --
                -- Me ++ -- -- -- ++ ++
                ME -- ME -- ME ME ++ ++
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
            MAP_SIREN_TEMPLATE=['HarukaAmami'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(1.18, 1.203),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.142, 1.163),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.108, 1.128),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
        ),
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
            camera_data_spawn_point=['E2'],
            map_data="""
                -- Me ME ++ ME -- ++ ++
                ++ -- -- -- -- SP SP ++
                ++ -- MS ME -- -- -- --
                ME -- -- Me __ ++ -- MS
                -- ME ++ -- MS -- Me --
                ME -- ME -- ME -- ++ ME
                -- MB -- -- -- Me ++ --
                ME ++ ++ ++ ME -- ME --
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
            MAP_SIREN_TEMPLATE=['AzusaMiura', 'IoriMinase'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(1.201, 1.223),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.161, 1.183),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.127, 1.148),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'sp4': Stage(
        base=BASE,
        map=dict(
            name='SP4',
            shape='I8',
            camera_data=['D2', 'D4', 'D6', 'F2', 'F4', 'F6'],
            camera_data_spawn_point=['F6', 'D6'],
            map_data="""
                ++ ++ ++ ME -- ME ++ ++ ++
                ME -- ++ -- MB -- ++ -- ME
                ++ ME Me -- Me -- Me ME ++
                ME -- ME MS ++ MS ME -- ME
                ++ ++ -- -- ++ -- -- ++ ++
                ++ ++ -- MS __ MS -- ++ ++
                ME -- Me -- ME -- Me -- ME
                -- ME ++ SP -- SP ++ ME --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 40 10 50 10 40 50 50
                50 50 45 20 50 20 45 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 40 50 50 50 40 50 50
                50 50 50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['AzusaMiura', 'ChihayaKisaragi', 'IoriMinase'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(1.008, 1.027),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.975, 0.993),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.947, 0.964),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            DETECTION_BACKEND='perspective',
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
            EDGE_LINES_HOUGHLINES_THRESHOLD=40,
            TRUST_EDGE_LINES=False,
            TRUST_EDGE_LINES_THRESHOLD=7,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 231),
                'width': (1.5, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (245, 255),
                'width': (1.5, 10),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
        ),
        battle={
            0: [
                ('do', 'fleet_2_push_forward'),
                "clear_siren(genre=('Siren_AzusaMiura', 'Siren_IoriMinase'))",
                'clear_enemy(scale=(1,))',
                'clear_enemy(scale=(2,))',
                'clear_enemy(scale=(3,))',
                'battle_default',
            ],
            5: 'fleet_boss.clear_boss',
        },
    ),
}
