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
@time: 2020-02-01 23:05 
@description：TODO
"""

import os
import shutil


def get_file_path_and_name(filename):
    """
    获取文件的路径、文件名（不含后缀），后缀名
    :param filename:
    :return:
    """
    (filepath, tempfilename) = os.path.split(filename)
    (shotname, extension) = os.path.splitext(tempfilename)
    return filepath, shotname, extension


def rename_file(path, filename):
    """
    更改文件名（处理文件名中包含空格的情况）
    :param path:
    :param filename:
    :return:
    """
    os.rename(os.path.join(path, filename), os.path.join(path, filename.replace(' ', '_')))


def mkdir_folder(file_path):
    """
    创建一个文件夹，如果不存在就创建；否则不做处理
    :param file_path:
    :return:
    """
    if os.path.exists(file_path):
        return

    os.mkdir(file_path)


def remove_folder(file_path):
    """
    删除文件夹
    :param file_path:
    :return:
    """
    shutil.rmtree(file_path)
