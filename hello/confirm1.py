import pyautogui
import time
print "cconfirming"
while True:
    try:
        confirming = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/confirm.png')
        if confirming is not None:
            print "comfirming"
            x, y = pyautogui.center(confirming)
            pyautogui.click(x, y)
    except:
        pass