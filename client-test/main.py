#!/usr/bin/python3# -*- coding: utf-8 -*-
# @Time : 2019/9/29 10:37
# @Author : "zhy"
import pytest

from local_lib.common.xml_update import update_xml_main


class TbpRunner(object):
    def __init__(self):
        pass

    def run(self, run_args=None):
        # 判断配置文件读取项目配置还是数据库配置
        pytest.main(["-s", "src/", "--alluredir", "report"])


if __name__ == "__main__":
    tbp_runner = TbpRunner()
    tbp_runner.run()
    update_xml_main()
