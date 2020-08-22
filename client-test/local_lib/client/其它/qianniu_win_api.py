#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2019/9/29 10:37
# @Author : "zhy"
import os
import time
import win32gui
import win32api
import win32con
import pyautogui
import pyperclip
from pywinauto.application import Application

from local_lib.const import *
from local_lib.client.其它.windows_api import kill_pid, press_hold_release, get_proccess_id


def verfy_code(handle, dm):
    """
    :param handle: 窗口句柄
    :param dm: 大漠实体
    :return:
    """
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


def qianniu_check_started(qianniu_pid_name, qianniu_dir):
    # 检测当前千牛是否启动，启动了杀掉
    qianniu_pid = get_proccess_id(qianniu_pid_name.lower())
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


def qianniu_login(dm, app):
    # 获取当前屏幕分辩率
    screenw, screenh = pyautogui.size()
    print("获取当前屏幕分辩率" + str(screenw) + "*" + str(screenh))

    # 获取千牛登录窗口的句柄
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
        time.sleep(8)

        # 处理千牛未处理消息
        deal_qianniu_messagebox(app)
        time.sleep(2)
        test = dm.FindMultiColor(x1, y1, x2, y2, "338cdd", "1|7|7cb5e9,-1|-8|378dde,3|-3|69aae6,"
                                                           "-6|3|1E90FF,7|3|3089dc,6|1|529ce2,-5|1|4294e0", 0.8, 0)
        if test[0] > 0:
            print("登陆失败")
            exit()
        verfy_code(handle, dm)
        time.sleep(10)
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


def open_qianniu_chat_windows(handle):
    # app_window = app.window(handle=handle)
    # win32gui.SetWindowPos(handle, win32con.HWND_TOPMOST, 0, 0, 0, 0,
    #                       win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER |
    #                       win32con.SWP_SHOWWINDOW)
    # q = app_window.children()[7].children()[2].children()[0]
    app = Application(backend="uia").connect(handle=handle)
    app_window = app.window(handle=handle)
    # app_window.print_control_identifiers()
    try:
        q = app_window.children()[8].children()[2].children()[0]
    except Exception as e:
        print(e)
        q = app_window.children()[7].children()[2].children()[0]
    #  坐标 q.element_info.rectangle
    x1, y1, x2, y2 = win32gui.GetWindowRect(q.handle)
    pyautogui.moveTo(x1, y1)
    pyautogui.click()


def change_chat_member_by_search(chat_member):
    # pid = get_proccess_id('AliWorkbench.exe'.lower())
    # app = Application(backend="uia").connect(process=pid[0])
    # app["Dialog"].children()[1].children()[5].parent().print_control_identifiers()
    pid = get_proccess_id("AliWorkbench.exe".lower())
    search_app = Application(backend="uia").connect(process=pid[0])
    print(pid)
    time.sleep(1)
    search_app[""].print_control_identifiers()
    a = search_app["Dialog"].children()[1].children()[5]
    x1, y1, = a.element_info.rectangle.left, a.element_info.rectangle.top
    pyautogui.moveTo(x1 + 60, y1 + 10)
    pyautogui.click()
    pyperclip.copy(chat_member)  # 先复制
    pyautogui.hotkey('ctrl', 'v')  # 再粘贴
    time.sleep(1)
    win32api.keybd_event(VK_CODE["enter"], 0, 0, 0)
    time.sleep(.05)
    win32api.keybd_event(VK_CODE["enter"], 0, win32con.KEYEVENTF_KEYUP, 0)


if __name__ == '__main__':
    # handle = win32gui.FindWindow(0, 'tb671067_2013:克明 - 工作台')
    # open_qianniu_chat_windows(handle)
    change_chat_member_by_search("kuaidanian")
