"""
Stages of event_20210415_tw, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage


STAGES = {
    'sp1': Stage(
        map=dict(
            name='SP1',
            shape='H6',
            camera_data=['D2', 'D4', 'E2', 'E4'],
            camera_data_spawn_point=['D4'],
            map_data="""
                ++ ++ ++ -- -- ME -- MB
                -- -- -- Me ME -- ME --
                -- -- ME -- ++ Me ++ ++
                -- ++ -- Me ME -- -- ++
                -- -- -- ++ -- ME ME --
                SP SP SP ++ -- ME -- MB
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
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=True,
        ),
        battle={
            0: 'battle_default',
            4: 'clear_boss',
        },
    ),
    'sp2': Stage(
        map=dict(
            name='SP2',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                ++ ++ ++ -- -- -- ME MB ME
                ++ -- -- Me -- ME -- ME --
                ++ -- ME -- ME -- ++ -- ME
                SP -- -- ++ ++ MB -- Me --
                SP -- ME MM ++ ME ME ME MB
                SP -- -- ME -- Me -- ++ ++
                ++ -- -- -- ME -- -- ++ ++
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
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1, 'mystery': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=True,
        ),
        battle={
            0: 'battle_default',
            4: 'clear_boss',
        },
    ),
    'sp3': Stage(
        map=dict(
            name='SP3',
            shape='J7',
            camera_data=['D2', 'D5', 'G2', 'G5'],
            camera_data_spawn_point=['G5', 'D5'],
            map_data="""
                ++ ++ ++ ++ ++ ME -- MB ++ ++
                ++ ++ -- MB ME -- ME -- MM ++
                ME -- Me -- ME -- ++ -- ME --
                -- ME -- ++ SP SP -- Me -- ME
                MB ME ME ++ SP SP ME -- ME --
                ++ ME -- -- Me ++ -- ME ME MB
                ++ -- -- ME -- ME -- ++ ++ ++
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
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1, 'mystery': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=True,
        ),
        battle={
            0: 'battle_default',
            5: 'fleet_boss.clear_boss',
        },
    ),
}
