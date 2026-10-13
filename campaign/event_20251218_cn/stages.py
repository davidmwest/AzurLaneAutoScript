"""
Stages of event_20251218_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']
PLAN_2 = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default']

STAGES = {
    'a1': Stage(
        map=dict(
            name='A1',
            shape='J8',
            camera_data=['D3', 'D6', 'G3', 'G6'],
            camera_data_spawn_point=['G2'],
            map_data="""
                ++ -- -- -- -- -- ++ -- SP --
                ++ ME ++ ++ ++ Me -- -- -- SP
                -- -- -- -- Me -- -- MS -- --
                ME -- ME -- -- -- __ -- ++ ++
                ++ -- ++ ++ -- MS -- -- ++ ++
                -- -- -- ++ ME -- ++ Me -- --
                -- MB -- -- -- -- -- -- -- --
                -- -- -- ++ ME -- ME ++ ++ ++
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
                {'battle': 3, 'enemy': 1, 'boss': 1},
                {'battle': 4, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Vboss_Star'],
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
            HOMO_STORAGE=((8, 6), [(137.405, 104.804), (1046.044, 104.804), (-12.171, 652.093), (1166.717, 652.093)]),
            HOMO_EDGE_COLOR_RANGE=(0, 17),
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.232, 1.255),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.191, 1.213),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.156, 1.177),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            3: 'clear_boss',
        },
    ),
    'a2': Stage(
        map=dict(
            name='A2',
            shape='J8',
            camera_data=['E3', 'E6', 'F3', 'F6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                -- -- -- -- -- ++ ME ++ -- --
                -- -- MB -- -- ME -- ME -- --
                ++ ++ -- ++ ++ -- -- -- ME --
                ++ -- __ -- ++ Me -- ++ ++ ++
                -- MS -- MS -- -- -- Me -- --
                -- -- MS -- -- Me -- -- ME --
                ++ -- -- -- -- ++ -- ME ++ ++
                ++ SP -- SP -- ME -- -- ++ ++
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
            MAP_SIREN_TEMPLATE=['Vboss_Star'],
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
        map=dict(
            name='A3',
            shape='K10',
            camera_data=['F3', 'F6'],
            camera_data_spawn_point=['F6'],
            map_data="""
                -- ++ ++ ++ -- -- -- ++ ++ ++ --
                -- ++ -- Me -- MB -- Me -- ++ --
                -- -- ME -- Me -- Me -- ME -- --
                -- -- ++ MS -- __ -- MS ++ -- --
                -- -- ++ -- -- MS -- -- ++ -- --
                ++ ++ ME -- -- -- -- -- ME ++ ++
                ++ ++ -- -- SP -- SP -- -- ++ ++
                -- -- ME -- ++ ++ ++ -- ME -- --
                -- ++ -- -- ++ ++ ++ -- -- ++ --
                -- -- -- -- ++ ++ ++ -- -- -- --
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
                50 50 50 50 50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['Vboss_Star'],
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
        map=dict(
            name='B1',
            shape='J8',
            camera_data=['D3', 'D6', 'G3', 'G6'],
            camera_data_spawn_point=['G2'],
            map_data="""
                ++ -- -- -- -- -- ++ -- SP --
                ++ ME ++ ++ ++ Me -- -- -- SP
                -- -- -- -- Me -- -- MS -- --
                ME -- ME -- -- -- __ -- ++ ++
                ++ -- ++ ++ -- MS -- -- ++ ++
                -- -- -- ++ ME -- ++ Me -- --
                -- MB -- -- -- -- -- -- -- --
                -- -- -- ++ ME -- ME ++ ++ ++
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
                {'battle': 0, 'enemy': 9, 'siren': 1},
                {'battle': 1},
                {'battle': 2},
                {'battle': 3},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Vboss_Hermit', 'Vboss_Lovers'],
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
            HOMO_STORAGE=((8, 6), [(137.405, 104.804), (1046.044, 104.804), (-12.171, 652.093), (1166.717, 652.093)]),
            HOMO_EDGE_COLOR_RANGE=(0, 17),
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.217, 1.24),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.177, 1.199),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.143, 1.163),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b2': Stage(
        map=dict(
            name='B2',
            shape='J8',
            camera_data=['E3', 'E6', 'F3', 'F6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                -- -- -- -- -- ++ ME ++ -- --
                -- -- MB -- -- ME -- ME -- --
                ++ ++ -- ++ ++ -- -- -- ME --
                ++ -- __ -- ++ Me -- ++ ++ ++
                -- MS -- MS -- -- -- Me -- --
                -- -- MS -- -- Me -- -- ME --
                ++ -- -- -- -- ++ -- ME ++ ++
                ++ SP -- SP -- ME -- -- ++ ++
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
                {'battle': 0, 'enemy': 9, 'siren': 1},
                {'battle': 1},
                {'battle': 2},
                {'battle': 3},
                {'battle': 4},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Vboss_Hermit', 'Vboss_Chariot'],
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
    'b3': Stage(
        map=dict(
            name='B3',
            shape='K10',
            camera_data=['F3', 'F6'],
            camera_data_spawn_point=['F6'],
            map_data="""
                -- ++ ++ ++ -- -- -- ++ ++ ++ --
                -- ++ -- Me -- MB -- Me -- ++ --
                -- -- ME -- Me -- Me -- ME -- --
                -- -- ++ MS -- __ -- MS ++ -- --
                -- -- ++ -- -- MS -- -- ++ -- --
                ++ ++ ME -- -- -- -- -- ME ++ ++
                ++ ++ -- -- SP -- SP -- -- ++ ++
                -- -- ME -- ++ ++ ++ -- ME -- --
                -- ++ -- -- ++ ++ ++ -- -- ++ --
                -- -- -- -- ++ ++ ++ -- -- -- --
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
                50 50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 9, 'siren': 2},
                {'battle': 1},
                {'battle': 2},
                {'battle': 3},
                {'battle': 4},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Vboss_Lovers', 'Vboss_Chariot'],
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
    'c1': Stage(
        map=dict(
            name='C1',
            shape='J8',
            camera_data=['D3', 'D6', 'G3', 'G6'],
            camera_data_spawn_point=['G2'],
            map_data="""
                ++ -- -- -- -- -- ++ -- SP --
                ++ ME ++ ++ ++ Me -- -- -- SP
                -- -- -- -- Me -- -- MS -- --
                ME -- ME -- -- -- __ -- ++ ++
                ++ -- ++ ++ -- MS -- -- ++ ++
                -- -- -- ++ ME -- ++ Me -- --
                -- MB -- -- -- -- -- -- -- --
                -- -- -- ++ ME -- ME ++ ++ ++
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
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Vboss_Star'],
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
            HOMO_STORAGE=((8, 6), [(137.405, 104.804), (1046.044, 104.804), (-12.171, 652.093), (1166.717, 652.093)]),
            HOMO_EDGE_COLOR_RANGE=(0, 17),
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.232, 1.255),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.191, 1.213),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.156, 1.177),
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
            shape='J8',
            camera_data=['E3', 'E6', 'F3', 'F6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                -- -- -- -- -- ++ ME ++ -- --
                -- -- MB -- -- ME -- ME -- --
                ++ ++ -- ++ ++ -- -- -- ME --
                ++ -- __ -- ++ Me -- ++ ++ ++
                -- MS -- MS -- -- -- Me -- --
                -- -- MS -- -- Me -- -- ME --
                ++ -- -- -- -- ++ -- ME ++ ++
                ++ SP -- SP -- ME -- -- ++ ++
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
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Vboss_Star'],
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
        map=dict(
            name='C3',
            shape='K10',
            camera_data=['F3', 'F6'],
            camera_data_spawn_point=['F6'],
            map_data="""
                -- ++ ++ ++ -- -- -- ++ ++ ++ --
                -- ++ -- Me -- MB -- Me -- ++ --
                -- -- ME -- Me -- Me -- ME -- --
                -- -- ++ MS -- __ -- MS ++ -- --
                -- -- ++ -- -- MS -- -- ++ -- --
                ++ ++ ME -- -- -- -- -- ME ++ ++
                ++ ++ -- -- SP -- SP -- -- ++ ++
                -- -- ME -- ++ ++ ++ -- ME -- --
                -- ++ -- -- ++ ++ ++ -- -- ++ --
                -- -- -- -- ++ ++ ++ -- -- -- --
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
                50 50 50 50 50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['Vboss_Star'],
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
        map=dict(
            name='D1',
            shape='J8',
            camera_data=['D3', 'D6', 'G3', 'G6'],
            camera_data_spawn_point=['G2'],
            map_data="""
                ++ -- -- -- -- -- ++ -- SP --
                ++ ME ++ ++ ++ Me -- -- -- SP
                -- -- -- -- Me -- -- MS -- --
                ME -- ME -- -- -- __ -- ++ ++
                ++ -- ++ ++ -- MS -- -- ++ ++
                -- -- -- ++ ME -- ++ Me -- --
                -- MB -- -- -- -- -- -- -- --
                -- -- -- ++ ME -- ME ++ ++ ++
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
                {'battle': 0, 'enemy': 9, 'siren': 2},
                {'battle': 1},
                {'battle': 2},
                {'battle': 3},
                {'battle': 4},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Vboss_Hermit', 'Vboss_Lovers'],
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
            HOMO_STORAGE=((8, 6), [(137.405, 104.804), (1046.044, 104.804), (-12.171, 652.093), (1166.717, 652.093)]),
            HOMO_EDGE_COLOR_RANGE=(0, 17),
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.217, 1.24),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.177, 1.199),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.143, 1.163),
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
            shape='J8',
            camera_data=['E3', 'E6', 'F3', 'F6'],
            camera_data_spawn_point=['E6'],
            map_data="""
                -- -- -- -- -- ++ ME ++ -- --
                -- -- MB -- -- ME -- ME -- --
                ++ ++ -- ++ ++ -- -- -- ME --
                ++ -- __ -- ++ Me -- ++ ++ ++
                -- MS -- MS -- -- -- Me -- --
                -- -- MS -- -- Me -- -- ME --
                ++ -- -- -- -- ++ -- ME ++ ++
                ++ SP -- SP -- ME -- -- ++ ++
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
                {'battle': 0, 'enemy': 9, 'siren': 3},
                {'battle': 1},
                {'battle': 2},
                {'battle': 3},
                {'battle': 4},
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Vboss_Hermit', 'Vboss_Chariot'],
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
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        map=dict(
            name='D3',
            shape='K10',
            camera_data=['F3', 'F6'],
            camera_data_spawn_point=['F6'],
            map_data="""
                -- ++ ++ ++ -- -- -- ++ ++ ++ --
                -- ++ -- Me -- MB -- Me -- ++ --
                -- -- ME -- Me -- Me -- ME -- --
                -- -- ++ MS -- __ -- MS ++ -- --
                -- -- ++ -- -- MS -- -- ++ -- --
                ++ ++ ME -- -- -- -- -- ME ++ ++
                ++ ++ -- -- SP -- SP -- -- ++ ++
                -- -- ME -- ++ ++ ++ -- ME -- --
                -- ++ -- -- ++ ++ ++ -- -- ++ --
                -- -- -- -- ++ ++ ++ -- -- -- --
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
                50 50 50 50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 9, 'siren': 3},
                {'battle': 1},
                {'battle': 2},
                {'battle': 3},
                {'battle': 4},
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Vboss_Lovers', 'Vboss_Chariot'],
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
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'sp': Stage(
        map=dict(
            name='SP',
            shape='I8',
            camera_data=['D3', 'D6', 'F3', 'F6'],
            camera_data_spawn_point=['F2'],
            map_data="""
                ++ ++ ++ -- -- -- -- SP --
                -- ME -- -- -- MS -- -- SP
                -- -- ME ++ -- -- MS -- --
                ME -- -- -- ME __ -- MS --
                -- ME -- ME ++ -- ++ ++ ME
                ++ -- -- -- -- -- ++ ++ --
                -- MB -- ++ ME -- ME -- --
                -- -- -- ++ -- ME ++ ++ ++
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
                {'battle': 0, 'enemy': 10, 'siren': 3},
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
            MAP_SIREN_TEMPLATE=['Vboss_Hermit', 'Vboss_Lovers', 'Vboss_Chariot'],
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
            HOMO_STORAGE=((8, 6), [(137.405, 104.804), (1046.044, 104.804), (-12.171, 652.093), (1166.717, 652.093)]),
            HOMO_EDGE_COLOR_RANGE=(0, 17),
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.18, 1.202),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.141, 1.162),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.108, 1.128),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_IS_ONE_TIME_STAGE=True,
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=2)', 'battle_default'],
            5: PLAN,
            7: 'fleet_boss.clear_boss',
        },
    ),
}
