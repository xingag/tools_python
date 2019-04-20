#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: AboutTime.py 
@time: 4/18/19 19:07 
@description：关于时间
"""

import time
import calendar

week = ['日', '一', '二', '三', '四', '五', '六']


def get_time():
    """
    获取时间
    :return:
    """
    # time.strftime("%F-%u-%j")
    # F:年月日；u：星期几；j：一年第几天

    # 时间数据
    # [2019, 4, 18, 4, 108]
    time_datas = [int(i) for i in time.strftime("%F-%u-%j").split('-')]

    # 年
    year = time_datas[0]
    # 月
    month = time_datas[1]
    # 日
    day = time_datas[2]
    # 星期几
    week_d = week[time_datas[3]]
    # 一年中的第几天
    time_d = time_datas[4]

    # 判断是否是闰年；闰年：366天，平年：365
    if calendar.isleap(year):
        percent = round(time_d * 100 / 366, 2)
    else:
        percent = round(time_d * 100 / 365, 2)

    # time_content = '今天是：%d 年 %d 月 %d 日，星期%s\n报告主人！今年 %.2f%% 时间已流逝。' % (year, month, day, week_d, percent)
    time_content = ('各位帅哥美女们，大家早上好！\n\n今天是：%d 年 %d 月 %d 日，星期%s~' % (year, month, day, week_d),
                    '\n\n报告主人！报告主人！报告主人！\n\n%d 年，岁月已陪伴主人走过：%.2f%%。' % (year, percent) + "余下时光，请主人们温柔以待哦！")
    return time_content

# print(get_time())
