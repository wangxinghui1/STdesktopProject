import pyautogui
print(pyautogui.size())
#进入进度页面
jinduX=411
jinduY=156
pyautogui.moveTo(jinduX,jinduY,0.5)
pyautogui.click(jinduX,jinduY)
#进入样本架页面
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
i=0
baocun=0
#导出按钮点击保存
while baocun>5:
    baocun=baocun+1
    daochuannuiX=1788
    daochuannuiY=351
    pyautogui.moveTo(daochuannuiX,daochuannuiY,0.5)
    pyautogui.click(daochuannuiX,daochuannuiY)
    if i>1:
        #点击另存为按钮
        lingcunweishiX=11
        lingcunweishiY=11
        pyautogui.moveTo(lingcunweishiX,lingcunweishiY,0.5)
        pyautogui.click(lingcunweishiX,lingcunweishiY)
        i=i+1
    #     break
    # #导出按钮点击保存
    # daochuannuiX=1788
    # daochuannuiY=351
    # pyautogui.moveTo(daochuannuiX,daochuannuiY,0.5)
    # pyautogui.click(daochuannuiX,daochuannuiY)
    if i>i+2:
        #点击否按钮
        lingcunweifouX=11
        lingcunweifouY=11
        pyautogui.moveTo(lingcunweifouX,lingcunweifouY,0.5)
        pyautogui.click(lingcunweifouX,lingcunweifouY)
#直接点击保存按钮
dianjibaocunanX=11
dianjibaocunanY=11
pyautogui.moveTo(dianjibaocunanX,dianjibaocunanY,0.5)
pyautogui.click(dianjibaocunanX,dianjibaocunanY)
#点击取消按钮
dianjiquxiaoannuiX=11
dianjiquxiaoannuiY=11
pyautogui.moveTo(dianjiquxiaoannuiX,dianjiquxiaoannuiY,0.5)
pyautogui.click(dianjibaocunanX,dianjibaocunanY)

#另存为点击保存
#确定替换
baocuntihuanX=961
baocuntihuanY=623

#导出按钮取消点击
quxiaoX=1469
quxiaoY=930
pyautogui.moveTo(quxiaoX,quxiaoY,0.5)
pyautogui.click(quxiaoX,quxiaoY)
#保存点击
baocunX=1099
baocunY=752
pyautogui.moveTo(baocunX,baocunY,0.5)
pyautogui.click(baocunX,baocunY)
#导出按钮点击
daochuannuiX=1788
daochuannuiY=351
pyautogui.moveTo(daochuannuiX,daochuannuiY,0.5)
pyautogui.click(daochuannuiX,daochuannuiY)
#导出按钮取消点击
quxiaoX=1469
quxiaoY=930
pyautogui.moveTo(quxiaoX,quxiaoY,0.5)
pyautogui.click(quxiaoX,quxiaoY)
#打印按钮点击
dayinannuiX=1785
daochuannuiY=402
pyautogui.moveTo(daochuannuiX,daochuannuiY,0.5)
pyautogui.click(daochuannuiX,daochuannuiY)
#打印点击确定按钮
dayinquedingX=301
dayinquedingY=521
pyautogui.moveTo(dayinquedingX,dayinquedingY,0.5)
pyautogui.click(dayinquedingX,dayinquedingY)
#打印按钮点击
dayinannuiX=1785
daochuannuiY=402
pyautogui.moveTo(daochuannuiX,daochuannuiY,0.5)
pyautogui.click(daochuannuiX,daochuannuiY)
#打印取消
dayinquxiaoX=404
dayinquxiaoY=522
pyautogui.moveTo(dayinquxiaoX,dayinquxiaoY,0.5)
pyautogui.click(dayinquxiaoX,dayinquxiaoY)




