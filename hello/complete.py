import pyautogui
import time
print "complete"
while True:
    try:
        complete = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/complete.png')
        if complete is not None:
            print "completing"
            x, y = pyautogui.center(complete)
            pyautogui.click(x, y)
    except:
        pass