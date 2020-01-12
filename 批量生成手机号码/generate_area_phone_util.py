#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: generate_area_phone_util.py 
@time: 2020-01-05 20:16 
@description：生成区域的电话号码
"""

from utils.addr_utils import *

def generate_phones(num, areas):
    """
    生成随机号码
    :param num:数目
    :param areas: 区域
    :return:
    """

    headers = {
        'authority': 'api.uukit.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': 'enote_app/json, text/javascript, */*; q=0.01',
        'origin': 'https://uutool.cn',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'referer': 'https://uutool.cn/phone-generate/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    data = {
        'phone_num': num,
        'area': areas,
        'segment': '133,153,189,180,181,177,173,139,138,137,136,135,134,159,158,157,150,151,152,147,188,187,182,183,184,178,130,131,132,156,155,186,185,145,176'
    }

    response = requests.post('https://api.uukit.com/phone/generate_batch', headers=headers, data=data)

    phones = json.loads(response.text).get('data').get('rows')

    return phones


if __name__ == '__main__':
    # 手机号码个数
    num = 100

    # 全国所有城市名称和id编号
    citys = get_all_citys()

    city_name = input('请输入手机归属地：')

    if city_name not in citys.keys():
        city_name = '北京'

    # 获取城市id
    city_id = citys.get(city_name)

    # 请输入要获取手机号码的归属地
    phones = generate_phones(num, city_id)
    print(phones)
