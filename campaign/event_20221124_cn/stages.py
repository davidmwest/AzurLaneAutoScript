"""
Stages of event_20221124_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']
PLAN_2 = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default']

STAGES = {
    'sp': Stage(
        base=BASE,
        map=dict(
            name='A.SP',
            shape='G8',
            camera_data=['D3', 'D6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ ++ ++ ++ ++ ++ ++
                ++ ++ -- MB -- ++ ++
                -- -- ++ -- ++ -- --
                -- ++ MS __ MS ++ --
                ++ ME -- -- -- ME ++
                ME -- -- MS -- -- ME
                ++ -- -- -- -- -- ++
                ++ -- SP -- SP -- ++
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
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 4, 'siren': 3},
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
            MAP_SIREN_TEMPLATE=['BBalchemist', 'CValchemist'],
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
            MAP_IS_ONE_TIME_STAGE=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 232),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (232, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_STORAGE=((7, 7), [(274.753, 70.34), (1050.178, 70.34), (138.583, 713.524), (1205.781, 713.524)]),
            HOMO_EDGE_COLOR_RANGE=(0, 23),
            MAP_SWIPE_MULTIPLY=(1.072, 1.092),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.037, 1.056),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.006, 1.025),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
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
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ME -- -- Me ++ -- ME -- --
                -- -- Me -- MS -- -- -- ++
                -- -- ++ ME __ -- -- MS --
                -- -- ++ -- -- ++ MS -- --
                SP -- -- -- -- ++ -- ME MB
                SP -- ME ME MS -- -- -- MB
                -- -- -- -- -- -- ME ++ ++
                ++ ++ ++ ME Me -- ME ++ ++
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
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['DDalchemist'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 232),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (232, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_EDGE_COLOR_RANGE=(0, 23),
            MAP_SWIPE_MULTIPLY=(1.083, 1.103),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.047, 1.067),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.017, 1.035),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    't2': Stage(
        base=BASE,
        map=dict(
            name='T2',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D2', 'D5'],
            map_data="""
                -- -- ME -- Me -- ++ ++ ++
                -- ME -- ME -- MS ME Me --
                SP -- -- MS -- -- -- -- --
                SP -- ++ ++ -- -- __ -- ME
                -- -- ++ ++ MS -- ++ MB --
                ++ -- -- ME -- -- ++ ++ --
                ME ME -- -- -- ME -- -- ME
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
                {'battle': 0, 'enemy': 3, 'siren': 1},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DDalchemist', 'CLalchemist'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.103, 1.123),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.066, 1.086),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.035, 1.054),
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
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- -- -- -- ME -- ++ MB MB
                -- ME Me -- -- MS ++ -- --
                ME -- ++ ++ ME -- __ -- --
                -- ME ++ ++ -- -- Me Me --
                ME -- MS -- -- -- -- ++ ME
                -- -- -- -- -- -- MS ++ --
                SP SP -- -- ++ ME -- ME --
                ++ ++ ++ -- -- -- ME -- --
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
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CLalchemist', 'CAalchemist'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.103, 1.123),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.066, 1.086),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.035, 1.054),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    't4': Stage(
        base=BASE,
        map=dict(
            name='T4',
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ ++ ++ MB -- ME -- ME ++
                ++ -- -- -- Me -- ME -- --
                -- -- MS -- -- MS -- -- ME
                Me __ -- ++ -- -- -- MS --
                -- -- -- ++ Me -- -- ++ ++
                -- -- ME ++ -- ME -- ++ ++
                ME -- -- -- -- -- ME -- ME
                -- ++ SP SP -- -- -- ME --
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
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CLalchemist', 'CAalchemist', 'BBalchemist'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.018, 1.037),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.984, 1.002),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.955, 0.973),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    't5': Stage(
        base=BASE,
        map=dict(
            name='T5',
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                ++ ++ ++ Me -- ME -- ME
                ++ MB -- ME -- ++ ++ --
                ++ -- -- __ MS ++ ++ ME
                Me -- MS -- -- -- ME --
                -- ++ ++ ME Me -- -- --
                ME ++ ++ ME -- -- SP ++
                -- MS -- -- -- SP -- ++
                ME -- ME -- -- ++ ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2, 'siren': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['BBalchemist', 'CValchemist'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.059, 1.079),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.025, 1.043),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.995, 1.013),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'th1': Stage(
        base=BASE,
        map=dict(
            name='TH1',
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ME -- -- Me ++ -- ME -- --
                -- -- Me -- MS -- -- -- ++
                -- -- ++ ME __ -- -- MS --
                -- -- ++ -- -- ++ MS -- --
                SP -- -- -- -- ++ -- ME MB
                SP -- ME ME MS -- -- -- MB
                -- -- -- -- -- -- ME ++ ++
                ++ ++ ++ ME Me -- ME ++ ++
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
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['DDalchemist', 'CLalchemist'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_MYSTERY_MAP_CLICK=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 232),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (232, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_EDGE_COLOR_RANGE=(0, 23),
            MAP_SWIPE_MULTIPLY=(1.083, 1.103),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.047, 1.067),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.017, 1.035),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: [('do', 'clear_map_items([F1, I1])'), 'fleet_boss.clear_boss'],
        },
    ),
    'th2': Stage(
        base=BASE,
        map=dict(
            name='TH2',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D2', 'D5'],
            map_data="""
                -- -- ME -- Me -- ++ ++ ++
                -- ME -- ME -- MS ME Me --
                SP -- -- MS -- -- -- -- --
                SP -- ++ ++ -- -- __ -- ME
                -- -- ++ ++ MS -- ++ MB --
                ++ -- -- ME -- -- ++ ++ --
                ME ME -- -- -- ME -- -- ME
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
                {'battle': 1, 'enemy': 2, 'siren': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='th1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DDalchemist', 'CLalchemist'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_SWIPE_MULTIPLY=(1.103, 1.123),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.066, 1.086),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.035, 1.054),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: [('do', 'clear_map_items([E2, E7])'), 'fleet_boss.clear_boss'],
        },
    ),
    'th3': Stage(
        base=BASE,
        map=dict(
            name='TH3',
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- -- -- -- ME -- ++ MB MB
                -- ME Me -- -- MS ++ -- --
                ME -- ++ ++ ME -- __ -- --
                -- ME ++ ++ -- -- Me Me --
                ME -- MS -- -- -- -- ++ ME
                -- -- -- -- -- -- MS ++ --
                SP SP -- -- ++ ME -- ME --
                ++ ++ ++ -- -- -- ME -- --
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
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='th1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CLalchemist', 'CAalchemist'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_SWIPE_MULTIPLY=(1.103, 1.123),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.066, 1.086),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.035, 1.054),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: [('do', 'clear_map_items([E4, E6])'), 'fleet_boss.clear_boss'],
        },
    ),
    'th4': Stage(
        base=BASE,
        map=dict(
            name='TH4',
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ ++ ++ MB -- ME -- ME ++
                ++ -- -- -- Me -- ME -- --
                -- -- MS -- -- MS -- -- ME
                Me __ -- ++ -- -- -- MS --
                -- -- -- ++ Me -- -- ++ ++
                -- -- ME ++ -- ME -- ++ ++
                ME -- -- -- -- -- ME -- ME
                -- ++ SP SP -- -- -- ME --
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
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='th1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CAalchemist', 'BBalchemist'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_SWIPE_MULTIPLY=(1.018, 1.037),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.984, 1.002),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.955, 0.973),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: [('do', 'clear_map_items([G5, I2])'), 'fleet_boss.clear_boss'],
        },
    ),
    'th5': Stage(
        base=BASE,
        map=dict(
            name='TH5',
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                ++ ++ ++ Me -- ME -- ME
                ++ MB -- ME -- ++ ++ --
                ++ -- -- __ MS ++ ++ ME
                Me -- MS -- -- -- ME --
                -- ++ ++ ME Me -- -- --
                ME ++ ++ ME -- -- SP ++
                -- MS -- -- -- SP -- ++
                ME -- ME -- -- ++ ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2, 'siren': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='th1',
        config=dict(
            MAP_SIREN_TEMPLATE=['BBalchemist', 'CValchemist'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_SWIPE_MULTIPLY=(1.059, 1.079),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.025, 1.043),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.995, 1.013),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: [('do', 'clear_map_items([G5, F6])'), 'fleet_boss.clear_boss'],
        },
    ),
    'ts1': Stage(
        base=BASE,
        map=dict(
            name='TS1',
            shape='H5',
            camera_data=['C3'],
            camera_data_spawn_point=['C3'],
            map_data="""
                ++ ++ ++ ++ ME ME ++ ++
                ++ -- -- -- MS -- ++ ++
                ME -- MS __ -- MB ++ --
                ME -- -- ME Me ++ -- --
                SP SP ME ++ ++ ++ -- --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CLalchemist', 'CAalchemist', 'BBalchemist'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_IS_ONE_TIME_STAGE=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 231),
                'width': (1.5, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (215, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
            EDGE_LINES_HOUGHLINES_THRESHOLD=40,
            MAP_GRID_CENTER_TOLERANCE=0.2,
            MAP_SWIPE_MULTIPLY=(1.168, 1.19),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.13, 1.15),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.097, 1.116),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
