"""
Stages of war_archives_20210527_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from campaign.event_20210527_cn.stages import STAGES as ARCHIVED
from module.campaign.stage import Stage, borrowed

BASE = '..campaign_war_archives.campaign_base:CampaignBase'
PLAN = ['clear_siren', 'battle_default']
PLAN_2 = [
    'clear_siren',
    'clear_enemy(scale=(1,))',
    'clear_enemy(scale=(2,))',
    'clear_enemy(scale=(3,))',
    'battle_default',
]

STAGES = {
    **borrowed(ARCHIVED, ['b1', 'd1'], base='..campaign_war_archives.campaign_base:CampaignBase'),
    'a1': Stage(
        base=BASE,
        map=dict(
            name='A1',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['F2'],
            map_data="""
                ++ ++ -- ME -- Me ++ -- --
                ++ ++ Me -- -- -- -- -- SP
                ME -- -- -- ++ MS -- ME SP
                -- -- ME -- ++ __ ME -- ++
                MB -- ++ MS -- ME -- -- --
                -- -- -- -- ME -- Me ++ ME
                -- ++ -- ME -- -- -- ++ --
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
                {'battle': 3, 'enemy': 1, 'boss': 1},
                {'battle': 4, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Dewey'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=1.778,
            MAP_SWIPE_MULTIPLY_MINITOUCH=1.719,
        ),
        battle={
            0: PLAN,
            3: 'clear_boss',
        },
    ),
    'a2': Stage(
        base=BASE,
        map=dict(
            name='A2',
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['E6', 'D6'],
            map_data="""
                -- ++ ++ ++ -- MB -- ++
                -- ME -- ME -- ME -- --
                ++ -- MS -- ME ++ Me --
                -- Me ++ -- Me -- -- --
                ME -- ++ ME -- __ ME MS
                -- MS -- Me -- ++ -- --
                ++ -- ME -- -- -- ME ++
                ++ -- -- SP SP -- ++ ++
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
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='a1',
        config=dict(
            MAP_SIREN_TEMPLATE=['DD'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=1.512,
            MAP_SWIPE_MULTIPLY_MINITOUCH=1.462,
        ),
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
            camera_data_spawn_point=['G6', 'D6'],
            map_data="""
                ++ ++ -- ++ ++ -- -- ME ++ ++
                -- -- MB -- ME -- MS -- ++ ++
                -- ME -- ME MS Me -- ME -- --
                -- ++ -- ++ -- __ -- Me -- MS
                ME ++ -- ++ ME Me ++ -- ME --
                -- -- -- Me -- -- ME -- -- --
                -- ME -- -- SP ++ -- ++ SP ++
                -- ++ ++ ++ -- SP -- SP -- ++
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
            MAP_SIREN_TEMPLATE=['CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=1.512,
            MAP_SWIPE_MULTIPLY_MINITOUCH=1.462,
        ),
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
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['G6'],
            map_data="""
                ++ ++ -- ME -- -- MS ++ ++ ++
                ++ ++ -- ++ ++ -- -- -- -- ME
                -- Me -- -- ME -- Me -- ++ --
                ME ++ MS MB -- -- ME -- ++ --
                -- ++ -- -- ME __ -- MS ++ ME
                -- ++ -- Me -- -- Me -- -- --
                ME -- ME -- -- ++ ++ -- -- SP
                ++ ++ ++ MS -- ME -- -- SP ++
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
            MAP_SIREN_TEMPLATE=['Atlanta', 'CL'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=1.523,
            MAP_SWIPE_MULTIPLY_MINITOUCH=1.472,
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'b3': Stage(
        base=BASE,
        map=dict(
            name='B3',
            shape='I9',
            camera_data=['D2', 'D6', 'D7', 'F2', 'F6', 'F7'],
            camera_data_spawn_point=['F7', 'D7'],
            map_data="""
                ++ -- ME -- -- -- ME -- ++
                ++ ++ ++ -- MB -- ++ ++ ++
                ME -- -- -- ++ -- -- -- ME
                -- ME Me -- Me -- Me ME --
                -- ++ ++ -- __ -- ++ ++ --
                MS ++ ++ -- Me -- ++ ++ MS
                -- ME MS -- -- -- MS ME --
                ME Me -- ++ -- ++ -- Me ME
                ++ -- -- SP -- SP -- -- ++
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='b1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Dewey', 'Northampton', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=1.477,
            MAP_SWIPE_MULTIPLY_MINITOUCH=1.428,
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c1': Stage(
        base=BASE,
        map=dict(
            name='C1',
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['F2'],
            map_data="""
                ++ ++ -- ME -- Me ++ -- --
                ++ ++ Me -- -- -- -- -- SP
                ME -- -- -- ++ MS -- ME SP
                -- -- ME -- ++ __ ME -- ++
                MB -- ++ MS -- ME -- -- --
                -- -- -- -- ME -- Me ++ ME
                -- ++ -- ME -- -- -- ++ --
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
        config=dict(
            MAP_SIREN_TEMPLATE=['Dewey', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=1.778,
            MAP_SWIPE_MULTIPLY_MINITOUCH=1.719,
            MAP_ENEMY_GENRE_DETECTION_SCALING={
                'DD': 1.111,
                'CL': 1.111,
                'CA': 1.111,
                'CV': 1.111,
                'BB': 1.111,
            },
        ),
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'c2': Stage(
        base=BASE,
        map=dict(
            name='C2',
            shape='H8',
            camera_data=['D2', 'D6', 'E2', 'E6'],
            camera_data_spawn_point=['E6', 'D6'],
            map_data="""
                -- ++ ++ ++ -- MB -- ++
                -- ME -- ME -- ME -- --
                ++ -- MS -- ME ++ Me --
                -- Me ++ -- Me -- -- --
                ME -- ++ ME -- __ ME MS
                -- MS -- Me -- ++ -- --
                ++ -- ME -- -- -- ME ++
                ++ -- -- SP SP -- ++ ++
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
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Atlanta', 'CA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=1.512,
            MAP_SWIPE_MULTIPLY_MINITOUCH=1.462,
        ),
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
            camera_data_spawn_point=['G6', 'D6'],
            map_data="""
                ++ ++ -- ++ ++ -- -- ME ++ ++
                -- -- MB -- ME -- MS -- ++ ++
                -- ME -- ME MS Me -- ME -- --
                -- ++ -- ++ -- __ -- Me -- MS
                ME ++ -- ++ ME Me ++ -- ME --
                -- -- -- Me -- -- ME -- -- --
                -- ME -- -- SP ++ -- ++ SP ++
                -- ++ ++ ++ -- SP -- SP -- ++
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
            MAP_SIREN_TEMPLATE=['Northampton', 'CA', 'BB'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=1.512,
            MAP_SWIPE_MULTIPLY_MINITOUCH=1.462,
        ),
        battle={
            0: PLAN_2,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'd2': Stage(
        base=BASE,
        map=dict(
            name='D2',
            shape='J8',
            camera_data=['D2', 'D6', 'G2', 'G6'],
            camera_data_spawn_point=['G6'],
            map_data="""
                ++ ++ -- ME -- -- MS ++ ++ ++
                ++ ++ -- ++ ++ -- -- -- -- ME
                -- Me -- -- ME -- Me -- ++ --
                ME ++ MS MB -- -- ME -- ++ --
                -- ++ -- -- ME __ -- MS ++ ME
                -- ++ -- Me -- -- Me -- -- --
                ME -- ME -- -- ++ ++ -- -- SP
                ++ ++ ++ MS -- ME -- -- SP ++
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
                {'battle': 2, 'enemy': 2, 'siren': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='d1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Dewey', 'Northampton', 'BB'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=1.523,
            MAP_SWIPE_MULTIPLY_MINITOUCH=1.472,
        ),
        battle={
            0: ['clear_siren', 'clear_enemy(scale=(2,))', 'clear_enemy(scale=(3,))', 'battle_default'],
            5: PLAN_2,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'd3': Stage(
        base=BASE,
        map=dict(
            name='D3',
            shape='I9',
            camera_data=['D2', 'D6', 'D7', 'F2', 'F6', 'F7'],
            camera_data_spawn_point=['F7', 'D7'],
            map_data="""
                ++ -- ME -- -- -- ME -- ++
                ++ ++ ++ -- MB -- ++ ++ ++
                ME -- -- -- ++ -- -- -- ME
                -- ME Me -- Me -- Me ME --
                -- ++ ++ -- __ -- ++ ++ --
                MS ++ ++ -- Me -- ++ ++ MS
                -- ME MS -- -- -- MS ME --
                ME Me -- ++ -- ++ -- Me ME
                ++ -- -- SP -- SP -- -- ++
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
            MAP_SIREN_TEMPLATE=['Atlanta', 'Northampton', 'CV'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_SWIPE_MULTIPLY=1.477,
            MAP_SWIPE_MULTIPLY_MINITOUCH=1.428,
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
        ),
        battle={
            0: [
                'fleet_2_protect',
                'clear_siren',
                'clear_enemy(scale=(2,))',
                'clear_enemy(scale=(3,))',
                'battle_default',
            ],
            5: PLAN_2,
            6: 'fleet_boss.clear_boss',
        },
    ),
}
