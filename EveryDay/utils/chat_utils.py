#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: chat_utils.py 
@time: 4/18/19 20:21 
@description：itchat 工具类
"""
import itchat


# 注意：默认获取到的群聊：保存在通讯录中的群聊


def send_word_helper(content):
    """
    向文件传输助手发送文字
    :param content:
    :return:
    """
    itchat.send(content, toUserName='filehelper')


def send_word_to_person(name, content):
    """
    发送消息给某个人
    :param name:
    :param content:
    :return:
    """
    users = itchat.search_friends(name)
    userName = users[0]['UserName']
    itchat.send(content, toUserName=userName)


def send_file_to_person(name, filename):
    """
    发送文件给某个人
    :param name:
    :param filename:
    :return:
    """
    users = itchat.search_friends(name)
    userName = users[0]['UserName']
    itchat.send_file(filename, toUserName=userName)


def send_word_to_group(group_name, word):
    """
    群聊中发送文字
    :param group_name:
    :param content:
    :return:
    """
    # 获取所有群聊
    # 显示所有的群聊信息，默认是返回保存到通讯录中的群聊
    itchat.dump_login_status()

    target_rooms = itchat.search_chatrooms(name=group_name)

    if target_rooms and len(target_rooms) > 0:
        target_rooms[0].send_msg(word)
    else:
        print('【发送文字】抱歉，不存在这个群聊：%s' % group_name)


def send_file_to_group(group_name, file_name):
    """
    发送文件到群聊
    :param group_name:
    :param file:
    :return:
    """
    itchat.dump_login_status()

    target_rooms = itchat.search_chatrooms(name=group_name)

    if target_rooms and len(target_rooms) > 0:
        target_rooms[0].send_file(file_name)
    else:
        print('【发送文件】抱歉，不存在这个群聊：%s' % group_name)
