#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2019/9/29 10:37
# @Author : "zhy"
import requests


def send_message(content):
    dingding_url = 'https://oapi.dingtalk.com/robot/send'
    params = {
        "access_token": "aa9a76956e0bcf39e7d5ddccc5437fc9afd11e81fecb41569d4b5415dd95c8e9"
    }
    data = {
        "msgtype": "text",
        "text": {
            "content": content,
        },
    }
    result = requests.post(dingding_url, json=data, params=params)
    return result.text
