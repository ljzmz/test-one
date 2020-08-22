#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2019/9/29 10:37
# @Author : "zhy"
import configparser


class WriteConfig:
    """
    专门读取配置文件的，.ini文件格式
    """

    def __init__(self, filename):
        self.configpath = filename

    def setValue(self, pro, val_name, val):
        try:
            config = configparser.ConfigParser()
            config.read(self.configpath, encoding="utf-8")
            config.set(pro, val_name, val)
            f = open(self.configpath, 'w', encoding="utf-8")
            config.write(f)
            f.close()
        except Exception as e:
            print(e)
        return


if __name__ == '__main__':
    from config.globalparam import write_config

    write_config.setValue('projectConfig', 'target_url', '方法')
