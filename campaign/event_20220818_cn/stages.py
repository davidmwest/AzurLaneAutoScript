"""
Stages of event_20220818_cn, see module/campaign/stage.py
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
            name='ESP',
            shape='E10',
            camera_data=['B5', 'B6'],
            camera_data_spawn_point=['B8'],
            map_data="""
                -- -- -- -- --
                ++ ++ -- ++ ++
                ++ ++ MB ++ ++
                -- ME -- ME --
                ME -- -- -- ME
                ++ ++ __ ++ ++
                ++ MS -- MS ++
                ++ -- MS -- ++
                -- -- -- -- --
                -- SP -- SP --
            """,
            weight_data="""
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
                50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 4, 'siren': 3},
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
            MAP_SIREN_TEMPLATE=['UlrichVonHutten', 'PeterStrasser'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=True,
            MAP_HAS_MYSTERY=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=35,
            EDGE_LINES_HOUGHLINES_THRESHOLD=35,
            MAP_ENSURE_EDGE_INSIGHT_CORNER='bottom',
            MAP_SWIPE_MULTIPLY=(0.96, 0.978),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.928, 0.946),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.901, 0.918),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=2)', 'battle_default'],
            5: PLAN,
            7: 'fleet_boss.clear_boss',
        },
    ),
    'sp1': Stage(
        base=BASE,
        map=dict(
            name='SP1',
            shape='I7',
            camera_data=['D4', 'E5', 'F4'],
            camera_data_spawn_point=['D3'],
            map_data="""
                -- ++ -- SP -- SP -- ++ ++
                -- ++ -- -- -- -- -- ME --
                ME -- -- -- MS -- -- -- ME
                -- -- Me ++ Me ++ Me -- --
                ME -- -- -- __ -- -- -- ME
                -- ++ ++ ME -- ME -- ME --
                -- -- ++ -- MB -- ++ ++ ++
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
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Z46', 'PrinzHeinrich', 'GrafZeppelin'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=True,
            MAP_HAS_MYSTERY=False,
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_SWIPE_MULTIPLY=(1.203, 1.226),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.164, 1.185),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.13, 1.15),
        ),
        enemy_filter=ENEMY_FILTER,
        attrs={'MAP_AIR_RAID_OVERLAY_TRANSPARENCY_THRESHOLD': 0.25},
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'sp2': Stage(
        base=BASE,
        map=dict(
            name='SP2',
            shape='I8',
            camera_data=['D3', 'D6'],
            camera_data_spawn_point=['D3'],
            map_data="""
                ++ -- -- ++ -- -- ++ ++ --
                -- SP -- Me -- -- ++ ++ --
                -- -- -- -- -- MS -- -- --
                -- SP -- Me -- -- Me -- --
                ++ ++ ++ -- ME __ -- ME --
                -- ME -- Me -- -- ME -- --
                MB -- -- -- -- Me ++ ++ --
                -- ME -- ME ++ -- -- -- --
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
                {'battle': 0, 'enemy': 3, 'siren': 1},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Magdeburg', 'PrinzAdalbert', 'GrafZeppelin'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=True,
            MAP_HAS_MYSTERY=False,
        ),
        enemy_filter=ENEMY_FILTER,
        attrs={'MAP_AIR_RAID_OVERLAY_TRANSPARENCY_THRESHOLD': 0.25},
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'sp3': Stage(
        base=BASE,
        map=dict(
            name='SP3',
            shape='H8',
            camera_data=['D5', 'E3', 'E5'],
            camera_data_spawn_point=['D5'],
            map_data="""
                -- -- -- -- ++ ++ -- --
                ++ ++ Me -- Me ++ ME --
                -- -- -- -- -- ME -- --
                SP -- -- MS __ -- -- MB
                SP -- -- MS -- ME -- --
                -- ++ Me -- Me -- -- ME
                -- ME -- ++ ++ ME ME ++
                -- -- -- ++ ++ -- -- ++
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
            MAP_SIREN_TEMPLATE=['GrafZeppelin', 'Weser', 'PeterStrasser'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=True,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.091, 1.112),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.056, 1.075),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.025, 1.043),
        ),
        enemy_filter=ENEMY_FILTER,
        attrs={'MAP_AIR_RAID_OVERLAY_TRANSPARENCY_THRESHOLD': 0.25},
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'sp4': Stage(
        base=BASE,
        map=dict(
            name='SP4',
            shape='I9',
            camera_data=['D6', 'F6', 'E3'],
            camera_data_spawn_point=['E7'],
            map_data="""
                -- -- -- ME -- ME -- -- --
                -- ++ ME -- MB -- ME ++ --
                -- -- -- -- Me -- -- -- --
                -- ++ ++ -- -- -- ++ ++ --
                -- ++ ++ Me MS Me ++ ++ --
                -- ME MS -- __ -- MS ME --
                ME -- -- ++ -- ++ -- -- ME
                -- ME -- -- -- -- -- ME --
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
                {'battle': 4},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='sp1',
        config=dict(
            MAP_SIREN_TEMPLATE=['UlrichVonHutten'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=True,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(0.995, 1.013),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.962, 0.98),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.934, 0.951),
        ),
        enemy_filter=ENEMY_FILTER,
        attrs={'MAP_AIR_RAID_OVERLAY_TRANSPARENCY_THRESHOLD': 0.25},
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
