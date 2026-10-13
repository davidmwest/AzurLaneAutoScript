"""
Stages of campaign_sos, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

BASE = '.campaign_base:CampaignBase'
PLAN = ['clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default']
PLAN_2 = ['clear_filter_enemy(self.ENEMY_FILTER, preserve=0)', 'battle_default']

STAGES = {
    'campaign_10_5': Stage(
        base=BASE,
        map=dict(
            name='SOS',
            shape='I6',
            camera_data=['D2', 'D4', 'F2', 'F4'],
            camera_data_spawn_point=['D4', 'F4'],
            map_data="""
                -- -- ME ME ME MB -- ++ --
                ME ++ ++ MB ME ME Me -- ME
                MB ME __ Me __ ME ME ME --
                -- Me ME ++ ME Me Me ++ ME
                ++ ME ME Me ME ME ++ ++ --
                ++ ++ ++ -- SP SP ME -- ME
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
                {'battle': 0, 'enemy': 4},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5},
                {'battle': 6, 'boss': 1},
            ],
        ),
        config_base='.campaign_base:ConfigBase',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
            EDGE_LINES_HOUGHLINES_THRESHOLD=40,
            COINCIDENT_POINT_ENCOURAGE_DISTANCE=1.5,
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
        ),
        battle={
            0: PLAN,
            3: PLAN,
            5: PLAN_2,
            6: 'fleet_boss.clear_boss',
        },
    ),
    'campaign_3_5': Stage(
        base=BASE,
        map=dict(
            name='SOS',
            shape='H5',
            camera_data=['D3', 'E3'],
            camera_data_spawn_point=['D3'],
            map_data="""
                -- -- ++ ++ -- Me -- --
                ++ Me ME ME ME MB ++ --
                -- ME SP SP __ Me ++ ME
                ME ++ ME ME ME Me ME ME
                -- ME Me ME ++ ME ME ++
            """,
            weight_data="""
                50 50 50 50 50 20 50 50
                50 50 30 20 10 10 50 50
                50 50 50 30 20 20 50 50
                50 50 30 30 30 30 50 50
                50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='.campaign_base:ConfigBase',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
            EDGE_LINES_HOUGHLINES_THRESHOLD=40,
            COINCIDENT_POINT_ENCOURAGE_DISTANCE=1.5,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (120, 206),
                'width': (1.5, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (206, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_EDGE_COLOR_RANGE=(0, 49),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
        ),
        battle={
            0: PLAN,
            2: PLAN_2,
            3: 'fleet_boss.clear_boss',
        },
    ),
    'campaign_4_5': Stage(
        base=BASE,
        map=dict(
            name='SOS',
            shape='H7',
            camera_data=['D2', 'D3', 'E5'],
            camera_data_spawn_point=['E5'],
            map_data="""
                ME -- ME -- ++ Me ME --
                -- Me ME MB MB ME ME --
                ME ++ __ ME ME __ ME ME
                ME ME ME Me ME ME ME ++
                -- ME ME SP SP ME ME ME
                ++ ME -- ME -- Me -- --
                ++ -- ++ -- ME -- ++ ME
            """,
            weight_data="""
                50 50 50 50 50 50 50 50
                50 50 10 10 10 10 50 50
                50 50 20 10 10 20 30 50
                50 50 20 20 20 20 30 50
                50 50 30 30 30 30 50 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 4},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
            ],
        ),
        config_base='.campaign_base:ConfigBase',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
            EDGE_LINES_HOUGHLINES_THRESHOLD=40,
            COINCIDENT_POINT_ENCOURAGE_DISTANCE=1.5,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (120, 222),
                'width': (1.5, 10),
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
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
        ),
        attrs={
            'MAP_AMBUSH_OVERLAY_TRANSPARENCY_THRESHOLD': 0.3,
            'MAP_AIR_RAID_OVERLAY_TRANSPARENCY_THRESHOLD': 0.25,
            'MAP_ENEMY_SEARCHING_OVERLAY_TRANSPARENCY_THRESHOLD': 0.65,
        },
        battle={
            0: PLAN,
            3: PLAN_2,
            4: 'fleet_boss.clear_boss',
        },
    ),
    'campaign_5_5': Stage(
        base=BASE,
        map=dict(
            name='SOS',
            shape='H6',
            camera_data=['D2', 'D4'],
            camera_data_spawn_point=['D4'],
            map_data="""
                ME ME ++ -- ME Me MB --
                -- -- ME MB MB ME ME MB
                ME ++ ME Me ME __ ME --
                -- ME __ ME Me ME ME ME
                -- ME ME SP SP ME ME --
                ++ ++ ME -- ME ME ++ --
            """,
            weight_data="""
                50 50 50 50 20 20 10 50
                50 50 50 10 10 10 10 10
                50 50 50 30 20 20 20 20
                50 50 20 50 30 30 30 30
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 4},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 2},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='.campaign_base:ConfigBase',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
            EDGE_LINES_HOUGHLINES_THRESHOLD=40,
            COINCIDENT_POINT_ENCOURAGE_DISTANCE=1.5,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (120, 206),
                'width': (1.5, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (206, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_EDGE_COLOR_RANGE=(0, 49),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
        ),
        battle={
            0: PLAN,
            3: PLAN_2,
            4: 'fleet_boss.clear_boss',
        },
    ),
    'campaign_6_5': Stage(
        base=BASE,
        map=dict(
            name='SOS',
            shape='H6',
            camera_data=['D2', 'D4'],
            camera_data_spawn_point=['D4'],
            map_data="""
                ++ ME -- -- -- ME ++ ++
                ME -- ME MB MB -- ME --
                -- ++ ME ME ME ME -- ME
                ME ME __ Me ME __ ME --
                ME Me ME MB ME ME ++ ME
                -- ++ Me SP SP ME ++ --
            """,
            weight_data="""
                50 50 50 50 50 50 50 50
                50 50 20 10 10 30 50 50
                50 50 20 10 20 30 50 50
                50 50 20 10 20 30 50 50
                50 50 20 10 20 30 50 50
                50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 5},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='.campaign_base:ConfigBase',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
            EDGE_LINES_HOUGHLINES_THRESHOLD=40,
            COINCIDENT_POINT_ENCOURAGE_DISTANCE=1.5,
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
        ),
        battle={
            0: PLAN,
            4: PLAN_2,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'campaign_7_5': Stage(
        base=BASE,
        map=dict(
            name='SOS',
            shape='H6',
            camera_data=['D2', 'D4'],
            camera_data_spawn_point=['D4'],
            map_data="""
                -- ME ME -- ++ ++ ++ MB
                ME Me ME ME ME ME ME --
                ME ME __ Me ++ __ ME ME
                ME ++ SP ME ME SP ME --
                -- ME ME ME ME ME ++ ME
                ++ -- Me -- -- ME -- --
            """,
            weight_data="""
                50 50 50 50 50 50 50 09
                50 50 50 14 13 12 11 10
                50 50 50 15 50 13 12 11
                50 50 50 14 13 13 12 50
                50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 4},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 3},
                {'battle': 3, 'enemy': 2},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='.campaign_base:ConfigBase',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
            EDGE_LINES_HOUGHLINES_THRESHOLD=40,
            COINCIDENT_POINT_ENCOURAGE_DISTANCE=1.5,
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
        ),
        battle={
            0: ['fleet_2_push_forward', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default'],
            4: PLAN_2,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'campaign_8_5': Stage(
        base=BASE,
        map=dict(
            name='SOS',
            shape='H7',
            camera_data=['D3', 'D5'],
            camera_data_spawn_point=['D3', 'D5'],
            map_data="""
                ++ ++ ME -- ME -- ME --
                ++ ++ ME ME -- ++ -- ME
                -- Me ME ME SP -- ME ME
                MB Me __ Me ME ME -- ++
                -- ++ ME Me ME -- ME ++
                ME ++ ME ME SP ME -- ME
                -- ME ME -- ME -- ++ ME
            """,
            weight_data="""
                50 50 50 50 50 50 50 50
                50 50 13 50 50 50 50 50
                50 11 12 13 50 50 50 50
                10 11 12 12 13 50 50 50
                50 50 12 13 50 50 50 50
                50 50 13 50 50 50 50 50
                50 50 50 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 4},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
            ],
        ),
        config_base='.campaign_base:ConfigBase',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
            EDGE_LINES_HOUGHLINES_THRESHOLD=40,
            COINCIDENT_POINT_ENCOURAGE_DISTANCE=1.5,
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={
                'height': (120, 206),
                'width': (0.9, 10),
                'prominence': 10,
                'distance': 35,
            },
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (206, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
            HOMO_EDGE_COLOR_RANGE=(0, 49),
        ),
        battle={
            0: PLAN,
            3: PLAN_2,
            4: 'fleet_boss.clear_boss',
        },
    ),
    'campaign_9_5': Stage(
        base=BASE,
        map=dict(
            name='SOS',
            shape='I6',
            camera_data=['D2', 'D4', 'F2', 'F4'],
            camera_data_spawn_point=['D2', 'F4'],
            map_data="""
                -- ++ ++ ++ -- MB ME -- ++
                -- Me ++ ME -- ME Me ME ++
                Me ME ME SP ME ++ __ ME --
                ME ME __ ME Me SP Me ME ME
                -- ME Me ++ ME -- ME ME --
                -- ++ ME MB -- -- ++ ++ ++
            """,
            weight_data="""
                50 50 50 50 10 10 30 50 50
                50 50 50 20 10 20 30 50 50
                50 50 30 20 10 50 30 50 50
                50 50 30 20 10 30 30 50 50
                50 50 30 50 10 50 50 50 50
                50 50 30 30 50 50 50 50 50
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='.campaign_base:ConfigBase',
        config=dict(
            MAP_HAS_MAP_STORY=False,
            MAP_HAS_FLEET_STEP=False,
            MAP_HAS_AMBUSH=False,
            STAR_REQUIRE_1=0,
            STAR_REQUIRE_2=0,
            STAR_REQUIRE_3=0,
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
            EDGE_LINES_HOUGHLINES_THRESHOLD=40,
            COINCIDENT_POINT_ENCOURAGE_DISTANCE=1.5,
        ),
        battle={
            0: PLAN,
            4: PLAN_2,
            5: 'fleet_boss.clear_boss',
        },
    ),
}
