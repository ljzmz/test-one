#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2019/12/12 14:09
# @Author : "zhy"
import allure
import requests
from local_lib.common.log import Log
from local_lib.common.utils import return_unified

log = Log()


def basic_requests(method, url, step, headers, need_assert=True, need_attach=True, **kwargs):
    with allure.step(step):
        try:
            if method == "get":
                send_data = kwargs
                log.info("send requests ：" + url + "\nsend data ：" + str(send_data))
                res = requests.get(url, params=send_data, headers=headers)
                log.info("get response ：\n" + str(res.text))
                res_list = return_unified(res)
            elif method == "post":
                send_data = kwargs.get("json_data", None)
                data = kwargs.get("form_data", None)
                files = kwargs.get('files', None)
                log.info("send requests ：" + url + "\nsend data ：" + str(send_data) + str(data))
                res = requests.post(url, json=send_data, data=data, headers=headers, files=files)
                log.info("get response ：\n" + str(res.text))
                res_list = return_unified(res)
            elif method == "delete":
                send_data = kwargs.get("json_data", None)
                data = kwargs.get("form_data", None)
                log.info("send requests ：" + url + "\nsend data ：" + str(send_data) + str(data))
                res = requests.delete(url, json=send_data, data=data, headers=headers)
                log.info("get response ：\n" + str(res.text))
                res_list = return_unified(res)
            else:
                res_list = "no support"
            if need_attach:
                allure.attach(str(res_list), "修改的内容", allure.attachment_type.TEXT)
        except Exception as e:
            log.error(e.args)
            return {"test_code": 'fail', "fail_message": e.args}
        if need_assert:
            assert res_list.get("code", "") == 0
        return res_list

