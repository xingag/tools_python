#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: js_code.py 
@time: 2020-07-22 13:30 
@description：待执行的JS代码
"""


def js_simple():
    """
    返回简单的js代码
    :return:
    """
    return """
    function add(num1 , num2){
        return num1 + num2;
    }
    """


def js_from_file(file_name):
    """
    读取js文件
    :return:
    """
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = file.read()

    return result
