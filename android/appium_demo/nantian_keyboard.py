#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: nantian_keyboard.py 
@time: 1/18/19 10:05 
@description：设备App测试密码键盘
"""

from config_nantian import *
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from element_utils import *
from random import randint


class Keyboard(object):

    def __init__(self):
        self.caps = {
            'automationName': DRIVER,
            'platformName': PLATFORM,
            'deviceName': DEVICE_NAME,
            'appPackage': APP_PACKAGE,
            'appActivity': APP_ACTIVITY,
            'platformVersion': ANDROID_VERSION,
            'autoGrantPermissions': AUTO_GRANT_PERMISSIONS,
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def login_and_web(self):
        """
        输入密码和信息交互
        :return:
        """
        while True:
            keyboard_input_element = is_element_exist(self.driver, 'com.nantian.home:id/etPassword')
            web_sure_element = is_element_exist(self.driver, 'com.nantian.home:id/web_btnOK')
            web_cancel_element = is_element_exist(self.driver, 'com.nantian.home:id/btnCancel')

            # 输入框
            if keyboard_input_element:
                print('找到元素，准备输入密码')
                keyboard_input_element.send_keys('123456')
            # Web页面
            elif web_sure_element:
                print('找到元素，准备点击确认按钮，或者取消按钮')
                web_sure_element.click() if randint(0, 1) == 0 else web_cancel_element.click()
            else:
                print('没有找到元素，继续')
                time.sleep(1)

    def run(self):
        self.login_and_web()


if __name__ == '__main__':
    keyboard = Keyboard()
    keyboard.run()
