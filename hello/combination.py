import pyautogui
import time
print "hello welcome"
while True:
    #trock
    try:
        trock = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/trock.png')      
        if trock is not None:
            print "rock found!"
            time.sleep(2)
            trock = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/trock.png')            
            if trock is not None:
                print "Teleporting"
                x, y = pyautogui.center(trock)                
                pyautogui.click(x, y)
                time.sleep(5)
   #             pyautogui.press("z")
   #             print"pressing z"
                for i in range (0,20):
                    pyautogui.press("space")
                    pyautogui,press("o")
    except:
        pass
#exit
    try:
        exit = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/exit.png')
        if exit is not None:
            print "Fixing profile stuck"
            x, y = pyautogui.center(exit)
            pyautogui.click(x, y)
    except:
        pass

#complete@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    try:
        complete = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/complete.png')
        if complete is not None:
            print "completing"
            x, y = pyautogui.center(complete)
            pyautogui.click(x, y)
    except:
        pass

#accepting@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    try:
        accept = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/accept.png')
        if accept is not None:
            print "accepting"
            x, y = pyautogui.center(accept)
            pyautogui.click(x, y)
            for i in range (0,20):
                pyautogui.press("space")

    except:
        pass

#reward@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    try:
        reward = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/reward.png')
        if reward is not None:
            print "rewarding"
            x, y = pyautogui.center(reward)
            pyautogui.click(x, y)
            time.sleep(3)
            pyautogui.press("z")
            print"pressing Quest button Z"
            for i in range (0,20):
                pyautogui.press("space")
                pyautogui,press("o")
    except:
        pass

#confirm @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    try:
        confirm = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/confirm.png')
        if confirm is not None:
            print "comfirming"
            x, y = pyautogui.center(comfirm)
            pyautogui.click(x, y)
    except:
        pass

#chinoise@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   try:
 #       chinoise = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/chinoise.png')
 #       if chinoise is not None:
 #           print "chinoise found"
  #          x, y = pyautogui.center(chinoise)
#            pyautogui.click(x, y)
 #   except:
 #       pass

 #skip1
    try:
        skip1 = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/skip.png', confidence=.5)
        if skip1 is not None:
            print "skipping1"
            for i in range (0,20):
                pyautogui.press("space")
  #              pyautogui.press("o")
    except:
        pass

#burning
    try:
        burning = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/burning.png')
        if burning is not None:
            print "burning"
            x, y = pyautogui.press("=")

    except:
        pass