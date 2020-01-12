#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: addr_utils.py 
@time: 2020-01-06 22:24 
@description：TODO
"""

import json
import re

import requests


# 所有的id和城市名称数据

def get_all_citys():
    """
    获取所有的城市数据
    :return:
    """

    headers = {
        'authority': 'uutool.cn',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'sec-fetch-user': '?1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'UM_distinctid=16f759fe6bd24b-0322efd0d180d8-1d376b5b-1aeaa0-16f759fe6beb69; CNZZDATA1275106188=191793625-1578225029-https%253A%252F%252Fwww.google.com%252F%7C1578316721',
    }

    resp = requests.get('https://uutool.cn/phone-generate/', headers=headers).text

    re_rule = r'areaArr:(.+?)segmentArr:'

    # 匹配换行符
    result_data = re.findall(re_rule, resp, re.S)[0].strip()[:-1]

    result = json.loads(result_data)

    # 获取所有的省份
    provices = result.keys()

    # 所有的城市
    citys = {}

    for provice in provices:
        current_citys = result.get(provice)
        # citys.extend(current_citys)
        for item in current_citys:
            citys[item.get('name')] = item.get('id')

    return citys

# get_all_citys()
