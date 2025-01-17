# -*- coding: utf-8 -*-
import cv2

# 读取图像
img = cv2.imread('1371719986828_.pic.jpg')

# 应用高斯模糊
blur_img = cv2.GaussianBlur(img, (225, 225), 0)

# 保存处理后的图像
cv2.imwrite('output.jpg', blur_img)

def update_spin_progress(self, bet):
    ret = {}
    delta_progress = FestivalSystemMath.spin_progress(
        bet, self._one_dollar, self._ctx.property.r_level, 
        self._daily_spin_token, 'valentines_2025'
    )
    if delta_progress > 0:
        self._progress += delta_progress
        self._progress = round(self._progress, 2)
        if self._progress >= 1:
            self._progress = 1
            extra_log = [['from', 'spin']]
            ret.update(self.add_pass_point(self._SPIN_TOKEN, extra_log=extra_log))
            self._daily_spin_token += self._SPIN_TOKEN
            ret.update({
                'valentines_progress': self._progress
            })
        if self._progress >= 1:
            self._progress = 0
    return {'valentines_pass_status': ret}