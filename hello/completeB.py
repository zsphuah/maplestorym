import pyautogui
import time
print "completeB"
while True:
    try:
        completeB = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/completeB.png')
        if available is not None:
            print "completeB"
            x, y = pyautogui.center(completeB)
            pyautogui.click(x, y)
    except:
        pass