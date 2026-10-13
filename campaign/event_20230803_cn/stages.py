"""
Stages of event_20230803_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = [
    ('when', 'map_is_clear_mode', ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)'], ["clear_any_enemy(sort=('cost_2',))"]),
    'battle_default',
]

STAGES = {
    'sp1': Stage(
        base=BASE,
        map=dict(
            name='SP1',
            shape='I6',
            camera_data=['F2', 'F4'],
            camera_data_spawn_point=['D2', 'D4'],
            map_data="""
                ++ ++ ++ -- -- ME -- -- --
                -- -- Me -- Me -- Me ++ ++
                SP -- -- -- -- ME -- MB ++
                -- -- -- MS -- -- __ -- ME
                SP -- -- -- ++ ME -- ME --
                -- ++ ME -- Me -- ME ++ --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 1, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['DD'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_WALK_SPEEDUP=True,
            MAP_HAS_MOVABLE_NORMAL_ENEMY=True,
            MOVABLE_NORMAL_ENEMY_TURN=(2,),
            MAP_SIREN_MOVE_WAIT=0.5,
            MAP_WALK_USE_CURRENT_FLEET=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 231),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (231, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_EDGE_COLOR_RANGE=(0, 24),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CAred': 1.111,
                'BBred': 1.111,
                'CV': 1.111,
            },
            MAP_SWIPE_MULTIPLY=(1.179, 1.201),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.14, 1.161),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.107, 1.127),
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
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['E5', 'D5'],
            map_data="""
                ++ ME -- -- -- -- ME --
                ME -- -- Me Me -- ++ --
                ME -- Me ++ ++ ME ++ ME
                -- __ -- ++ ++ -- Me --
                ME -- MS MB MB MS __ ME
                ++ -- -- -- -- -- -- ME
                ++ ME -- SP SP -- ME ++
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
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CAred'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.133, 1.155),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.096, 1.116),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.064, 1.083),
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
            shape='I8',
            camera_data=['D2', 'D4', 'D6', 'F2', 'F4', 'F6'],
            camera_data_spawn_point=['F2', 'D2'],
            map_data="""
                -- -- ME ++ ++ ++ ME -- --
                ++ Me -- -- MB -- -- Me ++
                ME -- -- SP -- SP -- -- ME
                -- MS -- -- __ -- -- MS --
                ME -- ++ -- ++ -- ++ -- ME
                -- Me ++ MS -- MS ++ Me --
                ME -- Me -- -- -- Me -- ME
                ++ ME -- ++ ++ ++ -- ME ++
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
                {'battle': 1, 'enemy': 2, 'siren': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['SirenBoss15'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_SWIPE_MULTIPLY=(1.205, 1.227),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.165, 1.187),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.131, 1.151),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
