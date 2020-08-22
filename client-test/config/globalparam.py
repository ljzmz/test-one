#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2019/9/29 10:37
# @Author : "zhy"
import os
from local_lib.common import readconfig
from local_lib.common import writeconfig

project_abs_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

pro_config_path = os.path.join(project_abs_path, 'config')
pro_ini_path = os.path.join(pro_config_path, 'pro_config.ini')

# 读取配置文件
write_config = writeconfig.WriteConfig(pro_ini_path)
read_config = readconfig.ReadConfig(pro_ini_path)

# 项目参数设置
# prj_path = read_config.getValue('projectConfig', 'project_path')
# prj_path1 = os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + ".")

# 日志路径
# log_path = os.path.join(prj_path, 'log')
log_path = os.path.join(project_abs_path, 'log')


