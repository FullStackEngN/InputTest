from datetime import datetime
import pyautogui

# 获取屏幕尺寸
screenWidth, screenHeight = pyautogui.size()
print("Screen width: " + str(screenWidth) + "; height: " + str(screenHeight))

# 获取当前坐标位置
currentMouseX, currentMouseY = pyautogui.position()
print("Current mouse position X: " + str(currentMouseX) + "; Y: " + str(currentMouseY))

current_time= datetime.now()
format_str = "%Y-%m-%d %H:%M:%S"
date_time = current_time.strftime(format_str)
print("Start time: " + date_time)

pyautogui.alert('Please minimize all applications, open Word(or Excel/PowerPoint) in maximize window. Once you click the "OK" button, Then the application will try to type contents in Word(or Excel/PowerPoint)')

# 鼠标左击
#pyautogui.click()
# 鼠标双击
# pyautogui.doubleClick()

# 键盘输入Hello world! 间隔为0.25秒
# pyautogui.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key

pyautogui.moveTo(screenWidth/2, screenHeight/2)
pyautogui.click()

# 获取当前坐标位置
currentMouseX, currentMouseY = pyautogui.position()
print("Current mouse position X: " + str(currentMouseX) + "; Y: " + str(currentMouseY))

x = 0
while x < 1000:


    # type with quarter-second pause in between each key
    pyautogui.typewrite('nihao2', interval=0.25)

    pyautogui.typewrite('jintiantianqizenmeyang ', interval=0.25)

    x += 1

current_time= datetime.now()
date_time = current_time.strftime(format_str)
print("End time: " + date_time)
