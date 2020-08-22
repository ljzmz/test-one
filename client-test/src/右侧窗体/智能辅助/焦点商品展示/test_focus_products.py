#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 15:38
# @Author : "zmz"
from local_lib.client.XdClient import XdClient
from local_lib.client.其它.wangwang_api import *
import configparser

@allure.feature("智能辅助")
@allure.story('焦点商品展示')
@pytest.mark.maoyan

class TestFocusProducts:
    @allure.title('识别焦点商品')
    @allure.severity('normal')
    def setup(self):
        self.
    def test_focus_valid(self):
        config = configparser.ConfigParser()
        config.read(os.path.dirname(__file__) + str("/Link.ini"), encoding="utf-8")
        link = config["杜可风按"]["valid_link"]
        wangwang_message_send("阿里旺旺 - zmz1054920870", link)
        ws_url = XdClient().get_websocket(tab="right_func_bar")["message"]


    def test_focus_invalid(self):
