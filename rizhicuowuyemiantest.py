import time
import pyautogui
print(pyautogui.size())
#进入日志页面
rizhiX=
rizhiY=
pyautogui.moveTo(rizhiX,rizhiY,0.5)
pyautogui.click(rizhiX,rizhiY)
#进入错误页面
cuowuX=
cuowuY=
pyautogui.moveTo(cuowuX,cuowuY,0.5)
pyautogui.click(cuowuX,cuowuY)
#样本时间区间1点击
shijianX1=
shijainY1=
pyautogui.moveTo(shijianX1,shijainY1,0.5)
pyautogui.click(shijianX1,shijainY1)
#样本时间区间2点击
shijianX2=
shijianY2=
pyautogui.moveTo(shijianX2,shijianY2,0.5)
pyautogui.click(shijianX2,shijianY2)
#点击模块状态
mokuaizhuangtaidianjiX=
mokuaizhuangtaidianjiY=
pyautogui.moveTo(mokuaizhuangtaidianjiX,mokuaizhuangtaidianjiY,0.5)
pyautogui.click(mokuaizhuangtaidianjiX,mokuaizhuangtaidianjiY)
#点击警告页面的进样检测按钮
jinyangjianceannuiX=
jinyangjianceannuiY=
pyautogui.moveTo(jinyangjianceannuiX,jinyangjianceannuiY,0.5)
pyautogui.click(jinyangjianceannuiX,jinyangjianceannuiY)
#点击输入搜索关键词按钮
sousuodingweiX=
sousuodingweiY=
pyautogui.moveTo(sousuodingweiX,sousuodingweiY,0.5)
pyautogui.click(sousuodingweiX,sousuodingweiY)
#输入搜索内容
pyautogui.write("ST00001")
#搜索按钮点击
sousuoannuiX=
sousuoannuiY=
pyautogui.moveTo(sousuoannuiX,sousuoannuiY,0.5)
pyautogui.click(sousuoannuiX,sousuoannuiY)
#点击导出按钮
daochuButtonX=
daochuButtonY=
#点击另存为是
lingcunweishiX=
lingcunweishiY=
#点击导出保存按钮
dianjibaocunanX =
dianjibaocunanY =
#点击另存为取消按钮
lingcunweifouX=
lingcunweifouY=
#点击导出取消按钮
daochuquxiaoX=
daochuquxiaoY=
i=0
for i in range(10):
    pyautogui.moveTo(daochuButtonX,daochuButtonY,0.5)
    pyautogui.click(daochuButtonX,daochuButtonY)
    time.sleep(1)
    print("第%d"%i+"次点击导出按钮")
    if i >= 1:
        #点击保存按钮
        pyautogui.moveTo(dianjibaocunanX, dianjibaocunanY, 0.5)
        pyautogui.click(dianjibaocunanX, dianjibaocunanY)
        time.sleep(1)
        # 点击另存为按钮
        pyautogui.moveTo(lingcunweifouX,lingcunweifouY,0.5)
        pyautogui.click(lingcunweifouX,lingcunweifouY)
        print("第一次点击另存为否按钮")
        time.sleep(1)
        #点击导出取消按钮
        pyautogui.moveTo(daochuquxiaoX,daochuquxiaoY,0.5)
        pyautogui.click(daochuquxiaoX,daochuquxiaoY)
        time.sleep(1)
    else:
        # 直接点击保存按钮
        print("第一次直接点保存按钮")
        pyautogui.moveTo(dianjibaocunanX,dianjibaocunanY,0.5)
        pyautogui.click(dianjibaocunanX,dianjibaocunanY)
        time.sleep(1)
    i = i+1
    #另存为取消按钮
for j in range(10):
        pyautogui.moveTo(daochuButtonX, daochuButtonY, 0.5)
        pyautogui.click(daochuButtonX, daochuButtonY)
        time.sleep(1)
        print("第%d" % i + "次点击导出按钮")
        if j >= 1:
            # 点击保存按钮
            pyautogui.moveTo(dianjibaocunanX, dianjibaocunanY, 0.5)
            pyautogui.click(dianjibaocunanX, dianjibaocunanY)
            time.sleep(1)

            # 点击另存否按钮
            pyautogui.moveTo(lingcunweishiX, lingcunweishiY, 0.5)
            pyautogui.click(lingcunweishiX, lingcunweishiY)
            time.sleep(1)

            print("第一次点击另存为按钮")
        else:
            # 直接点击保存按钮
            print("第一次直接点保存按钮")
            pyautogui.moveTo(dianjibaocunanX, dianjibaocunanY, 0.5)
            pyautogui.click(dianjibaocunanX, dianjibaocunanY)
            time.sleep(1)
        j = j + 1