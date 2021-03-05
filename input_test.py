import pyautogui
# 获取屏幕尺寸
screenWidth, screenHeight = pyautogui.size()
# 获取当前坐标位置
currentMouseX, currentMouseY = pyautogui.position()

print "Start : %s" % time.ctime()

time.sleep(10)

# 鼠标左击
#pyautogui.click()
# 鼠标双击
# pyautogui.doubleClick()

# 键盘输入Hello world! 间隔为0.25秒
# pyautogui.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key

x = 0
while x < 1000:
nihao2nihao2n2nihahao2nihao2ni
    pyautogui.moveTo(currentMouseX/2, currentMouseY/2)

    # type with quarter-second pause in between each key
    pyautogui.typewrite('nihao2', interval=0.25)

    x += 1

print "End : %s" % time.ctime()