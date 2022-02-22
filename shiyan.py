import pyautogui
import time
import pyperclip


img = r'wangyi.png'
clickTimes = 1
lOrR = 'left'
while True:
    location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
    if location is not None:
        pyautogui.click(location.x, location.y, clicks=clickTimes, interval=0.2, duration=0.2, button=lOrR)
        break
    print("未找到匹配图片,0.1秒后重试")
    time.sleep(0.1)