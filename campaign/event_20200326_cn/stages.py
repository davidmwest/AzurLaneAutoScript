"""
Stages of event_20200326_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

PLAN = ['clear_siren', 'clear_enemy(scale=(3,))', 'battle_default']

STAGES = {
    'a2': Stage(
        map=dict(
            shape='F8',
            map_data="""
                -- ME -- ME ME ME
                -- ME -- -- MS --
                ++ ++ ++ ME -- --
                SP -- -- -- -- SP
                ME -- -- -- ++ ++
                -- MS ME __ ++ ++
                ME -- ++ -- -- MB
                -- ME -- ME MB MB
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='campaign.event_20200326_cn.a1:Config',
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'a3': Stage(
        map=dict(
            shape='G7',
            map_data="""
                ++ ++ ME ME ME ++ --
                ++ MS -- ME -- MS ++
                ME -- -- __ -- -- ME
                ME -- SP MB SP -- ME
                ME -- -- MB -- -- ME
                -- MS -- MB ++ ++ ++
                ++ -- ME -- ME -- --
            """,
            weight_data="""
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 10 10 10 10
                10 10 10 20 20 20 20
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='campaign.event_20200326_cn.a1:Config',
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b1': Stage(
        map=dict(
            shape='H7',
            map_data="""
                -- ME -- ME ++ ++ SP SP
                ME -- MS -- ME -- -- SP
                ++ ME -- -- -- -- -- --
                ++ ME -- -- MS -- ME ++
                ME -- __ ME ++ -- -- --
                MB -- -- MS ++ -- ME ME
                MB MB ME -- ME -- ME --
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='campaign.event_20200326_cn.a1:Config',
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b2': Stage(
        map=dict(
            shape='F9',
            map_data="""
                ME ME MS MS ME ME
                ME -- -- -- -- ME
                ++ ++ -- -- ++ ++
                ++ ++ SP SP ME ++
                MS -- -- -- -- MS
                ME -- MB MB __ ME
                -- ME ++ ++ -- ME
                -- ME ++ ME -- ME
                -- -- ME -- -- ME
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
        config_base='campaign.event_20200326_cn.a1:Config',
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'b3': Stage(
        map=dict(
            shape='G9',
            map_data="""
                ME -- ME -- ME -- ME
                ++ -- -- ME -- -- ++
                ++ -- ++ ++ ++ -- ++
                MS -- MB MB MB -- MS
                ME ME -- __ -- ME ME
                ++ ++ SP -- SP ++ ++
                ++ ME -- -- -- ME ++
                ME -- -- ME -- -- ME
                -- MS ME -- ME MS --
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
        config_base='campaign.event_20200326_cn.a1:Config',
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        map=dict(
            shape='G9',
            map_data="""
                ME -- ME -- ME -- ME
                ++ -- -- ME -- -- ++
                ++ -- ++ ++ ++ -- ++
                MS -- MB MB MB -- MS
                ME ME -- __ -- ME ME
                ++ ++ SP -- SP ++ ++
                ++ ME -- -- -- ME ++
                ME -- -- ME -- -- ME
                -- MS ME -- ME MS --
            """,
            camera_data=['D3', 'D5', 'D7'],
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'enemy': 1, 'boss': 1},
            ],
            in_map_swipe_preset_data=(0, 2),
        ),
        config=dict(
            MAP_HAS_AMBUSH=False,
            CAMPAIGN_MODE='hard',
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (100, 220),
                'width': 1,
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (175, 255),
                'prominence': 2,
                'distance': 50,
                'wlen': 1000,
            },
        ),
        battle={
            0: PLAN,
            5: ['clear_enemy(scale=(1,))', 'clear_enemy(scale=(2,))', 'battle_default'],
            6: 'fleet_boss.clear_boss',
        },
    ),
}
