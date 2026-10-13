"""
Stages of event_20201126_cn, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'
PLAN = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']

STAGES = {
    'sp': Stage(
        base=BASE,
        map=dict(
            name='VSP',
            shape='I6',
            camera_data=['E4', 'E3'],
            camera_data_spawn_point=['E4'],
            map_data="""
                ++ ++ ++ ++ MB ++ ++ ++ ++
                ++ -- ME -- MS -- ME -- ++
                -- ME -- MS -- MS -- ME --
                ++ -- ME -- __ -- ME -- ++
                -- ++ ++ -- -- -- ++ ++ --
                -- ++ ++ SP -- SP ++ ++ --
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
                {'battle': 0, 'siren': 3},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 2},
                {'battle': 4},
                {'battle': 5},
                {'battle': 6},
                {'battle': 7, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            MAP_HAS_SIREN=True,
            MAP_SIREN_TEMPLATE=['KasumiDOA', 'NagisaDOA', 'NyotenguDOA'],
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=2)', 'battle_default'],
            5: ['clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default'],
            7: 'fleet_boss.clear_boss',
        },
    ),
    'sp1': Stage(
        base=BASE,
        map=dict(
            name='SP1',
            shape='H7',
            camera_data=['D2', 'D5', 'E2', 'E5'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- SP -- ++ ++ -- -- ++
                SP -- -- ++ ++ Me ME ++
                -- -- -- Me ME -- -- --
                ME ++ -- __ -- -- -- MB
                -- Me -- -- Me ME -- --
                ME -- -- ME ++ ++ ME ME
                ++ -- ME -- -- ++ -- --
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
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            STAGE_ENTRANCE=['normal', 'half'],
            MAP_SWIPE_MULTIPLY=(1.221, 1.244),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.181, 1.203),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.146, 1.167),
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (80, 215),
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
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D2', 'D5'],
            map_data="""
                -- -- MS ++ ME MB ME ++ ++
                -- ++ -- Me -- -- -- ME ++
                -- SP -- -- -- ME -- -- ME
                -- -- -- ME __ ++ -- Me --
                -- SP -- -- -- ++ -- -- ME
                ++ ++ -- Me -- -- -- ME ++
                ++ ++ MS -- ++ ME ME -- --
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
            MAP_SIREN_TEMPLATE=['MarieRoseDOA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.122, 1.143),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.085, 1.105),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.053, 1.072),
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
            shape='I7',
            camera_data=['D2', 'D5', 'F2', 'F5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- Me ++ ++ ++ ME -- -- --
                ++ -- ME -- Me -- ME ++ --
                ++ -- -- MS -- -- -- ME --
                SP -- -- __ ++ Me -- -- MB
                SP -- -- __ -- MS -- ME MB
                ++ -- Me MS -- -- -- ++ --
                ME -- ME ++ ++ ++ ME ++ --
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
            MAP_SIREN_TEMPLATE=['MisakiDOA', 'KasumiDOA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
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
    'sp4': Stage(
        base=BASE,
        map=dict(
            name='SP4',
            shape='I8',
            camera_data=['D2', 'D6', 'F2', 'F6'],
            camera_data_spawn_point=['F6', 'D6'],
            map_data="""
                -- -- ME ++ ++ ++ ME -- --
                ++ ME -- -- Me -- -- ME ++
                ME -- ME -- ++ -- ME -- ME
                ME -- ++ -- MB -- ++ -- ME
                ME -- ++ MS -- MS ++ -- ME
                ++ -- Me -- __ -- Me -- ++
                ME -- MS -- -- -- MS -- ME
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
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'siren': 2},
                {'battle': 1, 'enemy': 2, 'siren': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['MisakiDOA', 'KasumiDOA', 'NagisaDOA'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.064, 1.084),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.029, 1.048),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.999, 1.017),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: [
                'fleet_2_protect',
                'clear_siren',
                'clear_filter_enemy(self.ENEMY_FILTER, preserve=0)',
                'battle_default',
            ],
            5: 'fleet_boss.clear_boss',
        },
    ),
}
