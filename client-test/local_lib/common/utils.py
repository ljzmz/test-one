#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2019/9/29 10:37
# @Author : "zhy"
import hashlib
import inspect
import json
import time

import allure
import requests

from config.globalparam import pro_ini_path
from local_lib.common import readconfig
from local_lib.common.log import Log

log = Log()
re_try_num_refresh_redis = 0
re_try_num_cuidan_redis = 0
robot_reply_uri = '/api/admin/robot/reply?'


def return_unified(arg, removekey=None):
    # 接口测试统一返回函数
    if arg.status_code == 200:
        try:
            return_dict = arg.json()
            allure.attach('response:', str(json.dumps(arg.json())).encode().decode('unicode_escape'))
            return_dict["test_code"] = "success"
            return_dict["fail_message"] = ""
            if removekey:
                try:
                    del return_dict[removekey]
                except:
                    pass
        except:
            fail_data = {"test_code": "fail", "fail_message": "解析失败"}
            return fail_data
        return return_dict
    else:
        log.error(arg)
        return {"test_code": "fail", "fail_message": "接口调用失败"}


def get_md5(msg):
    m = hashlib.md5()
    msg += str(time.time())
    m.update(bytes(msg, 'utf-8'))
    return m.hexdigest()


def refresh_redis():
    try:
        read = readconfig.ReadConfig(pro_ini_path)
        target_url = read.getValue('projectConfig', 'target_url')
        if "test1" in target_url:
            url = 'http://zhy-test1.xiaoduoai.com/refresh_redis'
        elif "test2" in target_url:
            url = 'http://zhy-test2.xiaoduoai.com/refresh_redis'
        params = {
            "sign": 'ca61da42f143ef040fc22afee498a622',
        }
        log.info('\t'.join((url, str(params))))
        time.sleep(0.1)
        i = 0
        while i < 3:
            try:
                res = requests.get(url, params=params)
                if res.status_code == 200:
                    break
                else:
                    log.info("请求失败重试次数" + str(i + 1))
                    i += 1
            except Exception as e:
                log.error(e.args)
                log.info("请求失败重试次数" + str(i + 1))
                i += 1
                if i >= 3:
                    return {"test_code": 'fail', "fail_message": e.args}
        res_list = return_unified(res)
        return res_list
    except Exception as e:
        log.error(e.args)
        return {"test_code": 'fail', "fail_message": e.args}


def cuidan_redis(buyer, seller, status, tid, payment):
    _caller = inspect.stack()[1][1].split('/')[-1] + '::' + inspect.stack()[1][3]
    try:
        read = readconfig.ReadConfig(pro_ini_path)
        target_url = read.getValue('projectConfig', 'target_url')
        if "test1" in target_url:
            url = 'http://zhy-test1.xiaoduoai.com/cuidan_create'
        elif "test2" in target_url:
            url = 'http://zhy-test2.xiaoduoai.com/cuidan_create'

        params = {
            "sign": 'ca61da42f143ef040fc22afee498a622',
            "buyer": buyer,
            "seller": seller,
            "status": status,
            "tid": tid,
            "payment": payment,
        }
        log.info('\t'.join((_caller, url, str(params))))
        allure.attach('催单信息', "buyer:" + buyer + "\nseller:" + seller + "\nstatus:"
                      + status + "\ntid:" + tid + "\npayment:" + payment)
        time.sleep(0.1)
        i = 0
        while i < 3:
            try:
                res = requests.get(url, params=params)
                if res.status_code == 200:
                    break
                else:
                    log.info("请求失败重试次数" + str(i + 1))
                    i += 1
            except Exception as e:
                log.error(e.args)
                log.info("请求失败重试次数" + str(i + 1))
                i += 1
                if i >= 3:
                    return {"test_code": 'fail', "fail_message": e.args}
        res_list = return_unified(res)
        return res_list
    except Exception as e:
        log.error(e.args)
        return {"test_code": 'fail', "fail_message": e.args}


def restart_wangcai():
    try:
        url = 'http://10.0.1.70:8989/restart_xiaoduo'
        params = {
            "sign": 'ca61da42f143ef040fc22afee498a622',
        }
        log.info('\t'.join((url, str(params))))
        time.sleep(0.1)
        i = 0
        while i < 3:
            try:
                res = requests.get(url, params=params)
                if res.status_code == 200:
                    break
                else:
                    log.info("请求失败重试次数" + str(i + 1))
                    i += 1
            except Exception as e:
                log.error(e.args)
                log.info("请求失败重试次数" + str(i + 1))
                i += 1
                if i >= 3:
                    return {"test_code": 'fail', "fail_message": e.args}
        res_list = return_unified(res)
        return res_list
    except Exception as e:
        log.error(e.args)
        return {"test_code": 'fail', "fail_message": e.args}


def update_status(user):
    # 获取一次消息列表，使催单处于在线状态
    try:
        read = readconfig.ReadConfig(pro_ini_path)
        target_url = read.getValue('projectConfig', 'target_url')
        if "qa" in target_url:
            url = 'http://wangcai.qa.xiaoduoai.com/api/client/message_list'
        else:
            url = 'http://wangcai.test.xiaoduoai.com/api/client/message_list'
        params = {
            'limit': 10,
            'plat_user_id': user,
            'type': 'all'
        }
        log.info('\t'.join((url, str(params))))
        time.sleep(0.1)
        i = 0
        while i < 3:
            try:
                res = requests.get(url, params=params)
                if res.status_code == 200:
                    break
                else:
                    log.info("请求失败重试次数" + str(i + 1))
                    i += 1
            except Exception as e:
                log.error(e.args)
                log.info("请求失败重试次数" + str(i + 1))
                i += 1
                if i >= 3:
                    return {"test_code": 'fail', "fail_message": e.args}
        res_list = return_unified(res)
        return res_list
    except Exception as e:
        log.error(e.args)
        return {"test_code": 'fail', "fail_message": e.args}


def update_version(path, version):
    # 更改测试服务器上晓多的配置文件
    # path=C:\\Users\\tbp1\\Desktop\\2.20.6.6T\\conf\\config.ini
    # version=qa
    try:
        url = 'http://10.0.1.70:8989/wangcai/update_version'
        params = {
            'sign': "ca61da42f143ef040fc22afee498a622",
            'path': path,
            'version': version,
        }
        i = 0
        while i < 3:
            try:
                res = requests.post(url, data=params)
                if res.status_code == 200:
                    break
                else:
                    log.info("请求失败重试次数" + str(i + 1))
                    i += 1
            except Exception as e:
                log.error(e.args)
                log.info("请求失败重试次数" + str(i + 1))
                i += 1
                if i >= 3:
                    return {"test_code": 'fail', "fail_message": e.args}
        res_list = return_unified(res)
        return res_list
    except Exception as e:
        log.error(e.args)
        return {"test_code": 'fail', "fail_message": e.args}


def login_status(name):
    # 更新在线状态
    try:
        read = readconfig.ReadConfig(pro_ini_path)
        target_url = read.getValue('projectConfig', 'target_url')
        if "test1" in target_url:
            url = 'http://zhy-test1.xiaoduoai.com/login_msg'
        elif "test2" in target_url:
            url = 'http://zhy-test2.xiaoduoai.com/login_msg'
        data = {
            "name": name,
            "sign": "ca61da42f143ef040fc22afee498a622"
        }
        i = 0
        while i < 3:
            try:
                res = requests.post(url, data=data)
                if res.status_code == 200:
                    break
                else:
                    log.info("请求失败重试次数" + str(i + 1))
                    i += 1
            except Exception as e:
                log.error(e.args)
                log.info("请求失败重试次数" + str(i + 1))
                i += 1
                if i >= 3:
                    return {"test_code": 'fail', "fail_message": e.args}
        res_list = return_unified(res)
        return res_list
    except Exception as e:
        log.error(e.args)
        return {"test_code": 'fail', "fail_message": e.args}


def dispatch(server_name, method, word=None, msg=None):
    try:
        read = readconfig.ReadConfig(pro_ini_path)
        dispatch_url = read.getValue('projectConfig', 'dispatch_url')
        data = {
            "platform": "tbp",
            "server_name": server_name,
            "method": method,
            "word": word,
            "msg": msg
        }
        i = 0
        while i < 3:
            try:
                res = requests.post(dispatch_url, data=data)
                res.encoding = "utf-8"
                if res.status_code == 200:
                    break
                else:
                    log.info("请求失败重试次数" + str(i + 1))
                    i += 1
            except Exception as e:
                log.error(e.args)
                log.info("请求失败重试次数" + str(i + 1))
                i += 1
                if i >= 3:
                    return {"test_code": 'fail', "fail_message": e.args}
        res_list = return_unified(res)
        return res_list
    except Exception as e:
        log.error(e.args)
        return {"test_code": 'fail', "fail_message": e.args}
