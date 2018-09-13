# -*- coding:utf-8 -*-

"""
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm
@file: ReplaceApkResource.py 
@time: 2018/9/13 12:24 
@description：利用python替换apk的资源后重新打包
"""

import shutil
import os
import zipfile
import fileutils

# 设置签名信息
keystore_path = "**.keystore"
keystore_pass = "**"
keystore_alias = "**"
keystore_alias_pass = "**"

# 脚本根目录
root = os.getcwd()

# 创建一个临时目录
tmp_path = root + "/tmp/"

# 传入apk的名称,并更改后缀名为zip
apk_name_temp = input('请输入apk的名称:')

apk_name = fileutils.rename_file_suffix(apk_name_temp, 'zip')

# 保证tmp文件夹目录存在
if not os.path.exists(tmp_path):
	os.system("mkdir tmp")

# copy apk文件到临时文件夹内
shutil.copyfile(apk_name, tmp_path + apk_name)

print(tmp_path + apk_name)

tmp_path_all = tmp_path + apk_name

# 获取压缩包路径
azip = zipfile.ZipFile(tmp_path_all)


# 解压zip文件【到指定目录下】
azip.extractall(tmp_path)

# 注意：此处需要关闭对tmp_path的引用
azip.close()

# 删除签名信息和源zip【apk】
if os.path.exists(tmp_path + 'META-INF/'):
	shutil.rmtree(tmp_path + 'META-INF')

if os.path.exists(tmp_path_all):
	os.remove(tmp_path_all)

# 更新资源【图片替换到目标文件当中去】
shutil.copyfile('ic_logo.png', tmp_path + "res\drawable-mdpi-v4\ic_logo.png")


# 移动python文件到tmp目录下,然后显示执行这条Python脚本
shutil.copyfile('ziputils.py', r'./tmp/ziputils.py')

# 切换到./tmp/目录下，执行压缩文件为
os.chdir(tmp_path)
os.system('python ziputils.py')

# 切换到根目录下
os.chdir(root)

# 利用keystore文件进行签名
os.system(
	"jarsigner -verbose -digestalg SHA1 -sigalg MD5withRSA -keystore " + keystore_path + " -storepass " + keystore_pass + " -signedjar release-sign.apk release-nosign.apk " + keystore_alias + " -keypass " + keystore_alias_pass)

# 压缩对齐【利用zipalign去对齐应用apk】
os.system(
	"D:/Android/sdk/build-tools/28.0.1/zipalign -v 4 release-sign.apk release.apk")

# 删除临时文件和多余的apk文件
shutil.rmtree(tmp_path)
os.remove('release-nosign.apk')
os.remove('release-sign.apk')

# 验证签名
os.system("jarsigner -verify -certs release.apk")

print('恭喜，终于成功啦！')
