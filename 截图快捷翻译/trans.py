#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: trans.py 
@time: 2020-03-18 21:55 
@description：截屏快速翻译
"""

import tkinter.messagebox
from tkinter import *

import pytesseract
from PIL import Image
from PIL import ImageGrab
from googletrans import Translator

# 1、从剪切板获取图片，保存到本地
img = ImageGrab.grabclipboard()
if img and isinstance(img, Image.Image):
    image_result = './temp.png'
    img.save(image_result)

    # 2、OCR识别
    content_eng = pytesseract.image_to_string(Image.open(image_result), lang='eng')

    # 3、翻译
    translator = Translator(service_urls=['translate.google.cn'])

    content_chinese = translator.translate(content_eng, src='en', dest='zh-cn').text

    # 4、显示
    root = Tk()
    root.withdraw()
    tkinter.messagebox.showinfo('翻译结果', content_chinese)
