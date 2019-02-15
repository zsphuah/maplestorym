import pyautogui
import time
print "comfirm1"
while True:
    try:
        confirm = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/confirm.png')
        if confirm is not None:
            print "comfirming1"
            x, y = pyautogui.center(comfirm)
            pyautogui.click(x, y)
    except:
        pass