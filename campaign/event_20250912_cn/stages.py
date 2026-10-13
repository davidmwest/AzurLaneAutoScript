"""
Stages of event_20250912_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']
PLAN_2 = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default']

STAGES = {
    'a1': Stage(
        base=BASE,
        map=dict(
            name='A1',
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- ++ -- SP -- SP ++ ++ ++
                -- ++ Me -- __ -- Me -- Me
                -- Me -- -- MS -- -- ME --
                -- -- -- MS -- MS -- -- --
                ME ME -- ++ ++ ++ ++ -- ++
                ++ ++ -- -- ME ++ ME -- ME
                ++ ++ -- -- -- -- -- MB --
                -- -- ME -- ME ++ ME -- ME
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
                {'battle': 3, 'enemy': 1, 'boss': 1},
                {'battle': 4, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=[],
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
            STAGE_INCREASE_AB=True,
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
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
            MAP_SWIPE_MULTIPLY=(1.212, 1.235),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.172, 1.194),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.138, 1.158),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            3: 'clear_boss',
        },
    ),
    'a2': Stage(
        base=BASE,
        map=dict(
            name='A2',
            shape='I8',
            camera_data=['D2', 'F2', 'E6'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- SP ++ -- ME -- ME ++ --
                SP -- -- MS -- -- -- ME --
                ++ -- MS -- ++ ++ ME -- ME
                -- MS -- __ MB ++ ++ -- ++
                -- Me -- Me -- ME -- -- ME
                -- ++ -- -- Me -- -- ME --
                -- ++ Me -- -- -- ME ++ --
                -- -- -- -- ME -- -- ++ --
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
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.224, 1.247),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.184, 1.206),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.149, 1.17),
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
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['D4'],
            map_data="""
                -- -- ++ ++ ++ ME -- ME -- --
                -- Me -- Me -- ME -- ++ ++ --
                -- -- MS -- -- -- -- MB ++ ME
                SP -- -- MS ++ Me __ -- ME --
                SP -- -- MS ++ ME -- -- -- --
                -- -- MS -- -- -- -- ME -- ME
                -- Me ++ ++ Me -- ++ -- ++ --
                -- -- ++ ++ -- -- ME -- ME --
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.127, 1.148),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.09, 1.11),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.058, 1.077),
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
            shape='J8',
            camera_data=['E3', 'E6', 'G3', 'G6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                -- -- ++ ++ ++ Me -- ++ -- --
                -- MB -- -- Me -- -- -- ME --
                ++ ++ -- Me -- -- -- ME -- --
                ++ ++ -- ++ ME __ ME ++ ++ --
                -- -- MS -- MS -- -- ME ++ ME
                -- Me -- MS -- Me -- -- -- --
                -- ++ -- -- -- ++ ME -- ME --
                -- ++ SP -- SP ++ -- ME ++ --
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
            MAP_SIREN_TEMPLATE=['BlackDragonBoss02'],
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
            STAGE_INCREASE_AB=True,
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
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.078, 1.099),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.043, 1.062),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.013, 1.031),
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
            camera_data=['E2', 'E6', 'G4'],
            camera_data_spawn_point=['G6'],
            map_data="""
                ++ -- ME ++ -- ++ ++ ++ -- --
                -- ++ -- -- ME -- MB -- -- --
                -- ME -- ME ++ ME -- ME ++ ++
                -- ME -- -- Me -- __ -- ME ++
                ++ ++ ME -- -- MS -- MS -- Me
                ++ ++ -- -- Me -- MS -- Me --
                -- ME -- Me ++ -- -- -- ++ --
                -- -- ME -- ++ SP -- SP ++ --
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
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['BlackDragonBoss02'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.086, 1.106),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.05, 1.069),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.019, 1.038),
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
            shape='K9',
            camera_data=['F2', 'F5', 'F7', 'D5'],
            camera_data_spawn_point=['I5'],
            map_data="""
                -- -- ++ -- -- ME -- ME -- ++ --
                -- ++ ++ ME -- ++ ++ ++ -- -- ++
                ++ ++ ++ ME -- -- Me -- MS -- ++
                -- -- ME -- -- Me ++ MS -- -- SP
                MB -- -- -- -- -- -- -- -- __ --
                -- -- ME -- -- Me ++ MS -- -- SP
                ++ ++ ++ ME -- -- Me -- MS -- ++
                -- ++ ++ ME -- ++ ++ ++ -- -- ++
                -- -- ++ -- -- ME -- ME -- ++ --
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
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['BlackDragonBoss02'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_WALK_USE_CURRENT_FLEET=False,
            HOMO_STORAGE=((8, 6), [(137.405, 104.804), (1046.044, 104.804), (-12.171, 652.093), (1166.717, 652.093)]),
            MAP_SWIPE_MULTIPLY=(1.109, 1.13),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.073, 1.093),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.042, 1.06),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c1': Stage(
        base=BASE,
        map=dict(
            name='C1',
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- ++ -- SP -- SP ++ ++ ++
                -- ++ Me -- __ -- Me -- Me
                -- Me -- -- MS -- -- ME --
                -- -- -- MS -- MS -- -- --
                ME ME -- ++ ++ ++ ++ -- ++
                ++ ++ -- -- ME ++ ME -- ME
                ++ ++ -- -- -- -- -- MB --
                -- -- ME -- ME ++ ME -- ME
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
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=[],
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
            STAGE_INCREASE_AB=True,
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
            MAP_SIREN_HAS_BOSS_ICON_SMALL=True,
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
    'c2': Stage(
        base=BASE,
        map=dict(
            name='C2',
            shape='I8',
            camera_data=['D2', 'F2', 'E6'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- SP ++ -- ME -- ME ++ --
                SP -- -- MS -- -- -- ME --
                ++ -- MS -- ++ ++ ME -- ME
                -- MS -- __ MB ++ ++ -- ++
                -- Me -- Me -- ME -- -- ME
                -- ++ -- -- Me -- -- ME --
                -- ++ Me -- -- -- ME ++ --
                -- -- -- -- ME -- -- ++ --
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
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.224, 1.247),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.184, 1.206),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.149, 1.17),
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
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['D4'],
            map_data="""
                -- -- ++ ++ ++ ME -- ME -- --
                -- Me -- Me -- ME -- ++ ++ --
                -- -- MS -- -- -- -- MB ++ ME
                SP -- -- MS ++ Me __ -- ME --
                SP -- -- MS ++ ME -- -- -- --
                -- -- MS -- -- -- -- ME -- ME
                -- Me ++ ++ Me -- ++ -- ++ --
                -- -- ++ ++ -- -- ME -- ME --
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
            MAP_SIREN_TEMPLATE=[],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.127, 1.148),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.09, 1.11),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.058, 1.077),
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
            camera_data=['E3', 'E6', 'G3', 'G6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                -- -- ++ ++ ++ Me -- ++ -- --
                -- MB -- -- Me -- -- -- ME --
                ++ ++ -- Me -- -- -- ME -- --
                ++ ++ -- ++ ME __ ME ++ ++ --
                -- -- MS -- MS -- -- ME ++ ME
                -- Me -- MS -- Me -- -- -- --
                -- ++ -- -- -- ++ ME -- ME --
                -- ++ SP -- SP ++ -- ME ++ --
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
            MAP_SIREN_TEMPLATE=['BlackDragonBoss02'],
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
            STAGE_INCREASE_AB=True,
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
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.078, 1.099),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.043, 1.062),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.013, 1.031),
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
            camera_data=['E2', 'E6', 'G4'],
            camera_data_spawn_point=['G6'],
            map_data="""
                ++ -- ME ++ -- ++ ++ ++ -- --
                -- ++ -- -- ME -- MB -- -- --
                -- ME -- ME ++ ME -- ME ++ ++
                -- ME -- -- Me -- __ -- ME ++
                ++ ++ ME -- -- MS -- MS -- Me
                ++ ++ -- -- Me -- MS -- Me --
                -- ME -- Me ++ -- -- -- ++ --
                -- -- ME -- ++ SP -- SP ++ --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50
                50 50 50 20 50 10 10 10 50 50
                50 50 50 20 10 10 10 10 10 50
                50 50 20 20 10 10 10 10 10 20
                50 50 50 20 10 10 05 10 10 20
                50 50 50 20 50 10 10 10 50 50
                50 50 50 50 50 10 10 10 50 50
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
            MAP_SIREN_TEMPLATE=['BlackDragonBoss02'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.086, 1.106),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.05, 1.069),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.019, 1.038),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        base=BASE,
        map=dict(
            name='D3',
            shape='K9',
            camera_data=['F2', 'F5', 'F7', 'D5'],
            camera_data_spawn_point=['I5'],
            map_data="""
                -- -- ++ -- -- ME -- ME -- ++ --
                -- ++ ++ ME -- ++ ++ ++ -- -- ++
                ++ ++ ++ ME -- -- Me -- MS -- ++
                -- -- ME -- -- Me ++ MS -- -- SP
                MB -- -- -- -- -- -- -- -- __ --
                -- -- ME -- -- Me ++ MS -- -- SP
                ++ ++ ++ ME -- -- Me -- MS -- ++
                -- ++ ++ ME -- ++ ++ ++ -- -- ++
                -- -- ++ -- -- ME -- ME -- ++ --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 10 10 10 10 10 10
                50 50 50 50 50 10 10 10 10 10 10
                50 50 50 50 50 10 10 10 10 10 10
                50 50 50 50 50 10 10 10 10 10 10
                50 50 50 50 50 10 10 10 10 10 10
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['BlackDragonBoss02'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_WALK_USE_CURRENT_FLEET=False,
            HOMO_STORAGE=((8, 6), [(137.405, 104.804), (1046.044, 104.804), (-12.171, 652.093), (1166.717, 652.093)]),
            MAP_SWIPE_MULTIPLY=(1.109, 1.13),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.073, 1.093),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.042, 1.06),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
}
