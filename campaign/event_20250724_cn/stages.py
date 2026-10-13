"""
Stages of event_20250724_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBaseTS'
BASE_2 = '.campaign_base:CampaignBaseT'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']
PLAN_2 = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default']

STAGES = {
    't1': Stage(
        base=BASE_2,
        map=dict(
            name='T1',
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ -- ME -- ++ ++ ++ -- --
                -- ME -- -- -- ME -- -- --
                -- ++ ++ ME -- -- -- ME --
                ME ++ ++ -- Me -- -- ++ ME
                -- -- -- MS ++ MS -- ++ --
                -- ME -- -- MS -- -- ME --
                ME -- Me -- __ -- -- Me ++
                ++ ++ ++ SP -- SP -- -- MB
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
            MAP_SIREN_TEMPLATE=['CAalchemist2'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_CHAPTER_SWITCH_20241219=True,
            STAGE_ENTRANCE=['half', '20240725'],
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
            MAP_SWIPE_MULTIPLY=(1.068, 1.088),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.033, 1.052),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.003, 1.021),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    't2': Stage(
        base=BASE_2,
        map=dict(
            name='T2',
            shape='I8',
            camera_data=['D3', 'D5', 'F3', 'F5'],
            camera_data_spawn_point=['F6'],
            map_data="""
                ++ ++ -- -- -- -- -- -- ++
                ++ ++ ME -- ME -- ME -- ++
                ++ ME -- -- ++ ++ ++ -- ME
                -- ME -- ME -- -- Me -- --
                ME -- -- Me -- MB ++ MS --
                -- -- ME -- __ ++ MS -- --
                ++ ME ++ Me -- MS -- -- SP
                -- -- ++ -- -- -- -- SP --
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
                {'battle': 0, 'enemy': 3, 'siren': 1},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CLalchemist2'],
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
    't3': Stage(
        base=BASE_2,
        map=dict(
            name='T3',
            shape='I8',
            camera_data=['D2', 'E6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- -- ME -- ME ++ ++ ++ --
                -- ME ++ -- -- -- ME -- --
                ME -- -- -- Me -- -- ME --
                ++ ++ ++ -- -- Me -- ME --
                SP -- -- MS -- ME ++ ++ --
                SP -- -- MS -- Me ++ ++ --
                ++ -- MS -- __ -- ME ME --
                ++ -- ++ MB ++ -- -- -- ++
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
            MAP_SIREN_TEMPLATE=['DDalchemist2'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.095, 1.116),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.059, 1.079),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.028, 1.047),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    't4': Stage(
        base=BASE_2,
        map=dict(
            name='T4',
            shape='I8',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['F5'],
            map_data="""
                ++ ++ ++ ME -- ++ ++ -- --
                -- -- ME -- ME ++ ++ ME --
                ME ME ++ -- -- ME -- -- ME
                -- -- ++ Me -- ++ -- MS ++
                MB -- -- -- __ -- MS -- --
                -- -- ++ Me -- MS -- -- SP
                ME ME ++ -- Me ++ -- SP --
                -- -- -- -- -- ++ ++ ++ --
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
            MAP_SIREN_TEMPLATE=['BBalchemist2'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.094, 1.115),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.058, 1.078),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.027, 1.046),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    't5': Stage(
        base=BASE_2,
        map=dict(
            name='T5',
            shape='I9',
            camera_data=['D2', 'D5', 'D7', 'F2', 'F5', 'F7'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- ME -- ++ -- ++ -- ME --
                ME -- ME -- ++ -- ME -- ME
                -- -- -- ++ ++ ++ -- -- --
                ++ -- ME -- ++ -- ME -- ++
                ++ -- -- SP -- SP -- -- ++
                ME -- Me -- __ -- Me -- ME
                -- Me -- -- MS -- -- Me --
                ++ ++ -- MS -- MS -- ++ ++
                ++ ++ ME -- MB -- ME ++ ++
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
            MAP_SIREN_TEMPLATE=['CValchemist2'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.12, 1.141),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.083, 1.103),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.051, 1.07),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'ts1': Stage(
        base=BASE,
        map=dict(
            name='TS1',
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                ++ -- ME -- ++ ++ ++ -- --
                -- ME -- -- -- ME -- -- --
                -- ++ ++ ME -- -- -- ME --
                ME ++ ++ -- Me -- -- ++ ME
                -- -- -- MS ++ MS -- ++ --
                -- ME -- -- MS -- -- ME --
                ME -- Me -- __ -- -- Me ++
                ++ ++ ++ SP -- SP -- -- MB
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
            MAP_SIREN_TEMPLATE=['CAalchemist2'],
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
            MAP_CHAPTER_SWITCH_20241219=True,
            STAGE_ENTRANCE=['half', '20240725'],
            STAGE_INCREASE_CUSTOM=['TS1 > TS2 > TS3 > TS4 > TS5 > TS6'],
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
            MAP_SWIPE_MULTIPLY=(1.068, 1.088),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.033, 1.052),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.003, 1.021),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'ts2': Stage(
        base=BASE,
        map=dict(
            name='TS2',
            shape='I8',
            camera_data=['D3', 'D5', 'F3', 'F5'],
            camera_data_spawn_point=['F6'],
            map_data="""
                ++ ++ -- -- -- -- -- -- ++
                ++ ++ ME -- ME -- ME -- ++
                ++ ME -- -- ++ ++ ++ -- ME
                -- ME -- ME -- -- Me -- --
                ME -- -- Me -- MB ++ MS --
                -- -- ME -- __ ++ MS -- --
                ++ ME ++ Me -- MS -- -- SP
                -- -- ++ -- -- -- -- SP --
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
        config_base='ts1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CLalchemist2'],
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
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'ts3': Stage(
        base=BASE,
        map=dict(
            name='TS3',
            shape='I8',
            camera_data=['D2', 'E6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- -- ME -- ME ++ ++ ++ --
                -- ME ++ -- -- -- ME -- --
                ME -- -- -- Me -- -- ME --
                ++ ++ ++ -- -- Me -- ME --
                SP -- -- MS -- ME ++ ++ --
                SP -- -- MS -- Me ++ ++ --
                ++ -- MS -- __ -- ME ME --
                ++ -- ++ MB ++ -- -- -- ++
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
        config_base='ts1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DDalchemist2'],
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
            MAP_SWIPE_MULTIPLY=(1.095, 1.116),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.059, 1.079),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.028, 1.047),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'ts4': Stage(
        base=BASE,
        map=dict(
            name='TS4',
            shape='I8',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['F5'],
            map_data="""
                ++ ++ ++ ME -- ++ ++ -- --
                -- -- ME -- ME ++ ++ ME --
                ME ME ++ -- -- ME -- -- ME
                -- -- ++ Me -- ++ -- MS ++
                MB -- -- -- __ -- MS -- --
                -- -- ++ Me -- MS -- -- SP
                ME ME ++ -- Me ++ -- SP --
                -- -- -- -- -- ++ ++ ++ --
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
        config_base='ts1',
        config=dict(
            MAP_SIREN_TEMPLATE=['BBalchemist2'],
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
            MAP_SWIPE_MULTIPLY=(1.094, 1.115),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.058, 1.078),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.027, 1.046),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'ts5': Stage(
        base=BASE,
        map=dict(
            name='TS5',
            shape='I9',
            camera_data=['D2', 'D5', 'D7', 'F2', 'F5', 'F7'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- ME -- ++ -- ++ -- ME --
                ME -- ME -- ++ -- ME -- ME
                -- -- -- ++ ++ ++ -- -- --
                ++ -- ME -- ++ -- ME -- ++
                ++ -- -- SP -- SP -- -- ++
                ME -- Me -- __ -- Me -- ME
                -- Me -- -- MS -- -- Me --
                ++ ++ -- MS -- MS -- ++ ++
                ++ ++ ME -- MB -- ME ++ ++
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
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2, 'siren': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='ts1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CValchemist2'],
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
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.12, 1.141),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.083, 1.103),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.051, 1.07),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
}
