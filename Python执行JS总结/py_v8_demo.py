#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: py_v8_demo.py 
@time: 2020-07-22 14:53 
@description：PyV8调用JS
"""

import PyV8
from js_code import js_from_file

with PyV8.JSContext() as ctx:
    ctx.eval(js_from_file('./norm.js'))

# 调用js函数，指定参数
ctx.locals.add(1, 2)

