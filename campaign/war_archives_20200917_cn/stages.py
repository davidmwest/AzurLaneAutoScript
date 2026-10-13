"""
Stages of war_archives_20200917_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from campaign.event_20200917_cn.stages import STAGES as ARCHIVED
from module.campaign.stage import Stage, borrowed

BASE = '.campaign_base:CampaignBase'
PLAN = ['clear_siren', 'clear_enemy(scale=(2,))', 'clear_enemy(scale=(1,))', 'battle_default']

STAGES = {
    **borrowed(ARCHIVED, ['ht1', 'ht2', 'ht3', 'ht5', 't1', 't2', 't3', 't5']),
    'ht4': Stage(
        base=BASE,
        map=dict(
            name='HT4',
            shape='K9',
            camera_data=['D2', 'D5', 'D7', 'H2', 'H5', 'H7'],
            camera_data_spawn_point=['D2', 'D7'],
            portal_data=[('I5', 'C5'), ('C5', 'I5'), ('E5', 'E3'), ('E3', 'E5'), ('G5', 'G7'), ('G7', 'G5')],
            map_data="""
                Me -- -- ++ Me -- ME -- ME ++ ++
                -- MS -- ++ -- SP -- __ -- MS --
                -- -- Me ++ -- -- -- ME -- -- --
                ME -- ++ ++ ++ ++ ++ ++ ++ -- ME
                -- -- -- ++ -- MB -- ++ -- -- --
                ME -- ++ ++ ++ ++ ++ ++ ++ -- ME
                -- -- -- ME -- -- -- ++ Me -- --
                -- MS -- __ -- SP -- ++ -- MS --
                ++ ++ ME -- ME -- Me ++ -- -- Me
            """,
            map_data_loop="""
                Me -- -- ++ Me -- ME -- ME ++ ++
                -- MS -- -- -- SP -- __ -- MS --
                -- -- Me ++ -- -- -- ME -- -- --
                ME -- ++ ++ -- ++ -- ++ ++ -- ME
                -- -- -- ++ -- MB -- ++ -- -- --
                ME -- ++ ++ -- ++ -- ++ ++ -- ME
                -- -- -- ME -- -- -- ++ Me -- --
                -- MS -- __ -- SP -- -- -- MS --
                ++ ++ ME -- ME -- Me ++ -- -- Me
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 10 50 50 50 50 50
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
        config_base='ht1',
        config=dict(
            MAP_SIREN_TEMPLATE=['BB', 'SS'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_PORTAL=True,
            MAP_SWIPE_MULTIPLY_MINITOUCH=1.82,
            MAP_SWIPE_MULTIPLY=1.88,
        ),
        battle={
            0: [
                ('when', 'config.MAP_HAS_MOVABLE_ENEMY', [('do', 'fleet_2_push_forward')]),
                'clear_siren',
                ('when', 'map_is_clear_mode', ['clear_enemy(scale=(2,))', 'clear_enemy(scale=(1,))']),
                'battle_default',
            ],
            2: [
                'clear_siren',
                ('when', 'map_is_clear_mode', ['clear_enemy(scale=(2,))', 'clear_enemy(scale=(1,))']),
                'battle_default',
            ],
            5: 'fleet_boss.clear_boss',
        },
    ),
    'ht6': Stage(
        base=BASE,
        map=dict(
            name='HT6',
            shape='K10',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['D6', 'G6'],
            map_data="""
                -- -- -- ME -- Me -- ME -- -- --
                -- ++ ++ -- MS -- MS -- ++ ++ --
                -- ++ ME -- -- __ -- -- ME ++ --
                Me -- -- ++ ++ -- ++ ++ -- -- Me
                ++ ME -- ++ MS -- MS ++ -- ME ++
                ++ ME -- -- -- MB -- -- -- ME ++
                -- -- ++ Me -- -- -- Me ++ -- --
                -- ++ ++ ++ SP -- SP ++ ++ ++ --
                ++ -- -- ++ ++ -- ++ ++ -- -- ++
                -- -- -- ++ ++ -- ++ ++ -- -- --
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
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='ht1',
        config=dict(
            MAP_SIREN_TEMPLATE=['BB', 'CV', 'SS'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY_MINITOUCH=1.446,
            MAP_SWIPE_MULTIPLY=1.495,
        ),
        battle={
            0: [
                'fleet_2_protect',
                'clear_siren',
                'clear_enemy(scale=(2,))',
                'clear_enemy(scale=(1,))',
                'battle_default',
            ],
            2: PLAN,
            5: ['clear_enemy(scale=(1,))', 'clear_enemy(scale=(2,))', 'battle_default'],
            6: 'fleet_boss.clear_boss',
        },
    ),
    't4': Stage(
        base=BASE,
        map=dict(
            name='T4',
            shape='K9',
            camera_data=['D2', 'D5', 'D7', 'H2', 'H5', 'H7'],
            camera_data_spawn_point=['D2', 'D7'],
            portal_data=[('I5', 'C5'), ('C5', 'I5'), ('E5', 'E3'), ('E3', 'E5'), ('G5', 'G7'), ('G7', 'G5')],
            map_data="""
                Me -- -- ++ Me -- ME -- ME ++ ++
                -- MS -- ++ -- SP -- __ -- MS --
                -- -- Me ++ -- -- -- ME -- -- --
                ME -- ++ ++ ++ ++ ++ ++ ++ -- ME
                -- -- -- ++ -- MB -- ++ -- -- --
                ME -- ++ ++ ++ ++ ++ ++ ++ -- ME
                -- -- -- ME -- -- -- ++ Me -- --
                -- MS -- __ -- SP -- ++ -- MS --
                ++ ++ ME -- ME -- Me ++ -- -- Me
            """,
            map_data_loop="""
                Me -- -- ++ Me -- ME -- ME ++ ++
                -- MS -- -- -- SP -- __ -- MS --
                -- -- Me ++ -- -- -- ME -- -- --
                ME -- ++ ++ -- ++ -- ++ ++ -- ME
                -- -- -- ++ -- MB -- ++ -- -- --
                ME -- ++ ++ -- ++ -- ++ ++ -- ME
                -- -- -- ME -- -- -- ++ Me -- --
                -- MS -- __ -- SP -- -- -- MS --
                ++ ++ ME -- ME -- Me ++ -- -- Me
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 10 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50
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
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CL', 'SS'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_PORTAL=True,
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
            HOMO_EDGE_COLOR_RANGE=(0, 33),
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY_MINITOUCH=1.82,
            MAP_SWIPE_MULTIPLY=1.88,
        ),
        battle={
            0: [
                ('when', 'config.MAP_HAS_MOVABLE_ENEMY', [('do', 'fleet_2_push_forward')]),
                'clear_siren',
                'battle_default',
            ],
            4: 'clear_boss',
        },
    ),
    't6': Stage(
        base=BASE,
        map=dict(
            name='T6',
            shape='K10',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['D6', 'G6'],
            map_data="""
                -- -- -- ME -- Me -- ME -- -- --
                -- ++ ++ -- MS -- MS -- ++ ++ --
                -- ++ ME -- -- __ -- -- ME ++ --
                Me -- -- ++ ++ -- ++ ++ -- -- Me
                ++ ME -- ++ MS -- MS ++ -- ME ++
                ++ ME -- -- -- MB -- -- -- ME ++
                -- -- ++ Me -- -- -- Me ++ -- --
                -- ++ ++ ++ SP -- SP ++ ++ ++ --
                ++ -- -- ++ ++ -- ++ ++ -- -- ++
                -- -- -- ++ ++ -- ++ ++ -- -- --
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
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='t1',
        config=dict(
            MAP_SIREN_TEMPLATE=['CA', 'SS'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
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
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY_MINITOUCH=1.446,
            MAP_SWIPE_MULTIPLY=1.495,
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
