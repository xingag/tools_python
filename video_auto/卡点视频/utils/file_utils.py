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
@description：TODO
"""
import os


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
