#!/usr/bin/python3# -*- coding: utf-8 -*-
# @Time : 2019/9/29 10:37
# @Author : "zhy"
import sys
sys.path.append("C:\\git-data\\client-test")
import time
import win32clipboard

from pywinauto.application import Application
from local_lib.client.其它.windows_api import get_proccess_id
from local_lib.client.其它.qianniu_ws import get_qianniu_inject_id, get_qianniu_ws_path, qianniu_html, get_chat_message


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
    flag = str(int(time.time()))
    wangwang_message_send("kuaidanian", flag)
    wangwang_message_send("kuaidanian", "图片测试")
    time.sleep(5)
    pid = get_qianniu_inject_id()
    ws_path = get_qianniu_ws_path(pid)
    h = qianniu_html(ws_path)
    msg = get_chat_message(h)
    msg = str(msg).split(flag)[1]
    print(msg)
    if "img" in msg and "发送错误" not in msg:
        print("success")
    else:
        print("fail")
