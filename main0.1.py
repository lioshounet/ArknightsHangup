import pyautogui
import time
import pyperclip

#pyautogui库其他用法 https://blog.csdn.net/qingfengxd1/article/details/108270159

# mouseClick(1,"left",img路径,操作选择1234)
def FightClick(clickTimes,lOrR,img):

    location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
    if location is not None:
        pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
        print('点击了' + img)
    else:
        print("未找到" + img +"图片,5秒后重试")
    time.sleep(5)
    location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
    if location is not None:
        pyautogui.click(location.x, location.y, clicks=clickTimes, interval=0.2, duration=0.2, button=lOrR)


def OverClick(clickTimes,lOrR,img):
    OverFlag = 0
    location = pyautogui.locateCenterOnScreen(img,confidence=0.9)
    if location is not None:
        print('over')
        OverFlag = 1

    print("未找到over图片,5秒后重试")
    time.sleep(5)

    location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
    if location is not None:
        print('over')
        OverFlag = 1

#任务
def mainWork():
    while True:
        FightPath = r'FightPath.png'
        BeginPath = r'BeginPath.png'
        chengPath = r'cheng.png'
        OverPath = r'OverPath.png'
        FightClick(1,"left",FightPath)
        FightClick(1, "left", BeginPath)
        FightClick(1, "left", chengPath)
        OverFlag = OverClick(1,"left",OverPath)
        if (OverFlag):
            print('理智没了')
            break

if __name__ == '__main__':

    print('正在进行关卡脚本')
    mainWork()