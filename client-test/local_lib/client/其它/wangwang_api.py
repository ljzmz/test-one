#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2019/9/29 10:37
# @Author : "zhy"
import os
import time

from pywinauto.application import Application
from local_lib.client.其它.windows_api import get_proccess_id, getCopyTxet


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


def wangcai_check_started(wangcai_pid_name, wangcai_dir):
    # 检测当前千牛是否启动，启动了杀掉
    wangcai_pid = get_proccess_id(wangcai_pid_name)
    if not wangcai_pid or len(wangcai_pid) == 0:
        print("晓多未启动")
    else:
        print("晓多已启动：" + str(wangcai_pid))
        print("杀掉千牛")
        for i in wangcai_pid:
            kill_pid(i)
            time.sleep(1)
    # 启动千牛
    os.startfile(wangcai_dir)
    time.sleep(5)


def kill_pid(pid):
    try:
        os.popen('taskkill.exe /pid:' + str(pid) + ' -f')
        print('已杀死的进程' + str(pid))
    except OSError:
        print('没有如此进程!!!')


if __name__ == '__main__':
    while True:
        print(time.time())
        wangwang_message_send("kuaidanian", "10")
