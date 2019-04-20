#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: AboutWeather.py 
@time: 4/18/19 19:32 
@description：天气
"""

import requests


def get_weather():
    url = 'https://www.tianqiapi.com/api/?version=v1&cityid=101280601'

    result = requests.get(url).json().get('data')[0]

    city = '深圳天气：'

    # 天气
    wea = result.get('wea')

    # 空气质量
    air_level = result.get('air_level')

    # 最高温度
    tem_high = result.get('tem1')

    # 最低温度
    tem_low = result.get('tem2')

    result = city + str(wea) + "，最低温度：" + str(tem_low) + "，最高温度：" + str(tem_high) + "，空气质量:" + str(air_level) + "。"

    return result
