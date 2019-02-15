import pyautogui
import time
print "available"
while True:
    try:
        available = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/available.png')
        if available is not None:
            print "available"
            x, y = pyautogui.center(available)
            pyautogui.click(x, y)
    except:
        pass