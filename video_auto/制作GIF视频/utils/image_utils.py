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
import os
from utils.file_utils import *
from utils.video_utils import *
from imgpy import Img
import json
import re

# pip3 install imgpy


def analyseImage(path):
    """
    分析图片
    :param path:
    :return:
    """
    im = Image.open(path)
    results = {
        'size': im.size,
        'mode': 'full',
    }
    try:
        while True:
            if im.tile:
                tile = im.tile[0]
                update_region = tile[1]
                update_region_dimensions = update_region[2:]
                if update_region_dimensions != im.size:
                    results['mode'] = 'partial'
                    break
            im.seek(im.tell() + 1)
    except EOFError:
        pass
    return results


def get_gif_frames(gif_path, temp_path):
    """
    获取一段GIf图片下的所有静态帧
    get_gif_frames('./../gifs/3.gif', './../gif_temp/')
    :param gif_path:
    :return:
    """

    # 分析gif图片
    mode = analyseImage(gif_path)['mode']

    im = Image.open(gif_path)

    i = 1
    p = im.getpalette()
    last_frame = im.convert('RGBA')

    try:
        while True:
            # print("saving %s (%s) frame %d, %s %s" % (gif_path, mode, i, im.size, im.tile))

            '''
            If the GIF uses local colour tables, each frame will have its own palette.
            If not, we need to apply the global palette to the new frame.
            '''
            if not im.getpalette():
                im.putpalette(p)

            new_frame = Image.new('RGBA', im.size)

            '''
            Is this file a "partial"-mode GIF where frames update a region of a different size to the entire image?
            If so, we need to construct the new frame by pasting it on top of the preceding frames.
            '''
            if mode == 'partial':
                new_frame.paste(last_frame)

            new_frame.paste(im, (0, 0), im.convert('RGBA'))
            new_frame.save(temp_path + '/%s-%d.png' % (''.join(os.path.basename(gif_path).split('.')[:-1]), i), 'PNG')

            i += 1
            last_frame = new_frame
            im.seek(im.tell() + 1)
    except EOFError:
        # print('产生EOFError！！！')
        pass


def get_gif_info(gif_path):
    """
    获取gif文件的详细信息
    每一个gif的帧率不一样，有的<10fps；有的>10fps
    :param gif_path:
    :return:
    """
    with Img(fp=gif_path) as im:
        # 1.有多少帧
        frame_count = im.frame_count

        # 2.帧列表-PIL.Image.Image
        # print(im.frames)

        # 3.未知
        # print(im.exif)

        # 4.GIF
        # print(im.format)

        # 5.图片信息
        # {'version': b'GIF89a', 'background': 31, 'duration': 70, 'extension': (b'NETSCAPE2.0', 795), 'loop': 0}
        duration_pre = im.info.get('duration')

        # 根据规律，除以7位实际的播放时长
        duration = duration_pre / 7

        # 6.color palette
        # print(im.mode_desc)

        # print((frame_count, duration))

        # 返回帧率和时长
        return (frame_count / duration), duration