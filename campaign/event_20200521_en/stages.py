"""
Stages of event_20200521_en, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

PLAN = ['clear_siren', 'clear_enemy(scale=(2, 3))', 'battle_default']
PLAN_2 = ['clear_enemy(scale=(1,))', 'clear_enemy(scale=(2,))', 'battle_default']

STAGES = {
    'a2': Stage(
        map=dict(
            name='a2',
            shape='J6',
            map_data="""
                SP -- ME -- ME -- -- -- ME MB
                -- -- -- -- -- -- ++ -- - --
                ++ ++ ++ ME MS -- ++ __ ME ++
                SP -- -- -- ME -- ME -- -- ME
                -- -- ME -- -- -- -- ME -- --
                ++ ME ME -- ++ ME MM -- -- MB
            """,
        ),
        config=dict(
            POOR_MAP_DATA=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_SIREN=True,
            MAP_HAS_DYNAMIC_RED_BORDER=True,
            MAP_SIREN_COUNT=1,
            TRUST_EDGE_LINES=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 215),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (215, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
        ),
    ),
    'a3': Stage(
        map=dict(
            name='a3',
            shape='K7',
            map_data="""
                SP ++ ++ ++ ME -- -- -- ME -- MM
                -- -- -- -- -- -- ME -- -- -- --
                ME -- ++ ME -- -- -- -- ++ ++ --
                ME -- -- -- MS ++ __ -- MB ++ --
                -- -- ME -- -- -- -- -- -- -- --
                -- -- ++ ++ ME ME -- ME ++ ++ ++
                SP -- ++ MM ME -- -- -- -- ME MM
            """,
        ),
        config=dict(
            POOR_MAP_DATA=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_SIREN=True,
            MAP_HAS_DYNAMIC_RED_BORDER=True,
            MAP_SIREN_COUNT=1,
            MAP_GRID_CENTER_TOLERANCE=0.3,
            MAP_SIREN_TEMPLATE=['1', '2', '3', 'DD'],
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=50,
            MID_DIFF_RANGE_H=(45, 70),
            MID_DIFF_RANGE_V=(94, 100),
            TRUST_EDGE_LINES=True,
            VANISH_POINT_RANGE=((540, 740), (-4000, -2000)),
            DISTANCE_POINT_X_RANGE=((-2000, -1000),),
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 215),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
                'wlen': 100,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (215, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
        ),
    ),
    'b1': Stage(
        map=dict(
            name='b1',
            shape='H6',
            map_data="""
                ++ ++ ++ -- -- -- -- MB
                -- -- -- -- __ ME ME --
                ME -- ME ++ ++ ME -- --
                SP -- ME ++ ++ MS ME --
                ME -- -- -- -- -- -- --
                SP -- -- ME -- ME -- MB
            """,
        ),
        config=dict(
            SUBMARINE=0,
            FLEET_BOSS=0,
            POOR_MAP_DATA=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_SIREN=True,
            MAP_HAS_DYNAMIC_RED_BORDER=True,
            MAP_SIREN_COUNT=1,
            TRUST_EDGE_LINES=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 215),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (215, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
        ),
    ),
    'b2': Stage(
        map=dict(
            name='b2',
            shape='I7',
            map_data="""
                SP -- -- -- -- -- ME ++ MB
                -- ME -- -- ME -- -- ++ --
                -- -- ME ++ ++ ++ -- -- --
                ME __ -- ME ME ME -- MS --
                ME MS -- ++ ++ ++ -- -- --
                -- ME -- ME -- -- -- ++ --
                SP -- -- -- -- ME -- ++ MB
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
        config=dict(
            SUBMARINE=0,
            FLEET_BOSS=0,
            POOR_MAP_DATA=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_SIREN=True,
            MAP_HAS_DYNAMIC_RED_BORDER=True,
            MAP_SIREN_COUNT=2,
            TRUST_EDGE_LINES=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 215),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (215, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'b3': Stage(
        map=dict(
            name='b3',
            shape='I9',
            map_data="""
                SP -- ++ ++ -- -- -- ME --
                -- ME ++ ++ -- ME -- -- --
                -- -- -- -- -- -- ME ME --
                ME -- ME ME -- ME ++ ++ ++
                -- -- ++ __ -- -- -- MB ++
                -- ME ++ -- -- ME ++ ++ ++
                -- -- MS -- ++ ME -- ME --
                SP -- -- -- ++ -- -- ME --
                SP -- MS -- -- ME -- -- --
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
        config=dict(
            POOR_MAP_DATA=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_SIREN=True,
            MAP_SIREN_COUNT=2,
            MAP_HAS_DYNAMIC_RED_BORDER=True,
            MAP_GRID_CENTER_TOLERANCE=0.3,
            MAP_SIREN_TEMPLATE=['1', '2', '3', 'DD'],
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=50,
            MID_DIFF_RANGE_H=(45, 70),
            MID_DIFF_RANGE_V=(94, 100),
            TRUST_EDGE_LINES=True,
            VANISH_POINT_RANGE=((540, 740), (-4000, -2000)),
            DISTANCE_POINT_X_RANGE=((-2000, -1000),),
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 215),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
                'wlen': 100,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (215, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c1': Stage(
        map=dict(
            name='c1',
            shape='I5',
            map_data="""
                SP -- ++ ME -- ME ++ -- --
                -- ME -- -- ME -- ME ++ ME
                -- -- MS -- -- MS __ -- --
                -- ME -- -- ++ ME -- ME --
                SP -- -- ME ++ -- ME -- MB
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config=dict(
            POOR_MAP_DATA=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_SIREN=True,
            MAP_HAS_DYNAMIC_RED_BORDER=True,
            MAP_SIREN_COUNT=2,
            TRUST_EDGE_LINES=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 215),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (215, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'c2': Stage(
        map=dict(
            name='c2',
            shape='J6',
            camera_data=['F2', 'F4'],
            map_data="""
                SP -- ME MS ME -- -- -- ME MB
                -- -- -- -- -- -- ++ -- - --
                ++ ++ ++ ME MS -- ++ __ ME ++
                SP -- -- -- ME -- ME -- -- ME
                -- -- ME -- -- -- -- ME -- --
                ++ ME ME -- ++ ME MM -- -- MB
            """,
        ),
        config=dict(
            POOR_MAP_DATA=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_SIREN=True,
            MAP_HAS_DYNAMIC_RED_BORDER=True,
            MAP_SIREN_COUNT=2,
            TRUST_EDGE_LINES=True,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 215),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (215, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
        ),
    ),
    'c3': Stage(
        map=dict(
            name='c3',
            shape='K7',
            camera_data=['F2', 'F4', 'F6'],
            map_data="""
                SP ++ ++ ++ ME -- -- MS ME -- MM
                -- -- -- -- -- -- ME -- -- -- --
                ME -- ++ ME -- -- -- -- ++ ++ --
                ME -- -- -- MS ++ __ -- MB ++ --
                -- -- ME -- -- -- -- -- -- -- --
                -- -- ++ ++ ME ME -- ME ++ ++ ++
                SP -- ++ ++ ME -- -- -- -- ME MM
            """,
        ),
        config=dict(
            POOR_MAP_DATA=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_SIREN=True,
            MAP_SIREN_COUNT=2,
            MAP_GRID_CENTER_TOLERANCE=0.3,
            MAP_SIREN_TEMPLATE=['1', '2', '3', 'DD'],
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=50,
            MID_DIFF_RANGE_H=(45, 70),
            MID_DIFF_RANGE_V=(94, 100),
            TRUST_EDGE_LINES=True,
            VANISH_POINT_RANGE=((540, 740), (-4000, -2000)),
            DISTANCE_POINT_X_RANGE=((-2000, -1000),),
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 215),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
                'wlen': 100,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (215, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
        ),
    ),
    'd1': Stage(
        map=dict(
            name='d1',
            shape='H6',
            map_data="""
                ++ ++ ++ -- -- -- -- MB
                MS -- -- -- __ ME ME --
                ME -- ME ++ ++ MS -- --
                SP -- ME ++ ++ MS ME --
                ME -- -- -- -- -- -- --
                SP -- -- ME MS ME -- MB
            """,
        ),
        config=dict(
            SUBMARINE=0,
            FLEET_BOSS=0,
            POOR_MAP_DATA=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_SIREN=True,
            MAP_HAS_DYNAMIC_RED_BORDER=True,
            MAP_SIREN_COUNT=4,
        ),
    ),
    'd2': Stage(
        map=dict(
            name='d2',
            shape='I7',
            camera_data=['D2', 'D5', 'F3', 'F5'],
            map_data="""
                SP -- -- -- -- -- ME ++ MB
                -- ME -- MS ME -- -- ++ --
                -- -- ME ++ ++ ++ -- -- --
                ME __ -- ME ME ME -- MS --
                ME MS -- ++ ++ ++ -- -- --
                -- ME -- ME -- -- -- ++ --
                SP -- -- -- -- ME -- ++ MB
            """,
            weight_data="""
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 20 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config=dict(
            SUBMARINE=0,
            FLEET_BOSS=0,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_SIREN=True,
            MAP_HAS_DYNAMIC_RED_BORDER=False,
            MAP_SIREN_COUNT=3,
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=50,
            EDGE_LINES_HOUGHLINES_THRESHOLD=50,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 231),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (231, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
        ),
        battle={
            0: PLAN,
            5: PLAN_2,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        map=dict(
            name='d3',
            shape='I9',
            map_data="""
                SP -- ++ ++ -- -- -- ME --
                -- ME ++ ++ -- ME -- -- --
                -- -- -- -- -- -- ME ME --
                ME -- ME ME -- ME ++ ++ ++
                -- -- ++ __ -- -- -- MB ++
                -- ME ++ -- -- ME ++ ++ ++
                -- -- MS -- ++ ME -- ME --
                SP -- -- -- ++ -- -- ME --
                SP -- MS -- -- ME -- -- --
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config=dict(
            POOR_MAP_DATA=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_SIREN=True,
            MAP_SIREN_COUNT=3,
            MAP_HAS_DYNAMIC_RED_BORDER=True,
            MAP_GRID_CENTER_TOLERANCE=0.3,
            MAP_SIREN_TEMPLATE=['1', '2', '3', 'DD'],
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=50,
            MID_DIFF_RANGE_H=(45, 70),
            MID_DIFF_RANGE_V=(94, 100),
            TRUST_EDGE_LINES=True,
            VANISH_POINT_RANGE=((540, 740), (-4000, -2000)),
            DISTANCE_POINT_X_RANGE=((-2000, -1000),),
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 215),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
                'wlen': 100,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (215, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
        ),
        battle={
            0: PLAN,
            5: PLAN_2,
            6: 'fleet_boss.clear_boss',
        },
    ),
}
