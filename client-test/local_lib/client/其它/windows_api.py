#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2019/9/29 10:37
# @Author : "zhy"
import os
import time
import ctypes
import win32api
import win32con
import win32gui
import win32clipboard

import psutil
from local_lib.const import VK_CODE


def press_hold_release(*args):
    """
    组合建按下与释放
    """
    for arg in args:
        win32api.keybd_event(VK_CODE[arg], 0, 0, 0)
        time.sleep(.05)

    for arg in args:
        win32api.keybd_event(VK_CODE[arg], 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(.05)


def get_proccess_id(p_name):
    try:
        pid_list = []
        pids = psutil.pids()
        for pid in pids:
            try:
                p = psutil.Process(pid)
            except Exception as e:
                print(e.args)
                continue
            if p.name().lower() == p_name:
                pid_list.append(pid)
        return pid_list
    except Exception as e:
        print(e)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        print(e)
        return False


def kill_pid(pid):
    try:
        os.popen('taskkill.exe /pid:' + str(pid) + ' -f')
        print('已杀死的进程' + str(pid))
    except OSError:
        print('没有如此进程!!!')


def getCopyTxet():
    win32clipboard.OpenClipboard()
    copytxet = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return str(copytxet)


def set_clipboard_text(text):
    """设置剪贴板文本"""
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, text)
    win32clipboard.CloseClipboard()


def get_clipboard_text(hwnd):
    buf_size = 1 + win32gui.SendMessage(hwnd, win32con.WM_GETTEXTLENGTH, 0, 0)
    buffer = win32gui.PyMakeBuffer(buf_size)
    win32gui.SendMessage(hwnd, win32con.WM_GETTEXT, buf_size, buffer)
    return buffer[:buf_size]


def click(click_type, x_position=None, y_position=None, double_click=False, sleep=0.):
    """
    鼠标点击事件
    :param click_type: 类型，left, right
    :param x_position: 可选
    :param y_position: 可选
    :param double_click: True 双击，False 点击
    :param sleep: 点击之后暂停时间
    :return:
    """
    if click_type not in ["left", "right"]:
        click_type = "left"

    if click_type == "left":
        down, up = win32con.MOUSEEVENTF_LEFTDOWN, win32con.MOUSEEVENTF_LEFTUP
    else:
        down, up = win32con.MOUSEEVENTF_RIGHTDOWN, win32con.MOUSEEVENTF_RIGHTUP

    if x_position is not None and y_position is not None:
        move(x_position, y_position, sleep=sleep)

    win32api.mouse_event(down, 0, 0, 0, 0)
    win32api.mouse_event(up, 0, 0, 0, 0)
    if double_click:
        win32api.mouse_event(down, 0, 0, 0, 0)
        win32api.mouse_event(up, 0, 0, 0, 0)

    if sleep > 0:
        time.sleep(sleep)


def move(x_position, y_position, sleep=0.):
    """
    鼠标移动到指定位置
    :param x_position:
    :param y_position:
    :param sleep:
    :return:
    """
    win32api.SetCursorPos((x_position, y_position))
    if sleep > 0:
        time.sleep(sleep)


def click_left(x_position=None, y_position=None, sleep=0.1):
    """
    鼠标左键点击指定坐标
    :param x_position: x 点
    :param y_position: y 点
    :param sleep: 点击之后暂停时间
    :return: None
    """
    click("left", x_position=x_position, y_position=y_position, sleep=sleep)


def dclick_left(x_position=None, y_position=None, sleep=0.1):
    """
    鼠标左键双击指定坐标
    :param x_position: x 点
    :param y_position: y 点
    :param sleep: 双击之后暂停时间
    :return: None
    """
    click("left", x_position=x_position, y_position=y_position, double_click=True, sleep=sleep)


def click_right(x_position=None, y_position=None, sleep=0.1):
    """
    鼠标右键点击指定坐标
    :param x_position: x 点
    :param y_position: y 点
    :param sleep: 点击之后暂停时间
    :return: None
    """
    click("right", x_position=x_position, y_position=y_position, sleep=sleep)


def dclick_right(x_position=None, y_position=None, sleep=0.1):
    """
    鼠标右键点击指定坐标
    :param x_position: x 点
    :param y_position: y 点
    :param sleep: 点击之后暂停时间
    :return: None
    """
    click("right", x_position=x_position, y_position=y_position, double_click=True, sleep=sleep)


def get_clipboard_txet():
    win32clipboard.OpenClipboard()
    copytxet = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return str(copytxet)


def get_qianniu_msg(hwnd):
    x, y, z, c = win32gui.GetWindowRect(hwnd)
    click_left(x, y)
    time.sleep(0.1)
    press_hold_release("ctrl", "a")
    time.sleep(0.1)
    press_hold_release("ctrl", "c")
    text = get_clipboard_txet()
    return text


def send_qianniu_msg(hwnd):
    win32gui.PostMessage(hwnd, win32con.WM_PASTE, 0, 0)
    win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


def get_child_windows(parent):
    """
    获得parent的所有子窗口句柄
     返回子窗口句柄列表
    :param parent:
    :return:
    """
    if not parent:
        return
    hwnd_child_list = []
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd), hwnd_child_list)
    return hwnd_child_list


def get_parent(hwdn):
    x = 0
    handle = None
    while x <= 3:
        x += 1
        hwdn = win32gui.GetParent(hwdn)
        if hwdn == 0:
            break
        handle = hwdn
    return win32gui.GetClassName(handle)

