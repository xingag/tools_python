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
@time: 4/25/19 11:17 
@description：文件管理器
"""

import os
import shutil


def get_current_folder_file(file_type):
    """
    通过文件类型，获取到当前目录下的文件  filename = get_current_folder_file('apk')
    :param file_type:
    :return:
    """
    # 当前目录下所有的文件
    all_files = os.listdir('.')

    # 满足要求的文件列表
    target_files = []
    for file in all_files:
        if file.split('.')[-1] == file_type:
            target_files.append(file)

    # 返回第一项
    return target_files[0] if len(target_files) > 0 else ""


def rename_current_file(file_type, file_name):
    """
    重命令文件夹
    :param file_type:文件类型
    :param file_name:准备替换的名称
    :return:
    """
    file = get_current_folder_file(file_type)

    # 重命令操作
    os.rename(os.path.join('./', file), os.path.join('./', file_name))


def replace_file(file_from_path, file_to_path):
    """
    替换文件
    :param file_from_path:待替换的文件
    :param file_to_path:待被替换的文件
    :return:
    """
    shutil.copy(file_from_path, file_to_path)
