#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: email_by_zmail.py 
@time: 2020-07-09 19:57 
@description：zmail发送邮件
"""

# 依赖
# pip3 install zmail
# 公众号：AirPython

import zmail


class ZMailObject(object):

    def __init__(self):
        # 邮箱账号
        self.username = '**@126.com'

        # 邮箱授权码
        self.authorization_code = '授权码'

        # 构建一个邮箱服务对象
        self.server = zmail.server(self.username, self.authorization_code)

    def send_email(self, mail_to, mail_body):
        """
        发送邮件
        :param mail_to 发送对象
        :param mail: 发送主题、内容及附件
        :return:
        """

        if self.__check_pop_enable() and self.__check_smtp_enable():
            self.server.send_mail(mail_to, mail_body)
        else:
            pass

    def receive_email(self):
        """
        接受邮件
        :return:
        """
        try:
            # 接受邮件
            last_mail = self.server.get_latest()
            # last_mail = self.server.get_mail(2)
            # zmail.show(last_mail)
            for k, v in last_mail.items():
                print(k, v)
        except Exception as e:
            # 收件箱为空，则会报错
            print('接受异常异常')

    def __check_smtp_enable(self):
        """
        检查smtp是否正常
        :return:
        """
        return self.server.smtp_able()

    def __check_pop_enable(self):
        """
        检查pop功能是否正常
        :return:
        """
        return self.server.pop_able()


if __name__ == '__main__':
    zmail_obj = ZMailObject()

    # 发送内容及附件
    mail_to = '**@qq.com'

    # 邮件主体
    mail_body = {
        'subject': '测试报告',
        'content_text': '这是一个测试报告',  # 纯文本或者HTML内容
        'attachments': ['./attachments/report.png'],
    }

    # 发送邮件
    zmail_obj.send_email(mail_to, mail_body)

    # 接受邮件
    # zmail_obj.receive_email()
