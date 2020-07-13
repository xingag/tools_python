#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: email_by_yagmail.py 
@time: 2020-07-09 21:07 
@description：yagmail发送/接受邮件
"""

# 依赖：pip3 install yagmail
# 公众号：AirPython

import yagmail

# 连接服务器
# 用户名、授权码、服务器地址
yag_server = yagmail.SMTP(user='**@126.com', password='授权码', host='smtp.126.com')

# 发送邮件
# 发送对象列表
email_to = ['**@qq.com', ]
email_title = '测试报告'
email_content = "这是测试报告的具体内容"
# 附件列表
email_attachments = ['./attachments/report.png', ]
yag_server.send(email_to, email_title, email_content, email_attachments)

# 关闭连接
yag_server.close()
