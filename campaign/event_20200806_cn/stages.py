"""
Stages of event_20200806_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

PLAN = ['clear_siren', 'battle_default']

STAGES = {
    'sp1': Stage(
        map=dict(
            name='SP1',
            shape='H6',
            camera_data=['D3', 'D4'],
            camera_data_spawn_point=['D3', 'D4'],
            map_data="""
                ++ ++ ++ -- MS ME -- --
                -- ME -- Me -- -- ME --
                SP -- ME -- -- Me ++ ++
                -- ME -- __ -- -- MB ++
                SP -- -- ++ -- ME -- --
                -- -- Me -- MS -- ME --
            """,
            weight_data="""
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Amazon'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(1.139, 1.161),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.102, 1.122),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.07, 1.089),
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 215),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
        ),
        battle={
            0: PLAN,
            4: 'fleet_1.clear_boss',
        },
    ),
    'sp2': Stage(
        map=dict(
            name='SP2',
            shape='I7',
            camera_data=['D3', 'D5', 'F3', 'F5'],
            camera_data_spawn_point=['D3'],
            map_data="""
                -- -- -- -- -- -- ME -- ++
                -- ME ++ MS -- ME -- MS ++
                -- -- ME -- ME -- -- -- --
                SP -- -- -- -- __ -- -- MB
                SP -- ME -- ++ ME ME -- --
                -- ++ -- ME ++ Me -- ++ ++
                -- Me ME -- ME -- MS ++ ++
            """,
            weight_data="""
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN,
            4: 'fleet_1.clear_boss',
        },
    ),
    'sp3': Stage(
        map=dict(
            name='SP3',
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['E5'],
            map_data="""
                -- ME ++ ++ ++ MS -- --
                -- ME -- MB ME -- ME ME
                ME -- MS -- -- MS ME --
                ++ MS -- ++ -- __ -- ++
                ++ ME ME -- -- Me ME ++
                -- Me ++ ++ -- -- Me ME
                ME -- ++ ++ SP SP -- --
            """,
            weight_data="""
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2, 'siren': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Amazon'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
