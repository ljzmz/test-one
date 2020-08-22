#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2019/9/29 10:37
# @Author : "zhy"
import pytest
import allure
import time
import os

from local_lib.client.其它.wangwang_api import wangwang_message_send, wangwang_message_get


def verify_picture(msg):
    assert "！" in msg
    assert "@" in msg
    assert "#" in msg
    assert "￥" in msg
    assert "%" in msg
    assert "……" in msg
    assert "&" in msg
    assert "*" in msg
    assert "（）" in msg
    assert "？" in msg
    assert "《》" in msg
    assert "：" in msg
    assert "“”" in msg
    assert "{}" in msg


@allure.feature('特殊字符验证')
@pytest.mark.client_special_format
class TestClientSpecialFormat(object):
    def setup_class(self):
        self.ask_timeout = 1
        self.special_timeout = 3
        self.buyer = "kuaidanian"

    @allure.story('整句问答特殊字符')
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

        with pytest.allure.step('触发问答的特殊字符'):
            wangwang_message_send(self.buyer, "特殊字符")
            allure.attach('消息内容', flag)
            time.sleep(self.special_timeout)

        with pytest.allure.step('验证特殊字符是否发送成功'):
            msg = wangwang_message_get(self.buyer)
            msg = str(msg).split(flag)[1]

        verify_picture(msg)


if __name__ == '__main__':
    pytest.main(['-s', os.path.abspath(__file__)])
