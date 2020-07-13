#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: email_by_smtplib.py 
@time: 2020-07-09 21:30 
@description：smtplib发送邮件
"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SmtplibObject(object):

    def __init__(self):
        # 初始化
        self.smtp = smtplib.SMTP()
        # 连接邮箱服务器地址
        self.smtp.connect('smtp.126.com')

        # 加入主题和附件，邮件体
        self.email_body = MIMEMultipart('mixed')

        # 发件人地址及授权码
        self.email_from_username = '**@126.com'
        self.email_from_password = '授权码'

    def send_email(self, email_to_list, email_title, email_content, attchment_path, files):
        """
        发送邮件
        :return:
        """
        # 组成邮件体
        self.generate_email_body(email_to_list, email_title, email_content, attchment_path, files)

        # 登录邮箱
        # 参数为账号和密码（授权码）
        self.smtp.login(self.email_from_username, self.email_from_password)

        # 发送邮件
        # 注意：此处必须同时指定发件人与收件人，否则会当作垃圾邮件处理掉
        self.smtp.sendmail(self.email_from_username, email_to_list, self.email_body.as_string())

    def generate_email_body(self, email_to_list, email_title, email_content, attchment_path, files):
        """
        组成邮件体
        :param email_to_list:收件人列表
        :param email_title:邮件标题
        :param email_content:邮件正文内容
        :param attchment_path:附件的路径
        :param files:附件文件名列表
        :return:
        """
        self.email_body['Subject'] = email_title
        self.email_body['From'] = self.email_from_username
        self.email_body['To'] = ",".join(email_to_list)

        for file in files:
            file_path = attchment_path + '/' + file
            if os.path.isfile(file_path):
                # 构建一个附件对象
                att = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
                att["Content-Type"] = 'application/octet-stream'
                att.add_header("Content-Disposition", "attachment", filename=("gbk", "", file))
                self.email_body.attach(att)

        text_plain = MIMEText(email_content, 'plain', 'utf-8')
        self.email_body.attach(text_plain)

    def exit(self):
        """
        退出服务
        :return:
        """
        self.smtp.quit()


if __name__ == '__main__':
    # 收件人列表
    email_to_list = ['**@qq.com']
    email_title = "测试报告"
    email_content = '这是测试报告具体内容'
    # 附件路径
    attchment_path = './attachments/'
    # 附件文件列表
    attchment_files = ['report.png', 'config.json']

    # 发送邮件
    smtplib_object = SmtplibObject()
    smtplib_object.send_email(email_to_list, email_title, email_content, attchment_path, attchment_files)

    # 退出
    smtplib_object.exit()
