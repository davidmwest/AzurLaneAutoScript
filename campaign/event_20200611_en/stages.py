"""
Stages of event_20200611_en, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage

PLAN = [
    'clear_siren',
    'clear_enemy(scale=(1,))',
    "clear_enemy(scale=(2,), genre=['light', 'main', 'enemy', 'carrier'])",
    "clear_enemy(genre=['light', 'main', 'enemy'])",
    'battle_default',
]

STAGES = {
    'a2': Stage(
        map=dict(
            map_data="""
                -- -- -- -- -- -- -- -- ++
                -- -- -- ++ ++ -- -- -- ++
                ++ -- -- -- -- -- -- -- --
                ++ -- ++ -- -- -- -- -- --
                -- -- -- -- ++ ++ -- -- --
                -- -- -- -- ++ ++ -- -- --
            """,
            camera_data=['D1', 'D4', 'F2', 'F4'],
        ),
        config_base='campaign.event_20200611_en.a1:Config',
    ),
    'a3': Stage(
        map=dict(
            shape='H7',
            map_data="""
                -- ME ME ++ ++ ME ME ME
                ME -- -- MS -- -- MB --
                ++ ++ -- ME __ ME ++ ++
                ME ME -- ++ -- ME ++ ++
                ME -- -- ++ -- MS MB ME
                SP SP -- -- __ -- ME ++
                -- SP ME ++ ME MS -- ME
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='campaign.event_20200611_en.a1:Config',
        config=dict(
            POOR_MAP_DATA=False,
        ),
        battle={
            0: PLAN,
            4: 'fleet_boss.clear_potential_boss',
        },
    ),
    'b2': Stage(
        map=dict(
            shape='K7',
            map_data="""
                -- ME ME ME ++ ME -- -- ME ++ ++
                ME -- -- -- -- -- ++ ++ -- -- ME
                ++ -- ME ME __ ME ++ ++ ME __ --
                ME -- -- MS -- MS MB MB MS -- MS
                -- ME -- -- -- -- MB MB -- -- --
                ++ ++ ME -- SP -- ++ ++ -- SP --
                ++ -- -- -- -- -- ME ME -- -- --
            """,
            wall_data="""
    ·   · | ·   ·   ·   ·   ·   ·   ·   ·   · ,
          +                                   ,
    ·   ·   ·   ·   ·   ·   ·   ·   ·   · | · ,
          +       +   +               +   +   ,
    ·   · | ·   · | · | ·   ·   ·   · | ·   · ,
          +---+---+   |               |   +   ,
    ·   ·   · | ·   · | ·   ·   ·   · | · | · ,
              +---+   +---+       +---+   +-- ,
    ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   · ,
                                              ,
    ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   · ,
                                              ,
    ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   · ,
""",
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 1},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='campaign.event_20200611_en.b1:Config',
        config=dict(
            MAP_HAS_WALL=True,
            MAP_SIREN_TEMPLATE=['Algerie', 'Vauquelin'],
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.brute_clear_boss',
        },
    ),
    'b3': Stage(
        map=dict(
            shape='N10',
            map_data="""
                -- -- -- -- -- ME -- -- ME -- -- -- -- ++
                -- -- -- ME -- -- MB MB -- -- ME -- -- --
                ++ -- ME -- ME ME -- -- ME ME -- ME -- --
                ++ -- -- ME -- -- __ __ -- -- ME -- -- --
                -- -- -- -- ME MS -- -- MS ME -- -- ++ ++
                -- ++ -- ME ++ ++ -- -- ++ ++ ME -- -- --
                -- ++ -- ME ++ ++ -- -- ++ ++ ME -- -- --
                -- -- -- -- ME MS -- -- MS ME -- -- ++ ++
                ++ -- -- -- -- -- -- -- -- -- -- -- ++ ++
                -- -- -- -- -- -- SP SP -- -- -- -- -- --
            """,
            camera_data=['G8', 'G6', 'F3', 'H4'],
            wall_data="""
    ·   ·   ·   ·   · | ·   ·   ·   · | ·   ·   ·   ·   · ,
          +-----------+               +-----------+       ,
    ·   · | ·   ·   · | ·   ·   ·   · | ·   ·   · | ·   · ,
          |           |               |           |       ,
    ·   · | ·   ·   · | ·   ·   ·   · | ·   ·   · | ·   · ,
          +---+       +---+       +---+       +---+       ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              +-----------+       +-----------+           ,
    ·   ·   ·   ·   ·   · | ·   · | ·   ·   ·   ·   ·   · ,
""",
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'enemy': 1, 'boss': 1},
            ],
        ),
        config_base='campaign.event_20200611_en.b1:Config',
        config=dict(
            MAP_SIREN_COUNT=2,
            MAP_HAS_WALL=True,
            MAP_SIREN_TEMPLATE=['LaGalissonniere', 'Vauquelin'],
            EDGE_LINES_HOUGHLINES_THRESHOLD=40,
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.brute_clear_boss',
        },
    ),
    'c2': Stage(
        map=dict(
            map_data="""
                -- -- -- -- -- -- -- -- ++
                -- -- -- ++ ++ -- -- -- ++
                ++ -- -- -- -- -- -- -- --
                ++ -- ++ -- -- -- -- -- --
                -- -- -- -- ++ ++ -- -- --
                -- -- -- -- ++ ++ -- -- --
            """,
            camera_data=['D1', 'D4', 'F2', 'F4'],
        ),
        config_base='campaign.event_20200611_en.c1:Config',
    ),
    'c3': Stage(
        map=dict(
            shape='H7',
            map_data="""
                -- ME ME ++ ++ ME ME ME
                ME -- -- MS -- -- MB --
                ++ ++ -- ME __ ME ++ ++
                ME ME -- ++ -- ME ++ ++
                ME -- -- ++ -- MS MB ME
                SP SP -- -- __ -- ME ++
                -- SP ME ++ ME MS -- ME
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 2, 'siren': 2},
                {'battle': 1, 'enemy': 2},
                {'battle': 2, 'enemy': 2},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config_base='campaign.event_20200611_en.c1:Config',
        config=dict(
            FLEET_BOSS=2,
        ),
        battle={
            0: PLAN,
            5: 'fleet_boss.brute_clear_boss',
        },
    ),
    'd2': Stage(
        map=dict(
            map_data="""
                -- -- -- -- ++ -- -- -- -- ++ ++
                -- -- -- -- -- -- ++ ++ -- -- --
                ++ -- -- -- -- -- ++ ++ -- -- --
                -- -- -- -- -- -- -- -- -- -- --
                -- -- -- -- -- -- -- -- -- -- --
                ++ ++ -- -- -- -- ++ ++ -- -- --
                ++ -- -- -- -- -- -- -- -- -- --
            """,
            camera_data=['D3', 'D5', 'F3', 'F5', 'H3', 'H5'],
            wall_data="""
    ·   · | ·   ·   ·   ·   ·   ·   ·   ·   · ,
          +                                   ,
    ·   ·   ·   ·   ·   ·   ·   ·   ·   · | · ,
          +       +   +               +   +   ,
    ·   · | ·   · | · | ·   ·   ·   · | ·   · ,
          +---+---+   |               |   +   ,
    ·   ·   · | ·   · | ·   ·   ·   · | · | · ,
              +---+   +---+       +---+   +-- ,
    ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   · ,
                                              ,
    ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   · ,
                                              ,
    ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   · ,
""",
        ),
        config_base='campaign.event_20200611_en.d1:Config',
        config=dict(
            MAP_HAS_WALL=True,
            MAP_SIREN_TEMPLATE=['Algerie', 'Vauquelin'],
        ),
    ),
    'd3': Stage(
        map=dict(
            map_data="""
                -- -- -- -- -- ME -- -- ME -- -- -- -- ++
                -- -- -- ME -- -- MB MB -- -- ME -- -- --
                ++ -- ME -- ME ME -- -- ME ME -- ME -- --
                ++ -- -- ME -- -- __ __ -- -- ME -- -- --
                -- -- -- -- ME MS -- -- MS ME -- -- ++ ++
                -- ++ -- ME ++ ++ -- -- ++ ++ ME -- -- --
                -- ++ -- ME ++ ++ -- -- ++ ++ ME -- -- --
                -- -- -- -- ME MS -- -- MS ME -- -- ++ ++
                ++ -- -- -- -- -- -- -- -- -- -- -- ++ ++
                -- -- -- -- -- -- SP SP -- -- -- -- -- --
            """,
            weight_data="""
                10 10 10 10 10 10 10 10 10 10 10 10 10 10
                10 10 10 30 10 10 10 10 10 10 30 10 10 10
                10 10 30 10 10 10 10 10 10 10 10 30 10 10
                10 10 10 10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10 10 10 10
                10 10 10 30 10 10 10 10 10 10 30 10 10 10
                10 10 10 30 10 10 10 10 10 10 30 10 10 10
                10 10 10 10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10 10 10 10
                10 10 10 10 10 10 10 10 10 10 10 10 10 10
            """,
            camera_data=['G8', 'G6', 'F3', 'H4'],
            wall_data="""
    ·   ·   ·   ·   · | ·   ·   ·   · | ·   ·   ·   ·   · ,
          +-----------+               +-----------+       ,
    ·   · | ·   ·   · | ·   ·   ·   · | ·   ·   · | ·   · ,
          |           |               |           |       ,
    ·   · | ·   ·   · | ·   ·   ·   · | ·   ·   · | ·   · ,
          +---+       +---+       +---+       +---+       ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              +-----------+       +-----------+           ,
    ·   ·   ·   ·   ·   · | ·   · | ·   ·   ·   ·   ·   · ,
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
        config_base='campaign.event_20200611_en.d1:Config',
        config=dict(
            MAP_HAS_WALL=True,
            MAP_SIREN_COUNT=3,
            MAP_SIREN_TEMPLATE=['LaGalissonniere', 'Vauquelin'],
            EDGE_LINES_HOUGHLINES_THRESHOLD=40,
            EDGE_LINES_FIND_PEAKS_PARAMETERS={
                'height': (239, 255),
                'prominence': 10,
                'distance': 50,
                'wlen': 1000,
            },
        ),
        battle={
            0: [
                'clear_siren',
                "clear_enemy(scale=(2,), genre=['light', 'main', 'enemy', 'carrier'])",
                "clear_enemy(scale=(3,), genre=['light', 'main', 'enemy', 'carrier'])",
                'battle_default',
            ],
            5: [
                'clear_enemy(scale=(1,))',
                "clear_enemy(scale=(2,), genre=['light', 'main', 'enemy', 'carrier'])",
                "clear_enemy(genre=['light', 'main'])",
                'battle_default',
            ],
            6: 'fleet_boss.brute_clear_boss',
        },
    ),
}
