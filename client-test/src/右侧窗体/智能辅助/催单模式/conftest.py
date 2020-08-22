# -*- coding: utf-8 -*-
# @Time    : 2020/2/4 17:01
# @Author  : zhipeng
import pytest

from local_lib.client.XdClient import XdClient


@pytest.fixture(scope="session")
def get_websocket_url():
    return XdClient().get_websocket("right_func_bar")["message"]
