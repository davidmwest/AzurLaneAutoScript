"""
Stages of event_20240425_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']

STAGES = {
    'isp1': Stage(
        base=BASE,
        map=dict(
            name='ISP1',
            shape='E5',
            camera_data=['C2'],
            camera_data_spawn_point=['C2'],
            map_data="""
                -- ++ ++ ++ --
                -- ++ MB ++ --
                -- ++ -- ++ --
                ++ -- SP -- ++
                -- ++ ++ ++ --
            """,
            weight_data="""
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
            """,
            spawn_data=[{'battle': 0, 'boss': 1}],
        ),
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_HAS_CLEAR_PERCENTAGE=False,
            FLEET_2=0,
            MAP_IS_ONE_TIME_STAGE=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: 'clear_boss',
        },
    ),
    'isp2': Stage(
        base=BASE,
        map=dict(
            name='ISP2',
            shape='E5',
            camera_data=['C2'],
            camera_data_spawn_point=['C2'],
            map_data="""
                -- ++ ++ ++ --
                -- ++ MB ++ --
                -- ++ -- ++ --
                ++ -- SP -- ++
                -- ++ ++ ++ --
            """,
            weight_data="""
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
            """,
            spawn_data=[{'battle': 0, 'boss': 1}],
        ),
        config_base='isp1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: 'clear_boss',
        },
    ),
    'isp3': Stage(
        base=BASE,
        map=dict(
            name='ISP3',
            shape='E5',
            camera_data=['C2'],
            camera_data_spawn_point=['C2'],
            map_data="""
                -- ++ ++ ++ --
                -- ++ MB ++ --
                -- ++ -- ++ --
                ++ -- SP -- ++
                -- ++ ++ ++ --
            """,
            weight_data="""
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
            """,
            spawn_data=[{'battle': 0, 'boss': 1}],
        ),
        config_base='isp1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: 'clear_boss',
        },
    ),
    'isp4': Stage(
        base=BASE,
        map=dict(
            name='ISP4',
            shape='E5',
            camera_data=['C2'],
            camera_data_spawn_point=['C2'],
            map_data="""
                -- ++ ++ ++ --
                -- ++ MB ++ --
                -- ++ -- ++ --
                ++ -- SP -- ++
                -- ++ ++ ++ --
            """,
            weight_data="""
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
            """,
            spawn_data=[{'battle': 0, 'boss': 1}],
        ),
        config_base='isp1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: 'clear_boss',
        },
    ),
    'isp5': Stage(
        base=BASE,
        map=dict(
            name='ISP5',
            shape='E5',
            camera_data=['C2'],
            camera_data_spawn_point=['C2'],
            map_data="""
                -- ++ ++ ++ --
                -- ++ MB ++ --
                -- ++ -- ++ --
                ++ -- SP -- ++
                -- ++ ++ ++ --
            """,
            weight_data="""
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
            """,
            spawn_data=[{'battle': 0, 'boss': 1}],
        ),
        config_base='isp1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: 'clear_boss',
        },
    ),
    'isp6': Stage(
        base=BASE,
        map=dict(
            name='ISP6',
            shape='E5',
            camera_data=['C2'],
            camera_data_spawn_point=['C2'],
            map_data="""
                -- ++ ++ ++ --
                -- ++ MB ++ --
                -- ++ -- ++ --
                ++ -- SP -- ++
                -- ++ ++ ++ --
            """,
            weight_data="""
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
            """,
            spawn_data=[{'battle': 0, 'boss': 1}],
        ),
        config_base='isp1',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: 'clear_boss',
        },
    ),
    'sp1': Stage(
        base=BASE,
        map=dict(
            name='SP1',
            shape='I8',
            camera_data=['C3', 'C6', 'E3', 'E6'],
            camera_data_spawn_point=['E3'],
            camera_sight=(-2, -1, 3, 2),
            map_data="""
                -- -- -- -- -- -- -- -- --
                -- -- ME ++ ++ ++ -- ++ --
                ++ ME -- ++ MB ++ ME -- ME
                ++ -- -- ++ -- ++ -- -- --
                -- Me -- SP -- SP -- Me --
                ME -- -- -- __ -- -- -- ME
                -- ++ ME -- MS -- ME ++ ++
                -- -- -- Me ++ Me -- -- ++
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
            MAP_SIREN_TEMPLATE=['Laffey6'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 222),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            MAP_SWIPE_MULTIPLY=(1.062, 1.082),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.027, 1.046),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.997, 1.015),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_WALK_USE_CURRENT_FLEET=True,
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
            camera_data=['D2', 'D5', 'F5'],
            camera_data_spawn_point=['F2'],
            camera_sight=(-2, -1, 3, 2),
            map_data="""
                -- -- ME -- -- MS -- -- SP
                -- ++ ++ Me __ Me MS -- --
                -- ++ ++ Me -- MS -- -- SP
                -- -- ME -- -- -- ++ ++ ++
                -- ME -- -- ++ Me ++ MB ++
                ++ ++ ++ -- ME -- ++ -- ++
                -- -- ME -- -- -- -- -- ME
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
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['TashkentIdol', 'DidoIdol2'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            HOMO_STORAGE=((7, 4), [(179.668, 262.579), (1042.431, 262.579), (89.435, 660.188), (1122.585, 660.188)]),
            MAP_SWIPE_MULTIPLY=(1.246, 1.269),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.205, 1.227),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.17, 1.191),
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
            camera_data=['C4', 'E4', 'E6'],
            camera_data_spawn_point=['C6'],
            camera_sight=(-2, -1, 3, 2),
            map_data="""
                ++ ++ ++ ++ -- ++ ++ ++ --
                -- ++ MB ++ ME -- ME -- --
                ME ++ -- ++ -- Me -- ME --
                -- Me -- Me -- ++ -- ME ++
                -- MS __ MS -- Me -- -- ++
                -- -- MS -- -- -- -- ME --
                ++ -- -- -- ++ ++ ME ME --
                ++ SP -- SP ++ ++ -- -- --
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
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['SheffieldIdol', 'RoonIdol2'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
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
    'sp4': Stage(
        base=BASE,
        map=dict(
            name='SP4',
            shape='I8',
            camera_data=['C3', 'C6', 'F3', 'F6'],
            camera_data_spawn_point=['D2'],
            camera_sight=(-2, -1, 3, 2),
            map_data="""
                ++ ++ ++ SP -- SP ++ ++ ++
                -- Me -- -- -- -- -- Me --
                ME -- MS -- MS -- MS -- ME
                -- ++ -- Me __ Me -- ++ --
                -- Me -- ++ ++ ++ -- Me --
                ME -- -- ++ MB ++ -- -- ME
                ++ ME -- ++ -- ++ -- ME ++
                ++ ME -- -- -- -- -- ME ++
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
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Z23_5', 'Elizabeth3'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.251, 1.275),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.21, 1.232),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.175, 1.196),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'sp5': Stage(
        base=BASE,
        map=dict(
            name='SP5',
            shape='I9',
            camera_data=['C4', 'C7', 'F4', 'F7'],
            camera_data_spawn_point=['C7'],
            camera_sight=(-2, -1, 3, 2),
            map_data="""
                ++ ++ -- ++ ++ ++ -- ++ ++
                ++ ++ ME -- Me -- ME -- ++
                -- -- -- ME -- ME -- -- --
                -- ME -- ++ ++ ++ -- ME --
                ME ++ -- ++ MB ++ -- ++ ME
                -- ++ -- ++ -- ++ -- ++ --
                -- -- MS -- MS -- MS -- --
                Me -- -- -- __ -- -- -- Me
                -- Me ++ SP -- SP ++ Me --
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
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['GascogneIdol', 'TaihouIdol'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.012, 1.031),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.979, 0.997),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.95, 0.968),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default'],
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
}
