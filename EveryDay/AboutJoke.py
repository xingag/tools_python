#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: AboutJoke.py 
@time: 4/19/19 16:30 
@description：TODO
"""

import requests
from random import randint
import re
import schedule
import time


def gene_joke(index):
    joke_url = 'http://api.laifudao.com/open/xiaohua.json'

    resp = requests.get(joke_url)

    resp_content = resp.json()

    # 每天20个笑话
    # index = randint(0, len(resp_content))

    joke_random = resp_content[index]

    # 标题
    joke_title = joke_random['title']

    # 笑话
    joke_content = re.sub('/*<br/><br/>', r'\n', joke_random['content'])

    # print(joke_content)

    return "***某某童鞋，你家老公给你准备了笑话一则***\n"+joke_content.strip()

