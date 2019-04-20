#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: About_AI.py 
@time: 4/18/19 19:55 
@description：百度AI语音合成
"""

# 依赖：pip3 install baidu-aip

from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '你的APP_ID'
API_KEY = '你的API_KEY'
SECRET_KEY = '你的SECRET_KEY'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def gene_mp3(content, filename):
	# 百度声音
    result = client.synthesis(content, 'zh', 1, {
        'vol': 7,
        'spd': 4,
        'per': 4,

    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('%s.mp3' % filename, 'wb') as f:
            f.write(result)
