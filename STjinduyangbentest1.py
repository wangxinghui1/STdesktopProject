import time
import pyautogui
print(pyautogui.size())
#进入进度页面
jinduX=411
jinduY=156
pyautogui.moveTo(jinduX,jinduY,0.5)
pyautogui.click(jinduX,jinduY)
#进入样本页面
yangbenjiaX=127
yangbenjiaY=352
pyautogui.moveTo(yangbenjiaX,yangbenjiaY,0.5)
pyautogui.click(yangbenjiaX,yangbenjiaY)
#样本时间区间1点击
shijianX1=629
shijainY1=298
pyautogui.moveTo(shijianX1,shijainY1,0.5)
pyautogui.click(shijianX1,shijainY1)
#样本时间区间2点击
shijianX2=853
shijianY2=298
pyautogui.moveTo(shijianX2,shijianY2,0.5)
pyautogui.click(shijianX2,shijianY2)
#点击流程状态
liuchengzhuangtaiX=110
liuchengzhuangtaiY=110
pyautogui.moveTo(liuchengzhuangtaiX,liuchengzhuangtaiY,0.5)
pyautogui.click(liuchengzhuangtaiX,liuchengzhuangtaiY)
#点击流程状态的测试完成
liuchengzhuangtaiceshiwanchengX=110
liuchengzhuangtaiceshiwanchengy=110
pyautogui.moveTo(liuchengzhuangtaiceshiwanchengX,)
#点击项目
xiangmudianjiX=110
xiangmudianjiY=110
pyautogui.moveTo(xiangmudianjiX,xiangmudianjiY,0.5)
pyautogui.click(xiangmudianjiX,xiangmudianjiY)
#点击测试八项
ceshibaxiangX=110
ceshibaciangY=110
pyautogui.moveTo(ceshibaxiangX,ceshibaciangY,0.5)
pyautogui.click(ceshibaxiangX,ceshibaciangY)
#点击输入搜索关键词按钮
sousuodingweiX=1534
sousuodingweiY=297
pyautogui.moveTo(sousuodingweiX,sousuodingweiY,0.5)
pyautogui.click(sousuodingweiX,sousuodingweiY)
#输入搜索内容
pyautogui.write("ST00001")
#搜索按钮点击
sousuoannuiX=1788
sousuoannuiY=296
pyautogui.moveTo(sousuoannuiX,sousuoannuiY,0.5)
pyautogui.click(sousuoannuiX,sousuoannuiY)
#点击导出按钮
daochuButtonX=1786
daochuButtonY=365
#点击另存为是
lingcunweishiX=1036
lingcunweishiY=635
#点击导出保存按钮
dianjibaocunanX = 782
dianjibaocunanY = 535
#点击另存为取消按钮
lingcunweifouX=1134
lingcunweifouY=636
#点击导出取消按钮
daochuquxiaoX=890
daochuquxiaoY=535
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