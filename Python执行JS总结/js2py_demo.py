#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: js2py_demo.py 
@time: 2020-07-22 17:49 
@description：js2py
"""

# 依赖
# pip3 install js2py

import js2py

from js_code import *


def test_simple():
    """
    简单
    :return:
    """
    # 将js代码转为python
    add = js2py.eval_js(js_simple())

    # 当做python函数调用
    result = add(1, 2)

    print(result)


def test_js_from_file():
    """
    从文件中读取js进行执行
    :return:
    """

    # 从文件中读取js代码
    js_content = js_from_file('./norm.js')

    # 使用获取上下js2py生成一个上下文环境
    context = js2py.EvalJs()

    # 执行整段JS代码
    context.execute(js_content)

    # 使用context调用具体的函数
    result = context.add(1, 2)

    print(result)


if __name__ == '__main__':
    # test_simple()
    test_js_from_file()
