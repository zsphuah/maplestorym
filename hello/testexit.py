import pyautogui
import time
print "hello"
while True:
    try:
        exit = pyautogui.locateOnScreen(r'img/exit.png')
        if exit is not None:
            print "Fixing profile stuck"
            x, y = pyautogui.center(exit)
            pyautogui.click(x, y)
    except :
        pass