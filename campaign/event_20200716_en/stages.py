"""
Stages of event_20200716_en, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

PLAN = [('do', 'fleet_boss.capture_clear_boss')]
PLAN_2 = ['clear_siren', 'battle_default']

STAGES = {
    'a2': Stage(
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
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='campaign.event_20200716_en.a1:Config',
        battle={
            0: PLAN_2,
            4: PLAN,
        },
    ),
    'a3': Stage(
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
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
                {'battle': 5, 'enemy': 1},
            ],
        ),
        config_base='campaign.event_20200716_en.a1:Config',
        battle={
            0: PLAN_2,
            4: PLAN,
        },
    ),
    'b2': Stage(
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
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
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
        config_base='campaign.event_20200716_en.b1:Config',
        config=dict(
            MAP_SIREN_COUNT=2,
        ),
        battle={
            0: PLAN_2,
            5: PLAN,
        },
    ),
    'c2': Stage(
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
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='campaign.event_20200716_en.c1:Config',
        battle={
            0: PLAN_2,
            4: PLAN,
        },
    ),
    'c3': Stage(
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
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10
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
        config_base='campaign.event_20200716_en.c1:Config',
        battle={
            0: PLAN_2,
            5: PLAN,
        },
    ),
    'c4': Stage(
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
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
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
        config_base='campaign.event_20200716_en.c1:Config',
        battle={
            0: PLAN_2,
            5: PLAN,
        },
    ),
    'd2': Stage(
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
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10
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
        config_base='campaign.event_20200716_en.d1:Config',
        battle={
            0: PLAN_2,
            6: PLAN,
        },
    ),
}
