#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2019/9/29 10:37
# @Author : "zhy"
import pytest
import allure
import time
import os

from local_lib.client.其它.wangwang_api import wangwang_message_send
from local_lib.client.其它.qianniu_ws import get_qianniu_inject_id, get_qianniu_ws_path, qianniu_html, get_chat_message


def verify_picture(flag):
    with pytest.allure.step('获取千牛等待注入的进程id'):
        pid = get_qianniu_inject_id()
        allure.attach('pid：', pid)

    with pytest.allure.step('获取websocket地址'):
        ws_path = get_qianniu_ws_path(pid)
        allure.attach('ws_path：', ws_path)

    with pytest.allure.step('获取千牛页面内容并且解析'):
        h = qianniu_html(ws_path)
        allure.attach('获取到的源码内容', h)
        msg = get_chat_message(h)
        allure.attach('解析后的内容', msg)
        msg = str(msg).split(flag)[1]
        allure.attach('分割后的内容', msg)
        assert "img" in msg and "发送错误" not in msg


@allure.feature('客户端图片发送功能验证')
@pytest.mark.client_picture
class TestClientPicture(object):
    def setup_class(self):
        self.ask_timeout = 1
        self.picture_timeout = 3
        self.buyer = "kuaidanian"

    @allure.story('整句问答图片验证')
    @allure.severity('normal')
    def test_(self):
        """
        用例描述：问答触发发送图片，获取千牛的页面信息判断是否成功发送图片
        """
        with pytest.allure.step('发送用作隔断的flag'):
            flag = str(int(time.time()))
            wangwang_message_send(self.buyer, flag)
            allure.attach('flag内容', flag)
            time.sleep(self.ask_timeout)

        with pytest.allure.step('触发整句类型问答'):
            wangwang_message_send(self.buyer, "图片测试")
            allure.attach('消息内容', flag)
            time.sleep(self.picture_timeout)

        verify_picture(flag)


if __name__ == '__main__':
    pytest.main(['-s', os.path.abspath(__file__)])
