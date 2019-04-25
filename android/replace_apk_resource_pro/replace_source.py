#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: replace_source.py 
@time: 4/25/19 10:46 
@description：替换apk的资源文件
"""

from file_utils import *
import os
from subprocess import Popen, PIPE, STDOUT


class ReplaceApkSource(object):
    def __init__(self):
        self.file_name = 'logo_white.png'

        # 目标apk的名称
        self.target_apk_name = 'new.apk'

    def start(self):
        # 1.使用apktool.jar解压apk
        file_name_pre = self.__unzip_apk()

        # 2.替换资源
        self.__replace_source(file_name_pre)

        # 3.重新打包
        self.__rezip_apk(file_name_pre)

        # 4.再次签名
        self.__re_sign()

    def __unzip_apk(self):
        """
        解压当前目录下的apk文件
        :return:
        """
        # 文件名称，包含后缀名
        file_name = get_current_folder_file('apk')

        # 文件名称，不包含后缀名
        file_name_pre = file_name.split('.')[0]

        os.system('java -jar apktool.jar d %s' % file_name)

        print('第1步：解压成功~')

        return file_name_pre

    def __replace_source(self, file_name_pre):
        """
        替换资源
        @:param file_name_pre  文件夹的名称
        :return:
        """
        print('生成文件夹的名字是:%s' % file_name_pre)

        # 重命令当前目录下的文件
        rename_current_file("png", self.file_name)

        # 待替换的完成路径是
        logo_file_path = './%s/res/drawable-mdpi/logo_white.png' % file_name_pre

        # 开始替换文件
        replace_file('./%s' % self.file_name, logo_file_path)

        print('第2步：替换资源图片成功~')

    def __rezip_apk(self, folder_name):
        """
        重新打包成apk
        @:param folder_name 文件夹的名称  source
        :return:
        """

        # 重新打包成apk
        os.system('java -jar apktool.jar b %s -o %s' % (folder_name, self.target_apk_name))

        # 删除临时文件夹
        shutil.rmtree('./%s/' % folder_name)

        print('第3步：重新打包成功~')

    def __re_sign(self):
        """
        重新签名
        :return:
        """
        # 重新签名
        cmd = 'jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore **.keystore -storepass ** %s **' % self.target_apk_name
        p = Popen(cmd, stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=True)

        # 输入参数
        p.communicate(input=b'nantian')
        print('第4步：重新签名成功~')


if __name__ == '__main__':
    replace_apk_source = ReplaceApkSource()
    replace_apk_source.start()

    print('恭喜！完成操作~')
