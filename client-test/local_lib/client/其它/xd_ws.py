#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/21 19:00
# @Author : "zhy"
import json
import requests

import psutil
from websocket import create_connection

GET_DOCUMENT_REQ = '{"id": 1, "method": "DOM.getDocument"}'
GET_HTML_REQ = '{"id": 1, "method": "DOM.getOuterHTML", "params": {"nodeId": %s}}'
CLEAR_MSG_REQ = '{"id": 1, "method": "Console.clearMessages"}'
CONSOLE_ENABLE_REQ = {
    "id": 1, "method": "Console.enable",
    "params": {
        "expression": "document.documentElement.outerHTML",
        "objectGroup": "console",
        "includeCommandLineAPI": False,
        "doNotPauseOnExceptions": False,
        "returnByValue": True
    }
}
RUNTIME_EVALUATE_REQ = {
    "id": 1, "method": "Runtime.evaluate", "params":
        {
            "expression": "%s",
            "objectGroup": "console",
            "includeCommandLineAPI": True,
            "doNotPauseOnExceptions": False,
            "returnByValue": False
        }
}


def send_websocket_request(ws, req_type, req_para=None):
    if not ws:
        print("Send cmd failed, error")
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
            js = {
                "id": 1, "method": "Runtime.evaluate", "params": {
                    "expression": req_para,
                    "objectGroup": "console",
                    "includeCommandLineAPI": True,
                    "doNotPauseOnExceptions": False,
                    "returnByValue": False
                }
            }
            js = json.dumps(js)
            ws.send(js)
        elif req_type == 'invoke':
            invoke_str = "QN.wangwang.invoke(%s)" % req_para
            ws.send(json.dumps(RUNTIME_EVALUATE_REQ) % invoke_str)
        elif req_type == 'reg_event_listener':
            reg_event_str = "QN.event.regEvent(%s)" % req_para
            ws.send(json.dumps(RUNTIME_EVALUATE_REQ) % reg_event_str)
        elif req_type == 'unreg_event_listener':
            reg_event_str = "QN.event.unregEvent(%s)" % req_para
            ws.send(json.dumps(RUNTIME_EVALUATE_REQ) % reg_event_str)
    except:
        print("Send cmd failed, error")


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


def get_qianniu_ws_path():
    qianniu_url = "http://127.0.0.1:43333/json"
    res = requests.get(qianniu_url, timeout=5)
    content = json.loads(res.text)
    for i in content:
        if i["title"] == "小多MP千牛插件" and "_k" not in i["url"]:
            if "webSocketDebuggerUrl" in i:
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
    # backendNodeId = result["result"]["root"]["backendNodeId"]
    get_html = {
        "id": 2,
        "method": "DOM.getOuterHTML",
        "params": {
            "nodeId": nodeId,
            # "backendNodeId": backendNodeId,
        }
    }
    ws.send(json.dumps(get_html))
    result = ws.recv()
    html = json.loads(result)["result"]["outerHTML"]
    ws.close()
    return html


def send_js(ws_path, js):
    ws = create_connection(ws_path)
    send_websocket_request(ws, 'elevate', js)
    result = json.loads(ws.recv())
    ws.close()
    return result


if __name__ == '__main__':
    # print(qianniu_html(get_qianniu_ws_path()))
    # js = 'document.getElementsByClassName("ant-input")[0].value="123123123";'
    # js = 'function sleep(n) {' \
    #      'var start = new Date().getTime();' \
    #      'while (true) {' \
    #      'if (new Date().getTime() - start > n) {' \
    #      'break;' \
    #      '}' \
    #      '}' \
    #      '};' \
    #      'sleep(2000);' \
    #      'function getdata(){document.getElementsByClassName("ant-input")[0].value=1111112;};' \
    #      'sleep(2000);' \
    #      'getdata();'
    # js = "document.getElementsByClassName('ant-input')[0].value=1"
    js = "$x('/html/body/div[2]/div/div/div/ul/li[3]')[0].click();"
    # js = "document.evaluate('//*[@id='root']/div/div/ul/li[1]', document, null, XPathResult.ANY_TYPE, null)"
    print(send_js("ws://127.0.0.1:43333/devtools/page/7BFD6F31-D493-4CB4-9A88-9CE0BE74B6EA", js))
