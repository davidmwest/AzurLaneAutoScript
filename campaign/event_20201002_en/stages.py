"""
Stages of event_20201002_en, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

PLAN = ['clear_siren', 'battle_default']

STAGES = {
    'sp1': Stage(
        map=dict(
            name='SP1',
            shape='K7',
            camera_data=['D2', 'D5', 'H2', 'H5'],
            camera_data_spawn_point=['H5'],
            map_data="""
                ++ ++ ++ -- ME -- -- -- -- ++ --
                -- ME -- ++ -- ++ ++ ME -- ++ ME
                ME -- -- Me -- ME ++ -- Me ++ --
                -- -- -- -- -- ++ ME -- -- -- SP
                ME -- -- Me -- -- -- __ -- -- SP
                -- -- ME ++ -- MS -- Me -- -- --
                -- -- -- ++ MB -- MB ++ ++ ++ ++
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
                {'battle': 4, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Z18'],
            MOVABLE_ENEMY_TURN=(3,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'sp2': Stage(
        map=dict(
            name='SP2',
            shape='K7',
            camera_data=['D2', 'D5', 'H2', 'H5'],
            camera_data_spawn_point=['D2', 'H2'],
            map_data="""
                -- -- ++ ++ SP -- SP ++ ++ ++ ++
                -- ME ++ ++ -- -- -- -- -- ME ME
                ME -- -- MS -- -- -- ME -- -- MB
                ++ -- -- -- Me -- Me ++ __ -- MB
                -- -- ++ ++ ++ MS -- ++ -- -- ME
                -- ME -- ME ++ -- -- -- -- Me ++
                -- -- -- -- Me -- ME -- ME -- ++
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
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Z2'],
            MOVABLE_ENEMY_TURN=(3,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'sp3': Stage(
        map=dict(
            name='SP3',
            shape='K7',
            camera_data=['D2', 'D5', 'H2', 'H5'],
            camera_data_spawn_point=['D2'],
            map_data="""
                ++ ++ ++ MS ++ ME -- ME ++ ++ ++
                SP -- -- -- -- -- MS -- ME Me --
                SP -- -- -- -- Me -- __ -- -- ME
                ++ ++ ++ MS -- ++ ++ -- Me ++ --
                MB MB ++ -- Me ++ ++ -- -- ++ ++
                -- -- -- -- -- -- -- -- -- ME --
                ME ME -- Me -- ME ++ ME -- ME --
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
                {'battle': 1, 'enemy': 2, 'siren': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Z19'],
            MOVABLE_ENEMY_TURN=(3,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
