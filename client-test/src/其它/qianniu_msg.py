#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2019/10/21 14:14
# @Author : "zhy"
import win32api
import win32con
import win32gui
import time
import win32clipboard
from pywinauto.application import Application
import psutil

VK_CODE = {
    'backspace': 0x08,
    'tab': 0x09,
    'clear': 0x0C,
    'enter': 0x0D,
    'shift': 0x10,
    'ctrl': 0x11,
    'alt': 0x12,
    'pause': 0x13,
    'caps_lock': 0x14,
    'esc': 0x1B,
    'spacebar': 0x20,
    'page_up': 0x21,
    'page_down': 0x22,
    'end': 0x23,
    'home': 0x24,
    'left_arrow': 0x25,
    'up_arrow': 0x26,
    'right_arrow': 0x27,
    'down_arrow': 0x28,
    'select': 0x29,
    'print': 0x2A,
    'execute': 0x2B,
    'print_screen': 0x2C,
    'ins': 0x2D,
    'del': 0x2E,
    'help': 0x2F,
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,
    'a': 0x41,
    'b': 0x42,
    'c': 0x43,
    'd': 0x44,
    'e': 0x45,
    'f': 0x46,
    'g': 0x47,
    'h': 0x48,
    'i': 0x49,
    'j': 0x4A,
    'k': 0x4B,
    'l': 0x4C,
    'm': 0x4D,
    'n': 0x4E,
    'o': 0x4F,
    'p': 0x50,
    'q': 0x51,
    'r': 0x52,
    's': 0x53,
    't': 0x54,
    'u': 0x55,
    'v': 0x56,
    'w': 0x57,
    'x': 0x58,
    'y': 0x59,
    'z': 0x5A,
    'numpad_0': 0x60,
    'numpad_1': 0x61,
    'numpad_2': 0x62,
    'numpad_3': 0x63,
    'numpad_4': 0x64,
    'numpad_5': 0x65,
    'numpad_6': 0x66,
    'numpad_7': 0x67,
    'numpad_8': 0x68,
    'numpad_9': 0x69,
    'multiply_key': 0x6A,
    'add_key': 0x6B,
    'separator_key': 0x6C,
    'subtract_key': 0x6D,
    'decimal_key': 0x6E,
    'divide_key': 0x6F,
    'F1': 0x70,
    'F2': 0x71,
    'F3': 0x72,
    'F4': 0x73,
    'F5': 0x74,
    'F6': 0x75,
    'F7': 0x76,
    'F8': 0x77,
    'F9': 0x78,
    'F10': 0x79,
    'F11': 0x7A,
    'F12': 0x7B,
    'F13': 0x7C,
    'F14': 0x7D,
    'F15': 0x7E,
    'F16': 0x7F,
    'F17': 0x80,
    'F18': 0x81,
    'F19': 0x82,
    'F20': 0x83,
    'F21': 0x84,
    'F22': 0x85,
    'F23': 0x86,
    'F24': 0x87,
    'num_lock': 0x90,
    'scroll_lock': 0x91,
    'left_shift': 0xA0,
    'right_shift ': 0xA1,
    'left_control': 0xA2,
    'right_control': 0xA3,
    'left_menu': 0xA4,
    'right_menu': 0xA5,
    'browser_back': 0xA6,
    'browser_forward': 0xA7,
    'browser_refresh': 0xA8,
    'browser_stop': 0xA9,
    'browser_search': 0xAA,
    'browser_favorites': 0xAB,
    'browser_start_and_home': 0xAC,
    'volume_mute': 0xAD,
    'volume_Down': 0xAE,
    'volume_up': 0xAF,
    'next_track': 0xB0,
    'previous_track': 0xB1,
    'stop_media': 0xB2,
    'play/pause_media': 0xB3,
    'start_mail': 0xB4,
    'select_media': 0xB5,
    'start_application_1': 0xB6,
    'start_application_2': 0xB7,
    'attn_key': 0xF6,
    'crsel_key': 0xF7,
    'exsel_key': 0xF8,
    'play_key': 0xFA,
    'zoom_key': 0xFB,
    'clear_key': 0xFE,
    '+': 0xBB,
    ',': 0xBC,
    '-': 0xBD,
    '.': 0xBE,
    '/': 0xBF,
    '`': 0xC0,
    ';': 0xBA,
    '[': 0xDB,
    '\\': 0xDC,
    ']': 0xDD,
    "'": 0xDE,
}


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


def get_child_windows(parent):
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


def click_left(x_position=None, y_position=None, sleep=0.1):
    """
    鼠标左键点击指定坐标
    :param x_position: x 点
    :param y_position: y 点
    :param sleep: 点击之后暂停时间
    :return: None
    """
    click("left", x_position=x_position, y_position=y_position, sleep=sleep)


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


def get_qianniu_msg(hwnd):
    x, y, z, c = win32gui.GetWindowRect(hwnd)
    click_left(x, y)
    time.sleep(0.1)
    press_hold_release("ctrl", "a")
    time.sleep(0.1)
    press_hold_release("ctrl", "c")
    text = get_clipboard_txet()
    return text


def get_clipboard_txet():
    win32clipboard.OpenClipboard()
    copytxet = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return str(copytxet)


def get(name):
    handle = win32gui.FindWindow(0, name + ' - 接待中心')
    hwndChildList = get_child_windows(handle)
    for i in hwndChildList:
        cl_name = win32gui.GetClassName(i)
        if cl_name == "Aef_RenderWidgetHostHWND":
            parent_handle = get_parent(i)
            if parent_handle == "SplitterBar":
                time.sleep(1)
                data = get_qianniu_msg(i)
    return data


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


def wangwang_message_send(name, word):
    pid = get_proccess_id('AliIM.exe'.lower())
    app = Application(backend="uia").connect(process=pid[0])
    name = '阿里旺旺 - ' + name
    app[name]['Pane7'].type_keys(word)
    app[name]['Pane7'].type_keys("{ENTER}")
    time.sleep(0.5)
    app[name]['Pane7'].type_keys("{ENTER}")


if __name__ == '__main__':

    m_list = "你好|多少钱|什么快递|什么时候发货|怎么坏了".split("|")
    while True:
        try:
            # time.sleep(5)
            # m_list = get("杜可风按:c").split("\n")
            wangwang_message_send("tb671067_2013:克明", "在吗")
        except Exception as e:
            print(e)
        # for i in get("tb671067_2013:克明").split("\n"):
        #    if i != "\r" and i != '' and "tb671067_2013" not in i:
        #        if i.split(" 已读")[0] not in m_list:
        #            print(i.split(" 已读")[0] + "::" + "消息内容有误")


