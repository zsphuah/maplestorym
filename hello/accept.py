import pyautogui
import time
print "accept"
while True:
    try:
        accept = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/accept.png')
        if accept is not None:
            print "accepting"
            x, y = pyautogui.center(accept)
            pyautogui.click(x, y)
    except:
        pass