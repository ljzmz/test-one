#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2019/11/5 10:09
# @Author : "zhy"
import win32api
import win32con
import time

# 键盘编码
V_CODE = {
    "A": "65",
    "B": "66",
    "C": "67",
    "D": "68",
    "E": "69",
    "F": "70",
    "G": "71",
    "H": "72",
    "I": "73",
    "J": "74",
    "K": "75",
    "L": "76",
    "M": "77",
    "N": "78",
    "O": "79",
    "P": "80",
    "Q": "81",
    "R": "82",
    "S": "83",
    "T": "84",
    "U": "85",
    "V": "86",
    "W": "87",
    "X": "88",
    "Y": "89",
    "Z": "90",
    "0": "48",
    "1": "49",
    "2": "50",
    "3": "51",
    "4": "52",
    "5": "53",
    "6": "54",
    "7": "55",
    "8": "56",
    "9": "57",
    # "0": "96",
    # "1": "97",
    # "2": "98",
    # "3": "99",
    # "4": "100",
    # "5": "101",
    # "6": "102",
    # "7": "103",
    # "8": "104",
    # "9": "105",
    "*": "106",
    "+": "107",
    # "Enter": "108",
    "-": "109",
    ".": "110",
    "/": "111",
    "F1": "112",
    "F2": "113",
    "F3": "114",
    "F4": "115",
    "F5": "116",
    "F6": "117",
    "F7": "118",
    "F8": "119",
    "F9": "120",
    "F10": "121",
    "F11": "122",
    "F12": "123",
    "Backspace": "8",
    "Tab": "9",
    "Clear": "12",
    "Enter": "13",
    "Shift": "16",
    "Control": "17",
    "Alt": "18",
    "CapsLock": "20",
    "Esc": "27",
    "Spacebar": "32",
    "PageUp": "33",
    "PageDown": "34",
    "End": "35",
    "Home": "36",
    "LeftArrow": "37",
    "UpArrow": "38",
    "RightArrow": "39",
    "DownArrow": "40",
    "Insert": "45",
    "Delete": "46",
    "Help": "47",
    "NumLock": "144",
}

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


def click_key_bord(j):
    win32api.keybd_event(int(V_CODE[j]), 0, 0, 0)
    time.sleep(0.05)
    win32api.keybd_event(int(V_CODE[j]), 0, win32con.KEYEVENTF_KEYUP, 0)


if __name__ == '__main__':
    print("开始执行脚本")
    time.sleep(10)
    k8s_list = ["k8s-worker-new2-test001", "k8s-worker-new2-test002", "k8s-worker-new2-test003",
                "k8s-worker-new2-test004", "k8s-worker-new2-test005", "k8s-worker-new2-test006",
                "k8s-worker-new2-test007", "k8s-worker-new2-test008"]
    k8s_list2 = ['k8s-worker-new3-test001', 'k8s-worker-new3-test002', 'k8s-worker-new3-test003',
                 'k8s-worker-new3-test004', 'k8s-worker-new3-test005', 'k8s-worker-new3-test006',
                 'k8s-worker-new3-test007', 'k8s-worker-new3-test008', 'k8s-worker-new3-test009',
                 'k8s-worker-new3-test010', 'k8s-worker-new3-test011', 'k8s-worker-new3-test012',
                 'k8s-worker-new3-test013', 'k8s-worker-new3-test014', 'k8s-worker-new3-test015',
                 'k8s-worker-new3-test016', 'k8s-worker-new3-test017', 'k8s-worker-new3-test018',
                 'k8s-worker-new3-test019', 'k8s-worker-new3-test020', 'k8s-worker-new3-test021',
                 'k8s-worker-new3-test022', 'k8s-worker-new3-test023', 'k8s-worker-new3-test024',
                 'k8s-worker-new3-test025', 'k8s-worker-new3-test026', 'k8s-worker-new3-test027',
                 'k8s-worker-new3-test028', 'k8s-worker-new3-test029', 'k8s-worker-new3-test030',
                 'k8s-worker-new3-test031', 'k8s-worker-new3-test032', 'k8s-worker-new3-test033',
                 'k8s-worker-new3-test034', 'k8s-worker-new3-test035', 'k8s-worker-new3-test036',
                 'k8s-worker-new3-test037', 'k8s-worker-new3-test038', 'k8s-worker-new3-test039',
                 'k8s-worker-new3-test040']
    for i in k8s_list:
        for j in i.upper():
            click_key_bord(j)
        click_key_bord("Enter")
        time.sleep(0.5)
        click_key_bord("1")
        click_key_bord("Enter")
        time.sleep(3)
        for j in "killall":
            click_key_bord(j.upper())
        click_key_bord("Spacebar")
        for j in "locust":
            if j == "_":
                press_hold_release("shift", '-')
            else:
                click_key_bord(j.upper())
        click_key_bord("Enter")
        for j in "cd":
            click_key_bord(j.upper())
        click_key_bord("Spacebar")
        for j in "/opt/xiaoduo-tester/scripts/robot_performance":
            if j == "_":
                press_hold_release("shift", '-')
            else:
                click_key_bord(j.upper())
        click_key_bord("Enter")
        for j in "sh":
            click_key_bord(j.upper())
        click_key_bord("Spacebar")
        for j in "tt.sh":
            click_key_bord(j.upper())
        click_key_bord("Spacebar")
        for j in "5":
            click_key_bord(j.upper())
        click_key_bord("Enter")
        time.sleep(2)
        for j in "exit":
            click_key_bord(j.upper())
        click_key_bord("Enter")

    print("滴滴滴")
    for i in k8s_list2:
        for j in i.upper():
            click_key_bord(j)
        click_key_bord("Enter")
        time.sleep(0.5)
        click_key_bord("1")
        click_key_bord("Enter")
        time.sleep(3)
        for j in "killall":
            click_key_bord(j.upper())
        click_key_bord("Spacebar")
        for j in "locust":
            if j == "_":
                press_hold_release("shift", '-')
            else:
                click_key_bord(j.upper())
        click_key_bord("Enter")
        for j in "cd":
            click_key_bord(j.upper())
        click_key_bord("Spacebar")
        for j in "/opt/xiaoduo-tester/robot_performance":
            if j == "_":
                press_hold_release("shift", '-')
            else:
                click_key_bord(j.upper())
        click_key_bord("Enter")
        for j in "sh":
            click_key_bord(j.upper())
        click_key_bord("Spacebar")
        for j in "tt.sh":
            click_key_bord(j.upper())
        click_key_bord("Spacebar")
        for j in "5":
            click_key_bord(j.upper())
        click_key_bord("Enter")
        time.sleep(2)
        for j in "exit":
            click_key_bord(j.upper())
        click_key_bord("Enter")
        time.sleep(1)


