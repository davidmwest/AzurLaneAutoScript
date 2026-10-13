"""
Stages of war_archives_20180607_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '..campaign_war_archives.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']
PLAN_2 = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default']

STAGES = {
    'a2': Stage(
        base=BASE,
        map=dict(
            name='A2',
            camera_sight=(-4, -2, 4, 2),
            shape='G7',
            camera_data=['D2', 'D5'],
            camera_data_spawn_point=[],
            map_data="""
                ++ ++ ME -- Me -- MB
                ++ ++ -- __ -- -- --
                ++ ++ ME -- ME -- Me
                ME -- ME MS -- -- --
                -- ME __ -- -- Me MB
                SP -- -- ME -- ++ ++
                SP SP -- -- ME ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='a1',
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'a3': Stage(
        base=BASE,
        map=dict(
            name='A3',
            camera_sight=(-4, -2, 4, 2),
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=[],
            map_data="""
                -- -- ++ ++ ++ ++ ++ --
                -- SP ++ ++ ++ ++ ++ --
                SP -- -- ME -- ME -- MB
                -- ME -- -- -- -- -- --
                -- -- Me -- ME Me -- MB
                ME -- ME __ -- __ ++ ++
                ++ ++ -- -- MS -- ++ ++
                ++ ++ -- ME -- -- -- MB
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
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='a1',
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b2': Stage(
        base=BASE,
        map=dict(
            name='B2',
            camera_sight=(-4, -2, 4, 2),
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=[],
            map_data="""
                -- -- ++ ++ ++ ++ -- -- ++ ++
                MS -- MB ++ ++ ++ ME -- ++ ++
                -- Me -- -- ++ ++ MS __ -- --
                -- ++ ++ __ ++ ++ ME -- ME --
                Me -- ME -- -- ME -- -- -- SP
                MB -- -- -- -- __ -- ME -- SP
                Me -- ME Me ME -- -- ++ -- SP
                -- Me -- ++ ++ MS ME -- -- --
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
        config_base='b1',
        config=dict(
            MAP_SIREN_COUNT=2,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c1': Stage(
        base=BASE,
        map=dict(
            name='C1',
            camera_sight=(-4, -2, 4, 2),
            shape='I6',
            camera_data_spawn_point=[],
            map_data="""
                Me -- -- ME -- -- ME -- Me
                -- -- __ -- -- __ -- -- MB
                ME -- ME ++ ++ ME -- -- --
                -- -- ++ ++ ++ -- -- ME Me
                SP -- ++ ++ -- MS -- ++ ++
                SP SP -- -- -- ME MB ++ ++
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
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            SUBMARINE=0,
            POOR_MAP_DATA=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_SIREN=True,
            MAP_HAS_DYNAMIC_RED_BORDER=False,
            MAP_SIREN_COUNT=2,
            MAP_HAS_PT_BONUS=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (100, 231),
                'width': 1,
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (231, 255),
                'prominence': 2,
                'distance': 50,
                'wlen': 1000,
            },
            VANISH_POINT_RANGE=((540, 740), (-4000, -2000)),
            DISTANCE_POINT_X_RANGE=((-2000, -1000),),
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=50,
            EDGE_LINES_HOUGHLINES_THRESHOLD=50,
            COINCIDENT_POINT_ENCOURAGE_DISTANCE=1.0,
            MID_DIFF_RANGE_H=(45, 70),
            MID_DIFF_RANGE_V=(94, 100),
            TRUST_EDGE_LINES=True,
            MAP_GRID_CENTER_TOLERANCE=0.3,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'c2': Stage(
        base=BASE,
        map=dict(
            name='C2',
            camera_sight=(-4, -2, 4, 2),
            shape='G7',
            camera_data_spawn_point=[],
            map_data="""
                ++ ++ ME -- Me -- MB
                ++ ++ -- __ -- -- --
                ++ ++ ME -- ME -- Me
                ME -- ME MS -- -- --
                -- ME __ -- -- Me MB
                SP -- -- ME -- ++ ++
                SP SP -- -- ME ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='c1',
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'c3': Stage(
        base=BASE,
        map=dict(
            name='C3',
            camera_sight=(-4, -2, 4, 2),
            shape='H8',
            camera_data_spawn_point=[],
            map_data="""
                -- -- ++ ++ ++ ++ ++ --
                -- SP ++ ++ ++ ++ ++ --
                SP -- -- ME -- ME -- MB
                -- ME -- -- -- -- -- --
                -- -- Me -- ME Me -- MB
                ME -- ME __ -- __ ++ ++
                ++ ++ -- -- MS -- ++ ++
                ++ ++ -- ME -- -- -- MB
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
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='c1',
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c4': Stage(
        base=BASE,
        map=dict(
            name='C4',
            camera_sight=(-4, -2, 4, 2),
            shape='I7',
            camera_data_spawn_point=[],
            map_data="""
                ++ ++ ++ ++ ++ -- -- ++ ++
                ++ ++ ++ ++ ++ MB MB ++ ++
                -- ME Me ME -- -- -- ++ ++
                MS -- __ -- -- MS -- Me --
                ++ ++ ME -- ME -- ME __ ME
                ++ ++ -- -- -- ME -- ME --
                ++ ++ SP SP SP ++ ++ -- MS
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='c1',
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd1': Stage(
        base=BASE,
        map=dict(
            name='D1',
            camera_sight=(-4, -2, 4, 2),
            shape='J7',
            camera_data_spawn_point=[],
            map_data="""
                ++ ++ ++ MS -- ME ++ ++ ++ ++
                ++ ++ ++ -- ME __ -- ++ ++ ++
                ++ ++ ++ __ -- ME -- -- ++ ++
                ++ ++ ++ Me ++ ++ ME -- ++ ++
                -- MB -- -- ME ME -- ME -- SP
                -- -- Me -- -- -- -- __ -- SP
                ++ ++ -- Me MS ME Me ++ ME --
            """,
            weight_data="""
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
        config=dict(
            SUBMARINE=0,
            POOR_MAP_DATA=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_SIREN=True,
            MAP_HAS_DYNAMIC_RED_BORDER=False,
            MAP_SIREN_COUNT=3,
            MAP_HAS_PT_BONUS=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (100, 231),
                'width': 1,
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (231, 255),
                'prominence': 2,
                'distance': 50,
                'wlen': 1000,
            },
            VANISH_POINT_RANGE=((540, 740), (-4000, -2000)),
            DISTANCE_POINT_X_RANGE=((-2000, -1000),),
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=50,
            EDGE_LINES_HOUGHLINES_THRESHOLD=50,
            COINCIDENT_POINT_ENCOURAGE_DISTANCE=1.0,
            MID_DIFF_RANGE_H=(45, 70),
            MID_DIFF_RANGE_V=(94, 100),
            TRUST_EDGE_LINES=True,
            MAP_GRID_CENTER_TOLERANCE=0.3,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd2': Stage(
        base=BASE,
        map=dict(
            name='D2',
            camera_sight=(-4, -2, 4, 2),
            shape='J8',
            camera_data_spawn_point=[],
            map_data="""
                -- -- ++ ++ ++ ++ -- -- ++ ++
                MS -- MB ++ ++ ++ ME -- ++ ++
                -- Me -- -- ++ ++ MS __ -- --
                -- ++ ++ __ ++ ++ ME -- ME --
                Me -- ME -- -- ME -- -- -- SP
                MB -- -- -- -- __ -- ME -- SP
                Me -- ME Me ME -- -- ++ -- SP
                -- Me -- ++ ++ MS ME -- -- --
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
        config_base='d1',
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
}
