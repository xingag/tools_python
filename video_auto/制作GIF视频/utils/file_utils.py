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
@time: 5/17/19 10:15 
@description：文件操作工具类
"""
import os
import shutil


def rename(str):
    os.rename(str, './../temp_new1.aac')


def get_temp_path(file_path, temp_name):
    """
    获取同一级目录下临时文件的完整路径
    :param str:
    :return:
    """
    filepath, filename_with_extension, filename_without_extension, extension = get_filePath_fileName_all(file_path)

    return filepath + "/" + temp_name + extension


def get_filePath_fileName_all(filename):
    """
    获取文件的路径、文件名【带后缀】、文件名【不带后缀】、后缀名
    :param filename:
    :return:
    """
    (filepath, filename_with_extension) = os.path.split(filename)
    (filename_without_extension, extension) = os.path.splitext(filename_with_extension)

    return filepath, filename_with_extension, filename_without_extension, extension


def create_a_folder(path):
    """
    创建一个文件夹
    :param path:
    :return:
    """
    temp_folder = os.path.exists(path)
    if not temp_folder:
        os.makedirs(path)


def clean_a_folder(path):
    """
    清空某个目录下的所有文件
    :param path:
    :return:
    """
    shutil.rmtree(path)
    os.mkdir(path)


def time_convert(size):
    M, H = 60, 60 ** 2
    if size < M:
        return str(size) + u'秒'
    if size < H:
        return u'%s分钟%s秒' % (int(size / M), int(size % M))
    else:
        hour = int(size / H)
        mine = int(size % H / M)
        second = int(size % H % M)
        tim_srt = u'%s小时%s分钟%s秒' % (hour, mine, second)
        return tim_srt
