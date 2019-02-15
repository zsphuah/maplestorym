import pyautogui
import time
print "dungeon "
while True:

    try:
        cagain = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/Daily Dungeon/picture/cagain.png')
        if cagain is not None:
            print "challenge again"
            x, y = pyautogui.center(cagain)
            pyautogui.click(x, y)
   
            time.sleep(6)
            print "auto battle"
            pyautogui.press("`")

        inchance = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/Daily Dungeon/picture/inchance.png', confidence=.7)
        if inchance is not None:
            print "insufficient tickets"            
            exit = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/Daily Dungeon/picture/exit.png')
            if exit is not None:
                print "dungeon exit"
                x, y = pyautogui.center(exit)
                pyautogui.click(x, y)    
                time.sleep(6)
                print "auto battle"
                pyautogui.press("`")
                 
    except Exception:
        pass


    except Exception:
        pass

    try:
        start = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/Daily Dungeon/picture/start.png')
        if start is not None:
            print "start"
            x, y = pyautogui.center(start)
            pyautogui.click(x, y)
            time.sleep(7)
            print("auto battle")
            pyautogui.press("`")
    except Exception:
       pass

    try: 
        inchance = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/Daily Dungeon/picture/inchance.png', confidence=.7)
        if inchance is not None:
            print "insufficient tickets"            
            dexit = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/Daily Dungeon/picture/dexit.png')
            if dexit is not None:
                print "dungeon exit"
                x, y = pyautogui.center(dexit)
                pyautogui.click(x, y)
    except Exception:
        pass

    try:
        burning = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/Daily Dungeon/picture/burning.png', confidence=.9)
        if burning is not None:
            print "burning"
            pyautogui.press("=")
    except Exception:
        pass