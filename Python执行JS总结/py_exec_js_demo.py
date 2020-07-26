#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: py_exec_js_demo.py 
@time: 2020-07-22 13:24 
@description：使用PyExecJS调用JS代码
"""

# 依赖
# pip3 install PyExecJS

import execjs

from js_code import *

# 1、简单的JS字符串
# 编译并加载 js 文件内容,方便执行里面的方法
context = execjs.compile(js_simple())

# 使用call()函数调用js内部函数
result = context.call("add", 2, 3)

print(result)

# 2、js文件
# 编译加载js字符串
context1 = execjs.compile(js_from_file('./norm.js'))

# 调用js代码中的add()方法，参数为2和3
result1 = context1.call("add", 2, 3)

print(result1)
