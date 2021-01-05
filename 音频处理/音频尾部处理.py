#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: 尾部处理.py 
@time: 2021-01-02 09:59 
@description：TODO
"""

from pydub import AudioSegment
from pydub.playback import play

video_path = './raw.mp4'


def speed_change(sound, speed=1.0):
    """
    改变音频的速度
    参考：https://www.thinbug.com/q/51434897
    :param sound:
    :param speed:
    :return:
    """
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)


# 注意：加载视频不需要指定format
audio_sgement = AudioSegment.from_file(video_path)

# 截取尾部内容
audio_end = audio_sgement[70 * 1000:70 * 1000 + 3000]

# 变慢速度，具体根据视频速度去调整
audio_end2 = speed_change(audio_end, 0.55)

# 合并两段音频
audio_result = audio_end + audio_end2

# 尾部淡出处理
audio_result.fade_out(1000)

# 实时播放，方便调试
# play(audio_result)

# 视频导出
audio_result.export("result.wav", format='wav')


