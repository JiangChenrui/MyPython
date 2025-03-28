# -*- coding: utf-8 -*-
# 导入必要的库
import copy
import cv2
import logging
import unittest

# 配置日志
logging.basicConfig(level=logging.INFO)

# 定义高斯模糊函数
def gaussian_blur(image_path, output_path, kernel_size=(225, 225), sigma=0):
    # 验证 kernel_size 是否为正奇数
    if kernel_size[0] % 2 == 0 or kernel_size[1] % 2 == 0:
        logging.error("高斯核大小必须是正奇数")
        return None

    try:
        # 读取图像
        img = cv2.imread(image_path)
        if img is None:
            logging.error("无法读取图像，请检查路径是否正确")
            return None

        # 应用高斯模糊
        blurred_img = cv2.GaussianBlur(img, kernel_size, sigma)

        # 保存处理后的图像
        cv2.imwrite(output_path, blurred_img)
        logging.info(f"高斯模糊处理完成，结果已保存至 {output_path}")

        return blurred_img
    except Exception as e:
        logging.error(f"处理图像时发生错误: {e}")
        return None

# gaussian_blur('input.jpeg', 'output.jpeg')

K_SPIN_FREE_GAME = 'spin_free_game'
K_THEME_INFO = 'theme_info'
K_SPIN_FREE_SPINS = 'spin_free_spins'

def do_collect(ctx, req, ret):  # 在前端发送collect_coin请求之后的个性化处理
    if req['type'] == 0:
        ctx.theme.data['map_info']['is_emerald'] = 0
        ctx.theme.data['map_info']['is_gm'] = 0
        ctx.theme.data['map_info']['is_super'] = 0
        if ctx.theme.data['map_info']['map_level'] >= 7:
            ctx.theme.data['map_info']['map_level'] = 0
            ctx.theme.data['map_info']['wager'] = 0
            ctx.theme.data['map_info']['wager_count'] = 0
            ctx.theme.data['map_info']['avg_bet'] = 10000

        ctx.theme.data['map_info']['double_free_flag'] = 0
        ctx.theme.data['map_info']['piggy_bank_flag'] = 0
        ctx.theme.data['map_info']['super_wheel_flag'] = 0
    elif req['type'] == 1:
        pass
        # ctx.theme.data['map_info']['is_super'] = 0
        # if ctx.theme.data['map_info']['map_level'] >= 7:
        #     ctx.theme.data['map_info']['map_level'] = 0
        #     ctx.theme.data['map_info']['wager'] = 0
        #     ctx.theme.data['map_info']['wager_count'] = 0
        #     ctx.theme.data['map_info']['avg_bet'] = 10000
        # for i in range(4):
        #     if ctx.theme.data['map_info']['pot_status'][i] >= 3:
        #         ctx.theme.data['map_info']['pot_status'][i] = 0

    elif req['type'] == 2 and K_SPIN_FREE_GAME in ctx.theme.data:  # 选了，没买
        if 'paid' in ctx.theme.data[K_SPIN_FREE_GAME] and ctx.theme.data[K_SPIN_FREE_GAME]['paid']:
            ctx.theme.data[K_SPIN_FREE_GAME]['choose'] = 1
            ctx.theme.data[K_SPIN_FREE_GAME]['paid'] = 1
            ctx.theme.data['map_info']['is_emerald'] = 1
            ctx.theme.data['emerald_free'] = 1
            ctx.theme.data['emerald_free_bet'] = ctx.theme.data[K_SPIN_FREE_GAME]['bet']
            ret['receive_data'] = ctx.theme.data[K_SPIN_FREE_GAME]
            if K_THEME_INFO not in ret:
                ret[K_THEME_INFO] = {}
            ret[K_THEME_INFO]['first_free'] = ctx.theme.data['first_free']
        else:
            ctx.theme.data[K_SPIN_FREE_GAME]['choose'] = 1
            ctx.theme.data[K_SPIN_FREE_GAME]['paid'] = 0
            ctx.theme.data['map_info']['is_emerald'] = 0
            ret['receive_data'] = ctx.theme.data[K_SPIN_FREE_GAME]
            if K_THEME_INFO not in ret:
                ret[K_THEME_INFO] = {}
            ret[K_THEME_INFO]['first_free'] = ctx.theme.data['first_free']

    elif req['type'] == 3 and K_SPIN_FREE_GAME in ctx.theme.data and ctx.theme.data['first_free']:  # 首次必免费购买free次数
        if K_SPIN_FREE_GAME in ctx.theme.data:
            ctx.theme.data[K_SPIN_FREE_GAME]['choose'] = 1
            ctx.theme.data[K_SPIN_FREE_GAME]['paid'] = 1
            # ctx.theme.data['free_info']['paid'] = 1
            if 'free_spin_total' in ctx.theme.data[K_SPIN_FREE_GAME]:
                ctx.theme.data[K_SPIN_FREE_GAME]['free_spin_total'] += 1
            ctx.theme.data[K_SPIN_FREE_GAME]['free_spins'] += 1
            ctx.theme.data[K_SPIN_FREE_SPINS] = ctx.theme.data[K_SPIN_FREE_GAME]['free_spins']
            ctx.theme.free_spins += 1
            ctx.theme.data['map_info']['is_emerald'] = 1
            ctx.theme.data['emerald_free'] = 1
            ctx.theme.data['emerald_free_bet'] = ctx.theme.data[K_SPIN_FREE_GAME]['bet']
            ret['receive_data'] = ctx.theme.data[K_SPIN_FREE_GAME]
            ctx.theme.data['first_free'] = 0
            if K_THEME_INFO not in ret:
                ret[K_THEME_INFO] = {}
            ret[K_THEME_INFO]['first_free'] = ctx.theme.data['first_free']

class Theme:
    def __init__(self):
        self.data = {
            'first_free': 1,
            'is_emerald': 0,
            'is_gm': 0,
            'is_super': 0,
            'map_level': 0,
            'wager': 0,
            'wager_count': 0,
            'avg_bet': 0,
            'double_free_flag': 0,
            'piggy_bank_flag': 0,
            'super_wheel_flag': 0,
            'pot_status': [0, 0, 0, 0],
        }
        self.free_spins = 0
    def __getitem__(self, item):
        return self.data[item]
    def __setitem__(self, key, value):
        self.data[key] = value
    def __contains__(self, item):
        return item in self.data

class Context:
    def __init__(self):
        self.theme = Theme()

ctx = Context()

def update_badge_task(ctx, ret, task_type, win, game_type, extra_info, **kwargs):
    delta_current = 0
    if 104691 == task_type and game_type == 'bonus' and ctx.theme.data['badge_info'][0]:
        delta_current += ctx.theme.data['badge_info'][0]
        ctx.theme.data['badge_info'][0] = 0
    elif 104692 == task_type and ctx.theme.data['badge_info'][1]:
        delta_current += ctx.theme.data['badge_info'][1]
        ctx.theme.data['badge_info'][1] = 0
    elif 104693 == task_type and game_type == 'bonus' and ctx.theme.data['badge_info'][2]:
        delta_current += ctx.theme.data['badge_info'][2]
        ctx.theme.data['badge_info'][2] = 0
    elif 104694 == task_type and game_type == 'free':
        delta_current += 1
        ctx.theme.data['badge_info'][3] = 0
    elif 104695 == task_type and game_type == 'bonus' and ctx.theme.data['badge_info'][4]:
        delta_current += ctx.theme.data['badge_info'][4]
        ctx.theme.data['badge_info'][4] = 0
    # elif 104696 == task_type and game_type == 'free' and ctx.theme.data['badge_info'][5]:
    #     delta_current += ctx.theme.data['badge_info'][5]
    #     ctx.theme.data['badge_info'][4] = 0
    return delta_current


def update_badge_bonus_task_fixed(ctx, ret, win, extra_info, badge_index, **kwargs):
    """处理bonus类型的任务，固定返回1"""
    delta = 1
    ctx.theme.data['badge_info'][badge_index] = 0
    return delta

def update_badge_bonus_task_dynamic(ctx, ret, win, extra_info, badge_index, **kwargs):
    """处理bonus类型的任务，返回badge_info中的值"""
    if ctx.theme.data['badge_info'][badge_index]:
        delta = ctx.theme.data['badge_info'][badge_index]
        ctx.theme.data['badge_info'][badge_index] = 0
        return delta
    return 0

def update_badge_free_task_fixed(ctx, ret, win, extra_info, badge_index, **kwargs):
    """处理free类型的任务，固定返回1"""
    delta = 1
    ctx.theme.data['badge_info'][badge_index] = 0
    return delta

def update_badge_free_task_dynamic(ctx, ret, win, extra_info, badge_index, **kwargs):
    """处理free类型的任务，返回badge_info中的值"""
    if ctx.theme.data['badge_info'][badge_index]:
        delta = ctx.theme.data['badge_info'][badge_index]
        ctx.theme.data['badge_info'][badge_index] = 0
        return delta
    return 0

def update_badge_normal_task_fixed(ctx, ret, win, extra_info, badge_index, **kwargs):
    """处理普通任务，固定返回1"""
    delta = 1
    ctx.theme.data['badge_info'][badge_index] = 0
    return delta

def update_badge_normal_task_dynamic(ctx, ret, win, extra_info, badge_index, **kwargs):
    """处理普通任务，返回badge_info中的值"""
    if ctx.theme.data['badge_info'][badge_index]:
        delta = ctx.theme.data['badge_info'][badge_index]
        ctx.theme.data['badge_info'][badge_index] = 0
        return delta
    return 0

# 更新配置
TASK_CONFIG = {
    104691: {
        'game_type': 'bonus',
        'badge_index': 0,
        'handler': update_badge_bonus_task_dynamic
    },
    104692: {
        'game_type': None,
        'badge_index': 1,
        'handler': update_badge_normal_task_dynamic
    },
    104693: {
        'game_type': 'bonus',
        'badge_index': 2,
        'handler': update_badge_bonus_task_dynamic
    },
    104694: {
        'game_type': 'free',
        'badge_index': 3,
        'handler': update_badge_free_task_fixed
    },
    104695: {
        'game_type': 'bonus',
        'badge_index': 4,
        'handler': update_badge_bonus_task_dynamic
    },
}

def update_badge_task_new(ctx, ret, task_type, win, game_type, extra_info, **kwargs):
    """优化后的徽章任务更新方法"""
    if task_type not in TASK_CONFIG:
        return 0

    config = TASK_CONFIG[task_type]
    if config['game_type'] is not None and game_type != config['game_type']:
        return 0

    return config['handler'](ctx, ret, win, extra_info, config['badge_index'], **kwargs)

class TestBadgeTasks(unittest.TestCase):
    def setUp(self):
        self.ctx = Context()
        self.ctx.theme.data['badge_info'] = [5, 3, 2, 1, 4]
        self.ret = {}

    def _run_test_case(self, task_type, game_type, expected_delta):
        """运行测试用例并比较新旧方法的结果"""
        ctx_old = copy.deepcopy(self.ctx)
        ctx_new = copy.deepcopy(self.ctx)
        
        delta_old = update_badge_task(ctx_old, self.ret, task_type, True, game_type, {})
        delta_new = update_badge_task_new(ctx_new, self.ret, task_type, True, game_type, {})
        
        self.assertEqual(delta_old, delta_new)
        self.assertEqual(ctx_old.theme.data['badge_info'], ctx_new.theme.data['badge_info'])
        self.assertEqual(delta_new, expected_delta)

    def test_bonus_task_104691(self):
        """测试BONUS类型的任务104691"""
        self._run_test_case(104691, 'bonus', 5)
        
    def test_normal_task_104692(self):
        """测试普通任务104692"""
        self._run_test_case(104692, 'any', 3)
        
    def test_bonus_task_104693(self):
        """测试BONUS类型的任务104693"""
        self._run_test_case(104693, 'bonus', 2)
        
    def test_free_task_104694(self):
        """测试FREE类型的任务104694"""
        self._run_test_case(104694, 'free', 1)
        
    def test_bonus_task_104695(self):
        """测试BONUS类型的任务104695"""
        self._run_test_case(104695, 'bonus', 4)
        
    def test_invalid_game_type(self):
        """测试无效的游戏类型"""
        self._run_test_case(104691, 'free', 0)
        
    def test_invalid_task_type(self):
        """测试无效的任务类型"""
        self._run_test_case(999999, 'bonus', 0)

if __name__ == '__main__':
    unittest.main()