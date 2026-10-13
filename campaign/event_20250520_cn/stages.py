"""
Stages of event_20250520_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']

STAGES = {
    'a1': Stage(
        map=dict(
            name='A1',
            shape='I8',
            camera_data=['D3', 'D6', 'E4', 'E6'],
            camera_data_spawn_point=['D3'],
            map_data="""
                -- ++ ++ -- -- -- -- -- --
                -- SP ++ Me -- Me -- ME --
                SP -- -- -- -- ++ -- -- ++
                -- -- MS -- Me ++ ME -- --
                ++ MS -- -- -- -- -- ME --
                ++ -- __ ++ -- ME -- ME --
                MB -- ME -- -- ++ ++ -- ++
                -- ME -- ME -- ++ ++ -- --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50
                10 10 50 50 50 50 50 50 50
                10 10 20 25 50 50 50 50 50
                10 20 25 50 50 50 50 50 50
                50 25 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1, 'boss': 1},
                {'battle': 4, 'enemy': 1},
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
            MAP_CHAPTER_SWITCH_20241219=True,
            MAP_HAS_MODE_SWITCH=True,
            STAGE_ENTRANCE=['half', '20240725'],
            STAGE_INCREASE_AB=True,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (120, 238),
                'width': (1.5, 10),
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
            MAP_HAS_MOVABLE_NORMAL_ENEMY=True,
            MAP_SIREN_MOVE_WAIT=0.5,
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.259, 1.283),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.218, 1.24),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.182, 1.204),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            3: 'clear_boss',
        },
    ),
    'a2': Stage(
        map=dict(
            name='A2',
            shape='I8',
            camera_data=['D3', 'D6', 'E3', 'E6'],
            camera_data_spawn_point=['E3', 'D3'],
            map_data="""
                ++ -- ++ ++ ++ -- -- -- --
                -- -- SP -- SP -- ++ ++ --
                -- -- -- -- -- -- Me ++ --
                -- ++ -- __ -- -- -- Me --
                -- ++ MS -- MS -- ME -- --
                -- -- -- MB -- -- -- ME --
                -- ME ++ ++ ++ ME -- ME --
                ME -- -- ++ -- -- ME ++ --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50
                20 10 10 10 10 10 50 50 50
                50 10 10 10 10 10 20 50 50
                50 50 10 10 10 20 50 50 50
                50 50 20 20 20 50 50 50 50
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.234, 1.257),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.193, 1.215),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.158, 1.179),
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
            shape='I9',
            camera_data=['D5', 'D7', 'F5', 'F7'],
            camera_data_spawn_point=['F5', 'D5'],
            map_data="""
                -- -- -- -- -- -- -- -- --
                -- -- -- ++ ++ ++ -- -- --
                ++ -- -- ++ ++ ++ -- -- --
                -- ME -- ++ ++ ++ -- ME ++
                ME -- -- SP -- SP -- -- ME
                -- Me -- -- __ -- -- -- ME
                -- ++ Me -- MB -- Me ++ ++
                -- ++ -- MS -- MS -- ++ ++
                -- -- ME -- ++ -- ME -- --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 25 50 50 50 25 50 50
                50 25 10 10 10 10 10 25 50
                50 50 20 10 10 10 20 50 50
                50 50 25 20 20 20 25 50 50
                50 50 50 25 25 25 50 50 50
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.084, 1.104),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.048, 1.067),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.017, 1.036),
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
            shape='K8',
            camera_data=['D4', 'D6', 'G4', 'G6'],
            camera_data_spawn_point=['D4'],
            map_data="""
                -- -- -- -- -- -- -- -- -- ++ --
                -- ++ ++ ++ -- -- -- ++ -- -- ++
                -- ++ ++ ++ -- ME -- ME ME -- --
                -- ++ ++ ++ -- ++ ME -- -- ME --
                -- SP -- SP -- -- -- -- ++ ++ ++
                -- -- __ -- -- Me -- -- -- ME --
                Me -- MS -- Me ++ ++ ME ME -- ++
                -- MS MB MS -- ++ ++ -- -- ++ --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 20 50 50 50 50 50 50
                10 10 10 10 10 20 50 50 50 50 50
                20 10 10 10 20 20 50 50 50 50 50
                20 20 20 20 20 50 50 50 50 50 50
                20 20 20 20 50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.119, 1.14),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.082, 1.102),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.05, 1.069),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c1': Stage(
        map=dict(
            name='C1',
            shape='I8',
            camera_data=['D3', 'D6', 'E3', 'E6'],
            camera_data_spawn_point=['D3'],
            map_data="""
                -- ++ ++ -- -- -- -- -- --
                -- SP ++ Me -- Me -- ME --
                SP -- -- -- -- ++ -- -- ++
                -- -- MS -- Me ++ ME -- --
                ++ MS -- -- -- -- -- ME --
                ++ -- __ ++ -- ME -- ME --
                MB -- ME -- -- ++ ++ -- ++
                -- ME -- ME -- ++ ++ -- --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50
                10 10 50 50 50 50 50 50 50
                10 10 20 25 50 50 50 50 50
                10 20 25 50 50 50 50 50 50
                50 25 50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_CHAPTER_SWITCH_20241219=True,
            MAP_HAS_MODE_SWITCH=True,
            STAGE_ENTRANCE=['half', '20240725'],
            STAGE_INCREASE_AB=True,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (120, 238),
                'width': (1.5, 10),
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
            MAP_HAS_MOVABLE_NORMAL_ENEMY=True,
            MAP_SIREN_MOVE_WAIT=0.5,
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.259, 1.283),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.218, 1.24),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.182, 1.204),
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
            camera_data=['D3', 'D6', 'E3', 'E6'],
            camera_data_spawn_point=['E3', 'D3'],
            map_data="""
                ++ -- ++ ++ ++ -- -- -- --
                -- -- SP -- SP -- ++ ++ --
                -- -- -- -- -- -- Me ++ --
                -- ++ -- __ -- -- -- Me --
                -- ++ MS -- MS -- ME -- --
                -- -- -- MB -- -- -- ME --
                -- ME ++ ++ ++ ME -- ME --
                ME -- -- ++ -- -- ME ++ --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50
                20 10 10 10 10 10 50 50 50
                50 10 10 10 10 10 20 50 50
                50 50 10 10 10 20 50 50 50
                50 50 20 20 20 50 50 50 50
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.234, 1.257),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.193, 1.215),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.158, 1.179),
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
            shape='I9',
            camera_data=['D5', 'D7', 'F5', 'F7'],
            camera_data_spawn_point=['F5', 'D5'],
            map_data="""
                -- -- -- -- -- -- -- -- --
                -- -- -- ++ ++ ++ -- -- --
                ++ -- -- ++ ++ ++ -- -- --
                -- ME -- ++ ++ ++ -- ME ++
                ME -- -- SP -- SP -- -- ME
                -- Me -- -- __ -- -- -- ME
                -- ++ Me -- MB -- Me ++ ++
                -- ++ -- MS -- MS -- ++ ++
                -- -- ME -- ++ -- ME -- --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 25 50 50 50 25 50 50
                50 25 10 10 10 10 10 25 50
                50 50 20 10 10 10 20 50 50
                50 50 25 20 20 20 25 50 50
                50 50 50 25 25 25 50 50 50
                50 50 50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.084, 1.104),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.048, 1.067),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.017, 1.036),
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
            shape='K8',
            camera_data=['D4', 'D6', 'G4', 'G6'],
            camera_data_spawn_point=['D4'],
            map_data="""
                -- -- -- -- -- -- -- -- -- ++ --
                -- ++ ++ ++ -- -- -- ++ -- -- ++
                -- ++ ++ ++ -- ME -- ME ME -- --
                -- ++ ++ ++ -- ++ ME -- -- ME --
                -- SP -- SP -- -- -- -- ++ ++ ++
                -- -- __ -- -- Me -- -- -- ME --
                Me -- MS -- Me ++ ++ ME ME -- ++
                -- MS MB MS -- ++ ++ -- -- ++ --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 20 50 50 50 50 50 50
                10 10 10 10 10 20 50 50 50 50 50
                20 10 10 10 20 20 50 50 50 50 50
                20 20 20 20 20 50 50 50 50 50 50
                20 20 20 20 50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.119, 1.14),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.082, 1.102),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.05, 1.069),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default'],
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'sp': Stage(
        map=dict(
            name='SP',
            shape='I10',
            camera_data=['E6', 'E8'],
            camera_data_spawn_point=['E8'],
            map_data="""
                -- -- -- -- -- -- -- -- --
                -- ++ -- ++ ++ ++ -- ++ --
                ++ -- -- ++ ++ ++ -- -- --
                -- -- -- ++ ++ ++ -- -- ++
                -- -- ME -- MB -- ME -- --
                -- ME -- MS -- MS -- ME ++
                -- ++ ME -- MS -- ME ++ ++
                -- ++ -- -- __ -- -- ++ ++
                ++ ME -- SP -- SP -- ME --
                -- -- ME ++ ++ ++ ME -- --
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
                50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 10, 'siren': 3},
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
            MAP_SIREN_TEMPLATE=['RoyalOak', 'Victorious'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=False,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_CHAPTER_SWITCH_20241219=True,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_IS_ONE_TIME_STAGE=True,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (120, 238),
                'width': (1.5, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (238, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_STORAGE=((9, 6), [(205.118, 96.796), (1192.803, 96.796), (71.385, 634.321), (1407.083, 634.321)]),
            HOMO_EDGE_COLOR_RANGE=(0, 17),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_HAS_MOVABLE_NORMAL_ENEMY=True,
            MAP_SIREN_MOVE_WAIT=0.5,
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.014, 1.033),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.981, 0.999),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.952, 0.97),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=2)', 'battle_default'],
            5: PLAN,
            7: 'fleet_boss.clear_boss',
        },
    ),
}
