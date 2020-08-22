#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2019/9/29 10:37
# @Author : "zhy"
import os
import time
import pytest
import allure
import win32gui
import win32com.client
from pywinauto.application import Application

from local_lib.client.其它.wangwang_api import wangwang_message_send, wangwang_message_get
from local_lib.client.其它.qianniu_win_api import qianniu_check_started, get_proccess_id, qianniu_login, \
    open_qianniu_chat_windows, change_chat_member_by_search
from local_lib.client.其它.wangwang_api import wangcai_check_started


@allure.feature('自动启动问答')
@pytest.mark.client_special_format
class TestClientSpecialFormat(object):
    def setup_class(self):
        self.buyer = "kuaidanian"
        self.seller = "tb671067_2013:克明"
        self.ask_timeout = 1
        self.special_timeout = 3
        self.qianniu_dir = "C:\\software\\qianniu\\AliWorkbench.exe"
        self.wangcai_dir = "C:\\Users\\张大爷\\Desktop\\data\\xiaoduo\\xiaoduo-2.23.12\\2.23.12\\wangcai_main.exe"
        self.qianniu_pid_name = "AliWorkbench.exe".lower()
        self.wangcai_pid_name = "wangcai_main.exe".lower()

        # 加载大漠插件
        self.dm = win32com.client.Dispatch('dm.dmsoft')
        dm_ver = self.dm.ver()
        if dm_ver == "" or dm_ver is None:
            print("大漠插件加载失败")
            exit()
        else:
            print("大漠插件加载成功，当前版本：" + dm_ver)

        # 加载字典
        # dm.setDict(0, 'c:\dm_soft.txt')
        # dm.useDict(0)

    @allure.story('自动启动问答')
    @allure.severity('normal')
    def test_(self):
        """
        用例描述：自动检测晓多能否回复
        """
        with pytest.allure.step('检查千牛是否启动，启动了杀掉重启'):
            qianniu_check_started(self.qianniu_pid_name, self.qianniu_dir)

        with pytest.allure.step('获取千牛的pid'):
            pid = get_proccess_id(self.qianniu_pid_name)
            allure.attach('pid', pid)

        with pytest.allure.step('登录'):
            app = Application(backend="uia").connect(process=pid[0])
            qianniu_login(self.dm, app)

        with pytest.allure.step('打开聊天窗口'):
            handle = win32gui.FindWindow(0, self.seller + ' - 工作台')
            open_qianniu_chat_windows(handle)

        with pytest.allure.step('切换联系人'):
            change_chat_member_by_search(self.buyer)

        with pytest.allure.step('旺财启动'):
            wangcai_check_started(self.wangcai_pid_name, self.wangcai_dir)
            time.sleep(5)

        with pytest.allure.step('问答测试'):
            flag = str(int(time.time()))
            wangwang_message_send(self.buyer, flag)
            wangwang_message_send(self.buyer, "你好")
            time.sleep(2)
            msg = wangwang_message_get(self.buyer)
            msg = str(msg).split(flag)[1]
            assert "你好" in msg
            assert "您好，亲~~线上" in msg


if __name__ == '__main__':
    pytest.main(['-s', os.path.abspath(__file__)])
