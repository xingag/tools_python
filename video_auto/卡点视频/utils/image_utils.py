#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: image_utils.py 
@time: 5/17/19 13:03 
@description：图像工具类
"""
from PIL import Image


def resize_image(target_image_path, target_size):
    """
    调整图片大小，缺失的部分用黑色填充
    :param target_image_path: 图片路径
    :param target_size: 分辨率大小
    :return:
    """
    image = Image.open(target_image_path)

    iw, ih = image.size  # 原始图像的尺寸
    w, h = target_size  # 目标图像的尺寸
    scale = min(w / iw, h / ih)  # 转换的最小比例

    # 保证长或宽，至少一个符合目标图像的尺寸
    nw = int(iw * scale)
    nh = int(ih * scale)

    image = image.resize((nw, nh), Image.BICUBIC)  # 缩小图像
    # image.show()

    new_image = Image.new('RGB', target_size, (0, 0, 0, 0))  # 生成黑色图像
    # // 为整数除法，计算图像的位置
    new_image.paste(image, ((w - nw) // 2, (h - nh) // 2))  # 将图像填充为中间图像，两侧为灰色的样式
    # new_image.show()

    # 覆盖原图片
    new_image.save(target_image_path)
