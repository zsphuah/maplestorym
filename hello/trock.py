#Importing External libraries
import pyautogui
import time

#While true - Means it will run FOREVER
while True:
    #Try = We cant take the risk anything will fail.
    #Incase it will our try and except will catch the problem and will do pass which means nothing and go back to the loop
    try:
        #Looking for the image trock.png
        #Its path to the image!! so it will look for the image in the script folderimgtrock.png
        trock = pyautogui.locateOnScreen(r'imgtrock.png')
        #found
        if trock is not None:
            #sleep for 3 seconds
            time.sleep(3)
            #Look for it again
            trock = pyautogui.locateOnScreen(r'imgtrock.png')
            #Found again
            if trock is not None:
                #Log to the CMD Teleporting
                print Teleporting
                #Calculate the button location
                x, y = pyautogui.center(trock)
                #Click it
                pyautogui.click(x, y)
    except Exception :
        pass
