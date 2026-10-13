"""
Stages of event_20200603_en, see module/campaign/stage.py
Written by dev_tools/stage_convert.py
"""
from module.campaign.stage import Stage


STAGES = {
    'sp2': Stage(
        map=dict(
            name='sp2',
            shape='g7',
            camera_data=['D3', 'D5'],
            map_data="""
                ++ ++ -- ME -- ME MB
                MM ++ -- -- ME -- MB
                ME -- ME -- ++ ++ ++
                -- -- -- ME -- ME MB
                -- -- ++ -- ++ ME --
                SP SP -- -- ++ -- ME
                ++ SP -- ME -- ME --
            """,
            spawn_data=[
                {'battle': 0, 'enemy': 3, 'mystery': 1},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'boss': 1},
            ],
        ),
        config=dict(
            SUBMARINE=0,
            FLEET_BOSS=0,
            MAP_HAS_AMBUSH=False,
        ),
        battle={
            0: [('do', 'clear_all_mystery'), 'battle_default'],
            1: 'battle_default',
            4: 'brute_clear_boss',
        },
    ),
    'sp3': Stage(
        map=dict(
            name='sp3',
            shape='i6',
            map_data="""
                ++ MB -- ME -- ME -- ++ ++
                MB -- ME -- ++ -- ME ++ ++
                MB ME -- ME -- ME -- ME --
                ++ ++ ++ -- ME -- ME ++ --
                MB -- ME ME -- ++ -- -- SP
                -- ME -- -- -- ++ -- SP SP
            """,
            camera_data=['D3', 'F5'],
            spawn_data=[
                {'battle': 0, 'enemy': 3},
                {'battle': 1, 'enemy': 1},
                {'battle': 2, 'enemy': 1},
                {'battle': 3, 'enemy': 1},
                {'battle': 4, 'enemy': 1},
                {'battle': 5, 'boss': 1},
            ],
        ),
        config=dict(
            SUBMARINE=0,
            FLEET_BOSS=0,
            MAP_HAS_AMBUSH=False,
            INTERNAL_LINES_HOUGHLINES_THRESHOLD=40,
            EDGE_LINES_HOUGHLINES_THRESHOLD=40,
        ),
        battle={
            0: 'battle_default',
            5: 'brute_clear_boss',
        },
    ),
}
