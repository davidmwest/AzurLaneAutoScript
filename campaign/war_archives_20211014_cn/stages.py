"""
Stages of war_archives_20211014_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
PLAN = ['clear_siren', 'battle_default']

STAGES = {
    'sp1': Stage(
        base=BASE,
        map=dict(
            name='SP1',
            shape='G7',
            camera_data=['A3', 'A5'],
            camera_data_spawn_point=['A3'],
            camera_sight=(-2, -1, 3, 2),
            map_data="""
                ++ ++ ++ -- MS ME --
                -- ME -- ME -- ME --
                SP -- ME -- __ ME ++
                -- ME -- ++ -- -- MB
                SP -- -- -- -- ME --
                ++ ++ -- -- ME -- ME
                ++ ++ ME -- -- -- --
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
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['SheffieldIdol'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            DETECTION_BACKEND='perspective',
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
            EDGE_LINES_HOUGHLINES_THRESHOLD=40,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (150, 243),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (246, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_EDGE_COLOR_RANGE=(0, 9),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=180,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
        ),
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
            camera_data=['C2', 'C5', 'F2', 'F5'],
            camera_data_spawn_point=['A5'],
            camera_sight=(-2, -1, 3, 2),
            map_covered=['E3'],
            map_data="""
                -- -- -- -- -- -- ME -- --
                -- ME -- ME -- ME -- ME --
                -- -- ME -- -- -- ++ ++ --
                SP -- -- -- ++ __ -- -- MB
                SP -- ME -- -- ME ME -- --
                -- ++ -- ME ++ ME -- ++ ++
                -- ME ME -- ME -- ME ++ ++
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
            MAP_SIREN_TEMPLATE=['HipperIdol', 'ClevelandIdol'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(1.209, 1.231),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.169, 1.19),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.135, 1.155),
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'sp3': Stage(
        base=BASE,
        map=dict(
            name='SP3',
            shape='I7',
            camera_data=['C2', 'C5', 'F2', 'F5'],
            camera_data_spawn_point=['I4'],
            camera_sight=(-2, -1, 3, 2),
            map_covered=['E3'],
            map_data="""
                -- ME ++ ++ ++ ME -- -- --
                -- MS -- MB MS -- -- ME ++
                ++ -- ME -- -- ME ME -- --
                -- ME -- -- ++ __ -- ++ ++
                ME ME ME -- -- ME -- ME ME
                -- ME ++ ++ ME -- ME ME --
                ME -- ++ ++ SP SP -- -- --
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
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['HipperIdol', 'ClevelandIdol'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(1.209, 1.231),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.169, 1.19),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.135, 1.155),
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'sp4': Stage(
        base=BASE,
        map=dict(
            name='SP4',
            shape='I7',
            camera_data=['C2', 'C5', 'F2', 'F5'],
            camera_data_spawn_point=['C5'],
            camera_sight=(-2, -1, 3, 2),
            map_covered=['E3'],
            map_data="""
                -- ++ ++ -- -- -- ME -- ++
                ME ME -- MS -- -- -- MS ++
                -- -- ME -- -- -- -- ME --
                SP -- -- -- ++ -- -- -- MB
                SP -- ME -- __ ME ME -- --
                -- ++ -- ME -- -- -- ++ ++
                -- ME ME -- ME -- ME ++ ++
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
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['ClevelandIdol', 'HipperIdol', 'SpeeIdol'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(1.209, 1.231),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.169, 1.19),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.135, 1.155),
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'sp5': Stage(
        base=BASE,
        map=dict(
            name='SP5',
            shape='I7',
            camera_data=['C2', 'C5', 'F2', 'F5'],
            camera_data_spawn_point=['C4'],
            camera_sight=(-2, -1, 3, 2),
            map_covered=['E3'],
            map_data="""
                -- -- -- ++ ++ ++ ME -- --
                -- ME -- MB ME -- -- ++ ++
                ME ME ME -- -- ME ME ME --
                ME -- -- -- ++ __ -- -- --
                ME ME -- ME -- ME -- ++ ++
                -- ME -- ME -- -- -- ++ ++
                ME -- -- SP SP -- ME ME --
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
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['ClevelandIdol', 'HipperIdol', 'SpeeIdol'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=(1.209, 1.231),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.169, 1.19),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.135, 1.155),
        ),
        battle={
            0: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
}
