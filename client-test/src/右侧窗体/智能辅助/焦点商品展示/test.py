#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 14:56
# @Author : "zmz"

from local_lib.client.XdClient import XdClient
from local_lib.client.其它.wangwang_api import *
import configparser


def focus_Valid():
    wangwang_message_send("阿里旺旺 - zmz1054920870",
                          """https://item.taobao.com/item.htm?spm=a1z10.1-c.w4004-21232229734.2.50123ba17ZGkSv&id=585878791631
                          """)
    ws_url = XdClient().get_websocket(tab = "right_func_bar")["message"]
    return ws_url
    # PageResource = XdClient().get_page_resource(ws_url="ws_url")
    # print(PageResource)

def test_focus_Valid():

    config = configparser.ConfigParser()
    config.read(os.path.dirname(__file__) + str("/Link.ini"),encoding="utf-8")
    link = config["杜可风按"]["valid_link"]
    wangwang_message_send("阿里旺旺 - zmz1054920870",link)
    ws_url = XdClient().get_websocket(tab="right_func_bar")["message"]
    PageResource = XdClient().get_page_resource(ws_url="ws_url")

def test_focus_Invalid():
    pass



if __name__ == "__main__":
    test_focus_Valid()