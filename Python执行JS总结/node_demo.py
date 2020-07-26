#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: node_demo.py 
@time: 2020-07-22 22:19 
@description：使用node命令调用js
"""

import os


def func1():
    # 组成调用js的命令
    cmd = 'node -e "require(\\"%s\\").init(%s,%s)"' % ('./norm1', 3, 5)

    pipeline = os.popen(cmd)

    # 读取结果
    result = pipeline.read()

    print('结果是:', result)


if __name__ == '__main__':
    func1()
