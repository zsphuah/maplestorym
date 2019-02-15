import pyautogui
import time
print "reward"
while True:
    try:
        reward = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/reward.png')
        if reward is not None:
            print "rewarding"
            x, y = pyautogui.center(reward)
            pyautogui.click(x, y)
    except:
        pass