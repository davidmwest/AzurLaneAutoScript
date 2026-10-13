"""
Stages of event_20220915_cn, see module/campaign/stage.py
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
            shape='H8',
            camera_data=['D3', 'E4', 'E6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- ++ ++ -- -- -- -- --
                -- ME ++ ME Me ++ ++ --
                ME -- -- -- -- ++ ++ --
                MS -- MS -- Me -- MB --
                -- -- ++ ME __ -- -- ME
                -- -- ++ MS -- Me ME --
                SP -- -- -- Me ++ ++ --
                -- SP -- ME -- ++ ++ --
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
                {'battle': 3, 'enemy': 1, 'boss': 1},
                {'battle': 4, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Wakaba', 'Suzutsuki'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
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
            MAP_SWIPE_MULTIPLY=(1.093, 1.113),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.057, 1.076),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.026, 1.045),
            HOMO_EDGE_HOUGHLINES_THRESHOLD=210,
            MAP_WALK_USE_CURRENT_FLEET=True,
        ),
        enemy_filter=ENEMY_FILTER,
        attrs={'MAP_ENEMY_SEARCHING_OVERLAY_TRANSPARENCY_THRESHOLD': 0.65},
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
            camera_data=['D4', 'D6', 'E3'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- SP ++ ++ -- ME -- ME
                SP -- -- ++ Me -- -- --
                -- -- ME MS -- Me -- ++
                Me -- -- -- __ -- -- ++
                -- MS Me -- -- -- MB --
                -- ++ ++ ++ -- ++ ++ --
                ME -- -- ME -- ++ ++ --
                -- ME ++ -- ME -- -- ++
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
            MAP_SIREN_TEMPLATE=['Miyuki', 'Jintsuu'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.22, 1.243),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.18, 1.201),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.145, 1.166),
        ),
        enemy_filter=ENEMY_FILTER,
        attrs={'MAP_ENEMY_SEARCHING_OVERLAY_TRANSPARENCY_THRESHOLD': 0.65},
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'a3': Stage(
        base=BASE,
        map=dict(
            name='A3',
            shape='H8',
            camera_data=['D3', 'E4', 'E6'],
            camera_data_spawn_point=['E2'],
            map_data="""
                ++ ++ ++ ME -- -- SP --
                ME -- Me -- MS -- -- SP
                -- -- -- -- -- ++ -- --
                ME -- ME -- Me -- MS --
                -- ++ ++ ++ ME __ -- ME
                -- ++ ++ ++ -- -- Me --
                -- ++ ++ MB -- ME ++ ++
                -- -- -- -- Me -- ++ ++
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
            MAP_SIREN_TEMPLATE=['Hatakaze', 'Kinu', 'Haguro'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.22, 1.243),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.18, 1.201),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.145, 1.166),
        ),
        enemy_filter=ENEMY_FILTER,
        attrs={'MAP_ENEMY_SEARCHING_OVERLAY_TRANSPARENCY_THRESHOLD': 0.65},
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b1': Stage(
        base=BASE,
        map=dict(
            name='B1',
            shape='H8',
            camera_data=['D3', 'D5'],
            camera_data_spawn_point=['E6'],
            map_data="""
                ++ -- -- -- ME -- -- --
                -- -- -- ME -- ME ++ --
                -- ++ ++ ME -- Me ++ ME
                -- MB -- -- -- -- -- --
                Me -- -- __ Me ME MS --
                ++ ME -- ME -- ++ -- --
                -- -- Me -- MS -- -- SP
                -- ++ ++ ++ -- -- SP --
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
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 2, 'boss': 1},
                {'battle': 5, 'enemy': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Harutsuki', 'Kawakaze', 'Hiei'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
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
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.023, 1.043),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.99, 1.008),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.961, 0.978),
        ),
        enemy_filter=ENEMY_FILTER,
        attrs={'MAP_ENEMY_SEARCHING_OVERLAY_TRANSPARENCY_THRESHOLD': 0.65},
        battle={
            0: PLAN,
            4: 'clear_boss',
        },
    ),
    'b2': Stage(
        base=BASE,
        map=dict(
            name='B2',
            shape='M6',
            camera_data=['D4', 'E3', 'G3', 'G4'],
            camera_data_spawn_point=['H3'],
            map_data="""
                -- -- -- -- ME -- ++ ++ -- Me ++ ++ ++
                ++ ++ ++ ME -- Me ++ ++ MS -- -- -- --
                ++ ++ ++ ME -- __ -- MS -- -- SP ++ ++
                ++ ++ MB -- -- __ -- MS -- -- SP ++ ++
                ME -- -- -- -- Me ++ ++ MS -- -- -- --
                -- ME ME ++ ME -- ++ ++ -- Me ++ ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['Kongo', 'Yamashiro', 'Akagi', 'Kaga'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.123, 1.144),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.086, 1.106),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.054, 1.073),
        ),
        enemy_filter=ENEMY_FILTER,
        attrs={'MAP_ENEMY_SEARCHING_OVERLAY_TRANSPARENCY_THRESHOLD': 0.65},
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
            camera_data=['D3', 'D5', 'E5'],
            camera_data_spawn_point=['D7'],
            map_covered=['E3'],
            map_data="""
                ++ -- -- -- ME -- -- -- ++
                -- ME ME -- -- -- ME ME --
                -- ME ++ Me MS Me ++ ME --
                -- -- Me -- -- -- Me -- --
                ME -- MS -- ++ -- MS -- ME
                -- -- Me -- MB -- Me -- --
                -- ME ++ -- MS -- ++ ME --
                -- -- -- -- __ -- -- -- --
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
            MAP_SIREN_TEMPLATE=['Mikasa', 'Nagato', 'Akagi', 'Kaga'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(0.985, 1.003),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.952, 0.97),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.925, 0.941),
        ),
        enemy_filter=ENEMY_FILTER,
        attrs={'MAP_ENEMY_SEARCHING_OVERLAY_TRANSPARENCY_THRESHOLD': 0.65},
        battle={
            0: PLAN,
            5: 'fleet_boss.clear_boss',
        },
    ),
    'c1': Stage(
        base=BASE,
        map=dict(
            name='C1',
            shape='H8',
            camera_data=['D3', 'E4', 'E6'],
            camera_data_spawn_point=['D6'],
            map_data="""
                -- ++ ++ -- -- -- -- --
                -- ME ++ ME Me ++ ++ --
                ME -- -- -- -- ++ ++ --
                MS -- MS -- Me -- MB --
                -- -- ++ ME __ -- -- ME
                -- -- ++ MS -- Me ME --
                SP -- -- -- Me ++ ++ --
                -- SP -- ME -- ++ ++ --
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
        config=dict(
            MAP_SIREN_TEMPLATE=['Sakawa', 'Chitose', 'Chiyoda'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.093, 1.113),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.057, 1.076),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.026, 1.045),
            MAP_WALK_USE_CURRENT_FLEET=True,
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
            shape='H8',
            camera_data=['D4', 'D6', 'E3'],
            camera_data_spawn_point=['D2'],
            map_data="""
                -- SP ++ ++ -- ME -- ME
                SP -- -- ++ Me -- -- --
                -- -- ME MS -- Me -- ++
                Me -- -- -- __ -- -- ++
                -- MS Me -- -- -- MB --
                -- ++ ++ ++ -- ++ ++ --
                ME -- -- ME -- ++ ++ --
                -- ME ++ -- ME -- -- ++
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
            MAP_SIREN_TEMPLATE=['Jintsuu', 'Ryuuhou', 'Kaga'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.22, 1.243),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.18, 1.201),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.145, 1.166),
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
            shape='H8',
            camera_data=['D3', 'E4', 'E6'],
            camera_data_spawn_point=['E2'],
            map_data="""
                ++ ++ ++ ME -- -- SP --
                ME -- Me -- MS -- -- SP
                -- -- -- -- -- ++ -- --
                ME -- ME -- Me -- MS --
                -- ++ ++ ++ ME __ -- ME
                -- ++ ++ ++ -- -- Me --
                -- ++ ++ MB -- ME ++ ++
                -- -- -- -- Me -- ++ ++
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
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='c1',
        config=dict(
            MAP_SIREN_TEMPLATE=['Haguro', 'Kongo', 'Kirishima'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.22, 1.243),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.18, 1.201),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.145, 1.166),
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
            shape='H8',
            camera_data=['D3', 'D5'],
            camera_data_spawn_point=['E6'],
            map_data="""
                ++ -- -- -- ME -- -- --
                -- -- -- ME -- ME ++ --
                -- ++ ++ ME -- Me ++ ME
                -- MB -- -- -- -- -- --
                Me -- -- __ Me ME MS --
                ++ ME -- ME -- ++ -- --
                -- -- Me -- MS -- -- SP
                -- ++ ++ ++ -- -- SP --
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
                {'battle': 4, 'enemy': 2},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['Hiei', 'Haruna', 'Shokaku'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
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
            MAP_WALK_USE_CURRENT_FLEET=True,
            MAP_SWIPE_MULTIPLY=(1.023, 1.043),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.99, 1.008),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.961, 0.978),
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
            shape='M6',
            camera_data=['D4', 'E3', 'G3', 'G4'],
            camera_data_spawn_point=['H3'],
            map_data="""
                -- -- -- -- ME -- ++ ++ -- Me ++ ++ ++
                ++ ++ ++ ME -- Me ++ ++ MS -- -- -- --
                ++ ++ ++ ME -- __ -- MS -- -- SP ++ ++
                ++ ++ MB -- -- __ -- MS -- -- SP ++ ++
                ME -- -- -- -- Me ++ ++ MS -- -- -- --
                -- ME ME ++ ME -- ++ ++ -- Me ++ ++ ++
            """,
            weight_data="""
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
                50 50 50 50 50 50 50 50 50 50 50 50 50
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
            MAP_SIREN_TEMPLATE=['Kongo', 'Yamashiro', 'Akagi', 'Kaga'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(1.123, 1.144),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(1.086, 1.106),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(1.054, 1.073),
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
            shape='I9',
            camera_data=['D3', 'D5', 'E5'],
            camera_data_spawn_point=['D7'],
            map_covered=['E3'],
            map_data="""
                ++ -- -- -- ME -- -- -- ++
                -- ME ME -- -- -- ME ME --
                -- ME ++ Me MS Me ++ ME --
                -- -- Me -- -- -- Me -- --
                ME -- MS -- ++ -- MS -- ME
                -- -- Me -- MB -- Me -- --
                -- ME ++ -- MS -- ++ ME --
                -- -- -- -- __ -- -- -- --
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
            MAP_SIREN_TEMPLATE=['Mikasa', 'Nagato', 'Akagi', 'Kaga'],
            MOVABLE_ENEMY_TURN=(2,),
            MAP_HAS_SIREN=True,
            MAP_HAS_MOVABLE_ENEMY=True,
            MAP_HAS_MAP_STORY=True,
            MAP_HAS_FLEET_STEP=True,
            MAP_HAS_AMBUSH=False,
            MAP_HAS_MYSTERY=False,
            MAP_SWIPE_MULTIPLY=(0.985, 1.003),
            MAP_SWIPE_MULTIPLY_MINITOUCH=(0.952, 0.97),
            MAP_SWIPE_MULTIPLY_MAATOUCH=(0.925, 0.941),
        ),
        enemy_filter=ENEMY_FILTER,
        battle={
            0: PLAN_2,
            5: PLAN,
            6: 'fleet_boss.clear_boss',
        },
    ),
}
