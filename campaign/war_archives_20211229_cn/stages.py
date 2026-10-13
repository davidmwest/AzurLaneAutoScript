"""
Stages of war_archives_20211229_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = [
    ('when', 'map_is_clear_mode', ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)'], ["clear_any_enemy(sort=('cost_2',))"]),
    'battle_default',
]
PLAN_2 = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']

STAGES = {
    'a2': Stage(
        base=BASE,
        map=dict(
            name='A2',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                ME ME ++ ++ ++ -- ME -- ++
                -- -- -- -- MS -- -- ME ++
                -- MS -- ME -- MB MB -- --
                ++ ME -- ++ __ ++ ++ Me --
                ++ ME -- -- -- ++ ++ -- --
                SP -- -- MS -- -- ME -- Me
                -- SP -- ++ ++ -- -- ++ ME
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
            MAP_SIREN_TEMPLATE=['CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.093, 1.113),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.057, 1.076),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.026, 1.045),
            MAP_HAS_MISSILE_ATTACK=True,
        ),
        enemy_filter=ENEMY_FILTER,
        attrs={'MAP_ENEMY_SEARCHING_OVERLAY_TRANSPARENCY_THRESHOLD': 0.65},
        battle={
            0: PLAN_2,
            4: 'clear_boss',
        },
    ),
    'a3': Stage(
        base=BASE,
        map=dict(
            name='A3',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['G6'],
            map_data="""
                ++ ++ ++ ME -- ME -- -- ++ ++
                ++ ME -- -- -- -- -- MS ++ ++
                ME -- Me MB ++ ME -- -- -- ME
                -- -- ++ MB ++ -- -- ME -- --
                -- ME ++ MB Me MS ++ -- -- --
                ME -- Me -- __ ++ -- ++ -- SP
                ++ -- -- MS -- -- -- -- -- SP
                ++ Me -- ++ ++ ME -- SP SP ++
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
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DD', 'CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_MOVABLE_NORMAL_ENEMY=True,
            MOVABLE_NORMAL_ENEMY_TURN=(2,),
            MAP_SWIPE_MULTIPLY=(1.064, 1.084),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.029, 1.048),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.999, 1.017),
        ),
        enemy_filter=ENEMY_FILTER,
        attrs={'MAP_ENEMY_SEARCHING_OVERLAY_TRANSPARENCY_THRESHOLD': 0.65},
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b1': Stage(
        base=BASE,
        map=dict(
            name='B1',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- ME -- ++ ++ ++ MB MB MB --
                ME -- MS -- -- -- -- -- -- ++
                ++ ME -- -- ++ Me __ ME -- ++
                ++ -- -- ME -- MS -- -- ME --
                SP -- ++ -- -- -- ++ ++ Me --
                SP -- -- -- ME Me ++ ++ -- ME
                -- -- -- MS ++ -- -- MS -- --
                ++ ++ -- -- ME -- Me -- ME --
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
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
                {'battle': 5, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['DD', 'CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_MOVABLE_NORMAL_ENEMY=True,
            MOVABLE_NORMAL_ENEMY_TURN=(2,),
            MAP_SIREN_MOVE_WAIT=1.0,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 238),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (238, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_EDGE_COLOR_RANGE=(0, 17),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=180,
            MAP_SWIPE_MULTIPLY=(1.033, 1.053),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.999, 1.018),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.97, 0.988),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_WALK_USE_CURRENT_FLEET=True,
        ),
        enemy_filter=ENEMY_FILTER,
        attrs={'MAP_ENEMY_SEARCHING_OVERLAY_TRANSPARENCY_THRESHOLD': 0.65},
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
            camera_data_spawn_point=['F5'],
            map_data="""
                ++ ++ Me -- ME -- ++ ++ ++
                ++ ++ -- ME -- -- -- ME --
                Me -- -- -- ME ++ MS -- --
                -- -- -- -- ME -- -- ME ++
                Me -- MS ++ ME -- -- -- ++
                ++ ++ -- -- -- MS -- -- SP
                ME -- __ MS -- -- ++ -- SP
                -- -- -- ++ -- -- -- -- --
                MB MB MB ++ -- Me ++ ++ ++
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
            MAP_SIREN_TEMPLATE=['DD', 'CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.039, 1.059),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.005, 1.024),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.976, 0.993),
        ),
        enemy_filter=ENEMY_FILTER,
        attrs={'MAP_ENEMY_SEARCHING_OVERLAY_TRANSPARENCY_THRESHOLD': 0.65},
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'b3': Stage(
        base=BASE,
        map=dict(
            name='B3',
            shape='L6',
            camera_data=['E3', 'G4', 'I3'],
            camera_data_spawn_point=['D4'],
            map_data="""
                ++ ++ -- -- -- ME ME -- -- -- ++ ++
                ++ -- ++ ++ Me -- -- MS ++ ++ ++ ++
                -- Me Me ++ -- ME ++ -- ++ -- -- MB
                -- -- __ -- MS -- ++ -- -- MS -- MB
                SP -- -- Me ++ ++ ME -- ME -- ++ ++
                -- SP -- ++ ++ ++ -- ME -- ME ++ ++
            """,
            map_data_loop="""
                ++ ++ -- -- Me ME ME Me -- -- ++ ++
                ++ -- ++ ++ -- -- -- -- ++ ++ ++ ++
                -- MS Me ++ -- MS ++ -- ++ ME -- MB
                -- -- __ -- -- MS ++ -- -- -- -- MB
                SP -- -- Me ++ ++ ME -- ME -- ++ ++
                -- SP -- ++ ++ ++ -- ME -- ME ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 3},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'boss': 1},
            ],
            spawn_data_loop=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SIREN_TEMPLATE=['Lover'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_SWIPE_MULTIPLY=(1.123, 1.144),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.086, 1.106),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.054, 1.073),
        ),
        enemy_filter=ENEMY_FILTER,
        attrs={'MAP_ENEMY_SEARCHING_OVERLAY_TRANSPARENCY_THRESHOLD': 0.65},
        battle={
            0: PLAN_2,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'bs1': Stage(
        base=BASE,
        map=dict(
            name='BS1',
            shape='L6',
            camera_data=['D2', 'D4', 'I2', 'I4'],
            camera_data_spawn_point=['I2', 'I4'],
            map_data="""
                ++ ++ -- -- Me -- Me MS -- -- ++ ++
                ++ -- ++ ++ -- -- -- -- ++ ++ ++ ++
                ME -- ME ++ -- ME ++ -- ++ Me -- SP
                ME -- -- -- -- ME ++ -- -- -- -- SP
                -- MB -- ME ++ ++ Me -- __ -- ++ ++
                ME -- ME ++ ++ ++ -- MS ME MS ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
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
        config=dict(
            MAP_SIREN_TEMPLATE=['DD', 'CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 238),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (238, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            HOMO_EDGE_COLOR_RANGE=(0, 17),
            MAP_IS_ONE_TIME_STAGE=True,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
        ),
        enemy_filter=ENEMY_FILTER,
        attrs={'MAP_ENEMY_SEARCHING_OVERLAY_TRANSPARENCY_THRESHOLD': 0.65},
        battle={
            0: PLAN_2,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c2': Stage(
        base=BASE,
        map=dict(
            name='C2',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                ME ME ++ ++ ++ -- ME -- ++
                -- -- -- -- MS -- -- ME ++
                -- MS -- ME -- MB MB -- --
                ++ ME -- ++ __ ++ ++ Me --
                ++ ME -- -- -- ++ ++ -- --
                SP -- -- MS -- -- ME -- Me
                -- SP -- ++ ++ -- -- ++ ME
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
            MAP_SIREN_TEMPLATE=['CL', 'CA', 'CAgreen'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.093, 1.113),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.057, 1.076),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.026, 1.045),
            MAP_HAS_MISSILE_ATTACK=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            4: 'clear_boss',
        },
    ),
    'c3': Stage(
        base=BASE,
        map=dict(
            name='C3',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['G6'],
            map_data="""
                ++ ++ ++ ME -- ME -- -- ++ ++
                ++ ME -- -- -- -- -- MS ++ ++
                ME -- Me MB ++ ME -- -- -- ME
                -- -- ++ MB ++ -- -- ME -- --
                -- ME ++ MB Me MS ++ -- -- --
                ME -- Me -- __ ++ -- ++ -- SP
                ++ -- -- MS -- -- -- -- -- SP
                ++ Me -- ++ ++ ME -- SP SP ++
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
            MAP_SIREN_TEMPLATE=['CL', 'CA', 'CAgreen', 'BB'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_MOVABLE_NORMAL_ENEMY=True,
            MOVABLE_NORMAL_ENEMY_TURN=(2,),
            MAP_SWIPE_MULTIPLY=(1.064, 1.084),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.029, 1.048),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.999, 1.017),
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
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- ME -- ++ ++ ++ MB MB MB --
                ME -- MS -- -- -- -- -- -- ++
                ++ ME -- -- ++ Me __ ME -- ++
                ++ -- -- ME -- MS -- -- ME --
                SP -- ++ -- -- -- ++ ++ Me --
                SP -- -- -- ME Me ++ ++ -- ME
                -- -- -- MS ++ -- -- MS -- --
                ++ ++ -- -- ME -- Me -- ME --
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
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['DD', 'CL', 'CAgreen', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_HAS_MOVABLE_NORMAL_ENEMY=True,
            MOVABLE_NORMAL_ENEMY_TURN=(2,),
            MAP_SIREN_MOVE_WAIT=1.0,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 238),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (238, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_EDGE_COLOR_RANGE=(0, 17),
            MAP_SWIPE_MULTIPLY=(1.033, 1.053),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.999, 1.018),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.97, 0.988),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_WALK_USE_CURRENT_FLEET=True,
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
            shape='I9',
            camera_data=['D2', 'D5', 'D7', 'F2', 'F5', 'F7'],
            camera_data_spawn_point=['F5'],
            map_data="""
                ++ ++ Me -- ME -- ++ ++ ++
                ++ ++ -- ME -- -- -- ME --
                Me -- -- -- ME ++ MS -- --
                -- -- -- -- ME -- -- ME ++
                Me -- MS ++ ME -- -- -- ++
                ++ ++ -- -- -- MS -- -- SP
                ME -- __ MS -- -- ++ -- SP
                -- -- -- ++ -- -- -- -- --
                MB MB MB ++ -- Me ++ ++ ++
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
            MAP_SIREN_TEMPLATE=['CL', 'CAgreen', 'CA', 'BB'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.039, 1.059),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.005, 1.024),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.976, 0.993),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: [
                ('when', 'map_is_clear_mode', ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)'], ["clear_any_enemy(sort=('cost_2',))"]),
                'battle_default',
            ],
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        base=BASE,
        map=dict(
            name='D3',
            shape='L6',
            camera_data=['E3', 'G4', 'I3'],
            camera_data_spawn_point=['D4'],
            map_data="""
                ++ ++ -- -- -- ME ME -- -- -- ++ ++
                ++ -- ++ ++ Me -- -- MS ++ ++ ++ ++
                -- Me Me ++ -- ME ++ -- ++ -- -- MB
                -- -- __ -- MS -- ++ -- -- MS -- MB
                SP -- -- Me ++ ++ ME -- ME -- ++ ++
                -- SP -- ++ ++ ++ -- ME -- ME ++ ++
            """,
            map_data_loop="""
                ++ ++ -- -- Me ME ME Me -- -- ++ ++
                ++ -- ++ ++ -- -- -- -- ++ ++ ++ ++
                -- MS Me ++ -- MS ++ -- ++ ME -- MB
                -- -- __ -- -- MS ++ -- -- -- -- MB
                SP -- -- Me ++ ++ ME -- ME -- ++ ++
                -- SP -- ++ ++ ++ -- ME -- ME ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 3},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'boss': 1},
            ],
            spawn_data_loop=[
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
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SIREN_TEMPLATE=['Lover'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_SWIPE_MULTIPLY=(1.123, 1.144),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.086, 1.106),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.054, 1.073),
            MAP_HAS_MOVABLE_ENEMY=False,
            MAP_HAS_MOVABLE_NORMAL_ENEMY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: [
                ('when', 'map_is_clear_mode', ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)'], ['clear_siren']),
                'battle_default',
            ],
            5: [
                ('when', 'map_is_clear_mode', ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)'], ['clear_siren']),
                'battle_default',
            ],
            6: 'fleet_boss.clear_boss',
        },
    ),
    'ds1': Stage(
        base=BASE,
        map=dict(
            name='DS1',
            shape='L6',
            camera_data=['D2', 'D4', 'I2', 'I4'],
            camera_data_spawn_point=['I2', 'I4'],
            map_data="""
                ++ ++ -- -- Me -- Me MS -- -- ++ ++
                ++ -- ++ ++ -- -- -- -- ++ ++ ++ ++
                ME -- ME ++ -- ME ++ -- ++ Me -- SP
                ME -- -- -- -- ME ++ -- -- -- -- SP
                -- MB -- ME ++ ++ Me -- __ -- ++ ++
                ME -- ME ++ ++ ++ -- MS ME MS ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50
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
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CAgreen', 'CA', 'BB'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 238),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (238, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            HOMO_EDGE_COLOR_RANGE=(0, 17),
            MAP_IS_ONE_TIME_STAGE=True,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default'],
            5: PLAN_2,
            6: 'fleet_boss.clear_boss',
        },
    ),
}
