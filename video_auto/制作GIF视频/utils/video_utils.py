#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: video_utils.py 
@time: 5/28/19 21:08 
@description：视频工具类
"""

from moviepy.editor import *
from utils.math_utils import *


def pics_to_video(pics_path, output_path, fps, duration):
    """
    图片转为视频
    pics_to_video('./../gif_temp/', './../video_temp/temp1.mp4', 20)
    :param pics_path:
    :param output_path:
    :return:
    """
    image_paths = list(map(lambda x: pics_path + x, os.listdir(pics_path)))

    # 注意：这里必须进行一次排序，保证所有帧的顺序是一致
    image_paths = sort_strings_with_emb_numbers(image_paths)

    # 过滤掉非图片
    image_paths = list(filter(lambda image_path: image_path.endswith('.png'), image_paths))

    # 图片剪辑类
    clip = ImageSequenceClip(image_paths,
                             fps=fps)

    # 写成视频之前，需要把gif都转成同一个分辨率
    clip.write_videofile(output_path)
