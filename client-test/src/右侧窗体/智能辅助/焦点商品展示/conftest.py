#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 17:42
# @Author : "zmz"

from local_lib.client.XdClient import XdClient
import configparser
import os.path

# top_bar_mini：顶部导航栏收缩
# top_bar_index：顶部导航栏展开
# right_func_bar：右侧功能栏
# to_reply_list：待回复列表

# @pytest.fixture(scope="session")
def get_websocket_url():
    """{"code": "success", "message": "ws://127.0.0.1:43333/devtools/page/5C0E54B6-7181-4C7C-8A28-3EB21E3E03B3"}"""
    return XdClient().get_websocket("right_func_bar")["message"]

def Link_config():
    config = configparser.ConfigParser()
    config["杜可风按"] = {
        "valid_Link":"https://item.taobao.com/item.htm?spm=a1z10.1-c.w4004-21232229734.2.50123ba17ZGkSv&id=585878791631",
        "invalid_Link":"https://detail.tmall.com/item.htm?spm=a220o.1000855.w4023-16710863608.12.2fab551edxsH5G&id=577086554337"
    }
    with open(os.path.dirname(__file__)+str(r"/Link.ini"),"w",encoding="utf-8") as configfile:
        config.write(configfile)


if __name__ == '__main__':
    Link_config()
