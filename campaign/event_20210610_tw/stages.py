"""
Stages of event_20210610_tw, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage


STAGES = {
    'sp1': Stage(
        map=dict(
            name='SP1',
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['E5', 'D5'],
            map_data="""
                -- ++ ++ MB MB ++ ++ ++
                ME ++ Me -- -- ME Me --
                -- -- __ -- ME __ -- --
                ME -- ME -- -- -- ME --
                -- -- ++ ME -- Me ++ ME
                ME -- -- SP SP -- -- --
                ++ ++ -- -- -- -- ME ++
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
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: 'battle_default',
            4: 'clear_boss',
        },
    ),
    'sp2': Stage(
        map=dict(
            name='SP2',
            shape='K6',
            camera_data=['D2', 'D4', 'H2', 'H4'],
            camera_data_spawn_point=['D4'],
            map_data="""
                -- -- ++ ++ -- Me -- ++ ++ ME --
                Me ME ++ ++ ME -- ME -- ME -- ME
                -- -- MB -- MB -- -- -- -- -- --
                ++ -- -- MB -- __ Me ++ ++ ME ++
                SP -- Me -- ME -- -- ++ ME -- ME
                SP SP ++ ++ ++ ME -- -- -- -- ME
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
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: 'battle_default',
            4: 'clear_boss',
        },
    ),
    'sp3': Stage(
        map=dict(
            name='SP3',
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ ++ ++ ME ME ++ MB MB
                ME -- -- -- -- ME -- MB
                -- -- Me Me -- __ -- ++
                ME -- ++ ++ -- Me -- ME
                -- -- SP SP -- ++ -- ME
                ME -- -- -- ME ++ ME --
                ++ ++ Me -- -- -- -- ME
                ++ ME Me -- ME ++ ME --
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
                {'battle': 1, 'enemy': 2, 'siren': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: 'battle_default',
            5: 'fleet_boss.clear_boss',
        },
    ),
}
