"""
Stages of event_20220210_cn, see module/campaign/stage.py
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
            shape='J5',
            camera_data=['D2', 'D3', 'G2', 'G3'],
            camera_data_spawn_point=['D3', 'D2'],
            map_data="""
                ME -- ME ++ ME Me ME -- Me --
                -- SP -- ++ -- ME ++ ++ ++ MB
                ME -- -- -- -- __ -- -- -- --
                -- SP -- ++ -- ME -- MS ++ MB
                ME -- ME ++ ME Me ME -- Me --
            """,
            weight_data="""
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
            MAP_SIREN_TEMPLATE=['DD'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.002, 1.021),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.97, 0.987),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.941, 0.958),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=180,
            HOMO_EDGE_COLOR_RANGE=(0, 17),
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
            shape='G7',
            camera_data=['D2', 'D5'],
            camera_data_spawn_point=['D2', 'D5'],
            map_data="""
                Me ++ -- -- ME -- MB
                ME ++ ME ME ++ ++ --
                MS -- SP -- ++ ++ --
                -- ME -- __ -- -- --
                Me ++ ++ -- SP ME ME
                -- ME ++ -- ME MS --
                MB -- -- -- Me -- ME
            """,
            weight_data="""
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
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.002, 1.021),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.97, 0.987),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.941, 0.958),
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
            shape='I6',
            camera_data=['D2', 'D4', 'F2', 'F4'],
            camera_data_spawn_point=['D2'],
            map_data="""
                ME -- ME -- -- ++ ++ ++ ME
                SP SP -- ME -- -- MS -- Me
                SP SP -- ++ -- ME -- ME --
                -- -- -- -- __ -- ++ __ ME
                ME Me ++ ME -- -- ME -- MB
                Me ME ++ ME MS -- -- -- MB
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
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.084, 1.105),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.049, 1.068),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.018, 1.036),
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
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                MS -- ME -- ME -- -- MB
                ME ++ ++ ME -- ++ -- --
                -- ME ++ -- ME ME -- ++
                ++ -- Me __ -- -- -- ++
                ++ -- ME -- ME -- MS ME
                SP ME -- -- ++ ++ ME --
                SP SP -- ME ++ ++ -- Me
            """,
            weight_data="""
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
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(0.989, 1.008),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.957, 0.975),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.929, 0.946),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=180,
            HOMO_EDGE_COLOR_RANGE=(0, 17),
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
            shape='F8',
            camera_data=['C2', 'C6'],
            camera_data_spawn_point=['C6'],
            map_data="""
                MS ++ -- Me -- ME
                -- ++ ME MS ++ ++
                ME -- ME -- ME ++
                ME -- __ __ -- ME
                -- ++ ++ ++ -- ME
                Me -- ME ME -- ++
                -- SP -- -- SP Me
                MB -- ME ME -- MB
            """,
            weight_data="""
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['CL', 'CAlightning'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(0.989, 1.008),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.957, 0.975),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.929, 0.946),
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
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['D2', 'E2'],
            map_data="""
                MS -- ++ MB MB ++ -- MS
                -- ME ++ -- -- ++ ME --
                ME SP -- -- -- -- SP ME
                -- -- ME Me -- ME -- --
                -- ++ ++ ++ __ Me -- ++
                ME -- ME Me -- ++ ME ME
                -- ME -- ME -- -- ME --
            """,
            weight_data="""
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
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CAlightning'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(0.982, 1.001),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.95, 0.967),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.922, 0.939),
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
            shape='J5',
            camera_data=['D2', 'D3', 'G2', 'G3'],
            camera_data_spawn_point=['D3', 'D2'],
            map_data="""
                ME -- ME ++ ME Me ME -- Me --
                -- SP -- ++ -- ME ++ ++ ++ MB
                ME -- -- -- -- __ -- -- -- --
                -- SP -- ++ -- ME -- MS ++ MB
                ME -- ME ++ ME Me ME -- Me --
            """,
            weight_data="""
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
            MAP_SIREN_TEMPLATE=['CL', 'CA', 'BB'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.002, 1.021),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.97, 0.987),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.941, 0.958),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=180,
            HOMO_EDGE_COLOR_RANGE=(0, 17),
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
            shape='G7',
            camera_data=['D2', 'D5'],
            camera_data_spawn_point=['D2', 'D5'],
            map_data="""
                Me ++ -- -- ME -- MB
                ME ++ ME ME ++ ++ --
                MS -- SP -- ++ ++ --
                -- ME -- __ -- -- --
                Me ++ ++ -- SP ME ME
                -- ME ++ -- ME MS --
                MB -- -- -- Me -- ME
            """,
            weight_data="""
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
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CA', 'CV'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.002, 1.021),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.97, 0.987),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.941, 0.958),
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
            shape='I6',
            camera_data=['D2', 'D4', 'F2', 'F4'],
            camera_data_spawn_point=['D2'],
            map_data="""
                ME -- ME -- -- ++ ++ ++ ME
                SP SP -- ME -- -- MS -- Me
                SP SP -- ++ -- ME -- ME --
                -- -- -- -- __ -- ++ __ ME
                ME Me ++ ME -- -- ME -- MB
                Me ME ++ ME MS -- -- -- MB
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
            MAP_SIREN_TEMPLATE=['CL', 'CApurple', 'BBpurple'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.084, 1.105),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.049, 1.068),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.018, 1.036),
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
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                MS -- ME -- ME MS -- MB
                ME ++ ++ ME -- ++ -- --
                -- ME ++ -- ME ME -- ++
                ++ -- Me __ -- -- -- ++
                ++ -- ME -- ME -- MS ME
                SP ME -- -- ++ ++ ME --
                SP SP -- ME ++ ++ -- Me
            """,
            weight_data="""
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
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'CAlightning', 'Intruder'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(0.989, 1.008),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.957, 0.975),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.929, 0.946),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=180,
            HOMO_EDGE_COLOR_RANGE=(0, 17),
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
            shape='F8',
            camera_data=['C2', 'C6'],
            camera_data_spawn_point=['C6'],
            map_data="""
                MS ++ -- Me -- ME
                -- ++ ME MS ++ ++
                ME MS ME -- ME ++
                ME -- __ __ -- ME
                -- ++ ++ ++ -- ME
                Me -- ME ME -- ++
                -- SP -- -- SP Me
                MB -- ME ME -- MB
            """,
            weight_data="""
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
                50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['CAlightning', 'BBlightning', 'Intruder'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(0.989, 1.008),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.957, 0.975),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.929, 0.946),
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
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['D2', 'E2'],
            map_data="""
                MS -- ++ MB MB ++ -- MS
                -- ME ++ -- -- ++ ME --
                ME SP -- -- -- -- SP ME
                -- -- ME Me -- ME -- --
                -- ++ ++ ++ __ Me -- ++
                ME -- ME Me -- ++ ME ME
                -- ME -- ME MS -- ME --
            """,
            weight_data="""
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
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_SIREN_TEMPLATE=['BBlightning', 'CVlightning', 'Intruder'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(0.982, 1.001),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.95, 0.967),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.922, 0.939),
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
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['F5', 'D5'],
            map_data="""
                -- -- ME -- -- -- ME -- --
                -- Me -- ME __ ME -- Me --
                ME -- ++ ++ Me ++ ++ -- ME
                -- ME ++ ME -- ME ++ ME --
                -- -- ME ++ ++ ++ ME -- --
                MS -- -- ME MB ME -- -- MS
                MS -- -- SP -- SP -- -- MS
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
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['CAlightning', 'BBlightning', 'CVlightning'],
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
            MAP_SWIPE_MULTIPLY=(1.006, 1.025),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.973, 0.991),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.945, 0.962),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=180,
            HOMO_EDGE_COLOR_RANGE=(0, 17),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=2)', 'battle_default'],
            5: PLAN,
            7: 'fleet_boss.clear_boss',
        },
    ),
}
