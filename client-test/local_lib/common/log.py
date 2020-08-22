#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2019/9/29 10:37
# @Author : "zhy"
import time
import os
import logging
from config import globalparam

log_path = globalparam.log_path


class Log(object):

    def __init__(self):
        self.logname = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))

    def __printconsole(self, level, message):
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message=None, title='日志'):
        try:
            if isinstance(message, str):
                pass
            else:
                message = str(message)
        except Exception as e:
            print(e)
        # self.write.write_log(title, 'debug', '自动化测试日志', message)
        self.__printconsole('debug', time.strftime('%Y-%m-%d %H:%M:%S') + '\t' + message + '\n')

    def info(self, message=None, title='日志'):
        try:
            if isinstance(message, str):
                pass
            else:
                message = str(message)
        except Exception as e:
            print(e)
        # self.write.write_log(title, 'info', '自动化测试日志', message)
        self.__printconsole('info', time.strftime('%Y-%m-%d %H:%M:%S') + '\t' + message + '\n')

    def warning(self, message=None, title='日志'):
        try:
            if isinstance(message, str):
                pass
            else:
                message = str(message)
        except Exception as e:
            print(e)
        # self.write.write_log(title, 'warning', '自动化测试日志', message)
        self.__printconsole('warning', time.strftime('%Y-%m-%d %H:%M:%S') + '\t'  + message + '\n')

    def error(self, message=None, title='日志'):
        try:
            if isinstance(message, str):
                pass
            else:
                message = str(message)
        except Exception as e:
            print(e)
        # self.write.write_log(title, 'error', '自动化测试日志', message)
        self.__printconsole('error', time.strftime('%Y-%m-%d %H:%M:%S') + '\t' + message + '\n')
