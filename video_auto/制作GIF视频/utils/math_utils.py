#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: math_utils.py 
@time: 5/29/19 21:01 
@description：数学公式工具类
"""

import re

re_digits = re.compile(r'(\d+)')


def emb_numbers(s):
    pieces = re_digits.split(s)
    pieces[1::2] = map(int, pieces[1::2])
    return pieces


# 根据字符串中的数字排序，如f10应该在f2后面
def sort_strings_with_emb_numbers(alist):
    """
    DSU排序
    :param alist:
    :return:
    """
    aux = [(emb_numbers(s), s) for s in alist]
    aux.sort()
    return [s for __, s in aux]


def sort_strings_with_emb_numbers2(alist):
    """
    内置DSU排序
    :param alist:
    :return:
    """
    return sorted(alist, key=emb_numbers)
