"""
Stages of event_20200423_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage


STAGES = {
    'a2': Stage(
        map=dict(
            map_data="""
                -- -- -- -- -- -- --
                -- -- -- ++ ++ ++ --
                -- -- -- -- -- -- --
                -- -- ++ -- -- -- --
                -- -- -- -- -- -- --
                SP -- -- -- -- ++ --
                SP SP -- -- -- ++ --
            """,
        ),
        config_base='campaign.event_20200423_cn.a1:Config',
    ),
    'a3': Stage(
        map=dict(
            map_data="""
                SP SP -- -- -- -- -- -- --
                SP -- -- -- ++ ++ ++ -- --
                -- -- -- -- -- -- -- -- --
                -- ++ -- -- -- -- -- -- --
                -- ++ -- -- ++ ++ -- -- --
                -- -- -- -- -- -- -- ++ ++
                -- -- -- -- -- -- -- ++ ++
            """,
        ),
        config_base='campaign.event_20200423_cn.a1:Config',
    ),
    'b2': Stage(
        map=dict(
            map_data="""
                -- -- -- -- SP SP -- -- ++ ++
                -- -- -- -- -- -- -- -- ++ ++
                ++ ++ ++ -- -- -- -- -- -- --
                -- -- -- -- ++ ++ -- -- -- --
                -- -- -- -- -- -- -- -- -- --
                -- ++ -- -- -- -- ++ -- -- --
                -- ++ -- -- -- -- -- -- -- --
            """,
        ),
        config_base='campaign.event_20200423_cn.b1:Config',
        config=dict(
            FLEET_BOSS=2,
        ),
    ),
    'b3': Stage(
        map=dict(
            map_data="""
                -- -- -- -- -- -- -- -- --
                -- -- -- -- -- -- -- ++ ++
                ++ ++ -- -- ++ ++ -- -- --
                -- -- -- -- ++ ++ -- -- SP
                ++ ++ -- -- -- -- -- -- SP
                -- -- -- -- -- -- -- ++ --
                -- -- ++ ++ ++ -- -- -- --
            """,
        ),
        config_base='campaign.event_20200423_cn.b1:Config',
        config=dict(
            FLEET_BOSS=2,
        ),
    ),
    'c2': Stage(
        map=dict(
            map_data="""
                -- -- ME -- ME -- MB
                ME -- -- ++ ++ ++ --
                -- ME __ -- ME ME --
                ME -- ++ MS -- -- --
                -- -- -- -- -- -- --
                SP -- -- -- ME ++ --
                SP SP -- ME -- ++ MB
            """,
            camera_data=['D3', 'D5'],
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='campaign.event_20200423_cn.c1:Config',
        battle={
            0: ['clear_siren', 'clear_enemy(scale=(1, 2))', 'battle_default'],
            4: 'brute_clear_boss',
        },
    ),
    'c3': Stage(
        map=dict(
            map_data="""
                SP SP -- -- -- -- -- -- --
                SP -- -- -- ++ ++ ++ -- --
                -- -- -- -- -- -- -- -- --
                -- ++ -- -- -- -- -- -- --
                -- ++ -- -- ++ ++ -- -- --
                -- -- -- -- -- -- -- ++ ++
                -- -- -- -- -- -- -- ++ ++
            """,
        ),
        config_base='campaign.event_20200423_cn.c1:Config',
        config=dict(
            FLEET_BOSS=2,
        ),
    ),
    'd2': Stage(
        map=dict(
            map_data="""
                -- -- -- -- SP SP -- -- ++ ++
                -- -- -- -- -- -- -- -- ++ ++
                ++ ++ ++ -- -- -- -- -- -- --
                -- -- -- -- ++ ++ -- -- -- --
                -- -- -- -- -- -- -- -- -- --
                -- ++ -- -- -- -- ++ -- -- --
                -- ++ -- -- -- -- -- -- -- --
            """,
        ),
        config_base='campaign.event_20200423_cn.d1:Config',
        config=dict(
            FLEET_BOSS=2,
        ),
    ),
    'd3': Stage(
        map=dict(
            map_data="""
                MS -- -- ME -- MS -- ME --
                -- ME -- -- __ ME -- ++ ++
                ++ ++ -- ME ++ ++ ME -- ME
                MB -- -- -- ++ ++ -- -- SP
                ++ ++ -- -- -- -- -- -- SP
                ME -- ME ME ME -- -- ++ --
                -- ME ++ ++ ++ MS ME -- --
            """,
            weight_data="""
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                20 20 10 10 10 10 10 10 10
                20 20 10 10 10 10 10 10 10
            """,
            camera_data=['D3', 'D5', 'F3', 'F5'],
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
        config_base='campaign.event_20200423_cn.d1:Config',
        config=dict(
            FLEET_BOSS=2,
        ),
        battle={
            0: ['clear_siren', 'clear_enemy(scale=(2, 3))', 'battle_default'],
            5: ['clear_enemy(scale=(1,))', 'clear_enemy(scale=(2,))', 'battle_default'],
            6: 'fleet_boss.clear_boss',
        },
    ),
}
