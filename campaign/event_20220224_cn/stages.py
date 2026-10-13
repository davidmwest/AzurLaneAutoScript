"""
Stages of event_20220224_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']
PLAN_2 = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default']

STAGES = {
    'b1': Stage(
        map=dict(
            name='B1',
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- -- Me -- -- -- -- ++
                ME ME -- ++ ++ ME ME ++
                -- -- -- MB ++ -- -- --
                MS ME -- -- -- ME -- Me
                -- -- MS __ MS -- -- Me
                ++ ++ ++ -- -- -- ME ++
                -- ME -- SP SP -- Me --
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
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
                {'battle': 5, 'enemy': 1},
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
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CAred': 1.111,
                'BBred': 1.111,
                'CV': 1.111,
            },
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(0.974, 0.992),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.942, 0.959),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.914, 0.931),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b2': Stage(
        map=dict(
            name='B2',
            shape='I7',
            camera_data=['D3', 'D5', 'F3', 'F5'],
            camera_data_spawn_point=['E2'],
            map_data="""
                -- -- -- -- SP SP -- -- --
                -- ME ++ -- -- -- -- Me --
                -- -- ++ MS -- -- MS -- Me
                ME -- Me -- -- MS ++ ++ ++
                -- ME -- __ Me -- -- -- ME
                -- ME -- -- ++ -- Me -- ME
                ++ -- ME -- MB -- -- ME --
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'Soobrazitelny'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.11, 1.131),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.073, 1.093),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.042, 1.061),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'b3': Stage(
        map=dict(
            name='B3',
            shape='I9',
            camera_data=['D3', 'D5', 'F3', 'F5'],
            camera_data_spawn_point=['E7'],
            map_data="""
                ++ ++ ++ -- -- -- ++ ++ ++
                -- -- ME ME -- ME ME -- --
                -- ME -- -- MS -- -- ME --
                ++ -- -- ++ -- ++ -- -- ++
                ++ -- MS -- MB -- MS -- ++
                ME -- -- ++ -- ++ -- -- ME
                -- Me -- Me __ Me -- Me --
                ++ ++ -- -- -- -- -- ++ ++
                ++ ++ ++ SP -- SP ++ ++ ++
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
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CAred', 'Soobrazitelny', 'Kiev'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(0.99, 1.009),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.957, 0.975),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.93, 0.946),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd1': Stage(
        map=dict(
            name='D1',
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['E5', 'D5'],
            map_data="""
                -- -- Me -- -- -- -- ++
                ME ME -- ++ ++ ME ME ++
                -- -- -- MB ++ -- -- --
                MS ME -- -- -- ME -- Me
                -- -- MS __ MS -- -- Me
                ++ ++ ++ -- -- -- ME ++
                -- ME -- SP SP -- Me --
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
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['CAred', 'BBred'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 238),
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
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CAred': 1.111,
                'BBred': 1.111,
                'CV': 1.111,
            },
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(0.974, 0.992),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.942, 0.959),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.914, 0.931),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd2': Stage(
        map=dict(
            name='D2',
            shape='I7',
            camera_data=['D3', 'D5', 'F3', 'F5'],
            camera_data_spawn_point=['E2'],
            map_data="""
                -- -- -- -- SP SP -- -- --
                -- ME ++ -- -- -- -- Me --
                -- -- ++ MS -- -- MS -- Me
                ME -- Me -- -- MS ++ ++ ++
                -- ME -- __ Me -- -- -- ME
                -- ME -- -- ++ -- Me -- ME
                ++ -- ME -- MB -- -- ME --
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
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_SIREN_TEMPLATE=['BBred', 'Kiev'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.11, 1.131),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.073, 1.093),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.042, 1.061),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        map=dict(
            name='D3',
            shape='I9',
            camera_data=['D3', 'D5', 'F3', 'F5'],
            camera_data_spawn_point=['E7'],
            map_data="""
                ++ ++ ++ -- -- -- ++ ++ ++
                -- -- ME ME -- ME ME -- --
                -- ME -- -- MS -- -- ME --
                ++ -- -- ++ -- ++ -- -- ++
                ++ -- MS -- MB -- MS -- ++
                ME -- -- ++ -- ++ -- -- ME
                -- Me -- Me __ Me -- Me --
                ++ ++ -- -- -- -- -- ++ ++
                ++ ++ ++ SP -- SP ++ ++ ++
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
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_SIREN_TEMPLATE=['BBred', 'CV', 'Kiev', 'Volga'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(0.99, 1.009),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.957, 0.975),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.93, 0.946),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
}
