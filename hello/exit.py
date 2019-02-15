#Importing External libraries
import pyautogui
import time
 
#While true - Means it will run FOREVER
print "hello"
while True:

    #Try = We cant take the risk anything will fail.
    #Incase it will our "try" and "except" will catch the problem and will do "pass" which means nothing and go back to the loop
    try:

        #Find the Exit picture over the screen
        exit = pyautogui.locateOnScreen(r'D:/Zhe sean/Desktop/hello/img/exit.png')
        #Exist?
        if exit is not None:
            #Print that
            print "Fixing profile stuck"
            #Find the center
            x, y = pyautogui.center(exit)
            #Click it!
            pyautogui.click(x, y)
    except Exception:
            pass