# -*- coding:utf-8 -*-

import win32api
import win32con
import win32clipboard

def set_text_to_clipboard(str=None):
    print('set text :', str)
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_TEXT, str)
    win32clipboard.CloseClipboard()


def ctrl_v():
    win32api.keybd_event(17, 0, 0, 0)
    win32api.keybd_event(86, 0, 0, 0)
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)


def mouse_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 鼠标左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # 鼠标左键放开


def enter():
    win32api.keybd_event(13, 0, 0, 0)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)

# win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,1)  # 此处为鼠标滚动
# win32api.GetCursorPos()  # 获取当前鼠标的位置
