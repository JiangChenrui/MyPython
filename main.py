# -*- coding: utf-8 -*-
import random
import numpy as np
import config
from slots_game import daily_config
from rocket_config import *
from slots_math.wheel import *
from slots_math.util import *
from system_math.b_system_math import BSystemMath


class RocketMath(BSystemMath):
    CHEST = Wheel(CHEST_CONFIG)
    HELMET_CHEST = Wheel(HELMET_CHEST_CONFIG)
    DUCK_CHEST = Wheel(DUCK_CHEST_CONFIG)
    CHEST_COIN = Wheel(CHEST_COIN_CONFIG)

    # 抽中概率
    _SPIN_PROBABILITY = 0.1

    # 抽中后给多少进度(假设bet=avg_bet)，默认是0.33
    _SPIN_BASE_PROGRESS = 0.34

    # 抽中后最多给多少进度，默认是0.6
    _SPIN_MAX_PROGRESS = 0.6

    # 额外赢钱的系数
    _EXTRA_WIN_COEF = 0.07

    def spin_progress(self, bet, avg_bet, coef, r_level, round=0, is_first_progress=0, is_booster=0):
        if avg_bet == 0:
            avg_bet = 100000
        target_bet = avg_bet * coef * TARGET_BET_COEF[round if round <= 5 else 5]
        rand = TRIGGER_FREQ_COEF[r_level][round if round <= 5 else 5]
        if is_booster:
            rand += 8
            target_bet *= 2.2
        rand = (rand * coef)
        if is_first_progress:
            rand = 3
        ret = float(bet) / target_bet if np.random.randint(rand) == 0 else 0
        return min(0.6, ret)

    def r_level_multi(self,r_level=-1):
        # if r_level == 0:
        #     return 0.5
        return 1.0

    def get_wheel_result(self, ctx,current_pos,chapter,roll_count,super_wheel_booster=0,next_step_num=0,r_level=0,spin_count=0, is_booster=0):
        r = ctx.b_system_processor.b_system['rocket']
        if super_wheel_booster:
            return 6
        rocket_coefficient = self.get_rocket_coefficient(ctx)
        coefficient = self.get_ac_coefficient(rocket_coefficient['rlv'] * rocket_coefficient['steps'])
        user_type = ctx.user_persona.platform_type

        if r._round == 0 and r._index == 5 and r._pos > 1:
            coefficient *= daily_config.AC_CONFIG['rocket_difficulty']['before_end_' + USER_NAME[user_type]]

        weight_list = [1,1,1,1,1,1]
        coming_pos = []
        a = current_pos
        for i in range(6):
            a += 1
            coming_pos.append(a)
        if is_booster and random.random() <= daily_config.AC_CONFIG['rocket_difficulty'].get('no_chute_booster_modify'):
            weight_list = copy.deepcopy(BOOSTER_DICE_WEIGHT[r_level])
            for i, i_value in enumerate(coming_pos):
                if i_value > END_POINT_CONFIG[chapter]:
                    weight_list[i] = 0
                else:
                    if i_value in ROCKET_MAP_CONFIG[chapter]:
                        if ROCKET_MAP_CONFIG[chapter][i_value][0][0] == 0:
                            weight_list[i] /= [8, 15, 25, 25][r_level]
                        if ROCKET_MAP_CONFIG[chapter][i_value][0][0] == 1:
                            weight_list[i] = weight_list[i]
                        if 2 in ROCKET_MAP_CONFIG[chapter][i_value][0]:
                            weight_list[i] = weight_list[i] / [6, 10, 15, 15][r_level]
                        if 4 in ROCKET_MAP_CONFIG[chapter][i_value][0]:
                            weight_list[i] = weight_list[i] / [6, 10, 15, 15][r_level]
                        if 3 in ROCKET_MAP_CONFIG[chapter][i_value][0]:
                            weight_list[i] = 1
            return rand_with_weight(weight_list) + 1
        for i,i_value in enumerate(coming_pos):
            if not i_value > END_POINT_CONFIG[chapter]:
                if i_value in ROCKET_MAP_CONFIG[chapter]:
                    if chapter == 2 and i_value == 85:
                        weight_list[i] = 0
                    if ROCKET_MAP_CONFIG[chapter][i_value][0][0] == 0:
                        if current_pos <= 0.5 * END_POINT_CONFIG[chapter]:
                            if roll_count > ROLL_COUNT_CONFIG[chapter][0]:
                                if spin_count > CHAPTER_PROTECT_TIMES[chapter]:
                                    delta_weigt = 20
                                elif spin_count > CHAPTER_TIMES[chapter]:
                                    delta_weigt = 10
                                else:
                                    r_level_weight = [3,6,8,10]
                                    delta_weigt = r_level_weight[r_level]
                            elif roll_count <= ROLL_COUNT_CONFIG[chapter][1]:
                                if spin_count > CHAPTER_PROTECT_TIMES[chapter]:
                                    delta_weigt = 10
                                elif spin_count > CHAPTER_TIMES[chapter]:
                                    delta_weigt = 4
                                else:
                                    r_level_weight = [1,2,3,4]
                                    delta_weigt = r_level_weight[r_level]
                            else:
                                if spin_count > CHAPTER_PROTECT_TIMES[chapter]:
                                    delta_weigt = 12
                                elif spin_count > CHAPTER_TIMES[chapter]:
                                    delta_weigt = 6
                                else:
                                    r_level_weight = [2,4,5,6]
                                    delta_weigt = r_level_weight[r_level]
                            weight_list[i] += delta_weigt
                        else:
                            if roll_count > ROLL_COUNT_CONFIG[chapter][0]:
                                if spin_count > CHAPTER_PROTECT_TIMES[chapter]:
                                    delta_weigt = 12
                                elif spin_count > CHAPTER_TIMES[chapter]:
                                    delta_weigt = 6
                                else:
                                    r_level_weight = [2,4,5,6]
                                    delta_weigt = r_level_weight[r_level]
                            elif roll_count <= ROLL_COUNT_CONFIG[chapter][1]:
                                if spin_count > CHAPTER_PROTECT_TIMES[chapter]:
                                    delta_weigt = 6
                                elif spin_count > CHAPTER_TIMES[chapter]:
                                    delta_weigt = 2
                                else:
                                    r_level_weight = [1,1,1,2]
                                    delta_weigt = r_level_weight[r_level]
                            else:
                                if spin_count > CHAPTER_PROTECT_TIMES[chapter]:
                                    delta_weigt = 10
                                elif spin_count > CHAPTER_TIMES[chapter]:
                                    delta_weigt = 4
                                else:
                                    r_level_weight = [1,3,3,4]
                                    delta_weigt = r_level_weight[r_level]
                            weight_list[i] += delta_weigt
                    elif ROCKET_MAP_CONFIG[chapter][i_value][0][0] == 1:
                        if current_pos <= 0.5 * END_POINT_CONFIG[chapter]:
                            if roll_count > ROLL_COUNT_CONFIG[chapter][0]:
                                r_level_weight = [4,3,2,2]
                                delta_weigt = r_level_weight[r_level] + coefficient
                            elif roll_count <= ROLL_COUNT_CONFIG[chapter][1]:
                                r_level_weight = [6,5,4,4]
                                delta_weigt = r_level_weight[r_level] + coefficient
                            else:
                                r_level_weight = [5,4,3,3]
                                delta_weigt = r_level_weight[r_level] + coefficient
                            weight_list[i] += delta_weigt
                        else:
                            if roll_count > ROLL_COUNT_CONFIG[chapter][0]:
                                r_level_weight = [6,5,4,4]
                                delta_weigt = r_level_weight[r_level] + coefficient
                            elif roll_count <= ROLL_COUNT_CONFIG[chapter][1]:
                                r_level_weight = [8,7,6,6]
                                delta_weigt = r_level_weight[r_level] + coefficient
                            else:
                                r_level_weight = [5,4,3,3]
                                delta_weigt = r_level_weight[r_level] + coefficient
                            weight_list[i] += delta_weigt
                    elif ROCKET_MAP_CONFIG[chapter][i_value][0][0] == 2:
                        r_level_weight = [1,1,2,2]
                        weight_list[i] += r_level_weight[r_level]
                    else:
                        if np.random.randint(100) > 0:
                            weight_list[i] = 0
                else:
                    if random.randint(0,2) == 0:
                        r_level_weight = [40,20,10,10]
                        for k in range(3):
                            weight_list[k] += r_level_weight[r_level] - i
        if next_step_num:
            return next_step_num
        return rand_with_weight(weight_list) + 1

    def get_ac_coefficient(self, num):
        return int(num * 10) - 10

    def rocket_forward(self, ctx,chapter,current_pos,wheel_result,avg_bet, t_list, no_chute_booster=0, has_helmet=0, r_level=0):
        current_pos += wheel_result
        chest = {}
        finish_chapter = 0
        is_chute = 0
        is_helmet = 0
        is_rocket = 0
        is_portal = 0
        helmet_chest_flag = 0
        # print '---------current_pos----------'
        # print wheel_result
        # print current_pos
        # print '---------current_pos----------'
        if current_pos in ROCKET_MAP_CONFIG[chapter]:
            boost_result = ROCKET_MAP_CONFIG[chapter][current_pos]
            for i in boost_result[0]:
                if i == 0:
                    is_rocket = 1
                    current_pos = boost_result[1]
                    if current_pos in ROCKET_MAP_CONFIG[chapter]:
                        current_pos = self.prize_progress(ctx, chapter, avg_bet, current_pos, chest, t_list, has_helmet, helmet_chest_flag, r_level)
                elif i == 1 and not no_chute_booster:
                    if not has_helmet:
                        is_chute = 1
                        current_pos = boost_result[1]
                        if current_pos in ROCKET_MAP_CONFIG[chapter]:
                            current_pos = self.prize_progress(ctx, chapter, avg_bet, current_pos, chest, t_list,  has_helmet, helmet_chest_flag, r_level, no_helmet=1 if len(boost_result[0]) > 1 else 0)
                    else:
                        is_helmet = 1
                elif i == 2:
                    current_pos = self.prize_progress(ctx, chapter, avg_bet, current_pos, chest, t_list, has_helmet, helmet_chest_flag, r_level)
                elif i == 3:
                    is_portal = 1
                    current_pos = boost_result[1]
                elif i == 4:
                    current_pos = self.prize_progress(ctx, chapter, avg_bet, current_pos, chest, t_list, has_helmet, helmet_chest_flag, r_level)

        if current_pos >= END_POINT_CONFIG[chapter]:
            finish_chapter = 1
        ret = {
            'chest':chest,
            'current_pos':current_pos,
            'finish_chapter':finish_chapter,
            'is_chute':is_chute,
            'is_helmet': is_helmet,
            'is_rocket':is_rocket,
            'is_portal':is_portal,
            't_list': t_list,
        }

        # print '---------current_pos2----------'
        # print current_pos
        # print '---------current_pos2----------'
        return ret

    def check_in_prize(self, chapter, current_pos, t_list):
        ret = 0
        if ROCKET_MAP_CONFIG[chapter][current_pos][0][0] == 2 or ROCKET_MAP_CONFIG[chapter][current_pos][0][0] == 4:
            ret = 1
            flash_prize = copy.deepcopy(FLASH_PRIZE[chapter])
            for i_index, i in enumerate(flash_prize):
                if i_index < len(t_list) and i_index < len(flash_prize):
                    if flash_prize[i_index] == current_pos and t_list[i_index] == 0:
                        t_list[i_index] += 1
                    elif flash_prize[i_index] == current_pos and t_list[i_index] == 1:
                        ret = 0
        return ret

    def prize_progress(self, ctx, chapter, avg_bet, current_pos, chest, t_list, has_helmet, helmet_chest_flag, r_level, no_helmet=0):
        if self.check_in_prize(chapter, current_pos, t_list):
            box_info = self.do_rocket_box(ctx, chapter, avg_bet, current_pos, has_helmet=(has_helmet or helmet_chest_flag), r_level=r_level, no_helmet=no_helmet)
            chest.update(box_info['chest'])
            if 'helmet_flag' in box_info:
                helmet_chest_flag = 1
            if not current_pos == box_info['finish_pos']:
                current_pos = box_info['finish_pos']
                if current_pos in ROCKET_MAP_CONFIG[chapter] and self.check_in_prize(chapter, current_pos, t_list):
                    box_info = self.do_rocket_box(ctx, chapter, avg_bet, current_pos, no_rocket=1, has_helmet=(has_helmet or helmet_chest_flag), r_level=r_level)
                    chest.update(box_info['chest'])
        return current_pos

    def generate_limit_prize(self, chapter):
        length = len(FLASH_PRIZE[chapter])
        duration = TIME_CONFIG[chapter]

        return [0]*length, duration

    def do_rocket_box(self, ctx, chapter, avg_bet, current_pos,no_rocket=0,has_helmet=0, r_level=0, no_helmet=0):
        rocket_coefficient = self.get_rocket_coefficient(ctx)
        reward_coefficient = rocket_coefficient['rlv'] * rocket_coefficient['collect'] * rocket_coefficient['steps']
        result = ROCKET_MAP_CONFIG[chapter][current_pos]
        finish_pos = current_pos
        chest = {}
        helmet_flag = 0  # 是否获得头盔
        if result[0][0] == 2:
            chest_result = {}
            chest_type = self.CHEST.spin(index=no_rocket)
            if (has_helmet and chest_type == 5) or no_helmet:
                chest_type = self.HELMET_CHEST.spin(index=no_rocket)
            chest_result['type'] = chest_type
            if chest_type == 1:
                coins = int(avg_bet * float(np.random.choice([0.1, 0.2, 0.5, 1, 1.5],p=[0.2, 0.2, 0.3, 0.2, 0.1])) * 0.2 / float(5000) * 5000 * reward_coefficient)
                chest_result['coins'] = coins
            elif chest_type == 2:
                chest_result['ratio'] = 15
            elif chest_type == 3:
                chest_result['count'] = random.randint(1, 3)
            elif chest_type == 4:
                candidate_list = []
                if current_pos + 12 >= END_POINT_CONFIG[chapter]:
                    destination = END_POINT_CONFIG[chapter]
                    step = destination - current_pos
                    finish_pos = destination
                    chest_result['step'] = step
                else:
                    for k in range(current_pos + 11, END_POINT_CONFIG[chapter]):
                        if k not in ROCKET_MAP_CONFIG[chapter] or (
                                        # chapter == 6 and  # 此行用于规避超级火箭飞到有奖励的地方
                                        k in ROCKET_MAP_CONFIG[chapter] and len(
                                            ROCKET_MAP_CONFIG[chapter][k][0]) == 1 and
                                            ROCKET_MAP_CONFIG[chapter][k][0][0] == 2):
                            candidate_list.append(k)
                    weight_list = self.generate_normal_weight(len(candidate_list))
                    destination = candidate_list[rand_with_weight(weight_list)]
                    step = destination - current_pos
                    finish_pos = destination
                    chest_result['step'] = step
            elif chest_type == 5:
                helmet_flag = 1
                chest_result['chip_price'] = [1000,800,600,500][r_level]  # 重新激活头盔的第二货币价格
            chest[str(current_pos)] = chest_result
            ret = {
                'current_pos':current_pos,
                'chest':chest,
                'finish_pos':finish_pos
            }
            if helmet_flag:
                ret.update({
                    'helmet_flag': 1
                })
            return ret
        elif result[0][0] == 4:
            chest_result = {}
            chest_type = self.DUCK_CHEST.spin()
            chest_result['type'] = chest_type
            if chest_type == 101:
                chest_result['stamp'] = [5, [0, 0], [0, 0], [1, 3], -1]
            elif chest_type == 102:
                chest_result['duration'] = 24 * 3600
            elif chest_type == 103:  # slot of cash
                pass
            elif chest_type == 104:
                chest_result['duration'] = 24 * 3600
            elif chest_type == 105:  # super bomb bonus game
                pass
            elif chest_type == 106:
                chest_result['chips'] = [100,80,60,50][r_level]
            chest[str(current_pos)] = chest_result
            ret = {
                'current_pos': current_pos,
                'chest': chest,
                'finish_pos': finish_pos
            }
            return ret


    def get_rocket_coefficient(self, ctx):
        user_type = ctx.user_persona.platform_type
        rlv = ctx.property.r_level
        rlv_coefficient = daily_config.AC_CONFIG['rocket_difficulty'][USER_INDEX[rlv]+'_coefficient_'+USER_NAME[user_type]]
        meter_collecting_coefficient = daily_config.AC_CONFIG['rocket_difficulty']['meter_collecting_'+ USER_NAME[user_type]]
        steps_to_end_coefficient = daily_config.AC_CONFIG['rocket_difficulty']['steps_to_endpoint_'+ USER_NAME[user_type]]
        ret = {
            'rlv':rlv_coefficient,
            'collect':meter_collecting_coefficient,
            'steps':steps_to_end_coefficient
        }
        return ret


    def generate_normal_weight(self, length):
        weight_list = []
        for i in range(length):
            if i <= 0.3 * length:
                weight_list.append(i + 1)
            else:
                weight_list.append(length - i)
        return weight_list