import pyautogui
import time
print "chinoise"
while True:
    try:
        chinoise = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/chinoise.png')
        if chinoise is not None:
            print "comfirming"
            x, y = pyautogui.center(chinoise)
            pyautogui.click(x, y)
    except:
        pass