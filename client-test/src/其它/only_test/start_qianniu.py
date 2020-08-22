#!/usr/bin/python3# -*- coding: utf-8 -*-
# @Time : 2019/9/29 10:37
# @Author : "zhy"
import os
import sys
sys.path.append("C:\\git-data\\client-test")
import time
import win32gui
import win32api
import win32con
import pyautogui
import pyperclip
import win32com.client
import win32clipboard

from local_lib.const import *
from pywinauto.application import Application
from local_lib.client.其它.windows_api import kill_pid, press_hold_release, get_proccess_id


def qianniu_check_started():
    # 检测当前千牛是否启动，启动了杀掉
    qianniu_pid = get_proccess_id(qianniu_pid_name)
    if not qianniu_pid or len(qianniu_pid) == 0:
        print("千牛未启动")
    else:
        print("千牛已启动：" + str(qianniu_pid))
        print("杀掉千牛")
        for i in qianniu_pid:
            kill_pid(i)
            time.sleep(1)
    # 启动千牛
    os.startfile(qianniu_dir)
    time.sleep(5)


def qianniu_login(app):
    screenw, screenh = pyautogui.size()
    print("获取当前屏幕分辩率" + str(screenw) + "*" + str(screenh))
    handle = win32gui.FindWindow(0, '千牛 - 卖家工作台')
    if handle == "" or handle is None:
        print("获取handle失败")
    else:
        print("获取到千牛登录窗口：" + str(handle))
    # 获取千牛窗口的坐标
    qianniu_size = win32gui.GetWindowRect(handle)
    x1, y1, x2, y2 = qianniu_size
    # 缩小坐标范围
    x1 += 240
    print(qianniu_size)
    # 找到输入用户名的框
    user_name = dm.FindMultiColor(x1, y1, x2, y2, "338cdd", "1|7|7cb5e9,-1|-8|378dde,3|-3|69aae6,"
                                                            "-6|3|1E90FF,7|3|3089dc,6|1|529ce2,-5|1|4294e0", 0.8, 0)
    if user_name[0] > 0:
        print("找到用户名框：", user_name)
        # 移动鼠标到该位置并完成操作
        pyautogui.moveTo(user_name[1], user_name[2] - 50)
        pyautogui.click()
        pyautogui.moveTo(user_name[1] + 50, user_name[2])
        pyautogui.click()
        # 清空输入框
        press_hold_release("ctrl", "a")
        win32api.keybd_event(0x2E, 0, 0, 0)
        time.sleep(.05)
        win32api.keybd_event(0x2E, 0, win32con.KEYEVENTF_KEYUP, 0)
        pyperclip.copy('tb671067_2013:克明')
        pyautogui.hotkey('ctrl', 'v')
        # 找到密码框
        pyautogui.moveTo(user_name[1], user_name[2] - 50)
        pyautogui.click()
        pyautogui.moveTo(user_name[1] + 50, user_name[2])
        pyautogui.click()
        pyautogui.moveTo(user_name[1] + 50, user_name[2] + 50)
        pyautogui.click()
        press_hold_release("ctrl", "a")
        win32api.keybd_event(0x2E, 0, 0, 0)
        time.sleep(.05)
        win32api.keybd_event(0x2E, 0, win32con.KEYEVENTF_KEYUP, 0)
        pyperclip.copy('ckm123456')  # 先复制
        pyautogui.hotkey('ctrl', 'v')  # 再粘贴

        # 点击登录登录
        pyautogui.moveTo(user_name[1] + 100, user_name[2] + 120)
        pyautogui.click()
        time.sleep(7)

        # 处理千牛未处理消息
        deal_qianniu_messagebox(app)
        time.sleep(2)
        test = dm.FindMultiColor(x1, y1, x2, y2, "338cdd", "1|7|7cb5e9,-1|-8|378dde,3|-3|69aae6,"
                                                           "-6|3|1E90FF,7|3|3089dc,6|1|529ce2,-5|1|4294e0", 0.8, 0)
        if test[0] > 0:
            print("登陆失败")
            exit()
        verfy_code(handle)
        time.sleep(5)
    else:
        print("用户名输入框定位失败")


def deal_qianniu_messagebox(app):
    try:
        a = app["Dialog"]["千牛卖家工作台"].children()[2]
        x1, y1, = a.element_info.rectangle.left, a.element_info.rectangle.top
        pyautogui.moveTo(x1, y1)
        pyautogui.click()
    except Exception as e:
        print(e)
        pass


def verfy_code(handle):
    # 重新获取获取千牛窗口的坐标
    try:
        qianniu_size = win32gui.GetWindowRect(handle)
    except Exception as e:
        print(e.args)
        print("获取不到验证码窗体")
        return
    x1, y1, x2, y2 = qianniu_size
    # 缩小坐标范围
    x1 += 240
    # 找到输入用户名的框
    verfy_code_pos = dm.FindMultiColor(x1 + 40, y1 + 190, x2 - 50, y2 - 210, "dbdbdb", "6|5|e0e0e0", 0.8, 0)
    if verfy_code_pos[0] > 0:
        print("处理验证码")
        print(verfy_code_pos)
        code_x, code_y = verfy_code_pos[1], verfy_code_pos[2]
        win32api.SetCursorPos((code_x + 20, code_y + 25))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        code_x += 260
        win32api.SetCursorPos((code_x + 260, code_y + 25))
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    else:
        print("没有验证码")


def open_qianniu_chat_windows(handle):
    app = Application(backend="uia").connect(handle=handle)
    # app_window = app.window(handle=handle)
    # win32gui.SetWindowPos(handle, win32con.HWND_TOPMOST, 0, 0, 0, 0,
    #                       win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER |
    #                       win32con.SWP_SHOWWINDOW)
    # q = app_window.children()[7].children()[2].children()[0]
    app_window = app.window(handle=handle)
    q = app_window.children()[7].children()[2].children()[0]
    #  坐标 q.element_info.rectangle
    x1, y1, x2, y2 = win32gui.GetWindowRect(q.handle)
    pyautogui.moveTo(x1, y1)
    pyautogui.click()


def open_qianniu_workstation(qianniu_name):
    # draw_outline(colour="red")
    taskbar_list = []
    overflow_list = []
    qianniu_name = qianniu_name + " - 千牛"
    app = Application(backend="uia").connect(title="任务栏")
    for i in app["任务栏"].children()[4].children()[1].children()[0].children():
        taskbar_list.append(i.element_info.name)
    if qianniu_name in taskbar_list:
        print("千牛任务图标在任务栏区域")
        app["任务栏"][qianniu_name].click()
        return True
    app["任务栏"].children()[4].children()[0].click()
    time.sleep(1)
    app = Application(backend="uia").connect(title="通知溢出")
    # app["通知溢出"]["溢出通知区域"].print_control_identifiers()
    for i in app["通知溢出"]["溢出通知区域"].children():
        overflow_list.append(i.element_info.name)
    if qianniu_name in overflow_list:
        print("千牛任务图标在通知溢出区域")
        app["通知溢出"][qianniu_name].click()
        return True
    print("千牛图标未找到")
    return False


def change_chat_member(app):
    # pid = get_proccess_id('AliWorkbench.exe'.lower())
    # app = Application(backend="uia").connect(process=pid[0])
    my_friend = app.Dialog.children()[1].children()[2].children()[0].children()[2]
    my_friend_postion = win32gui.GetWindowRect(my_friend.handle)
    x1, y1, x2, y2 = my_friend_postion
    pyautogui.moveTo(x1, y1)
    pyautogui.click()
    friend_list = []
    friend_list_tree = []
    friend_tree = \
    app.Dialog.children()[1].children()[2].children()[1].children()[0].children()[0].children()[0].children()[
        0].children()[0].children()
    for i in friend_tree:
        if "(" in i.element_info.name and ")" in i.element_info.name and "/" in i.element_info.name:
            friend_list_tree.append(i.element_info.name)
        else:
            friend_list.append(i.element_info.name)
    print(friend_list)
    print(friend_list_tree)
    for i in (app["Dialog"]["未分组好友(2/5)"]).parent().children():
        if i.element_info.name == "黑名单(0/0)":
            x1, y1, = i.element_info.rectangle.left, i.element_info.rectangle.top
            pyautogui.moveTo(x1, y1)
            pyautogui.click()


def change_chat_member_by_search(app, chat_member):
    # pid = get_proccess_id('AliWorkbench.exe'.lower())
    # app = Application(backend="uia").connect(process=pid[0])
    # app["Dialog"].children()[1].children()[5].parent().print_control_identifiers()
    # app["Dialog"].print_control_identifiers()
    a = app["Dialog"].children()[1].children()[5]
    x1, y1, = a.element_info.rectangle.left, a.element_info.rectangle.top
    pyautogui.moveTo(x1 + 60, y1 + 10)
    pyautogui.click()
    pyperclip.copy(chat_member)  # 先复制
    pyautogui.hotkey('ctrl', 'v')  # 再粘贴
    time.sleep(1)
    win32api.keybd_event(VK_CODE["enter"], 0, 0, 0)
    time.sleep(.05)
    win32api.keybd_event(VK_CODE["enter"], 0, win32con.KEYEVENTF_KEYUP, 0)


def wangcai_check_started():
    # 检测当前千牛是否启动，启动了杀掉
    wangcai_pid = get_proccess_id(wangcai_pid_name)
    if not wangcai_pid or len(wangcai_pid) == 0:
        print("晓多未启动")
    else:
        print("晓多已启动：" + str(wangcai_pid))
        print("杀掉千牛")
        for i in wangcai_pid:
            kill_pid(i)
            time.sleep(1)
    # 启动千牛
    os.startfile(wangcai_dir)
    time.sleep(5)


def wangwang_message_send(name, word):
    pid = get_proccess_id('AliIM.exe'.lower())
    app = Application(backend="uia").connect(process=pid[0])
    name = '阿里旺旺 - ' + name
    app[name]['Pane7'].type_keys(word)
    app[name]['Pane7'].type_keys("{ENTER}")
    time.sleep(0.5)
    app[name]['Pane7'].type_keys("{ENTER}")


def wangwang_message_get(name):
    pid = get_proccess_id('AliIM.exe'.lower())
    app = Application(backend="uia").connect(process=pid[0])
    name = '阿里旺旺 - ' + name
    # app['阿里旺旺 - kuaidanian'].print_control_identifiers()
    app[name]['聊天窗口'].type_keys("^A")
    app[name]['聊天窗口'].type_keys("^C")
    time.sleep(5)
    data = getCopyTxet()
    return data


def getCopyTxet():
    win32clipboard.OpenClipboard()
    copytxet = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return str(copytxet)


if __name__ == '__main__':
    qianniu_dir = "C:\\software\\qianniu\\AliWorkbench.exe"
    qianniu_pid_name = "AliWorkbench.exe".lower()
    wangcai_dir = "C:\\Users\\张大爷\\Desktop\\data\\xiaoduo\\xiaoduo-2.23.12\\2.23.12\\wangcai_main.exe"
    wangcai_pid_name = "wangcai_main.exe".lower()

    # 加载大漠插件
    dm = win32com.client.Dispatch('dm.dmsoft')
    dm_ver = dm.ver()
    if dm_ver == "" or dm_ver is None:
        print("大漠插件加载失败")
        exit()
    else:
        print("大漠插件加载成功，当前版本：" + dm_ver)

    # 加载字典
    # dm.setDict(0, 'c:\dm_soft.txt')
    # dm.useDict(0)

    x = 0
    while x < 1:
        try:
            qianniu_check_started()
            pid = get_proccess_id(qianniu_pid_name)
            app = Application(backend="uia").connect(process=pid[0])
            qianniu_login(app)
            handle = win32gui.FindWindow(0, 'tb671067_2013:克明 - 工作台')
            open_qianniu_chat_windows(handle)
            # open_qianniu_workstation("杜可风按:c")
            change_chat_member_by_search(app, "kuaidanian")
            wangcai_check_started()
            time.sleep(5)
            flag = str(int(time.time()))
            wangwang_message_send("kuaidanian", flag)
            wangwang_message_send("kuaidanian", "你好")
            time.sleep(2)
            msg = wangwang_message_get("kuaidanian")
            print(msg)
            x += 1
        except Exception as e:
            print(e)
            x += 1
    # isadmin = "1"  # 启动方式 1为管理员
    # if isadmin == "1":
    #     if is_admin():
    #         pass
    #     else:
    #         if sys.version_info[0] == 3:
    #             ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    #         else:
    #             print("no support py2")
    #             exit()
    # win32api.ShellExecute(None, 'runas', exe_path, None, None, 1)
