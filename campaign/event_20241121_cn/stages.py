"""
Stages of event_20241121_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']

STAGES = {
    't1': Stage(
        base=BASE,
        map=dict(
            name='T1',
            shape='I8',
            camera_data=['E3', 'E6', 'F3', 'F6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                -- ++ -- -- -- -- -- -- --
                -- -- ME ++ ++ ++ -- -- --
                -- ME -- MS -- -- -- ME --
                -- -- -- -- Me -- ME -- ME
                -- Me -- SP ++ ++ -- -- --
                -- -- -- SP ++ ++ -- ME ++
                -- ME -- -- Me ME __ -- ++
                -- ++ ME -- -- -- -- -- MB
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
            MAP_SIREN_TEMPLATE=['ToLoveNana03'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAGE_ENTRANCE=['half', '20240725'],
            MAP_CHAPTER_SWITCH_20241219=True,
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
            MAP_SWIPE_MULTIPLY=(1.107, 1.128),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.071, 1.091),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.04, 1.059),
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
            camera_data=['E2', 'E5', 'F2', 'F5'],
            camera_data_spawn_point=['F2'],
            map_data="""
                ++ ++ -- -- -- -- -- -- SP
                ++ ++ Me -- Me -- MS -- --
                -- ME -- -- ++ -- -- -- SP
                -- -- Me -- ++ -- ++ ++ ++
                -- ME ++ -- -- __ -- -- MB
                -- -- -- -- ME -- ME -- --
                -- ME ++ ME -- ME -- ME ++
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
            MAP_SIREN_TEMPLATE=['ToLoveNana03', 'ToLoveNana01'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.212, 1.235),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.172, 1.194),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.138, 1.158),
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
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['D2'],
            map_covered=['D4'],
            map_data="""
                -- Me ++ ++ ++ -- -- ++ ++
                ++ -- SP -- SP -- Me ++ ++
                -- -- -- -- -- -- -- ME --
                Me -- -- MS -- Me -- -- --
                -- __ MS -- ++ ++ ME -- ++
                -- Me -- -- ++ ++ ME -- --
                MB ++ ME -- -- ME -- -- ++
                -- ++ -- ME -- -- -- ME --
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
            MAP_SIREN_TEMPLATE=['ToLoveNana01', 'ToLoveHaruna04'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.181, 1.203),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.142, 1.163),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.109, 1.129),
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
            camera_data_spawn_point=['D4'],
            map_covered=['D4'],
            map_data="""
                ++ -- -- -- -- -- -- ME ++
                ME -- ++ ++ -- ME -- -- ++
                -- -- ++ ++ -- ++ ME -- --
                SP -- -- MS -- Me -- -- ME
                -- -- MS -- Me -- ++ -- --
                SP -- -- ++ ++ ++ -- ME --
                ++ ME __ Me -- Me -- -- ME
                MB -- -- -- -- -- -- ME --
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
            MAP_SIREN_TEMPLATE=['ToLoveHaruna04', 'ToLoveGoldenDarkness05'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.112, 1.132),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.075, 1.095),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.044, 1.062),
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
            shape='I9',
            camera_data=['E3', 'E5'],
            camera_data_spawn_point=['E7'],
            map_data="""
                -- ++ ++ -- -- -- ++ ++ --
                -- ++ ++ -- MB -- ++ ++ --
                ++ ME ME -- -- -- ME ME ++
                -- -- -- Me -- Me -- -- --
                -- ME ++ -- -- -- ++ ME --
                -- ME ++ MS -- MS ++ ME --
                -- -- Me -- MS -- Me -- --
                ++ -- -- -- __ -- -- -- ++
                ++ ++ ++ SP -- SP ++ ++ ++
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
            MAP_SIREN_TEMPLATE=['ToLoveGoldenDarkness05', 'ToLoveYui02'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.034, 1.053),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.0, 1.018),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.971, 0.988),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default'],
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'ttl2': Stage(
        base=BASE,
        map=dict(
            name='TTL2',
            shape='E5',
            camera_data=['C2'],
            camera_data_spawn_point=['C2'],
            map_data="""
                ++ ++ -- ++ ++
                ++ ++ MB ++ ++
                -- -- -- -- --
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
        config_base='ttl1',
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
    'ttl3': Stage(
        base=BASE,
        map=dict(
            name='TTL3',
            shape='E5',
            camera_data=['C2'],
            camera_data_spawn_point=['C2'],
            map_data="""
                ++ ++ -- ++ ++
                ++ ++ MB ++ ++
                -- -- -- -- --
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
        config_base='ttl1',
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
    'ttl4': Stage(
        base=BASE,
        map=dict(
            name='TTL4',
            shape='E5',
            camera_data=['C2'],
            camera_data_spawn_point=['C2'],
            map_data="""
                ++ ++ -- ++ ++
                ++ ++ MB ++ ++
                -- -- -- -- --
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
        config_base='ttl1',
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
    'ttl5': Stage(
        base=BASE,
        map=dict(
            name='TTL5',
            shape='E5',
            camera_data=['C2'],
            camera_data_spawn_point=['C2'],
            map_data="""
                ++ ++ -- ++ ++
                ++ ++ MB ++ ++
                -- -- -- -- --
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
        config_base='ttl1',
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
}
