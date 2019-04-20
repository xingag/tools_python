#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: date_utils.py 
@time: 4/16/19 23:59 
@description：日期工具类
"""

import datetime


def get_today():
    # 获取今天的日期
    # <class 'datetime.date'>
    today = datetime.date.today()
    return today


def get_today_day():
    """
    获取年月日
    :return: int类型
    """
    # datetime.datetime.now().year
    # datetime.datetime.now().month
    return datetime.datetime.now().day


def get_today_ymd():
    """
    获取年月日
    :return: int类型
    """
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day

    return "%d_%d_%d" % (year, month, day)


def get_current_time():
    # 当前时间
    current_time = datetime.datetime.now()
    # 时
    current_hour = current_time.hour
    # 分
    current_minute = current_time.minute
    # 秒
    current_second = current_time.second

    # print('当前时间:%d:%d:%d' % (current_hour, current_minute, current_second))

    return current_hour, current_minute, current_second
