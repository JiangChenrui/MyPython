# -*- coding: utf-8 -*-
import random

def get_journey_stamps(type):
        ret = {'config': [], 'label': 'Cash Journey', 'place': 31}
        if type == 2: # 普通卡包
            ret['config'] = [5, [3, random.randint(3,5)],[0, 0],[0, 0], -1]
        elif type == 3: # frenzy
            ret['config'] = [5, [1, random.randint(3,5)],[0, 0],[1, random.randint(2,4)], -1]
        elif type == 9: # words game 卡包
            ret['config'] = [2, [0, 0], [0, 0], [0, 0], -1]
            ret['stamp_type'] = 5
        elif type == 10: # mansion
            ret['config'] = [1, [1, 3], [0, 0], [0, 0], -1]
            ret['stamp_type'] = 7
        elif type == 11: # club cash
            ret['config'] = [1, [0, 0], [0, 0], [0, 0], -1]
            ret['stamp_type'] = 9
        else:  # wild package
            # ret['config'] = [5, [1, random.randint(3, 5)],[1, self.random_by_weights([20, 5, 1]) + 3],[0, 0], 1, -1]
            ret['config'] = [0, [0, 0], [0, 0], [0, 0], -10]
        return ret


if __name__ == '__main__':
    for i in [2, 3, 4, 9, 10, 11]:
        print get_journey_stamps(i)