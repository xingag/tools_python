#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: ziputils.py 
@time: 2018/9/13 14:54 
@description：zip 压缩工具
"""
import os
import zipfile
from os.path import isfile, isdir, join


def dfs_get_zip_file(input_path, result):
	files = os.listdir(input_path)
	for file in files:
		# 排除掉py文件
		if file == 'ziputils.py':
			continue
		if os.path.isdir(input_path + '/' + file):
			dfs_get_zip_file(input_path + '/' + file, result)
		else:
			result.append(input_path + '/' + file)


def zip_path(input_path, output_file_full):
	"""

	:param input_path: 待压缩的文件夹
	:param output_file_full: 压缩的完整目录，包含文件名
	:return:
	"""
	f = zipfile.ZipFile(output_file_full, 'w', zipfile.ZIP_DEFLATED)
	filelists = []
	dfs_get_zip_file(input_path, filelists)
	for file in filelists:
		# 写入到zip目录下
		f.write(file)
	f.close()
	return output_file_full


if __name__ == '__main__':

	# 根目录下打包所有文件
	zip_path(r"./", r'../release-nosign.apk')
