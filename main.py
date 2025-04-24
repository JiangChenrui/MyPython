# -*- coding: utf-8 -*-
# 导入必要的库
import asyncio
from concurrent.futures import ThreadPoolExecutor
import copy
import time
import cv2
import logging
import unittest

from util import timeit

# 配置日志
logging.basicConfig(level=logging.INFO)

async def async_imread(image_path):
    image = await asyncio.to_thread(cv2.imread, image_path)
    return image

async def async_imwrite(output_path, blurred_img):
    await asyncio.to_thread(cv2.imwrite, output_path, blurred_img)

async def async_GaussianBlur(img, kernel_size, sigma):
    blurred_img = await asyncio.to_thread(cv2.GaussianBlur, img, kernel_size, sigma)
    return blurred_img


# 定义高斯模糊函数
async def gaussian_blur(image_path, output_path, kernel_size=(5, 5), sigma=0):
    # 验证 kernel_size 是否为正奇数
    if kernel_size[0] % 2 == 0 or kernel_size[1] % 2 == 0:
        logging.error("高斯核大小必须是正奇数")
        return None

    try:
        # 读取图像
        img = await async_imread(image_path)
        if img is None:
            logging.error("无法读取图像，请检查路径是否正确")
            return None

        # 应用高斯模糊
        blurred_img =  await async_GaussianBlur(img, kernel_size, sigma)
        # 保存处理后的图像
        await async_imwrite(output_path, blurred_img)
        logging.info(f"高斯模糊处理完成，结果已保存至 {output_path}")

        return blurred_img
    except Exception as e:
        logging.error(f"处理图像时发生错误: {e}")
        return None


# async def main():
#     # 创建自定义线程池
#     # executor = ThreadPoolExecutor(max_workers=5)
#     pic_count = 5
#     input_list = ['input copy {}.jpeg'.format(i+1) for i in range(pic_count)]
#     output_list = ['output copy {}.jpeg'.format(i+1) for i in range(pic_count)]
    
#     tasks = [
#         gaussian_blur(input_list[i], output_list[i])
#         for i in range(pic_count)
#     ]
#     await asyncio.gather(*tasks)


def gaussian_blur_sync(image_path, output_path, kernel_size=(5, 5), sigma=0):
    """同步版本的高斯模糊函数"""
    if kernel_size[0] % 2 == 0 or kernel_size[1] % 2 == 0:
        logging.error("高斯核大小必须是正奇数")
        return None

    try:
        img = cv2.imread(image_path)
        if img is None:
            logging.error("无法读取图像")
            return None
        
        blurred_img = cv2.GaussianBlur(img, kernel_size, sigma)
        cv2.imwrite(output_path, blurred_img)
        logging.info(f"高斯模糊处理完成，结果已保存至 {output_path}")
        return blurred_img
    except Exception as e:
        logging.error(f"处理图像时发生错误: {e}")
        return None


async def main():
    # 创建自定义线程池
    pic_count = 5
    executor = ThreadPoolExecutor(max_workers=pic_count)
    loop = asyncio.get_running_loop()
    
    input_list = ['input copy {}.jpeg'.format(i+1) for i in range(pic_count)]
    output_list = ['output copy {}.jpeg'.format(i+1) for i in range(pic_count)]
    
    tasks = [
        loop.run_in_executor(executor, gaussian_blur_sync, input_list[i], output_list[i])
        for i in range(pic_count)
    ]
    await asyncio.gather(*tasks)


start = time.time()
asyncio.run(main())
logging.info(f"共耗时 {round(time.time()-start, 4)}s")

