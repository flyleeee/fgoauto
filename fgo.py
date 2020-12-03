import pyautogui as p
import time
import random
import win32gui
import win32con
import win32com.client
from PyQt5 import QtCore, QtGui, QtWidgets
from fgoui import Ui_MainWindow as UI
import sys


def findwindow(x):
    #这个是可以偷懒几秒的函数，就是在你运行程序以后直接切到fgo的窗口，但是需要提前知道窗口的句柄
    #当时只是为了好玩而实现，可以在开头多sleep几秒并删掉这个函数
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.ShowWindow(x, win32con.SW_SHOWNORMAL)
    win32gui.SetForegroundWindow(x)


def find_and_click(image):
    #寻找并点击这张图片的位置
    x, y = p.locateCenterOnScreen(image, confidence=0.9)
    p.click(x, y)


def fclicks(x1, y1, x2, y2):
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)
    p.click(x, y)
    time.sleep(random.uniform(3.5, 4.2))


def aclicks(x1, y1, x2, y2):
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)
    p.click(x, y)
    time.sleep(random.uniform(0.5, 1.2))


def rclick(x1, y1, x2, y2):
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)
    p.click(x, y)
    time.sleep(random.uniform(0.5, 1.2))


def masterskill(skill, servent, yn):  
    #礼装技能，第三个变量设为'y'则为第'servent'号从者释放，否则默认为全体技能
    aclicks(x1=1557, y1=441, x2=1610, y2=488)
    if skill == 1:
        aclicks(x1=1239, y1=439, x2=1285, y2=484)
    elif skill == 2:
        aclicks(x1=1336, y1=440, x2=1381, y2=486)
    elif skill == 3:
        aclicks(x1=1440, y1=443, x2=1482, y2=483)
    if yn == 'y':
        if servent == 1:
            fclicks(x1=570, y1=557, x2=682, y2=693)
        elif servent == 2:
            fclicks(x1=874, y1=525, x2=1011, y2=690)
        elif servent == 3:
            fclicks(x1=1220, y1=512, x2=1402, y2=695)
    else:
        time.sleep(random.uniform(3.5, 4.2))


def rmove(x1, y1, x2, y2): 
    #移动鼠标到指定范围 
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)
    p.moveTo(x, y)

def findce(image):
    #寻找礼装
    findfail = r'.\images\findfail.png'
    findfail2 = r'.\images\findfail2.png'
    while p.locateCenterOnScreen(findfail, confidence=0.9) is not None:
        aclicks(x1=1180, y1=237, x2=1224, y2=276)
        aclicks(x1=1082, y1=733, x2=1284, y2=764)
        aclicks(x1=921, y1=734, x2=988, y2=753)
        time.sleep(random.uniform(3, 4))
    rmove(x1=343, y1=363, x2=1449, y2=481)
    start1 = time.perf_counter()
    while p.locateCenterOnScreen(image, confidence=0.9) is None:
        time.sleep(random.uniform(0.1, 0.2))
        p.scroll(-1)

        if int(time.perf_counter()) - start1 > 8:
            aclicks(x1=1180, y1=237, x2=1224, y2=276)
            if p.locateCenterOnScreen(findfail2, confidence=0.9) is not None:
                aclicks(x1=921, y1=734, x2=988, y2=753)
            else:
                aclicks(x1=1082, y1=733, x2=1284, y2=764)

            rmove(x1=343, y1=363, x2=1449, y2=481)
            time.sleep(random.uniform(1, 2))
            start1 = time.perf_counter()
    x, y = p.locateCenterOnScreen(image, confidence=0.9)
    p.click(x, y - random.uniform(75, 85))


def aoe(x):
    if x == 1:
        aclicks(x1=650, y1=260, x2=779, y2=392)  # 一号位宝具
    elif x == 2:
        aclicks(x1=919, y1=278, x2=1025, y2=390)  # 二号位宝具
    elif x == 3:
        aclicks(x1=1182, y1=261, x2=1294, y2=414)  # 三号位宝具


def attackcard(x):
    #选择第二张或第三张指令卡，反正都靠光炮，所以这都是乱选的
    if x == 1:
        aclicks(x1=320, y1=596, x2=432, y2=745)  # 一号a
    elif x == 2:
        aclicks(x1=615, y1=602, x2=724, y2=734)  # 二号a


def skill(x, y):
    if x == 1:
        if y == 1:
            fclicks(x1=292, y1=732, x2=339, y2=774)  # 一号位一技能
        elif y == 2:
            fclicks(x1=401, y1=740, x2=449, y2=784)
        elif y == 3:
            fclicks(x1=504, y1=733, x2=547, y2=768)  # 一号位三技能
    elif x == 2:
        if y == 1:
            fclicks(x1=657, y1=733, x2=692, y2=762)  # 二号位一技能
        elif y == 2:
            fclicks(x1=761, y1=741, x2=801, y2=777)
        elif y == 3:
            fclicks(x1=861, y1=728, x2=905, y2=772)  # 二号位三技能
    elif x == 3:
        if y == 1:
            fclicks(x1=1013, y1=725, x2=1057, y2=768)  # 三号位一技能
        elif y == 2:
            fclicks(x1=1119, y1=728, x2=1156, y2=772)  # 三号位二技能
        elif y == 3:
            fclicks(x1=1223, y1=730, x2=1261, y2=771)  # 三号位三技能


def selectteam(image):
    #选择是第几个队伍出战
    while p.locateCenterOnScreen(image, confidence=0.9) is None:
        aclicks(x1=1654, y1=535, x2=1654, y2=535)


def startfrom_icon(icon):
    #选择点击开始那个关卡的图片
    if p.locateCenterOnScreen(icon, confidence=0.95) is None:
        aclicks(x1=1339, y1=837, x2=1603, y2=894)
        time.sleep(1)
    find_and_click(icon)
    time.sleep(3)


def gan(self):
    x = win32gui.FindWindow('Qt5QWindowIcon', '命运-冠位指定 - MuMu模拟器') #如果你并不是在MuMu模拟器上运行fgo，请将这一行删掉
    fgologo = r'.\images\fgologo.png'
    startmission = r'.\images\startmission.png'
    event = r'.\images\event.png'
    qp = r'.\images\qp.png'
    attack = r'.\images\attack.png'
    ce3 = r'.\images\ce3.png'
    ce1 = r'.\images\ce1.png'
    ce2 = r'.\images\ce2.png'
    add = r'.\images\add.png'
    qpce = r'.\images\qpce.png'
    findfail = r'.\images\findfail.png'
    part1 = r'.\images\part1.png'
    team9 = r'.\images\team9.png'
    findfail2 = r'.\images\findfail2.png'
    continueToFight = r'.\images\continueToFight.png'


    start = time.perf_counter()
    ap = int(ui.lineEdit.text())
    cost = 40
    findwindow(x)  #如果你并不是在MuMu模拟器上运行fgo，请将这一行删掉，并适当提高下一行的sleep时间

    time.sleep(1)
    for x in range(200):
        startfrom_icon(qp)

        if ap < cost:
            rclick(x1=725, y1=473, x2=1230, y2=490)  # 吃苹果
            time.sleep(random.uniform(3, 3.5))
            rclick(x1=1074, y1=724, x2=1275, y2=746)
            ap += 139
            time.sleep(random.uniform(3, 3.5))

        findce(qpce)

        time.sleep(random.uniform(3, 3.5))
        if x == 0:
            selectteam(team9)

        find_and_click(startmission)

        time.sleep(10)
        # ================第一面==============
        while p.locateCenterOnScreen(attack, confidence=0.9) is None:
            time.sleep(1.5)
        
        skill(2, 1)
        skill(3, 3)
        

        aclicks(x1=1477, y1=740, x2=1543, y2=816)
        time.sleep(random.uniform(1.5, 2))
        aoe(2)
        attackcard(1)
        attackcard(2)
        time.sleep(10)
        # ===============第二面==============
        while p.locateCenterOnScreen(attack, confidence=0.9) is None:
            time.sleep(1.5)

        # masterskill(2,3,'y')

        aclicks(x1=1477, y1=740, x2=1543, y2=816)
        time.sleep(random.uniform(1.5, 2))
        aoe(3)

        attackcard(1)
        attackcard(2)
        time.sleep(5)

        # ====================第三面================
        while p.locateCenterOnScreen(attack, confidence=0.9) is None:
            time.sleep(1.5)

        aclicks(x1=1477, y1=740, x2=1543, y2=816)
        time.sleep(random.uniform(1.5, 2))
        aoe(1)
        attackcard(1)
        attackcard(2)
        time.sleep(12)
        while p.locateCenterOnScreen(part1, confidence=0.9) is None:
            time.sleep(1.5)
        time.sleep(random.uniform(1.5, 2))
        rclick(x1=349, y1=191, x2=1575, y2=826)
        time.sleep(random.uniform(4, 4.5))
        rclick(x1=349, y1=191, x2=1575, y2=826)
        time.sleep(random.uniform(4, 4.5))
        aclicks(x1=1339, y1=837, x2=1603, y2=894)
        time.sleep(random.uniform(2, 2.5))
        if p.locateCenterOnScreen(add, confidence=0.9) is not None:
            aclicks(x1=477, y1=784, x2=732, y2=827)
        time.sleep(random.uniform(8, 8.5))

        ap -= cost
        if time.perf_counter() - start > 300:
            ap += 1
            start -= 300


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    widgets = QtWidgets.QMainWindow()

    
    ui = UI()
    ui.setupUi(widgets)
    ui.pushButton.clicked.connect(gan)
    widgets.show()

    sys.exit(app.exec_())
