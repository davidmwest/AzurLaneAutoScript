"""
Stages of event_20200507_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage


STAGES = {
    'sp2': Stage(
        map=dict(
            map_data="""
                -- -- ++ ++ -- ME -- ++ ++ ME --
                ME ME ++ ++ ME -- ME -- ME -- ME
                ME -- MB -- MB -- -- -- -- -- --
                ++ -- MB MB -- __ ME ++ ++ ME ++
                SP -- ME -- ME -- -- ++ ME -- ME
                SP SP ++ ++ ++ ME -- -- -- -- ME
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='campaign.event_20200507_cn.sp1:Config',
        battle={
            0: 'battle_default',
            4: 'brute_clear_boss',
        },
    ),
    'sp3': Stage(
        map=dict(
            map_data="""
                ++ ++ ++ ME ME ++ MB MB
                ME -- -- -- -- ME -- MB
                -- -- ME ME -- __ -- ++
                ME -- ++ ++ -- ME -- ME
                -- -- SP SP -- ++ -- ME
                ME -- -- -- ME ++ ME --
                ++ ++ ME -- -- -- -- ME
                ++ ME ME -- ME ++ ME --
            """,
            camera_data=['D3', 'D6'],
            spawn_data=[
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='campaign.event_20200507_cn.sp1:Config',
        config=dict(
            FLEET_BOSS=2,
        ),
        battle={
            0: ['clear_enemy(scale=(2,))', 'clear_enemy(scale=(1,))', 'battle_default'],
            5: 'brute_clear_boss',
        },
    ),
}
