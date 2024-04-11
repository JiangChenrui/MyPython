# -*- coding: utf-8 -*-
import cv2

# 读取图像
img = cv2.imread('input.jpeg')

# 应用高斯模糊
blur_img = cv2.GaussianBlur(img, (155, 155), 0)

# 保存处理后的图像
cv2.imwrite('output.jpg', blur_img)