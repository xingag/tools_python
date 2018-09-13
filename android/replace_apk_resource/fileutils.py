#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: fileutils.py 
@time: 2018/9/13 17:44 
@description：文件工具
"""
import os


def rename_file_suffix(name, suffix):
	"""
	更改文件的后缀名
	:param name: 源文件名称
	:param suffix: 新的后缀名
	:return: 新的文件名称
	"""
	base = os.path.splitext(name)[0]
	apk_name = base + suffix
	os.rename(name, apk_name)
	return apk_name
