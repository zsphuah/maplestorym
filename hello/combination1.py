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

                for i in range (0,20):
                    pyautogui.press("space")
                    pyautogui.press("o")
    except Exception:
        pass
#exit
 
#complete@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    try:
        complete = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/complete.png')
        if complete is not None:
            print "completing"
            x, y = pyautogui.center(complete)
            pyautogui.click(x, y)
    except Exception:
        pass
                     
#accepting@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    try:
        accept = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/accept.png')
        if accept is not None:
            print "accepting"
            x, y = pyautogui.center(accept)
            pyautogui.click(x, y)
#            for i in range (0,20):
 #s               pyautogui.press("space")

    except Exception:
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
                pyautogui.press("o")
    except Exception:
        pass

#confirm @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    try:
        confirm = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/confirm.png')
        if confirm is not None:
            print "comfirming"
            pyautogui.press("o")
    except Exception:
        pass
  
 #skip1
    try:
        skip1 = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/skip.png', confidence=.8)
        if skip1 is not None:
            print "skipping"
            for i in range (0,20):
                pyautogui.press("space")
            pyautogui.press("o")
    except Exception:
        pass

#burning
    try:
        burning = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/burning.png',confidence=9)
        if burning is not None:
            print "burning"
            pyautogui.press("=")
    except Exception:
        pass

#available
    try:
        available = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/available.png')
        if available is not None:
            print "available"
            x, y = pyautogui.center(available)
            pyautogui.click(x, y)
    except Exception:
        pass



#revive @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    try:
        revive = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/revive.png')
        if revive is not None:
            print "revive"
            x,y=pyautogui.center(revive)
            pyautogui.click(x,y)
            time.sleep(5)
            print"pressing Quest Z"
            pyautogui.press("z")
            
    except Exception:
        pass