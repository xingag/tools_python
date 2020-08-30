#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: ninecell_video.py 
@time: 2020-08-28 23:16 
@description：九宫格视频朋友圈
"""

from PIL import Image

from utils.video_utils import *


class VideoObj(object):
    def __init__(self, file_path):
        self.video_raw_clip = VideoFileClip(file_path)

        # 宽、高
        self.video_width, self.video_height = self.video_raw_clip.w, self.video_raw_clip.h

        # 帧率
        self.fps = self.video_raw_clip.fps

        # 视频时长
        self.during = self.video_raw_clip.duration

        # 白色间隙宽度，用于分割图片
        self.item_space = 10

        # 视频原路径
        self.path_video_raw = file_path

        # 临时文件夹，用于保存处理后的帧图片
        self.path_temp = './temp/'

        # 输出文件夹
        self.path_output = './output/'

        # 音频文件保存路径
        self.path_bgm = self.path_temp + 'bg.wav'

        # 临时保存的视频文件
        self.path_video_temp = self.path_temp + 'temp.mp4'

        # 最终输出的视频文件
        self.path_video_output = self.path_output + 'result.mp4'

    def pre(self):
        """
        准备工作
        :return:
        """
        # 新建临时文件夹和输出文件夹
        mkdir_folder(self.path_temp)
        mkdir_folder(self.path_output)

    def start(self):

        # 1、准备工作
        self.pre()

        print('视频宽/高为:', self.video_width, '/', self.video_height, '帧率/时长:', self.fps, '/', self.during)

        # 2、获取音频文件保存到本地
        get_audio_from_video(self.video_raw_clip, self.path_bgm)

        # 3、保存所有的帧图片到临时文件夹
        self.save_frames()

        # 4、将一篮子图片重新合成视频
        pics_to_video(self.path_temp, self.path_video_temp, self.fps)

        # 5、视频加入BGM
        video_with_audio(self.path_video_temp, self.path_bgm, self.path_video_output)

        # 6、删除临时文件
        self.teardown()

    def save_frames(self):
        """
        保存视频的所有帧，并做处理
        :return:
        """
        i = 1
        for frame in self.video_raw_clip.iter_frames():
            image = Image.fromarray(frame)

            # 视频帧图片保存的临时路径（完整路径）
            frame_file_complete_path = self.path_temp + "%04d.jpg" % i

            # 对图片进一步处理，加入白色间隔距离
            self.handle_frame(image, frame_file_complete_path)

            i += 1

    def handle_frame(self, image, frame_file_complete_path):
        """
        对帧图片进一步的处理
        包含，裁剪图片、新建扩张画布、粘贴裁剪图片、保存新图片到本地
        :return:
        """
        # 1、剪成9张图片，计算每张图片的宽、高
        item_width = int(self.video_width / 3)
        item_height = int(self.video_height / 3)

        # 2、新的宽、高
        item_width_new = self.video_width + self.item_space * 2
        item_height_new = self.video_height + self.item_space * 2

        # 3、重新建一个画布背景
        new_image = Image.new(image.mode, (item_width_new, item_height_new),
                              color='white')

        # 4、裁剪图片，然后粘贴到新的画布中去
        # i:横向、j：纵向
        for i in range(0, 3):
            for j in range(0, 3):
                # 裁剪区域
                box = (j * item_width, i * item_height, (j + 1) * item_width, (i + 1) * item_height)

                # 坐标，左、顶部、右、底
                # print(box)

                # 根据区域，裁剪图片
                crop_image = image.crop(box)

                # 横向、纵向第2块和第3块，要加上偏移距离
                x = 0 if j == 0 else (item_width + self.item_space) * j
                y = 0 if i == 0 else (item_height + self.item_space) * i

                # 将9张图片，按照上面计算的坐标值，粘贴到背景中去
                new_image.paste(crop_image, (int(x), int(y)))

        # 保存图片到本地
        new_image.save(frame_file_complete_path)

    def teardown(self):
        """
        最后处理
        :return:
        """
        # 删除临时文件
        remove_folder(self.path_temp)


if __name__ == '__main__':
    # 待处理的文件
    file_path = './raw/至今无人超越的3个动作.mp4'
    video_obj = VideoObj(file_path)

    # 处理
    video_obj.start()
