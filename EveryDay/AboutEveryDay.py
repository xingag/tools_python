#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: About_EveryDay.py 
@time: 4/18/19 19:50 
@description：每天运行
"""

from AboutTime import *
from AboutWeather import *
from AboutAI import *
from AboutJoke import *
import itchat
from utils.chat_utils import *
from utils.date_utils import *
import schedule


# 依赖： pip3 install schedule


class EveryDay(object):
    def __init__(self):
        self.time_start = ''
        self.time_end = ''
        self.weather = ''

        # mp3名称
        self.file_name = 'everyday_%s' % get_today_ymd()

    def start(self):
        self.time_start, self.time_end = get_time()
        self.weather = get_weather()

        self.__run()

    def __run(self):
        # 最后要发送的内容
        result_word = self.time_start + "\n\n" + self.weather + "\n" + self.time_end
        print(result_word)

        # 语音内容
        result_mp3 = (
                self.time_start + "。\n\n" + self.weather + "\n" + self.time_end + "你们工作吧，我要休息了！我们明天再见！拜拜~").replace(
            '，', '。')

        gene_mp3(result_mp3, self.file_name)

        # self.send_msg(result_word)

        self.send_word('微信上某位联系人', result_word)

        self.send_file('微信上某位联系人')

    def send_msg(self, result_word):
        # ===================================================
        target_peoples = [
            '微信上某位联系人',
            '微信上某位联系人2'
        ]

        for target in target_peoples:
            send_word_to_person(target, result_word)
            send_file_to_person(target, '%s.mp3' % self.file_name)

        print('单聊信息发送完成')

        # ===================================================
        target_group_names = [
            '微信上某个群聊1',
            '微信上某个群聊2',
            '微信上某个群聊3',
            '微信上某个群聊4'
        ]

        for target2 in target_group_names:
            send_word_to_group(target2, result_word)
            send_file_to_group(target2, '%s.mp3' % self.file_name)

        print('全部内容发送完成！')

    def send_word(self, target_name, result_word):
        """
        发送文字
        :param result_word:
        :return:
        """
        send_word_to_person(target_name, result_word)

    def send_file(self, target_name):
        """
        发送文件
        :return:
        """
        send_file_to_person(target_name, '%s.mp3' % self.file_name)


if __name__ == '__main__':
    every_day = EveryDay()

    # 准备调用itchat发送图片
    itchat.auto_login(hotReload=True)
    # itchat.auto_login(hotReload=True,enableCmdQR=2)

    # 每天早上8：00执行
    # 发送Norm信息【一天一次】
    schedule.every().day.at("08:00").do(every_day.start)

    # 每隔3分钟执行一次
    # schedule.every(3).minutes.do(every_day.start)

    # 分段发几个笑话【时间段：整点发送】
    target_name = '微信发送的对象'
    schedule.every().day.at("09:30").do(every_day.send_word, target_name, gene_joke(0))
    schedule.every().day.at("10:30").do(every_day.send_word, target_name, gene_joke(1))
    schedule.every().day.at("11:30").do(every_day.send_word, target_name, gene_joke(2))
    schedule.every().day.at("12:30").do(every_day.send_word, target_name, gene_joke(3))
    schedule.every().day.at("13:30").do(every_day.send_word, target_name, gene_joke(4))
    schedule.every().day.at("14:30").do(every_day.send_word, target_name, gene_joke(5))
    schedule.every().day.at("15:30").do(every_day.send_word, target_name, gene_joke(6))
    schedule.every().day.at("16:30").do(every_day.send_word, target_name, gene_joke(7))
    schedule.every().day.at("17:30").do(every_day.send_word, target_name, gene_joke(8))
    schedule.every().day.at("18:30").do(every_day.send_word, target_name, gene_joke(9))
    schedule.every().day.at("19:30").do(every_day.send_word, target_name, gene_joke(10))
    schedule.every().day.at("20:30").do(every_day.send_word, target_name, gene_joke(11))
    schedule.every().day.at("21:30").do(every_day.send_word, target_name, gene_joke(12))
    schedule.every().day.at("22:30").do(every_day.send_word, target_name, gene_joke(13))
    schedule.every().day.at("23:30").do(every_day.send_word, target_name, gene_joke(14))

    while True:
        schedule.run_pending()
        time.sleep(1)
