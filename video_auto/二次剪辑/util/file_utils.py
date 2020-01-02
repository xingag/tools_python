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
@time: 2019-12-29 11:30 
@description：TODO
"""

import os


def del_temp_file(path):
    """
    删除目录下的临时文件
    :param path:
    :return:
    """
    # 删除临时文件
    g = os.walk(path)

    for path, dir_list, file_list in g:
        print(path)
        for file_name in file_list:
            print(file_name)
            if file_name.startswith('temp'):
                os.remove(path + file_name)



