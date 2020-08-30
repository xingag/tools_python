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
@time: 2020-02-01 22:32 
@description：公众号：AirPython
"""

import random

from moviepy.editor import *

from utils.file_utils import *
from utils.math_utils import *


def gene_random():
    """
    生成随机数字
    :return:
    """
    str = ""
    for i in range(6):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        str += ch
    return str


def get_audio_from_video(video_raw_clip, output_path):
    """
    从视频中提取音频
    :param video_raw_clip: 视频Clip对象
    :param output_path: 输出音频文件完整路径
    :return:
    """
    audio = video_raw_clip.audio
    audio.write_audiofile(output_path)

    return output_path


def mov2mp4(video_path, output_path):
    """
    mov格式转为mp4
    注意：原视频文件名不能包含空格
    :param video_path:
    :param output_path:
    :return:
    """
    filename = gene_random()
    try:
        filename = get_file_path_and_name(video_path)[1]
    except Exception as e:
        pass

    output_path = output_path + filename + ".mp4"

    # 格式转换
    os.system('ffmpeg -i %s -qscale 0 %s' % (video_path, output_path))


def pics_to_video(pics_path, output_path, fps):
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
    image_paths = list(filter(lambda image_path: image_path.endswith('.jpg'), image_paths))

    # 图片剪辑类
    clip = ImageSequenceClip(image_paths,
                             fps=fps)

    clip.write_videofile(output_path)


def video_with_other_audio(path_video_raw, path_bgm_raw, output):
    """
    视频合成音频（混合音效）
    :return:
    """
    videoclip = VideoFileClip(path_video_raw)
    audioclip = AudioFileClip(path_bgm_raw)

    new_audioclip = CompositeAudioClip([videoclip.audio, audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile(output)


def video_with_audio(path_video_raw, path_bgm_raw, output):
    """
    视频合成音频
    :return:
    """
    videoclip = VideoFileClip(path_video_raw)
    audioclip = AudioFileClip(path_bgm_raw)

    # 设置视频音频，并写入到文件中去
    videoclip.set_audio(audioclip).write_videofile(output,
                                                   codec='libx264',
                                                   audio_codec='aac',
                                                   temp_audiofile='temp-audio.m4a',
                                                   remove_temp=True
                                                   )
