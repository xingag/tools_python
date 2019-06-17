#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: xag
@license: Apache Licence
@contact: xinganguo@gmail.com
@site: http://www.xingag.top
@software: PyCharm
@file: gif_make_video.py
@time: 5/26/19 22:22
@description：抓取一些gif，转为视频
"""

from moviepy.editor import *
import cv2
from utils.image_utils import *
import math


class Gif_TO_VIDEO(object):
    def __init__(self, gifs_path, bgm_path):
        # gif目录
        self.gifs_path = gifs_path

        # BGM目录
        self.bgm_path = bgm_path

        # 视频帧率
        self.fps = 10

        self.img_size = (int(1280), int(720))

        # gif文件临时目录
        self.temp_gif_path = './gif_temp/'

        # 视频文件临时目录
        self.temp_video_path = './video_temp/'

        # 合成的视频文件完整目录
        self.video_output_temp = './video_temp/target_temp.mp4'

        # 最后生成的视频文件目录
        self.video_output = './target.mp4'

    def run(self):
        # 1.获取所有gif的文件
        gifs_path = self.__get_gifs()

        # 2.遍历文件，分别把每个gif转成一个视频
        videos_output = []
        for gif_path in gifs_path:
            print('要处理的gif文件完整路径是：%s' % gif_path)

            # 获取文件名，不带后缀
            filename = get_filePath_fileName_all(gif_path)[2]

            # 输出的文件名
            video_name = self.temp_video_path + filename + ".mp4"

            self.__gif_to_video(gif_path, video_name)

            # 所有输入视频片段的完整路径
            videos_output.append(video_name)

            # 清空gif文件夹
            clean_a_folder(self.temp_gif_path)

        # 3.遍历视频目录，合并成一个视频
        self.compound_a_video(videos_output)
        print('合成单个视频成功~')

        # 4.合并音视频
        self.__add_bgm_to_video()
        print('恭喜，合成一条包含BGM的视频成功！！！')

        # 5.清空临时视频文件夹
        clean_a_folder(self.temp_video_path)

    def __get_gifs(self):
        """
        获取所有gif列表
        :return:
        """

        list_temp = list(map(lambda x: self.gifs_path + x, os.listdir(self.gifs_path)))

        # 排序
        list_temp.sort()

        print('排序之后的gif文件列表数据为：')
        print(list_temp)

        # 过滤一次，保证获取到的是gif图片
        return list(filter(lambda gif_path: gif_path.endswith('.gif'), list_temp))

    def __gif_to_video(self, gif_path, video_name):
        """
        gif转为视频
        :param gif_path:源gif的完整路径
        :param video_name:视频输出的完整目录
        :return:
        """
        # 1.把gif图片转为帧图片
        get_gif_frames(gif_path, self.temp_gif_path)

        # 2.把帧图片转为固定分辨率的图片
        file_paths_pre = os.listdir(self.temp_gif_path)

        file_paths = list(filter(lambda gif_path: gif_path.endswith('.png'), file_paths_pre))

        for file_path in file_paths:
            resize_image(self.temp_gif_path + file_path, self.img_size)
        print('图片分辨率批量修改成功！')

        # 3.把图片合并成一个视频
        # 注意：如果直接对图片采用固定的帧率处理，会导致最后生成的视频不流畅
        source_frame_rate, source_duration = get_gif_info(gif_path)

        print('源gif的帧率为:%f,时长为:%fs' % (source_frame_rate, source_duration))

        # 4.获取当前视频应该播放的时长
        duration = source_duration / (self.fps / source_frame_rate)

        # print('现有视频,帧率设置为:%d,时长应该设置为:%f' % (self.fps, duration))

        pics_to_video(self.temp_gif_path, video_name, self.fps, duration)

        print('合成视频素材:%s成功' % video_name)

    def compound_a_video(self, videos_path):
        """
        合成一个视频
        :param videos_output:视频集合的完整目录
        :return:
        """
        # 定义一个数组
        L = []

        for video_path in videos_path:
            # 载入视频
            video = VideoFileClip(video_path)
            # 添加到数组
            L.append(video)

        # 拼接视频
        final_clip = concatenate_videoclips(L)

        # 生成目标视频文件
        final_clip.to_videofile(self.video_output_temp, fps=self.fps, remove_temp=False)

    def __add_bgm_to_video(self):
        """
        针对合成的视频，新增BGM
        :return:
        """
        # 1.音频文件
        audioclip = AudioFileClip(self.bgm_path)

        # 2.视频文件
        videoclip = VideoFileClip(self.video_output_temp)

        # 3.获取视频和音频的时长
        video_time = videoclip.duration
        audio_time = audioclip.duration

        print('视频时长:%f，音频时长:%f' % (video_time, audio_time))

        # 4.对视频或者音频进行裁剪
        if video_time > audio_time:
            # 视频时长>音频时长，对视频进行截取
            videoclip_new = videoclip.subclip(0, audio_time)
            audioclip_new = audioclip
        else:
            # 音频时长>视频时长，对音频进行截取
            videoclip_new = videoclip
            audioclip_new = audioclip.subclip(0, video_time)

        # 5.视频中加入音频
        video_with_new_audio = videoclip_new.set_audio(audioclip_new)

        # 6.写入到新的视频文件中
        video_with_new_audio.write_videofile("mp4_with_audio.mp4",
                                             codec='libx264',
                                             audio_codec='aac',
                                             temp_audiofile='temp-audio.m4a',
                                             remove_temp=True
                                             )


if __name__ == '__main__':
    # gif目录
    gif_path = './gifs/'

    # BGM目录
    bgm_path = './backup/dancy.mp3'

    gif_to_video = Gif_TO_VIDEO(gif_path, bgm_path)

    # 把所有gif转换为一个视频
    gif_to_video.run()
