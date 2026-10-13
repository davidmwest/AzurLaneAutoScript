"""
Stages of war_archives_20190314_en, see module/campaign/stage.py
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
            name='SP1',
            shape='H5',
            camera_data=['D2', 'D3', 'E2', 'E3'],
            camera_data_spawn_point=['D3'],
            map_data="""
                ++ ++ ++ -- ME ME MB ++
                -- -- -- Me -- ME -- --
                -- -- ++ -- Me ++ MB --
                SP SP -- ME -- ++ -- ME
                SP SP -- -- ME -- Me --
            """,
            weight_data="""
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
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'sp2': Stage(
        base=BASE,
        map=dict(
            name='SP2',
            shape='G7',
            camera_data=['D2', 'D5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                ++ ++ -- ME -- ME MB
                MM ++ -- -- ME -- MB
                ME -- Me -- ++ ++ ++
                -- -- -- Me -- ME MB
                -- -- ++ -- ++ ME --
                SP SP -- -- ++ -- ME
                ++ SP -- Me -- ME --
            """,
            weight_data="""
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'mystery': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
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
            name='SP3',
            shape='I6',
            camera_data=['D2', 'D4', 'F2', 'F4'],
            camera_data_spawn_point=['F4'],
            map_data="""
                ++ MB -- ME -- Me -- ++ ++
                MB -- ME -- ++ -- ME ++ ++
                MB ME -- Me -- ME -- ME --
                ++ ++ ++ -- ME -- Me ++ --
                MB -- ME Me -- ++ -- -- SP
                -- ME -- -- -- ++ -- SP SP
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
