import pyautogui
import time
print "dungeon "
while True:

    try:
		exit = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/Daily Dungeon/picture/exit.png')
		print"hello123"
		if exit is not None:
			print"hello"
			x,y=pyautogui.center(exit)
			pyautogui.click(x,y)
    except Exception:
        pass