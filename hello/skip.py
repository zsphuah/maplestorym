import pyautogui
import time
print "skip"
while True:
    try:
        skip1 = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/skip.png')
        if skip1 is not None:
            print "skipping1"
            x,y=pyautogui.center(skip1)
            pyautogui.click(x.y)
    except:
        pass