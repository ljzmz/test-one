#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/7/9 15:37
# @Author : "zhy"
import os

import allure
import pytest
from local_lib.client.XdClient import XdClient
from local_lib.client.右侧窗体.智能辅助.催单模式.reminder_status import ReminderStatus


@allure.feature('智能辅助')
@allure.story('催单模式')
@pytest.mark.maoyan
class TestReminderStatus(object):
    reminder_status = ReminderStatus()

    @allure.title('修改催单模式')
    @allure.severity('normal')
    def test_set_status(self, get_websocket_url):
        """
        author: 张怀宇
        测试描述： 修改催单模式
        """
        with allure.step('执行修改催单模式js'):
            self.reminder_status.set_status(get_websocket_url,
                                            "$x('/html/body/div[2]/div/div/div/ul/li[3]')[0].click()")
        with allure.step('获取页面源码判断'):
            page = XdClient().get_page_resource(get_websocket_url)
            print(page)


if __name__ == '__main__':
    pytest.main('-s', os.path.abspath(__file__))
