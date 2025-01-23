# -*- coding: utf-8 -*-
# 导入必要的库
import cv2

# 定义高斯模糊函数
def gaussian_blur(image_path, output_path, kernel_size=(225, 225), sigma=0):
    """
    对图像进行高斯模糊处理
    :param image_path: 输入图像路径
    :param output_path: 输出图像路径
    :param kernel_size: 高斯核大小，必须是正奇数
    :param sigma: 高斯核标准差，0表示自动计算
    :return: 无
    """
    # 读取图像
    img = cv2.imread(image_path)

    # 检查图像是否成功读取
    if img is None:
        print("无法读取图像，请检查路径是否正确")
        return

    # 应用高斯模糊
    blurred_img = cv2.GaussianBlur(img, kernel_size, sigma)

    # 保存处理后的图像
    cv2.imwrite(output_path, blurred_img)

    print(f"高斯模糊处理完成，结果已保存至 {output_path}")

gaussian_blur('input.jpeg', 'output.jpeg')

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

