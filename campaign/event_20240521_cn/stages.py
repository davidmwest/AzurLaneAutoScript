"""
Stages of event_20240521_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']

STAGES = {
    'a2': Stage(
        map=dict(
            name='A2',
            shape='I8',
            camera_data=['E2', 'E6', 'F2', 'F6'],
            camera_data_spawn_point=['E2'],
            map_data="""
                ++ SP -- SP ++ ++ ++ -- --
                ++ -- -- -- Me ++ ME -- --
                -- -- MS -- -- Me -- -- ME
                -- MS -- MS -- -- __ Me ++
                ++ -- -- ++ ++ Me -- ME ++
                -- ME -- ++ ++ Me -- -- ME
                -- -- ME -- -- -- -- MB --
                -- -- -- ++ ++ ++ ME -- --
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
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='a1',
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
                'height': (80, 238),
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
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_SWIPE_MULTIPLY=(1.268, 1.292),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.226, 1.249),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.19, 1.212),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'a3': Stage(
        map=dict(
            name='A3',
            shape='K7',
            camera_data=['F2', 'F5', 'H2', 'H5'],
            camera_data_spawn_point=['H2'],
            map_data="""
                ++ -- -- ME -- ME ++ ++ SP -- SP
                ++ ++ ++ ++ ME -- ME ++ -- -- --
                -- -- -- ++ -- __ -- -- -- MS --
                -- -- MB -- -- Me ++ ++ ++ -- MS
                -- -- -- ++ -- -- Me -- -- MS --
                ++ ++ ++ ++ ME -- -- ++ Me -- Me
                ++ -- -- ME -- ME -- -- -- ME --
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
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=['SirenBoss18', 'SirenBoss182', 'SirenBoss19'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 238),
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
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_SWIPE_MULTIPLY=(1.232, 1.255),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.191, 1.213),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.156, 1.177),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'c2': Stage(
        map=dict(
            name='C2',
            shape='I8',
            camera_data=['E2', 'E6', 'F2', 'F6'],
            camera_data_spawn_point=['E2'],
            map_data="""
                ++ SP -- SP ++ ++ ++ -- --
                ++ -- -- -- Me ++ ME -- --
                -- -- MS -- -- Me -- -- ME
                -- MS -- MS -- -- __ Me ++
                ++ -- -- ++ ++ Me -- ME ++
                -- ME -- ++ ++ Me -- -- ME
                -- -- ME -- -- -- -- MB --
                -- -- -- ++ ++ ++ ME -- --
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
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='c1',
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
                'height': (80, 238),
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
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_SWIPE_MULTIPLY=(1.268, 1.292),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.226, 1.249),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.19, 1.212),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'c3': Stage(
        map=dict(
            name='C3',
            shape='K7',
            camera_data=['F2', 'F5', 'H2', 'H5'],
            camera_data_spawn_point=['H2'],
            map_data="""
                ++ -- -- ME -- ME ++ ++ SP -- SP
                ++ ++ ++ ++ ME -- ME ++ -- -- --
                -- -- -- ++ -- __ -- -- -- MS --
                -- -- MB -- -- Me ++ ++ ++ -- MS
                -- -- -- ++ -- -- Me -- -- MS --
                ++ ++ ++ ++ ME -- -- ++ Me -- Me
                ++ -- -- ME -- ME -- -- -- ME --
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
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['SirenBoss18', 'SirenBoss182', 'SirenBoss19'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 238),
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
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_SWIPE_MULTIPLY=(1.232, 1.255),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.191, 1.213),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.156, 1.177),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
