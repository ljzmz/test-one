#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2019/9/29 10:37
# @Author : "zhy"
import requests
from local_lib.common.utils import return_unified


def get_test_data(sub_function_name):
    try:
        url = 'http://zhy-test1.xiaoduoai.com/auto_test_data'
        params = {
            "sign": 'ca61da42f143ef040fc22afee498a622',
            "sub_function_name": sub_function_name,
        }
        i = 0
        while i < 3:
            try:
                res = requests.post(url, data=params)
                if res.status_code == 200:
                    break
                else:
                    i += 1
            except Exception as e:
                i += 1
                if i >= 3:
                    return {"test_code": 'fail', "fail_message": e.args}
        res_list = return_unified(res)
        return res_list
    except Exception as e:
        return {"test_code": 'fail', "fail_message": e.args}

