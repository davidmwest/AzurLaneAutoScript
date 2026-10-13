"""
Stages of war_archives_20181020_en, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '..campaign_war_archives.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']

STAGES = {
    'sp1': Stage(
        base=BASE,
        map=dict(
            name='SP.1',
            shape='G3',
            camera_data=['D1'],
            camera_data_spawn_point=['D1'],
            map_data="""
                SP ++ ++ ++ -- -- MB
                -- Me -- -- ME ++ ++
                SP ++ ++ ++ -- ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
            """,
            spawn_data=[{'battle': 0, 'enemy': 1, 'mystery': 1}, {'battle': 1, 'enemy': 1}, {'battle': 2, 'boss': 1}],
        ),
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=True,
            MAP_HAS_MYSTERY=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            2: 'clear_boss',
        },
    ),
    'sp2': Stage(
        base=BASE,
        map=dict(
            name='SP.2',
            shape='G5',
            camera_data=['D2', 'D3'],
            camera_data_spawn_point=['D3'],
            map_data="""
                -- ++ -- ME Me MB ++
                -- Me ME -- -- ++ ++
                -- -- ++ ++ Me ME ME
                SP ME ++ ++ -- ME --
                -- SP Me -- Me -- MB
            """,
            weight_data="""
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'mystery': 1},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=True,
            MAP_HAS_MYSTERY=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'sp3': Stage(
        base=BASE,
        map=dict(
            name='SP.3',
            shape='H5',
            camera_data=['D2', 'D3', 'E2', 'E3'],
            camera_data_spawn_point=['D3', 'D2'],
            map_data="""
                ++ ME SP ME ME -- ++ ++
                SP Me -- -- -- ME ++ ++
                ME -- ++ -- ME -- Me ME
                -- ME ++ MM -- Me -- MB
                SP -- ++ ++ ++ -- ME MB
            """,
            weight_data="""
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'mystery': 1},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=True,
            MAP_HAS_MYSTERY=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
