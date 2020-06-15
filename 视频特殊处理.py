#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: file_utils.py 
@time: 2020-06-15 09:35 
@description：公众号：AirPython
"""

import hashlib

from moviepy.editor import *


def get_file_md5(file_path):
    """
    获取文件的MD5值
    :param file_path:
    :return:
    """
    with open(file_path, 'rb') as file:
        temp_md5 = hashlib.md5()
        temp_md5.update(file.read())
        hash_code = str(temp_md5.hexdigest()).lower()
    return hash_code


def modify_file_md5(file_path):
    """
    修改文件的md5值
    :param file_path:
    :return:
    """
    with open(file_path, 'a') as file:
        file.write("####&&&&")


def get_file_md5_2(file_path):
    """
    分段读取，获取文件的md5值
    :param file_path:
    :return:
    """
    with open(file_path, 'rb') as file:
        md5_obj = hashlib.md5()
        while True:
            buffer = file.read(8096)
            if not buffer:
                break
            md5_obj.update(buffer)
        hash_code = md5_obj.hexdigest()
    md5 = str(hash_code).lower()
    return md5


def handle_frame(image_frame):
    """
    处理图片帧
    :param image_frame:图片帧
    :return:
    """
    image_frame_result = image_frame * 1.2
    # 如果颜色值超过255，直接设置为255
    image_frame_result[image_frame_result > 255] = 255
    return image_frame_result


def increase_video_brightness(file_path):
    """
    增加视频整体亮度
    :param file_path:源视频路径
    :return:
    """
    video = VideoFileClip(file_path)
    result = video.fl_image(handle_frame)

    file_path_new = "/Users/xingag/Desktop/new.mp4"
    result.write_videofile(file_path_new)


def increase_video_brightness2(file_path):
    """
    增加视频整体亮度2
    :param file_path:源视频路径
    :return:
    """
    # 调整系数值
    coefficient_value = 1.2

    video = VideoFileClip(file_path)
    file_path_new = "/Users/xingag/Desktop/new.mp4"
    video.fx(vfx.colorx, coefficient_value).write_videofile(file_path_new)


def decrease_video_brightness(file_path):
    """
    降低亮度
    :param file_path:
    :return:
    """
    # 调整系数值
    coefficient_value = 0.8

    video = VideoFileClip(file_path)
    file_path_new = "/Users/xingag/Desktop/new.mp4"
    video.fx(vfx.colorx, coefficient_value).write_videofile(file_path_new)


def change_video_bhd(file_path):
    """
    黑白处理
    :param file_path:
    :return:
    """
    video = VideoFileClip(file_path)
    file_path_new = "/Users/xingag/Desktop/new.mp4"
    video.fx(vfx.blackwhite).write_videofile(file_path_new)


def change_video_todo(file_path):
    """
    先获取图片帧，单张进行处理，然后合成
    :param file_path:
    :return:
    """
    pass


if __name__ == "__main__":
    file_path = r'/Users/xingag/Desktop/1.mp4'
    # print(get_file_md5_2(file_path))
    # modify_file_md5(file_path)
    # print(get_file_md5_2(file_path))

    # 2、增加亮度
    # increase_video_brightness(file_path)
    # increase_video_brightness2(file_path)

    # 降低亮度
    # decrease_video_brightness(file_path)

    # 3、饱和度
    change_video_bhd(file_path)



# 注意：更多复杂的操作可以参考之前的文章