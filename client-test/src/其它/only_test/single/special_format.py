#!/usr/bin/python3# -*- coding: utf-8 -*-
# @Time : 2019/9/29 10:37
# @Author : "zhy"
import sys
sys.path.append("C:\\git-data\\client-test")
import time
import win32clipboard

from pywinauto.application import Application
from local_lib.client.其它.windows_api import get_proccess_id


def wangwang_message_send(name, word):
    pid = get_proccess_id('AliIM.exe'.lower())
    app = Application(backend="uia").connect(process=pid[0])
    name = '阿里旺旺 - ' + name
    app[name]['Pane7'].type_keys(word)
    app[name]['Pane7'].type_keys("{ENTER}")
    time.sleep(0.5)
    app[name]['Pane7'].type_keys("{ENTER}")


def wangwang_message_get(name):
    pid = get_proccess_id('AliIM.exe'.lower())
    app = Application(backend="uia").connect(process=pid[0])
    name = '阿里旺旺 - ' + name
    # app['阿里旺旺 - kuaidanian'].print_control_identifiers()
    app[name]['聊天窗口'].type_keys("^A")
    app[name]['聊天窗口'].type_keys("^C")
    time.sleep(5)
    data = getCopyTxet()
    return data


def getCopyTxet():
    win32clipboard.OpenClipboard()
    copytxet = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return str(copytxet)


if __name__ == '__main__':
    qianniu_dir = "C:\\software\\qianniu\\AliWorkbench.exe"
    qianniu_pid_name = "AliWorkbench.exe".lower()
    wangcai_dir = "C:\\Users\\张大爷\\Desktop\\data\\xiaoduo\\xiaoduo-2.23.12\\2.23.12\\wangcai_main.exe"
    wangcai_pid_name = "wangcai_main.exe".lower()

    flag = str(int(time.time()))
    wangwang_message_send("kuaidanian", flag)
    wangwang_message_send("kuaidanian", "特殊字符")
    time.sleep(2)
    msg = wangwang_message_get("kuaidanian")
    print(msg)
