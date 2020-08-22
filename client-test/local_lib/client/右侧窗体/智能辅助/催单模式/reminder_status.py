#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/7/9 15:32
# @Author : "zhy"
from local_lib.client.XdClient import XdClient


class ReminderStatus(XdClient):

    def set_status(self, ws_url, js):
        self.run_js(ws_url, js)
