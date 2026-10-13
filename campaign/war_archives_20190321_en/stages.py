"""
Stages of war_archives_20190321_en, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '..campaign_war_archives.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_filter_enemy(self.ENEMY_FILTER, preserve=2)', 'battle_default']
PLAN_2 = ['clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']

STAGES = {
    'b3': Stage(
        base=BASE,
        map=dict(
            name='B3',
            shape='F10',
            camera_data=['C2', 'C6', 'C8'],
            camera_data_spawn_point=['C8'],
            map_data="""
                ++ ++ ++ ++ ++ ++
                ++ MB ++ ++ MB ++
                ++ -- ++ ++ -- ++
                ++ ME ME ME ME ++
                ++ ME ME ME ME ++
                -- Me ME ME Me --
                ME ++ ++ ++ ++ Me
                Me ME -- -- ME Me
                -- -- SP SP -- --
                ++ ++ ++ ++ ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50
                50 10 50 50 10 50
                50 10 50 50 10 50
                50 10 40 40 10 50
                50 20 40 40 20 50
                50 30 20 20 30 50
                20 50 50 50 50 20
                20 20 50 50 20 20
                50 50 50 50 50 50
                50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 4},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'enemy': 1},
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=True,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: PLAN_2,
            7: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        base=BASE,
        map=dict(
            name='D3',
            shape='F10',
            camera_data=['C2', 'C6', 'C8'],
            camera_data_spawn_point=['C8'],
            map_data="""
                ++ ++ ++ ++ ++ ++
                ++ MB ++ ++ MB ++
                ++ -- ++ ++ -- ++
                ++ ME ME ME ME ++
                ++ ME ME ME ME ++
                -- Me ME ME Me --
                ME ++ ++ ++ ++ Me
                Me ME -- -- ME Me
                -- -- SP SP -- --
                ++ ++ ++ ++ ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50
                50 10 50 50 10 50
                50 10 50 50 10 50
                50 10 40 40 10 50
                50 20 40 40 20 50
                50 30 20 20 30 50
                20 50 50 50 50 20
                20 20 50 50 20 20
                50 50 50 50 50 50
                50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 4},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'enemy': 1},
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=True,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: PLAN_2,
            7: 'fleet_boss.clear_boss',
        },
    ),
}
