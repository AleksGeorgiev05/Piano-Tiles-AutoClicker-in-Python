from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32con
import win32api

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    #Tile 1
    if pyautogui.pixel(1411, 770)[0] == 0:
        click(1411, 770)
    #Tile 2
    if pyautogui.pixel(1617, 770)[0] == 0:
        click(1617, 770)
    #Tile 3
    if pyautogui.pixel(1816, 770)[0] == 0:
        click(1816, 770)
    #Tile 4
    if pyautogui.pixel(2033, 770)[0] == 0:
        click(2033, 770)