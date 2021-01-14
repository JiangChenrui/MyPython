# -*- coding: utf-8 -*-

BINGO_INDEX_PRIZE = [
    {  # 1
        'stamp_list': [{
            # 'config': [5, [2, 3], [0, 0], [0, 0], -1],
            # 'label': 'Bingo Frenzy',
            # 'place': 14,
            # 'config': [5, [0, 0], [0, 0], [1, 4], -1],
            'config': [1, [0, 0], [1, 3], [0, 0], -1],
            'label': 'Bingo Frenzy',
            'place': 14,
            # 'stamp_type': 5
        }],
        # 'lounge_pass': 3,
        # 'atw': [0, 5, 0, 0, 0],
        'base_coins': 5,
    },
    {  # 2
        # 'stamp_list': [{
        #     'config': [1, [0, 0], [1, 3], [0, 0], -1],
        #     'label': 'Bingo Frenzy',
        #     'place': 14
        # }],
        # 'mq_skip_card': 1,
        'atw': [0, 0, 5, 0, 0],
        # 'lounge_pass': 1,
        # 'wild_depot_puzzles': 10,
        'byd': [0, 5, 0, 0],
        'base_coins': 8
    },
    {  # 3
        # 'stamp_list': [{
        #     'config': [5, [0, 0], [0, 0], [0, 0], 1, -1],
        #     'label': 'Bingo Frenzy',
        #     'place': 14
        # }],
        'coupon_list': [{
            'coupon_type': 21,
            'ratio': 25,
            'duration': 86400  # 单位:秒
        }],
        # 'atw': [0, 0, 3, 0, 0],
        # 'byd': [0, 25, 0, 0],
        'chips': 100,
        'base_coins': 10,
    },
    {  # 4
        # 'coupon_list': [{
        #     'coupon_type': 20,
        #     'ratio': 60,
        #     'duration': 86400  # 单位:秒
        # }],
        # 'stamp_list': [{
        #     # 'config': [1, [0, 0], [1, 3], [0, 0], -1],
        #     'config': [5, [0, 0], [0, 0], [1, 3], -1],
        #     'label': 'Bingo Frenzy',
        #     'place': 14
        # }],
        'atw': [0, 0, 0, 1, 0],
        'byd': [0, 0, 1, 0],
        'base_coins': 10
    },
    {  # 5
        'stamp_list': [{
            'config': [5, [0, 0], [0, 0], [1, 3], -1],
            'label': 'Bingo Frenzy',
            'place': 14
            # 'config': [5, [0, 0], [0, 0], [0, 0], 1, -1],
            # 'label': 'Bingo Frenzy',
            # 'place': 14
        }],
        # 'chips': 50,
        'coupon_list': [{
            'coupon_type': 20,
            'ratio': 60,
            'duration': 86400  # 单位:秒
        }],
        # 'byd': [0, 25, 0, 0],
        # 'atw': [0, 0, 0, 1, 0],
        # 'byd': [0, 0, 3, 0],
        # 'chips': 100,
        'base_coins': 20,
    },
    {  # 6
        'stamp_list': [{
            # 'config': [5, [0, 0], [0, 0], [1, 3], -1],
            'config': [1, [0, 0], [1, 4], [0, 0], -1],
            'label': 'Bingo Frenzy',
            'place': 14
        }],
        # 'atw': [0, 0, 0, 0, 1],
        # 'byd': [0, 0, 1, 0],
        'mq_skip_card': 1,
        'base_coins': 30
    },
    {  # 7
        # 'stamp_list': [{
        #     'config': [1, [0, 0], [1, 4], [0, 0], -1],
        #     'label': 'Bingo Frenzy',
        #     'place': 14
        # }],
        # 'byd': [0, 0, 0, 1],
        # 'coupon_list': [{
        #     'coupon_type': 21,
        #     'ratio': 25,
        #     'duration': 86400  # 单位:秒
        # }],
        'byd': [0, 0, 0, 1],
        'atw': [0, 0, 0, 0, 1],
        'base_coins': 45
    }
]

BINGO_FINAL_PRIZE = {
    0: {
        'stamp_list': [{
            'config': [5, [0, 0], [0, 0], [1, 4], -1],
            'label': 'Bingo Frenzy',
            'place': 14
        }],
        # 'atw': [0, 0, 0, 3, 0],
        'byd': [0, 0, 3, 0],
        # 'wild_depot_puzzles': 20,
        'base_coins': 80,
    },
    1: {
        'stamp_list': [{
            'config': [5, [0, 0], [0, 0], [1, 5], -1],
            'label': 'Bingo Frenzy',
            'place': 14
        }],
        # 'byd': [0, 0, 0, 1],
        'atw': [0, 0, 0, 5, 0],
        'base_coins': 100
    },
    2: {
        'stamp_list': [{
            'config': [0, [0, 0], [0, 0], [0, 0], -1],
            'label': 'Bingo Frenzy',
            'place': 14
        }],
        'byd': [0, 0, 5, 0],
        # 'atw': [0, 0, 0, 5, 0],
        # 'wild_depot': [50000],
        # 'chips': 500,
        'base_coins': 100
    },
    -1: {
        'stamp_list': [{
            'config': [5, [0, 0], [0, 0], [1, 5], -1],
            'label': 'Bingo Frenzy',
            'place': 14
        }],
        'atw': [0, 0, 0, 5, 0],
        # 'byd': [0, 0, 0, 1],
        # 'wild_depot_puzzles': 20,
        'base_coins': 100
    },
}

