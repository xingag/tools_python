#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: delete_build.py 
@time: 11/14/18 16:33 
@description：删除build文件夹
"""

import os

# 待删除的目录
path = './'


def get_file_name(file_full_path):
    """
    :param file_full_path: 文件的完整路径
    :return: 上层父目录、文件名【带后缀】、文件名【不带后缀】、文件后缀
    """
    # 上层父目录、文件名【带后缀】
    (filepath, tempfilename) = os.path.split(file_full_path)

    # 文件名【不带后缀】，文件名
    (filename, extension) = os.path.splitext(tempfilename)

    return (filepath, tempfilename, filename, extension)


def remove_dir(dir_path):
    print("删除文件夹的目录是:"+dir_path)

    # 如果是空文件夹
    if not os.listdir(dir_path):
       os.removedirs(dir_path)

    for root, dirs, files in os.walk(dir_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


def traverse_files(path):
    """
    遍历
    :param path:
    :return:
    """
    for item in os.scandir(path):

        file_name = get_file_name(item.path)[2]
        # 判断是文件夹还是文件
        if item.is_dir():
            # print(item.path)
            # 删除build文件夹
            if file_name == 'build':
                remove_dir(item.path)
            else:
                traverse_files(item.path)


traverse_files(path)
