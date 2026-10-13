"""
Stages of war_archives_20181026_en, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '..campaign_war_archives.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']
PLAN_2 = [
    ('do', 'clear_all_mystery'),
    'clear_siren',
    'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)',
    'battle_default',
]
PLAN_3 = ['clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']

STAGES = {
    'a1': Stage(
        base=BASE,
        map=dict(
            name='A1',
            shape='H6',
            camera_data=['D2', 'D4', 'E2', 'E4'],
            camera_data_spawn_point=['D2', 'D4'],
            map_data="""
                ++ ++ ++ -- ME -- ++ ++
                SP -- -- ME ++ -- ++ ++
                -- -- -- -- __ -- -- --
                -- -- ME -- -- Me -- ME
                SP -- -- -- -- -- -- --
                -- -- ME ++ -- ME -- MB
            """,
            weight_data="""
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'boss': 1},
                {'battle': 4},
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
            0: PLAN_3,
            3: 'clear_boss',
        },
    ),
    'a2': Stage(
        base=BASE,
        map=dict(
            name='A2',
            shape='I6',
            camera_data=['E2', 'E4', 'F2', 'F4'],
            camera_data_spawn_point=['E4'],
            map_data="""
                ++ ++ ++ -- ME -- MS -- ++
                ++ -- ME -- -- -- ++ ME ++
                -- -- -- Me -- __ -- -- MB
                -- Me -- -- -- Me -- -- --
                ++ -- ME -- SP ++ MB ME MB
                ++ -- -- SP -- -- ++ ++ ++
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
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DD'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'a3': Stage(
        base=BASE,
        map=dict(
            name='A3',
            shape='J7',
            camera_data=['D2', 'D5', 'G2', 'G5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                MB -- ME ++ ++ ++ -- MS -- MB
                ++ -- -- -- -- ME -- -- -- --
                -- ME -- -- Me -- __ ME ++ --
                -- -- MS -- -- -- Me -- -- ME
                ++ ++ ++ ME __ -- -- -- -- --
                SP -- -- -- -- ME -- ++ -- --
                SP -- -- -- ME ++ -- ++ -- MB
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DD'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b1': Stage(
        base=BASE,
        map=dict(
            name='B1',
            shape='J6',
            camera_data=['D2', 'D4', 'G2', 'G4'],
            camera_data_spawn_point=['D2', 'D4'],
            map_data="""
                -- -- -- ME ++ ++ ++ ME -- MB
                -- -- __ -- Me -- -- -- __ --
                ++ Me SP -- -- -- Me MS Me ++
                ME -- -- ++ -- ME MS ME -- ++
                -- -- SP ++ -- -- -- -- -- --
                -- SP ++ ++ ++ ++ MB -- ME MB
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['DD'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b2': Stage(
        base=BASE,
        map=dict(
            name='B2',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- ME -- -- ME ++ ++ ME -- --
                ME MB ++ -- -- MS ++ -- MB ++
                -- -- -- Me -- -- -- -- -- --
                -- Me -- -- -- Me -- -- Me --
                ++ ++ ++ -- ME -- ME -- -- --
                ++ SP SP -- __ ME ++ -- -- ME
                ++ SP SP -- -- MS ++ -- MB ++
                ++ ++ ++ ME -- -- -- ME ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DD', 'CL'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'b3': Stage(
        base=BASE,
        map=dict(
            name='B3',
            shape='L9',
            camera_data=['D2', 'D6', 'D7', 'I2', 'I6', 'I7'],
            camera_data_spawn_point=['D7'],
            map_data="""
                -- -- -- ++ ++ ++ ME -- ME MM ++ ++
                -- -- -- -- MB ME -- Me ++ ME ++ ++
                -- -- Me -- -- -- -- __ -- MS -- ME
                -- -- -- MS -- -- ME -- -- -- MM --
                -- ME MB ++ -- Me ++ -- -- ME -- --
                ++ ++ ++ ME -- -- ME -- ++ -- MB --
                SP -- -- -- -- -- -- __ ++ -- -- --
                -- SP -- -- -- Me MS -- -- -- ME --
                -- -- SP -- -- ++ ME -- -- ME -- ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 1, 'siren': 1},
                {'battle': 2, 'enemy': 1, 'mystery': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DD', 'CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c1': Stage(
        base=BASE,
        map=dict(
            name='C1',
            shape='H6',
            camera_data=['D2', 'D4', 'E2', 'E4'],
            camera_data_spawn_point=['D2', 'D4'],
            map_data="""
                ++ ++ ++ -- ME -- ++ ++
                SP -- -- ME ++ -- ++ ++
                -- -- -- -- __ -- -- --
                -- -- ME -- -- Me -- ME
                SP -- -- -- -- -- -- --
                -- -- ME ++ -- ME -- MB
            """,
            weight_data="""
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2},
                {'battle': 3},
                {'battle': 4, 'boss': 1},
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
            0: PLAN_3,
            4: 'clear_boss',
        },
    ),
    'c2': Stage(
        base=BASE,
        map=dict(
            name='C2',
            shape='I6',
            camera_data=['E2', 'E4', 'F2', 'F4'],
            camera_data_spawn_point=['E4'],
            map_data="""
                ++ ++ ++ -- ME -- MS -- ++
                ++ -- ME -- -- -- ++ ME ++
                -- -- -- Me -- __ -- -- MB
                -- Me -- -- -- Me -- -- --
                ++ -- ME -- SP ++ MB ME MB
                ++ -- -- SP -- -- ++ ++ ++
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
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DD'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'c3': Stage(
        base=BASE,
        map=dict(
            name='C3',
            shape='J7',
            camera_data=['D2', 'D5', 'G2', 'G5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                MB -- ME ++ ++ ++ -- MS -- MB
                ++ -- -- -- -- ME -- -- -- --
                -- ME -- -- Me -- __ ME ++ --
                -- -- MS -- -- -- Me -- -- ME
                ++ ++ ++ ME __ -- -- -- -- --
                SP -- -- -- -- ME -- ++ -- --
                SP -- -- -- ME ++ -- ++ -- MB
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DD'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd1': Stage(
        base=BASE,
        map=dict(
            name='D1',
            shape='J6',
            camera_data=['D2', 'D4', 'G2', 'G4'],
            camera_data_spawn_point=['D2', 'D4'],
            map_data="""
                -- -- -- ME ++ ++ ++ ME -- MB
                -- -- __ -- Me -- -- -- __ --
                ++ Me SP -- -- -- Me MS Me ++
                ME -- -- ++ -- ME MS ME -- ++
                -- -- SP ++ -- -- -- -- -- --
                -- SP ++ ++ ++ ++ MB -- ME MB
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['DD'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd2': Stage(
        base=BASE,
        map=dict(
            name='D2',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- ME -- -- ME ++ ++ ME -- --
                ME MB ++ -- -- MS ++ -- MB ++
                -- -- -- Me -- -- -- -- -- --
                -- Me -- -- -- Me -- -- Me --
                ++ ++ ++ -- ME -- ME -- -- --
                ++ SP SP -- __ ME ++ -- -- ME
                ++ SP SP -- -- MS ++ -- MB ++
                ++ ++ ++ ME -- -- -- ME ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4},
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DD', 'CL'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default'],
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        base=BASE,
        map=dict(
            name='D3',
            shape='L9',
            camera_data=['D2', 'D6', 'D7', 'I2', 'I6', 'I7'],
            camera_data_spawn_point=['D7'],
            map_data="""
                -- -- -- ++ ++ ++ ME -- ME MM ++ ++
                -- -- -- -- MB ME -- Me ++ ME ++ ++
                -- -- Me -- -- -- -- __ -- MS -- ME
                -- -- -- MS -- -- ME -- -- -- MM --
                -- ME MB ++ -- Me ++ -- -- ME -- --
                ++ ++ ++ ME -- -- ME -- ++ -- MB --
                SP -- -- -- -- -- -- __ ++ -- -- --
                -- SP -- -- -- Me MS -- -- -- ME --
                -- -- SP -- -- ++ ME -- -- ME -- ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 4, 'siren': 2},
                {'battle': 1, 'enemy': 1, 'siren': 1},
                {'battle': 2, 'enemy': 1, 'mystery': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DD', 'CL', 'CA'],
            MOVABLE_ENEMY_TURN=(2, 3),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: [
                ('do', 'clear_all_mystery'),
                'clear_siren',
                'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)',
                'battle_default',
            ],
            5: PLAN_2,
            6: 'fleet_boss.clear_boss',
        },
    ),
}
