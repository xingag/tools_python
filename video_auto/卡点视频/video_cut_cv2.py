#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: video_cut.py 
@time: 5/16/19 17:18 
@description：Python 生成一段10s的卡点视频
"""

import cv2
import numpy as np
import time
import os
import math
from utils.file_utils import *
from utils.image_utils import *
from PIL import Image

# 最后影片的分辨率片，根据视频来设置，默认是1920*1080
img_size = (int(1920), int(1080))


def cut_film(soure_filename, output_filename, start_time, peroid):
    """
    裁剪视频
    :param start_time: 开始时间【s】
    :param peroid: 持续时间【s】
    :param soure_filename 源视频
    :param output_filename 输出视频
    :return:
    """
    global img_size

    # 数据源
    videoCapture = cv2.VideoCapture(soure_filename)

    if videoCapture.isOpened():
        print('open success')
    else:
        print('open fail')

    fps = videoCapture.get(cv2.CAP_PROP_FPS)

    # 获取大小(1920*1080)
    img_size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    video_writer = cv2.VideoWriter(output_filename, cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, img_size)

    i = 0

    # 开始帧和结束帧
    start_frame = fps * start_time
    end_frame = start_frame + peroid * fps

    print(type(start_frame))
    print('即将裁剪的开始帧为:%f,结束帧为:%f' % (start_frame, end_frame))

    while True:
        success, frame = videoCapture.read()  # 循环读取下一帧

        if success:
            i += 1
            if start_frame <= i <= end_frame:
                # 将截取到的画面写入“新视频”
                video_writer.write(frame)
        else:
            print('end')
            break

    videoCapture.release()

    return fps


def compound_film(film_names, video_output_path):
    """
    合并视频
    :param film_names:
    :return:
    """
    print('一共要合成%d段视频' % len(film_names))
    print(film_names)

    # 通过第一个视频，获取帧率、宽、高
    videoCaptureNorm = cv2.VideoCapture(film_names[0])

    # 帧率、宽、高
    fps = videoCaptureNorm.get(cv2.CAP_PROP_FPS)
    width = (int(videoCaptureNorm.get(cv2.CAP_PROP_FRAME_WIDTH)))
    height = (int(videoCaptureNorm.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    # =====================================================================
    # 待写入对象，写入到result.mp4文件中
    videoWriter = cv2.VideoWriter(video_output_path, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (width, height))

    for index, film_name in enumerate(film_names):
        print('视频名称:%s' % film_name)
        videoCapture = cv2.VideoCapture(film_name)

        # 循环写入数据
        while True:
            success, frame = videoCapture.read()

            # 视频必须保证分辨率一致，才能合并
            # frame_suitable = cv2.resizeWindow(frame, (width, height), interpolation=cv2.INTER_CUBIC)
            videoWriter.write(frame)
            if success:
                continue
            else:
                break

        videoCapture.release()
        print('第%d个视频合成完成~' % (index + 1))

    videoWriter.release()
    videoCaptureNorm.release()


def compound_pic_special(images_path, output_video_path, fps):
    """
    图片合成视频【卡点视频】
    :param path: 图片文件路径
    :param output_video_path:合成视频的路径
    :param size:
    :return:
    """

    # 获取该目录下的所有文件名
    filelist = os.listdir(images_path)

    print('一共有%d张图片' % len(filelist))

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

    video = cv2.VideoWriter(output_video_path, fourcc, fps, img_size)

    total_count = math.ceil(fps / 2)
    print('每张图片都需要重复写入%d帧' % total_count)

    for item in filelist:
        if item.endswith('.jpg'):  # 判断图片后缀是否是.jpg
            image_path = images_path + '/' + item

            # 缩放图片到合适的分辨率，并覆盖源文件
            resize_image(image_path, img_size)

            frame = cv2.imread(image_path)

            # 直接缩放到指定大小
            frame_suitable = cv2.resize(frame, (img_size[0], img_size[1]), interpolation=cv2.INTER_CUBIC)

            # 把图片写进视频
            # 重复写入多少次
            count = 0
            while count < total_count:
                video.write(frame_suitable)
                count += 1
        else:
            print('名称为:%s,文件格式不对，过滤掉~' % item)
    # 释放资源
    video.release()


def compound_bgm(video_path, bgm_path):
    """
    通过视频、BGM 合成一段视频
    :param video_path: 视频路径
    :param bgm_path: BGM路径
    :return:
    """
    # $ ffmpeg -i 2_003_014.mp4 -vn -y -acodec copy 3.aac
    # 1.提前temp.mp4这个视频的BGM，文件结果为：temp.aac
    # os.system('ffmpeg -i temp.mp4 -vn -y -acodec copy temp.aac')

    # 2.获取视频的长度
    cap = cv2.VideoCapture(video_path)
    # 帧率
    fps = cap.get(cv2.CAP_PROP_FPS)
    # 总帧数
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    # 总时长-秒，这里做取整操作 【浮点类型】
    time_count = math.floor(frame_count / fps)

    print('帧率:%f,总帧数:%d' % (fps, frame_count))
    print(time_count)

    # 3.截取音频
    # 为了简单，这里一般不会超过一分钟
    bgm_temp_path = get_temp_path(bgm_path, 'temp_new')
    os.system('ffmpeg -i %s -ss 00:00:00 -t 00:00:%d -acodec copy %s' % (bgm_path, time_count, bgm_temp_path))

    # 3.1 删除源音频并重命令当前文件
    os.remove(bgm_path)
    os.rename(bgm_temp_path, bgm_path)

    # 4.视频、音频合二为一
    video_temp_path = get_temp_path(video_path, 'temp')
    os.system('ffmpeg -i %s  -i %s  -vcodec copy -acodec copy %s' % (video_path, bgm_path, video_temp_path))
    os.remove(video_path)
    os.rename(video_temp_path, video_path)

    print('音视频合成完成~')


def add_water_mask(video_path, mask_word):
    """
    给视频增加水印
    :param video_part3: 视频源
    :param mask_word: 水印文字
    :return:
    """
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 保证帧率不变
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video_temp_path = get_temp_path(video_path, 'temp')
    video_writer = cv2.VideoWriter(video_temp_path, fourcc, fps, img_size)

    ret, frame = cap.read()

    while ret:
        # 文字在图中的坐标(注意:这里的坐标原点是图片左上角)
        x, y = img_size[0] - 200, img_size[1] - 50

        cv2.putText(img=frame, text=mask_word,
                    org=(x, y), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    fontScale=1, color=(255, 255, 255))

        video_writer.write(frame)
        ret, frame = cap.read()

    # 删除源文件，并重命名临时文件
    os.remove(video_path)
    os.rename(video_temp_path, video_path)

    print('水印添加完成~')
    video_writer.release()
    cap.release()


def make_sticke_point_video(source_film_path, source_image_path, source_bgm_path):
    """
    制作卡点视频
    :return:
    """
    # 说明：一共10s
    # 素材：一段2s的视频，然后准备16张图片，每张图片显示0.5s

    # 1.从一段视频中剪辑前2s的视频
    # 也可以指定开始帧和持续时间
    # 生成的第一段视频2s
    video_part1 = './part1.mp4'
    fps = cut_film(source_film_path, video_part1, 3, 2)
    print('第一段视频剪辑完成~')
    print('第一段视频的帧率是:%f' % fps)

    # 2.把所有图片合成一个视频
    # 分析：一张图片0.5s，一共16张图片，一共8s；1张图片1帧，fps：2帧/s
    # fps:2 1秒2帧
    # 注意：由于最后合成的一段视频帧率为同一个值，这里设置需要一张图片写入30帧，即30次
    video_part2 = './part2.mp4'
    compound_pic_special(source_image_path, video_part2, fps)
    print('第二段视频合成完成~')

    # 3.把两段视频拼接在一起
    video_part3 = './output.mp4'
    compound_film([video_part1, video_part2], video_part3)
    print('上面两段视频合并完成~')

    # 4.给视频加入水印
    add_water_mask(video_part3, '@xingag')

    # 5.加入背景音乐
    compound_bgm(video_part3, source_bgm_path)


if __name__ == '__main__':
    # 制作卡点视频
    source_film_path = './1.mp4'
    source_image_path = './images'
    source_bgm_path = './bgm.aac'
    make_sticke_point_video(source_film_path, source_image_path, source_bgm_path)
