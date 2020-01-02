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
@time: 2019-12-26 21:58 
@description：视频工具类
"""

from moviepy.editor import *


def time_to_hms(seconds_time):
    """
    时间转为时分秒
    :param seconds_time: 秒数
    :return:
    """
    m, s = divmod(seconds_time, 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)


def synthetic_video(video1_clip, video2_clip2):
    """
    合成两段视频，生成视频的宽高以第一段视频为准
    :param video1_clip:
    :param video2_clip2:
    :return:
    """
    # 最后生成视频的宽、高
    width, height = video1_clip.w, video1_clip.h

    # 第二段视频的实际宽、高
    video_width, video_height = video2_clip2.w, video2_clip2.h

    # 最第二段视频进行缩放
    video_clip1 = video2_clip2.resize((width, width * video_height / video_width))

    # 合成视频的路径
    synthetic_video_clip = CompositeVideoClip([video1_clip, video_clip1.set_pos("center")])

    synthetic_video_clip.write_videofile(
        './source/temp_synthetic_video.mp4')

    return synthetic_video_clip


def video_with_text(synthetic_video_clip, desc_text_clip):
    """
    视频中加入文字信息
    :param synthetic_video_clip:
    :param param:
    :return:
    """

    video_with_text_clip = CompositeVideoClip([synthetic_video_clip, desc_text_clip.set_start(0)])
    video_with_text_clip.write_videofile(
        './source/temp_video_with_text.mp4')

    return video_with_text_clip

    # video_with_text_clip.write_videofile(
    #     './source/temp_video_with_text.mp4')


def get_frame_from_video(video_name, frame_time, img_path):
    """
    获取视频某个时间的帧图片，保存在本地
    :param video_name: 视频路径
    :param frame_time: 截取帧的时间位置(s)
    :param img_path:生成图片的完整路径
    :return:
    """
    # 秒转为时、分、秒
    time_pre = time_to_hms(frame_time)

    os.system('ffmpeg -ss %s -i %s -frames:v 1 %s' % (time_pre, video_name, img_path))


def generate_text_clip(text_content, font_params, duration):
    """
    产生字幕
    :return:
    """
    # 显示位置
    position = font_params.get('position')
    position_text = 'top' if position == 0 else 'bottom'

    return TextClip(text_content, font='./fonts/STHeiti Medium.ttc',
                    fontsize=font_params.get('size'), kerning=font_params.get('kerning'),
                    color=font_params.get('color')).set_position(("center", 150)).set_duration(duration)

