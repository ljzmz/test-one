#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/7/9 15:20
# @Author : "zhy"
from local_lib.common import readconfig
from config.globalparam import pro_ini_path
from local_lib.base_requests import basic_requests


class XdClient(object):
    def __init__(self):
        self.read = readconfig.ReadConfig(pro_ini_path)
        self.target_url = self.read.getValue('projectConfig', 'target_url')
        self.runJS_url = self.target_url + '/api/client/runJS'
        self.getWebSocket_url = self.target_url + '/api/client/getWebSocket'
        self.getPageResource_url = self.target_url + '/api/client/getPageResource'

    def get_websocket(self, tab, need_attach=False):
        """
        :param headers:
        :param json_data:
        :return:
        """
        step = "获取websocket地址"
        method = "post"
        json_data = {
            "tab": tab,
            "host": self.read.getValue('projectConfig', 'cef_host'),
            "port": self.read.getValue('projectConfig', 'cef_port')
        }
        return basic_requests(method, self.getWebSocket_url, step, headers=None, json_data=json_data,
                              need_attach=need_attach, need_assert=False)

    def run_js(self, ws_url, js, ws_session=None, close=True, timeout=None, need_attach=False):
        """
        :param headers:
        :param json_data:
        :return:
        """
        # print(close)
        step = "执行js"
        method = "post"
        json_data = {
            "ws_url": ws_url,
            "js": js,
            "close": close,
            "timeout": timeout,
            "ws_session": ws_session
        }
        return basic_requests(method, self.runJS_url, step, headers=None, json_data=json_data, need_attach=need_attach
                              , need_assert=False)

    def get_page_resource(self, ws_url, need_attach=False):
        """
        :param headers:
        :param json_data:
        :return:
        """
        step = "获取页面源码"
        method = "post"
        json_data = {
            "ws_url": ws_url
        }
        return basic_requests(method, self.getPageResource_url, step, headers=None, json_data=json_data,
                              need_attach=need_attach, need_assert=False)
