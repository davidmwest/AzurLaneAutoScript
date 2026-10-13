"""
Stages of event_20250814_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']
PLAN_2 = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default']

STAGES = {
    'ht1': Stage(
        base=BASE,
        map=dict(
            name='HT1',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['F2'],
            map_data="""
                -- -- -- ++ ++ -- -- SP --
                ++ ME ME ++ ++ MS -- -- SP
                ++ -- -- -- Me -- __ -- --
                -- -- ME -- -- -- -- MS ++
                MB -- ++ ++ ++ Me -- -- ME
                -- -- ME -- ME -- -- Me --
                -- ME -- ME -- -- ++ -- --
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
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Jiulaimu_Mud', 'Jiulaimu_Statue', 'Jiulaimu_Demon'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_CHAPTER_SWITCH_20241219=True,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_HAS_MODE_SWITCH=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 222),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (222, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            MAP_SWIPE_MULTIPLY=(1.267, 1.29),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.225, 1.248),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.189, 1.211),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'ht2': Stage(
        base=BASE,
        map=dict(
            name='HT2',
            shape='G10',
            camera_data=['C5', 'C8'],
            camera_data_spawn_point=['C2'],
            map_data="""
                -- -- SP -- SP -- --
                -- -- -- -- -- -- --
                ++ ++ -- MS -- ++ ++
                -- ++ MS -- MS ++ --
                -- Me -- __ -- Me --
                -- -- Me -- Me -- --
                ++ ++ ++ -- ++ ++ ++
                -- -- ME -- ME -- --
                -- ME -- MB -- ME --
                -- -- ME -- ME -- --
            """,
            weight_data="""
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='ht1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Jiulaimu_Mud', 'Jiulaimu_Statue', 'Jiulaimu_Demon'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.222, 1.245),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.182, 1.204),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.148, 1.168),
            MAP_WALK_USE_CURRENT_FLEET=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'ht3': Stage(
        base=BASE,
        map=dict(
            name='HT3',
            shape='J6',
            camera_data=['D2', 'D4', 'G2', 'G4'],
            camera_data_spawn_point=['D2'],
            map_data="""
                ++ ++ ++ -- MB ++ ME -- -- --
                SP -- -- MS -- Me -- ME -- ++
                SP -- -- MS __ -- -- -- ME ++
                ++ -- MS -- -- Me -- -- -- ME
                ++ -- -- -- ME ++ ++ -- ME --
                -- Me ++ Me -- ++ ++ ME -- --
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
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='ht1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Jiulaimu_Mud', 'Jiulaimu_Statue', 'Jiulaimu_Demon'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.193, 1.216),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.154, 1.175),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.12, 1.141),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'ht4': Stage(
        base=BASE,
        map=dict(
            name='HT4',
            shape='K8',
            camera_data=['E3', 'E6', 'H3', 'H6'],
            camera_data_spawn_point=['H6'],
            map_data="""
                -- -- -- -- -- -- -- ++ -- ME --
                -- -- ME ++ ++ ME ME ++ ME -- ME
                -- ME -- ++ ++ -- -- -- -- -- --
                -- Me -- -- -- Me -- ++ ++ ++ --
                -- ++ ++ ++ -- -- -- MS MB MS --
                -- -- ++ Me -- Me -- -- MS -- --
                -- -- ME -- -- ++ ++ -- __ -- ++
                ++ -- -- ME -- ++ ++ SP -- SP ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50
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
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='ht1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Jiulaimu_Mud', 'Jiulaimu_Statue', 'Jiulaimu_Demon'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.069, 1.089),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.034, 1.053),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.004, 1.022),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'ht5': Stage(
        base=BASE,
        map=dict(
            name='HT5',
            shape='I8',
            camera_data=['D4', 'F4', 'E2', 'E6'],
            camera_data_spawn_point=['E2'],
            map_data="""
                ++ ++ -- SP -- SP -- ++ ++
                ++ ++ -- -- -- -- -- ++ ++
                Me -- -- MS -- MS -- -- Me
                Me -- MS ++ ++ ++ MS -- Me
                ++ -- -- -- ME -- -- -- ++
                -- ME ME -- __ -- ME ME --
                -- ++ ++ ME -- ME ++ ++ --
                -- ++ ++ -- MB -- ++ ++ --
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
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='ht1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Jiulaimu_Ghost'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.234, 1.257),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.193, 1.215),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.158, 1.179),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'ht6': Stage(
        base=BASE,
        map=dict(
            name='HT6',
            shape='I9',
            camera_data=['E5', 'D6', 'F6'],
            camera_data_spawn_point=['E5'],
            map_data="""
                -- -- -- ++ ++ ++ -- -- --
                -- -- -- ++ ++ ++ -- -- --
                -- ++ ++ ++ MB ++ ++ ++ --
                ++ -- Me -- -- -- Me -- ++
                -- Me -- MS -- MS -- Me --
                ME -- -- -- MS -- -- -- ME
                ME -- ME -- __ -- ME -- ME
                ++ ME ++ SP -- SP ++ ME ++
                -- -- ++ -- -- -- ++ -- --
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
                50 50 50 50 50 50 50 50 50
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
        config_base='ht1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Jiulaimu_Ghost'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.043, 1.063),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.009, 1.028),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.98, 0.997),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'sp': Stage(
        base=BASE,
        map=dict(
            name='SP',
            shape='I9',
            camera_data=['E3', 'E5'],
            camera_data_spawn_point=['E3'],
            map_data="""
                ++ ++ -- ++ ++ ++ -- ++ ++
                ++ ++ ME -- MB -- ME ++ ++
                -- ME -- -- -- -- -- ME --
                -- -- -- SP -- SP -- -- --
                ++ ME -- -- __ -- -- ME ++
                ++ -- ME -- MS -- ME -- ++
                -- ++ -- MS -- MS -- ++ --
                -- ++ ++ ++ -- ++ ++ ++ --
                -- -- -- ++ -- ++ -- -- --
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
                50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 8, 'siren': 3},
                {'battle': 1},
                {'battle': 2},
                {'battle': 3},
                {'battle': 4},
                {'battle': 5},
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Jiulaimu_Ghost'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_CHAPTER_SWITCH_20241219=True,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_IS_ONE_TIME_STAGE=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 222),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (222, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            HOMO_STORAGE=((8, 6), [(146.885, 86.89), (1029.321, 86.89), (-24.037, 613.962), (1148.33, 613.962)]),
            MAP_SWIPE_MULTIPLY=(1.116, 1.137),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.079, 1.099),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.048, 1.066),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=2)', 'battle_default'],
            5: PLAN,
            7: 'fleet_boss.clear_boss',
        },
    ),
    't1': Stage(
        base=BASE,
        map=dict(
            name='T1',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['F2'],
            map_data="""
                -- -- -- ++ ++ -- -- SP --
                ++ ME ME ++ ++ MS -- -- SP
                ++ -- -- -- Me -- __ -- --
                -- -- ME -- -- -- -- MS ++
                MB -- ++ ++ ++ Me -- -- ME
                -- -- ME -- ME -- -- Me --
                -- ME -- ME -- -- ++ -- --
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
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1, 'boss': 1},
                {'battle': 4, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Jiulaimu_Mud', 'Jiulaimu_Statue', 'Jiulaimu_Demon'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_CHAPTER_SWITCH_20241219=True,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_HAS_MODE_SWITCH=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 222),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (222, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            MAP_SWIPE_MULTIPLY=(1.267, 1.29),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.225, 1.248),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.189, 1.211),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            3: 'clear_boss',
        },
    ),
    't2': Stage(
        base=BASE,
        map=dict(
            name='T2',
            shape='G10',
            camera_data=['C5', 'C8'],
            camera_data_spawn_point=['C2'],
            map_data="""
                -- -- SP -- SP -- --
                -- -- -- -- -- -- --
                ++ ++ -- MS -- ++ ++
                -- ++ MS -- MS ++ --
                -- Me -- __ -- Me --
                -- -- Me -- Me -- --
                ++ ++ ++ -- ++ ++ ++
                -- -- ME -- ME -- --
                -- ME -- MB -- ME --
                -- -- ME -- ME -- --
            """,
            weight_data="""
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
                50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Jiulaimu_Mud', 'Jiulaimu_Statue', 'Jiulaimu_Demon'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.222, 1.245),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.182, 1.204),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.148, 1.168),
            MAP_WALK_USE_CURRENT_FLEET=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    't3': Stage(
        base=BASE,
        map=dict(
            name='T3',
            shape='J6',
            camera_data=['D2', 'D4', 'G2', 'G4'],
            camera_data_spawn_point=['D2'],
            map_data="""
                ++ ++ ++ -- MB ++ ME -- -- --
                SP -- -- MS -- Me -- ME -- ++
                SP -- -- MS __ -- -- -- ME ++
                ++ -- MS -- -- Me -- -- -- ME
                ++ -- -- -- ME ++ ++ -- ME --
                -- Me ++ Me -- ++ ++ ME -- --
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
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Jiulaimu_Mud', 'Jiulaimu_Statue', 'Jiulaimu_Demon'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.193, 1.216),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.154, 1.175),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.12, 1.141),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    't4': Stage(
        base=BASE,
        map=dict(
            name='T4',
            shape='K8',
            camera_data=['E3', 'E6', 'H3', 'H6'],
            camera_data_spawn_point=['H6'],
            map_data="""
                -- -- -- -- -- -- -- ++ -- ME --
                -- -- ME ++ ++ ME ME ++ ME -- ME
                -- ME -- ++ ++ -- -- -- -- -- --
                -- Me -- -- -- Me -- ++ ++ ++ --
                -- ++ ++ ++ -- -- -- MS MB MS --
                -- -- ++ Me -- Me -- -- MS -- --
                -- -- ME -- -- ++ ++ -- __ -- ++
                ++ -- -- ME -- ++ ++ SP -- SP ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
                {'battle': 5, 'enemy': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Jiulaimu_Mud', 'Jiulaimu_Statue', 'Jiulaimu_Demon'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.069, 1.089),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.034, 1.053),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.004, 1.022),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    't5': Stage(
        base=BASE,
        map=dict(
            name='T5',
            shape='I8',
            camera_data=['D4', 'F4', 'E2', 'E6'],
            camera_data_spawn_point=['E2'],
            map_data="""
                ++ ++ -- SP -- SP -- ++ ++
                ++ ++ -- -- -- -- -- ++ ++
                Me -- -- MS -- MS -- -- Me
                Me -- MS ++ ++ ++ MS -- Me
                ++ -- -- -- ME -- -- -- ++
                -- ME ME -- __ -- ME ME --
                -- ++ ++ ME -- ME ++ ++ --
                -- ++ ++ -- MB -- ++ ++ --
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
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Jiulaimu_Ghost'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.234, 1.257),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.193, 1.215),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.158, 1.179),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    't6': Stage(
        base=BASE,
        map=dict(
            name='T6',
            shape='I9',
            camera_data=['E5', 'D6', 'F6'],
            camera_data_spawn_point=['E5'],
            map_data="""
                -- -- -- ++ ++ ++ -- -- --
                -- -- -- ++ ++ ++ -- -- --
                -- ++ ++ ++ MB ++ ++ ++ --
                ++ -- Me -- -- -- Me -- ++
                -- Me -- MS -- MS -- Me --
                ME -- -- -- MS -- -- -- ME
                ME -- ME -- __ -- ME -- ME
                ++ ME ++ SP -- SP ++ ME ++
                -- -- ++ -- -- -- ++ -- --
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
                50 50 50 50 50 50 50 50 50
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
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Jiulaimu_Ghost'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.043, 1.063),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.009, 1.028),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.98, 0.997),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
