"""
Stages of war_archives_20211111_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '..campaign_war_archives.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']

STAGES = {
    'sp1': Stage(
        base=BASE,
        map=dict(
            name='SP1',
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                ME -- ME ++ ++ ++ MB MB
                ++ -- ME Me __ -- -- MB
                -- Me -- -- Me Me ME --
                -- ME ++ -- ME ++ ++ --
                ME -- ++ MS -- ME -- --
                -- -- -- ++ -- -- -- ME
                SP SP -- -- -- ME ME ++
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
                {'battle': 0, 'enemy': 3, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MAP_HAS_SIREN=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
            MAP_SWIPE_MULTIPLY=(1.122, 1.143),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.085, 1.105),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.054, 1.073),
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
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                ++ -- -- -- ME -- MB ++ ++
                ME -- MS -- -- -- ME MB ++
                -- -- ++ ++ ++ __ -- -- MB
                -- Me ++ MS -- Me -- ++ ++
                -- -- -- -- ME -- Me ME --
                ME -- ME ME ++ ME -- -- ME
                SP SP -- -- ++ ++ ME ME ME
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
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MAP_HAS_SIREN=True,
            MAP_HAS_MAP_STORY=True,
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
    'sp3': Stage(
        base=BASE,
        map=dict(
            name='SP3',
            shape='I8',
            camera_data=['D3', 'D6', 'F3', 'F6'],
            camera_data_spawn_point=['F6'],
            map_data="""
                ++ ++ ++ ++ ME ME -- -- ME
                MB MB MB ++ -- -- -- ME --
                -- ME -- ME Me ++ MS -- ++
                ME MS -- __ ME -- ME -- ++
                ++ ++ ++ -- -- ++ ++ -- ME
                ME ME MS Me -- ++ ++ ME --
                -- -- -- -- -- SP SP -- --
                Me ME ++ ME -- -- -- -- ME
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=[],
            MAP_HAS_SIREN=True,
            MAP_HAS_MAP_STORY=True,
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
