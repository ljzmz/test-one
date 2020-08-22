#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2019/9/29 10:37
# @Author : "zhy"
import json
import re
import time
import os
from websocket import create_connection

import requests
import psutil
from bs4 import BeautifulSoup


def get_qianniu_inject_id():
    data = []
    try:
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)
            if p.name().lower() == "aliapp.exe":
                parent_pid = p.ppid()
                parent = psutil.Process(parent_pid)
                if parent.name().lower() == "aliworkbench.exe":
                    data.append(pid)
    except Exception as e:
        print(e)
    return data


def get_chorme_port(pid):
    dos_cmd = 'netstat -nao | find "%s" | find "127.0.0.1"' % pid
    p = os.popen(dos_cmd)
    time.sleep(1)
    word = str(p.read())
    matchObj = re.match(r'.*?127.0.0.1:(.*?) ', word, re.M | re.I)
    if matchObj:
        return str(matchObj.group(1))
    else:
        return ""


def get_qianniu_ws_path(pid):
    chorme_port = get_chorme_port(pid)
    qianniu_url = "http://127.0.0.1:" + str(chorme_port) + "/json"
    res = requests.get(qianniu_url, timeout=5)
    content = json.loads(res.text)
    for i in content:
        if i["title"] == "当前聊天窗口":
            return i["webSocketDebuggerUrl"]


def qianniu_html(ws_path):
    ws = create_connection(ws_path)
    get_document = {
        "id": 1,
        "method": "DOM.getDocument"
    }
    ws.send(json.dumps(get_document))
    result = ws.recv()
    result = json.loads(result)
    nodeId = result["result"]["root"]["nodeId"]
    backendNodeId = result["result"]["root"]["backendNodeId"]
    get_html = {
        "id": 2,
        "method": "DOM.getOuterHTML",
        "params": {
            "nodeId": nodeId,
            "backendNodeId": backendNodeId,
        }
    }
    ws.send(json.dumps(get_html))
    result = ws.recv()
    html = json.loads(result)["result"]["outerHTML"]
    ws.close()
    return html


GET_DOCUMENT_REQ = '{"id": 1, "method": "DOM.getDocument"}'
GET_HTML_REQ = '{"id": 1, "method": "DOM.getOuterHTML", "params": {"nodeId": %s}}'
CLEAR_MSG_REQ = '{"id": 1, "method": "Console.clearMessages"}'
CONSOLE_ENABLE_REQ = {"id": 1, "method": "Console.enable",
                      "params": {"expression": "document.documentElement.outerHTML",
                                 "objectGroup": "console", "includeCommandLineAPI": False,
                                 "doNotPauseOnExceptions": False, "returnByValue": True}}
RUNTIME_EVALUATE_REQ = {
    "id": 1, "method": "Runtime.evaluate", "params":
        {
            "expression": "%s",
            "objectGroup": "console",
            "includeCommandLineAPI": True,
            "doNotPauseOnExceptions": False,
            "returnByValue": True
        }
}


def send_websocket_request(ws, req_type, req_para=None):
    if not ws:
        return
    try:
        if req_type == 'get_document':
            ws.sock.send(GET_DOCUMENT_REQ)
        elif req_type == 'get_html':
            ws.sock.send(GET_HTML_REQ % req_para)
        elif req_type == 'clear_msg':
            ws.send(CLEAR_MSG_REQ)
        elif req_type == 'console_enable_req':
            ws.send(json.dumps(CONSOLE_ENABLE_REQ))
        elif req_type == 'elevate':
            ws.send(json.dumps(RUNTIME_EVALUATE_REQ) % req_para)
        elif req_type == 'invoke':
            invoke_str = "QN.wangwang.invoke(%s)" % req_para
            ws.send(json.dumps(RUNTIME_EVALUATE_REQ) % invoke_str)
        elif req_type == 'reg_event_listener':
            reg_event_str = "QN.event.regEvent(%s)" % req_para
            ws.send(json.dumps(RUNTIME_EVALUATE_REQ) % reg_event_str)
        elif req_type == 'unreg_event_listener':
            reg_event_str = "QN.event.unregEvent(%s)" % req_para
            ws.send(json.dumps(RUNTIME_EVALUATE_REQ) % reg_event_str)
    except Exception as e:
        print(e)


def send_message(ws):
    # send_websocket_request(ws, 'clear_msg')
    # req_para = "clear_msg"
    # ws.send(json.dumps(RUNTIME_EVALUATE_REQ) % req_para)
    return


def get_chat_message(html):
    chat_msg_list = []
    soup = BeautifulSoup(html, "lxml")
    for i in soup.select('.msg-content-body'):
        img = i.select('.J_imImage')
        error = i.select('.J_resend')
        if error:
            if img:
                chat_msg_list.append(str(img[0]) + "(发送错误)")
            chat_msg_list.append(i.text + "(发送错误)")
        else:
            if img:
                chat_msg_list.append(str(img[0]))
            chat_msg_list.append(i.text)
    return chat_msg_list


def open_chat_window_by_pin(ws, pin):
    req_param = "if (window.im_sdk_client) {" \
                "window.im_sdk_client.invoke('application.openChat', {nick: '%s'});" \
                "} else {" \
                "console.error('open chat failed, %s');" \
                "}" % (pin.encode('utf-8'), pin.encode('utf-8'))
    send_websocket_request(ws, 'elevate', req_param)
    result = ws.recv()
    print(result)


if __name__ == '__main__':
    # from urllib.parse import quote
    # print(quote("tb671067_2013"))
    # pid = get_qianniu_inject_id()
    # # ws_path = get_qianniu_ws_path(pid)  # 127.0.0.1:50856
    # # h = qianniu_html(ws_path)
    # # l = get_chat_message(h)
    # # print(l)
    # ws_path = "ws://127.0.0.1:50856/devtools/page/(5FFC67AAD22AEB56970EAA6B39DC9A4A)"
    # ws = create_connection(ws_path)
    # send_message(ws)
    # req_para = ("window.xd_send_msg('%s', '%s', decodeURIComponent('%s'));" % ("cntaobaokuaidanian", quote("大大声道所"),
    #                                                                            quote("大大声道所")))
    # send_websocket_request(ws, 'elevate', req_para)
    # result = ws.recv()
    # print(result)
    # # open_chat_window_by_pin(ws, "sundayinsumme5")
    # ws.close()
    print(get_qianniu_inject_id())
