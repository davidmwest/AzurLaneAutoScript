"""
Stages of event_20221222_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
ENEMY_FILTER_2 = '1L > 1M > 2L > 2M > 3L > 3M > 1E > 2E > 3E > 1C > 2C > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']

STAGES = {
    'a1': Stage(
        base=BASE,
        map=dict(
            name='A1',
            shape='H8',
            camera_data=['D2', 'E3', 'E6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- -- ME -- -- -- ++ ++
                -- ME -- ME -- Me ++ ++
                -- -- ++ -- ++ -- MB --
                ME -- ++ MS -- Me -- --
                -- ME -- -- __ -- -- ME
                -- -- -- -- -- MS ++ --
                SP -- -- Me ME -- -- ME
                -- SP ++ ++ ++ ME -- --
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
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1, 'boss': 1},
                {'battle': 4, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
            MAP_ENEMY_TEMPLATE=['Light20221222', 'Main20221222', 'Carrier20221222'],
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 222),
                'width': (1.5, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (222, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_EDGE_COLOR_RANGE=(0, 33),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=300,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(1.04, 1.06),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.006, 1.025),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.977, 0.994),
        ),
        enemy_filter=ENEMY_FILTER_2,
        battle={
            0: PLAN,
            3: 'clear_boss',
        },
    ),
    'a2': Stage(
        base=BASE,
        map=dict(
            name='A2',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                ME -- -- ME ++ Me -- ++ ++
                -- -- Me -- MS -- -- -- Me
                -- ++ -- -- -- __ MS -- --
                SP -- -- ++ ME ++ ++ MB --
                SP -- ME -- MS ++ ++ MB Me
                -- ME -- -- ME -- ME -- --
                ++ ++ ++ ME -- -- ME -- --
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
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.074, 1.095),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.039, 1.058),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.009, 1.027),
        ),
        enemy_filter=ENEMY_FILTER_2,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'a3': Stage(
        base=BASE,
        map=dict(
            name='A3',
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['F2'],
            map_data="""
                ++ ++ ++ -- -- ME -- SP --
                -- Me -- MS ME -- -- -- SP
                -- ME -- ++ -- -- -- -- --
                ME -- ME -- -- ME ME Me --
                Me -- MS -- ++ -- ++ ++ ME
                ++ -- __ -- -- MS ++ ++ --
                -- -- -- ++ Me -- -- ME --
                MB MB -- ++ -- ME ++ ++ ++
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
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.095, 1.116),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.059, 1.079),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.028, 1.047),
        ),
        enemy_filter=ENEMY_FILTER_2,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b2': Stage(
        base=BASE,
        map=dict(
            name='B2',
            shape='I9',
            camera_data=['D2', 'D5', 'D7', 'F2', 'F5', 'F7'],
            camera_data_spawn_point=['F2'],
            map_data="""
                ME -- -- ME -- ++ ++ -- --
                -- Me ME -- -- SP SP -- --
                -- -- ++ ++ ME -- -- -- ME
                ME -- ++ ++ ME -- -- MS ++
                ME -- -- MS -- -- ME ME --
                -- Me -- __ -- MS ++ -- ME
                ++ -- -- -- ME -- -- MS ++
                -- MB MB -- -- Me -- -- ++
                -- ++ ++ -- -- -- Me -- ++
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
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='',
            MAP_SWIPE_MULTIPLY=(1.056, 1.076),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.021, 1.04),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.992, 1.009),
        ),
        enemy_filter=ENEMY_FILTER_2,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c1': Stage(
        map=dict(
            name='C1',
            shape='H8',
            camera_data=['D2', 'E3', 'E6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- -- ME -- -- -- ++ ++
                -- ME -- ME -- Me ++ ++
                -- -- ++ -- ++ -- MB --
                ME -- ++ MS -- Me -- --
                -- ME -- -- __ -- -- ME
                -- -- -- -- -- MS ++ --
                SP -- -- Me ME -- -- ME
                -- SP ++ ++ ++ ME -- --
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
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 231),
                'width': (1.5, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (231, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_EDGE_COLOR_RANGE=(0, 24),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=300,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(1.04, 1.06),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.006, 1.025),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.977, 0.994),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'c2': Stage(
        map=dict(
            name='C2',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                ME -- -- ME ++ Me -- ++ ++
                -- -- Me -- MS -- -- -- Me
                -- ++ -- -- -- __ MS -- --
                SP -- -- ++ ME ++ ++ MB --
                SP -- ME -- MS ++ ++ MB Me
                -- ME -- -- ME -- ME -- --
                ++ ++ ++ ME -- -- ME -- --
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
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.074, 1.095),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.039, 1.058),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.009, 1.027),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'c3': Stage(
        map=dict(
            name='C3',
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['F2'],
            map_data="""
                ++ ++ ++ -- -- ME -- SP --
                -- Me -- MS ME -- -- -- SP
                -- ME -- ++ -- -- -- -- --
                ME -- ME -- -- ME ME Me --
                Me -- MS -- ++ -- ++ ++ ME
                ++ -- __ -- -- MS ++ ++ --
                -- -- -- ++ Me -- -- ME --
                MB MB -- ++ -- ME ++ ++ ++
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
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
    'd2': Stage(
        map=dict(
            name='D2',
            shape='I9',
            camera_data=['D2', 'D5', 'D7', 'F2', 'F5', 'F7'],
            camera_data_spawn_point=['F2'],
            map_data="""
                ME -- -- ME -- ++ ++ -- --
                -- Me ME -- -- SP SP -- --
                -- -- ++ ++ ME -- -- -- ME
                ME -- ++ ++ ME -- -- MS ++
                ME -- -- MS -- -- ME ME --
                -- Me -- __ -- MS ++ -- ME
                ++ -- -- -- ME -- -- MS ++
                -- MB MB -- -- Me -- -- ++
                -- ++ ++ -- -- -- Me -- ++
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
        config_base='d1',
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='',
            MAP_SWIPE_MULTIPLY=(1.056, 1.076),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.021, 1.04),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.992, 1.009),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default'],
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'sp': Stage(
        map=dict(
            name='SP',
            shape='I9',
            camera_data=['E5'],
            camera_data_spawn_point=['E7'],
            map_data="""
                ++ ++ ++ -- ++ -- ++ ++ ++
                -- -- -- ++ ++ ++ -- -- --
                -- -- -- -- ++ -- -- -- --
                -- -- ME -- MB -- ME -- --
                -- -- ++ ME __ ME ++ -- --
                -- -- MS ++ MS ++ MS -- --
                ++ -- -- -- -- -- -- -- ++
                -- ++ -- -- -- -- -- ++ --
                -- ++ -- SP -- SP -- ++ --
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
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['SirenBoss15', 'SirenBoss16'],
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
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 231),
                'width': (1.5, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (231, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_EDGE_COLOR_RANGE=(0, 24),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=300,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(0.992, 1.011),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.959, 0.977),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.931, 0.948),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=2)', 'battle_default'],
            5: PLAN,
            7: 'fleet_boss.clear_boss',
        },
    ),
}
