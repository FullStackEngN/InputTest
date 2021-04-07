from datetime import datetime
import pyautogui
import random

screenWidth, screenHeight = pyautogui.size()
print("Screen width: " + str(screenWidth) + "; height: " + str(screenHeight))

currentMouseX, currentMouseY = pyautogui.position()
print("Current mouse position X: " +
      str(currentMouseX) + "; Y: " + str(currentMouseY))

current_time = datetime.now()
format_str = "%Y-%m-%d %H:%M:%S"
date_time = current_time.strftime(format_str)
print("Start time: " + date_time)

pyautogui.alert('Please minimize all applications, open Word(or Excel/PowerPoint) in maximize window. Once you click the "OK" button, Then the application will try to type contents in Word(or Excel/PowerPoint)')

# pyautogui.click()
# pyautogui.doubleClick()

# pyautogui.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key

pyautogui.moveTo(screenWidth/2, screenHeight/2)
pyautogui.click()

currentMouseX, currentMouseY = pyautogui.position()
print("Current mouse position X: " +
      str(currentMouseX) + "; Y: " + str(currentMouseY))

mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

x = 0
while x < 10000:
    # type with quarter-second pause in between each key
    #pyautogui.typewrite('nihao2', interval=0.25)

    char1 = random.choice(mylist)
    char2 = random.choice(mylist)
    char3 = random.choice(mylist)

    pyautogui.typewrite(char1 + char2 + char3 + ' ', interval=0.25)

    x += 1

    if(x % 1000 == 0):
        pyautogui.hotkey('ctrl', 'm')
        pyautogui.moveTo(screenWidth/2, screenHeight/2)
        pyautogui.click()

current_time = datetime.now()
date_time = current_time.strftime(format_str)
print("End time: " + date_time)
