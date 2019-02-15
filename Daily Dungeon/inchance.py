import pyautogui
import time
print "inchance test "
while True:

    try: 
		inchance = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/Daily Dungeon/picture/inchance.png', confidence=.7)
		if inchance is not None:
			print "insufficient tickets"       		
			exit = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/Daily Dungeon/picture/exit.png')
			if exit is not None:
				print "dungeon exit"
				x, y = pyautogui.center(exit)
				pyautogui.click(x, y)
    except Exception:
        pass
    