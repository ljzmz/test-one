#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2019/9/29 10:37
# @Author : "zhy"
import win32api
from ctypes import *

from config.globalparam import pro_ini_path
from local_lib.common import readconfig


# dll_path = 'C:\\QNCefWorker.dll'.encode('ascii', 'ignore')
read = readconfig.ReadConfig(pro_ini_path)
dll_path = read.getValue('projectConfig', 'dll_path').encode('ascii', 'ignore')


def injectDll(pid, string=None):
    print("---------------------------------start inject QNCefWorker.dll----------------------------------------------")
    PAGE_READWRITE = 0x04
    PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)
    VIRTUAL_MEM = (0x1000 | 0x2000)

    dll_len = len(dll_path)
    print(dll_len)
    kernel32 = windll.kernel32

    h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, int(pid))
    if not h_process:
        print('could not acquire a handle to pid')

    arg_adress = kernel32.VirtualAllocEx(h_process, None, dll_len, VIRTUAL_MEM, PAGE_READWRITE)
    written = c_int(0)
    whhh = kernel32.WriteProcessMemory(h_process, arg_adress, dll_path, dll_len, byref(written))
    print('arg_address:%x' % arg_adress, whhh)

    h_kernel32 = win32api.GetModuleHandle('kernel32.dll')
    h_loadlib = win32api.GetProcAddress(h_kernel32, 'LoadLibraryA')
    print('%x' % h_kernel32, '%x' % h_loadlib)
    thread_id = c_ulong(0)
    handle = kernel32.CreateRemoteThread(h_process, None, 0, h_loadlib, arg_adress, 0, byref(thread_id))
    print(handle)
    print("-----------------------------------end inject QNCefWorker.dll----------------------------------------------")
    return h_kernel32


if __name__ == '__main__':
    injectDll(31756)
