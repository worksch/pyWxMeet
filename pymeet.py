# -*- coding: utf-8 -*- 

import win32api
import win32con
import win32gui

import pyautogui
import pyperclip

from pykeyboard import *
from pymouse import *


import win32gui as gui


handle = win32gui.FindWindow('TXGuiFoundation', '成员')
print('%x' % handle)

ctrl=win32gui.FindWindowEx(handle, None,'cchCopied', None)
print(ctrl)

#win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)
'''title = win32gui.GetWindowText(handle)
print(title)

clsname = win32gui.GetClassName(handle)
print(clsname)'''

#
#win32api.SetCursorPos([81,156])    #为鼠标焦点设定一个位置
#win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
#win32api.keybd_event(81,156,win32con.KEYEVENTF_KEYUP,0)  #释放按键
#m = PyMouse()
#k = PyKeyboard()
#m.click(81, 156)
#k.type_string()
#pyperclip.copy('魏绍飞')
#pyautogui.hotkey('ctrl', 'v')  # 再粘贴

#lpszText
#cchTextMax 518 lpszText
#cchCopied: 2 lpszText
#t1=win32gui.GetDlgItem(handle, 10000)
#win32gui.SendMessage(t1,win32con.WM_SETTEXT,None,'902723')