"""
Stages of event_20260326_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']
PLAN_2 = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default']

STAGES = {
    'ht1': Stage(
        map=dict(
            name='HT1',
            shape='I7',
            camera_data=['E2', 'F5'],
            camera_data_spawn_point=['E5'],
            map_data="""
                -- -- MB -- ++ -- ME -- --
                -- ME -- Me ++ ME -- ME --
                -- ++ Me -- -- -- -- -- ++
                -- MS ++ MS -- Me -- ME --
                -- -- MS -- ++ ++ ME -- --
                ++ -- __ -- ++ ++ -- -- ME
                ++ SP -- SP -- -- -- ME --
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_CHAPTER_SWITCH_20241219_SP=True,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_HAS_MODE_SWITCH=True,
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (120, 222),
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
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_SWIPE_MULTIPLY=(1.147, 1.168),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.109, 1.129),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.077, 1.096),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'ht2': Stage(
        map=dict(
            name='HT2',
            shape='I7',
            camera_data=['D2', 'D5', 'F5'],
            camera_data_spawn_point=['F2'],
            map_data="""
                -- -- ++ ++ SP -- SP ++ --
                ME ME ++ ++ -- -- -- ++ --
                -- -- -- -- -- MS -- Me --
                ME ME ++ ++ ++ -- ++ ++ ++
                -- -- -- -- MS -- MS -- Me
                ME ME ++ -- -- __ -- -- ++
                -- -- ++ -- Me MB Me -- ME
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
            MAP_SIREN_TEMPLATE=[],
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
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'ht3': Stage(
        map=dict(
            name='HT3',
            shape='I8',
            camera_data=['E3', 'E6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                -- -- -- ++ ++ ++ -- -- --
                -- ++ -- Me -- Me -- ++ --
                -- -- Me -- -- -- Me -- --
                -- ME -- -- MB -- -- ME --
                -- ++ ++ MS -- MS ++ ++ --
                -- ++ ++ -- MS -- ++ ++ --
                -- ME -- -- __ -- -- ME --
                -- ME -- SP -- SP -- ME --
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
            MAP_SIREN_TEMPLATE=[],
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
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    't1': Stage(
        map=dict(
            name='T1',
            shape='I7',
            camera_data=['E2', 'F5'],
            camera_data_spawn_point=['E5'],
            map_data="""
                -- -- MB -- ++ -- ME -- --
                -- ME -- Me ++ ME -- ME --
                -- ++ Me -- -- -- -- -- ++
                -- MS ++ MS -- Me -- ME --
                -- -- MS -- ++ ++ ME -- --
                ++ -- __ -- ++ ++ -- -- ME
                ++ SP -- SP -- -- -- ME --
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_CHAPTER_SWITCH_20241219_SP=True,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_HAS_MODE_SWITCH=True,
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (120, 222),
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
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_SWIPE_MULTIPLY=(1.147, 1.168),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.109, 1.129),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.077, 1.096),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    't2': Stage(
        map=dict(
            name='T2',
            shape='I7',
            camera_data=['D2', 'D5', 'F5'],
            camera_data_spawn_point=['F2'],
            map_data="""
                -- -- ++ ++ SP -- SP ++ --
                ME ME ++ ++ -- -- -- ++ --
                -- -- -- -- -- MS -- Me --
                ME ME ++ ++ ++ -- ++ ++ ++
                -- -- -- -- MS -- MS -- Me
                ME ME ++ -- -- __ -- -- ++
                -- -- ++ -- Me MB Me -- ME
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
            MAP_SIREN_TEMPLATE=[],
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
    't3': Stage(
        map=dict(
            name='T3',
            shape='I8',
            camera_data=['E3', 'E6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                -- -- -- ++ ++ ++ -- -- --
                -- ++ -- Me -- Me -- ++ --
                -- -- Me -- -- -- Me -- --
                -- ME -- -- MB -- -- ME --
                -- ++ ++ MS -- MS ++ ++ --
                -- ++ ++ -- MS -- ++ ++ --
                -- ME -- -- __ -- -- ME --
                -- ME -- SP -- SP -- ME --
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
            MAP_SIREN_TEMPLATE=[],
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
            5: 'fleet_boss.clear_boss',
        },
    ),
}
