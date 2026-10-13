"""
Stages of war_archives_20191031_en, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '..campaign_war_archives.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']

STAGES = {
    'a1': Stage(
        base=BASE,
        map=dict(
            name='A1',
            shape='I5',
            camera_data=['D2', 'D3', 'F2', 'F3'],
            camera_data_spawn_point=['D3', 'D2'],
            map_data="""
                SP -- ++ ME -- ME -- ++ --
                -- ME -- -- ME -- Me ++ Me
                -- -- ME -- -- -- __ -- --
                -- ME -- ++ ++ Me -- Me --
                SP -- -- Me ++ -- Me -- MB
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            3: 'clear_boss',
        },
    ),
    'a2': Stage(
        base=BASE,
        map=dict(
            name='A2',
            shape='K6',
            camera_data=['D2', 'D4', 'H2', 'H4'],
            camera_data_spawn_point=['D2', 'D4'],
            map_data="""
                SP ME -- ME -- -- -- -- -- Me --
                SP -- -- -- -- ME -- Me ++ ++ --
                SP -- ME ++ ++ ++ -- -- __ Me --
                SP -- ME ++ ++ ++ -- ME -- -- Me
                SP -- -- ME -- -- -- -- ++ -- --
                SP -- -- -- -- ME -- MB ++ -- MB
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            3: 'clear_boss',
        },
    ),
    'a3': Stage(
        base=BASE,
        map=dict(
            name='A3',
            shape='J6',
            camera_data=['D2', 'D4', 'G2', 'G4'],
            camera_data_spawn_point=['D2'],
            map_data="""
                SP ++ ME -- ME -- -- -- Me MB
                SP ++ -- -- -- -- ME -- -- --
                -- -- -- ME ++ ++ ++ __ Me ++
                -- ME -- -- -- -- Me -- -- Me
                -- -- -- -- ME -- -- Me -- --
                ++ ME ME ++ ++ ++ MM -- -- MB
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2, 'mystery': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'a4': Stage(
        base=BASE,
        map=dict(
            name='A4',
            shape='K7',
            camera_data=['D2', 'D5', 'H2', 'H5'],
            camera_data_spawn_point=['D2', 'D5'],
            map_data="""
                SP -- -- ++ ME -- -- -- Me -- MM
                -- -- ++ ++ ++ -- Me -- -- -- --
                ME -- -- ME -- -- -- ++ ++ ++ --
                ME -- -- -- -- ++ __ ++ MB -- --
                -- -- ME -- -- -- Me ++ ++ ++ --
                -- -- ++ ++ ME -- -- Me -- -- --
                SP -- ME ++ -- ME -- -- -- Me MM
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2, 'mystery': 1},
                {'battle': 3, 'enemy': 1, 'mystery': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b1': Stage(
        base=BASE,
        map=dict(
            name='B1',
            shape='H6',
            camera_data=['D2', 'D4', 'E2', 'E4'],
            camera_data_spawn_point=['D4'],
            map_data="""
                ++ ME -- -- -- -- -- MB
                ++ -- -- ME __ Me Me --
                ME -- ME ++ ++ ++ -- --
                -- -- ME ++ ++ ++ ME --
                SP -- -- -- -- -- -- --
                SP -- -- ME -- Me -- MB
            """,
            weight_data="""
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
        ),
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
            shape='F8',
            camera_data=['C2', 'C6'],
            camera_data_spawn_point=['C6'],
            map_data="""
                MB -- -- -- -- MB
                Me -- ++ ++ -- Me
                -- __ Me ++ -- --
                Me -- -- ME -- ME
                -- ME -- -- -- MM
                ++ ++ -- -- ME ++
                -- ++ -- ME -- --
                SP -- -- -- -- SP
            """,
            weight_data="""
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2, 'mystery': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=True,
            HOMO_EDGE_COLOR_RANGE=(0, 12),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_SWIPE_MULTIPLY=(1.101, 1.122),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.065, 1.085),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.034, 1.053),
            HOMO_STORAGE=((6, 5), [(211, 175), (782, 175), (158, 569), (800, 569)]),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='top',
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b3': Stage(
        base=BASE,
        map=dict(
            name='B3',
            shape='G8',
            camera_data=['D2', 'D6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ Me Me MM Me -- ++
                -- -- __ -- -- -- Me
                -- Me ++ ++ ++ -- --
                -- -- ++ MB ++ Me --
                ME -- -- -- -- -- --
                -- -- ++ ++ ++ -- ME
                -- ME -- ME -- -- --
                SP -- -- -- -- ME SP
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
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2, 'mystery': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'b4': Stage(
        base=BASE,
        map=dict(
            name='B4',
            shape='I9',
            camera_data=['D2', 'D6', 'D7', 'F2', 'F6', 'F7'],
            camera_data_spawn_point=['D7'],
            map_data="""
                ++ -- -- ME -- -- -- -- Me
                -- ME -- -- -- Me -- -- --
                -- -- -- Me -- ++ ++ Me --
                ME -- Me ++ -- ++ ++ -- --
                -- -- -- -- MB -- -- -- --
                -- ME ++ ++ -- ++ Me -- ME
                -- -- -- ++ -- Me __ -- --
                SP -- -- ME -- -- -- ME --
                SP SP -- -- -- ME -- -- ++
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
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            HOMO_EDGE_COLOR_RANGE=(0, 12),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_SWIPE_MULTIPLY=(1.101, 1.122),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.065, 1.085),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.034, 1.053),
            HOMO_STORAGE=((6, 4), [(448, 180), (1051, 180), (426, 513), (1100, 513)]),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='top',
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
            shape='I5',
            camera_data=['D2', 'D3', 'F2', 'F3'],
            camera_data_spawn_point=['D3', 'D2'],
            map_data="""
                SP -- ++ ME -- ME -- ++ --
                -- ME -- -- ME -- Me ++ Me
                -- -- ME -- -- -- __ -- --
                -- ME -- ++ ++ Me -- Me --
                SP -- -- Me ++ -- Me -- MB
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            3: 'clear_boss',
        },
    ),
    'c2': Stage(
        base=BASE,
        map=dict(
            name='C2',
            shape='K6',
            camera_data=['D2', 'D4', 'H2', 'H4'],
            camera_data_spawn_point=['D2', 'D4'],
            map_data="""
                SP ME -- ME -- -- -- -- -- Me --
                SP -- -- -- -- ME -- Me ++ ++ --
                SP -- ME ++ ++ ++ -- -- __ Me --
                SP -- ME ++ ++ ++ -- ME -- -- Me
                SP -- -- ME -- -- -- -- ++ -- --
                SP -- -- -- -- ME -- MB ++ -- MB
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
        ),
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
            shape='J6',
            camera_data=['D2', 'D4', 'G2', 'G4'],
            camera_data_spawn_point=['D2'],
            map_data="""
                SP ++ ME -- ME -- -- -- Me MB
                SP ++ -- -- -- -- ME -- -- --
                -- -- -- ME ++ ++ ++ __ Me ++
                -- ME -- -- -- -- Me -- -- Me
                -- -- -- -- ME -- -- Me -- --
                ++ ME ME ++ ++ ++ MM -- -- MB
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2, 'mystery': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'c4': Stage(
        base=BASE,
        map=dict(
            name='C4',
            shape='K7',
            camera_data=['D2', 'D5', 'H2', 'H5'],
            camera_data_spawn_point=['D2', 'D5'],
            map_data="""
                SP -- -- ++ ME -- -- -- Me -- MM
                -- -- ++ ++ ++ -- Me -- -- -- --
                ME -- -- ME -- -- -- ++ ++ ++ --
                ME -- -- -- -- ++ __ ++ MB -- --
                -- -- ME -- -- -- Me ++ ++ ++ --
                -- -- ++ ++ ME -- -- Me -- -- --
                SP -- ME ++ -- ME -- -- -- Me MM
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2, 'mystery': 1},
                {'battle': 3, 'enemy': 1, 'mystery': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=True,
        ),
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
            shape='H6',
            camera_data=['D2', 'D4', 'E2', 'E4'],
            camera_data_spawn_point=['D4'],
            map_data="""
                ++ ME -- -- -- -- -- MB
                ++ -- -- ME __ Me Me --
                ME -- ME ++ ++ ++ -- --
                -- -- ME ++ ++ ++ ME --
                SP -- -- -- -- -- -- --
                SP -- -- ME -- Me -- MB
            """,
            weight_data="""
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd2': Stage(
        base=BASE,
        map=dict(
            name='D2',
            shape='F8',
            camera_data=['C2', 'C6'],
            camera_data_spawn_point=['C6'],
            map_data="""
                MB -- -- -- -- MB
                Me -- ++ ++ -- Me
                -- __ Me ++ -- --
                Me -- -- ME -- ME
                -- ME -- -- -- MM
                ++ ++ -- -- ME ++
                -- ++ -- ME -- --
                SP -- -- -- -- SP
            """,
            weight_data="""
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2, 'mystery': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=True,
            HOMO_EDGE_COLOR_RANGE=(0, 12),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_SWIPE_MULTIPLY=(1.101, 1.122),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.065, 1.085),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.034, 1.053),
            HOMO_STORAGE=((6, 5), [(211, 175), (782, 175), (158, 569), (800, 569)]),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='top',
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        base=BASE,
        map=dict(
            name='D3',
            shape='G8',
            camera_data=['D2', 'D6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ Me Me MM Me -- ++
                -- -- __ -- -- -- Me
                -- Me ++ ++ ++ -- --
                -- -- ++ MB ++ Me --
                ME -- -- -- -- -- --
                -- -- ++ ++ ++ -- ME
                -- ME -- ME -- -- --
                SP -- -- -- -- ME SP
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
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2, 'mystery': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd4': Stage(
        base=BASE,
        map=dict(
            name='D4',
            shape='I9',
            camera_data=['D2', 'D6', 'D7', 'F2', 'F6', 'F7'],
            camera_data_spawn_point=['D7'],
            map_data="""
                ++ -- -- ME -- -- -- -- Me
                -- ME -- -- -- Me -- -- --
                -- -- -- Me -- ++ ++ Me --
                ME -- Me ++ -- ++ ++ -- --
                -- -- -- -- MB -- -- -- --
                -- ME ++ ++ -- ++ Me -- ME
                -- -- -- ++ -- Me __ -- --
                SP -- -- ME -- -- -- ME --
                SP SP -- -- -- ME -- -- ++
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
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            HOMO_EDGE_COLOR_RANGE=(0, 12),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_SWIPE_MULTIPLY=(1.101, 1.122),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.065, 1.085),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.034, 1.053),
            HOMO_STORAGE=((6, 4), [(448, 180), (1051, 180), (426, 513), (1100, 513)]),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='top',
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
