import pyautogui
import time
print "skip3"
while True:
    try:
        skip3 = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/skip3.png')
        if skip3 is not None:
            print "skipping3"
            space= pyautogui.center(skip)
            pyautogui.press("space")
    except:
        pass