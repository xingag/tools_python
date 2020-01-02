#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: video_rework.py 
@time: 2019-12-25 15:47 
@description：抖音视频二次创作
"""

from moviepy.video import fx

from util.img_utils import *
from util.video_utils import *
from util.file_utils import *


class Video_Re(object):

    def __init__(self, video_raw_path, desc):
        # 原始素材
        self.video_raw_path = video_raw_path

        # 描述信息
        self.desc = desc

        # 视频和音频
        self.video_clip = None
        self.audio = None

        # 视频的宽、高
        self.video_width = 0
        self.video_height = 0

        # 视频的默认帧率、时长
        self.fps = 25
        self.time = 10

        # 文字字体属性，包含：字体大小、字体颜色、字体位置，一般是上(0)下(1)
        self.font_params = {
            'size': 50,
            'color': 'red',
            'kerning': 5,
            'position': 0
        }

    def run(self):
        # 1、获取视频的属性数据，并裁掉抖音最后加入的素材数据（抖音记录美好生活，一般为3s）
        self.__pre()

        # 2、获取视频的某一帧，去PS量取视频的左上角、右下角坐标
        position1, position2 = self.__get_frame(3)

        # 3、对原视频进行一次剪辑，重新产生一个横向的视频
        croped_video_clip = self.video_crop(position1, position2, './source/temp_source_croped.mp4')

        print(f'视频宽为：{self.video_width}，高为:{self.video_height}，帧率：{self.fps}，时长：{self.time}')

        # 4、一张图片组成背景视频，和视频同帧率、同时长
        image_video_clip = one_pic_to_video('./source/1.jpeg', './source/temp_img_video.mp4', self.fps, self.time)

        # 5、合成两段视频
        synthetic_video_clip = synthetic_video(image_video_clip, croped_video_clip)

        # 6、生成描述信息
        desc_text_clip = generate_text_clip(self.desc, self.font_params, synthetic_video_clip.duration)

        # 7、视频加入描述信息
        video_with_text_clip = video_with_text(synthetic_video_clip, desc_text_clip)

        # 8、视频加入音频，并删除临时文件
        self.video_with_audio(video_with_text_clip)

    def video_crop(self, position1, position2, croped_video_path):
        """
        视频裁剪
        :return:
        """
        # 裁剪的坐标，包含左上角x轴和y轴；右下角x轴和y轴
        clip2 = fx.all.crop(self.video_clip, x1=position1[0], y1=position1[1], x2=position2[0], y2=position2[1])

        # 保存文件
        clip2.write_videofile(croped_video_path)

        # 时长
        self.time = clip2.duration

        return clip2

    def __pre(self):
        """
        准备工作
        :return:
        """
        self.video_raw_clip = VideoFileClip(self.video_raw_path)

        # 视频宽、高
        self.video_width, self.video_height = self.video_raw_clip.w, self.video_raw_clip.h

        self.fps = self.video_raw_clip.fps

        # 分离出音频
        self.audio = self.video_raw_clip.audio.subclip(0, self.video_raw_clip.duration - 4)

        # 裁剪尾部的视频素材
        temp_video_clip = self.video_raw_clip.subclip(0, self.video_raw_clip.duration - 4)

        # 生成新的视频,并保存到本地
        temp_video_clip.set_audio(self.audio)

        video_path = './source/temp_source_video.mp4'

        temp_video_clip.write_videofile(video_path, codec='libx264',
                                        audio_codec='aac',
                                        temp_audiofile='temp-audio.m4a',
                                        remove_temp=True)

        # 重新初始化VideoFileClip，便于后面剪辑
        self.video_clip = VideoFileClip(video_path)

    def __get_frame(self, time):
        """
        获取视频的某一帧
        :param time:
        :return:
        """
        # get_frame_from_video(self.path_video_source, time, './output.jpg')

        # 获取要截取视频的左上坐标、右下坐标（328  631）
        # position1 = (0, 328)
        # position2 = (self.video_width, 631)

        # 注意：坐标值必须为偶数，不然会裁剪失败
        position1 = (0, 328)
        position2 = (self.video_width, 630)

        return position1, position2

    def video_with_audio(self, video_with_text_clip):
        """
        视频合成音频，并删除临时文件
        :return:
        """
        # 设置视频音频，并写入到文件中去
        video_with_text_clip.set_audio(self.audio).write_videofile("output.mp4",
                                                                   codec='libx264',
                                                                   audio_codec='aac',
                                                                   temp_audiofile='temp-audio.m4a',
                                                                   remove_temp=True
                                                                   )
        # 删除所有的临时文件
        del_temp_file("./source/")


if __name__ == '__main__':
    # 原视频文件
    video_source = './source/source.mp4'
    desc = '我是描述信息'

    video_re = Video_Re(video_source, desc)
    video_re.run()
