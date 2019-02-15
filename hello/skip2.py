import pyautogui
import time
print "skip2"
while True:
    try:
        skip2 = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/skip2.png')
        if skip2 is not None:
            print "skipping2"
            space= pyautogui.center(skip2)
            pyautogui.press("space")
    except:
        pass