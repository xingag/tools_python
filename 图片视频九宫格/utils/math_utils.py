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
@time: 2020-08-29 10:14 
@description：TODO
"""


import re

re_digits = re.compile(r'(\d+)')


def emb_numbers(s):
    pieces = re_digits.split(s)
    pieces[1::2] = map(int, pieces[1::2])
    return pieces


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