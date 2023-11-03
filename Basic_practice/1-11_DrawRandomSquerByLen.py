import turtle as tle
import random
tle.colormode(255)
tle.speed(0)
tle.tracer(0) #取消繪製動畫
#固定視窗
high=1000
long=1000
tle.setup(high,long)
#建立25個座標加入串列
allsquare=[]
for x in range(-2,3):
     for y in range(-2,3):         #建立25個元組
        t=(x*high/5,y*long/5) #定義所有方形中心的座標
        allsquare.append(t)     #將25個座標加進串列
print(allsquare)
#繪製剩餘顏色
for square in range(25):
    colorR=random.randint(0,255)
    colorG=random.randint(0,255)
    colorB=random.randint(0,255)
    tle.pencolor(colorR,colorG,colorB)
    tle.fillcolor(colorR,colorG,colorB)
    tle.penup()
    tle.goto(allsquare[square]) #畫筆移至方形左下座標
    tle.seth(0)                 #設定箭頭指向0度
    for pos in range(2):        #前進位置至頂點
        tle.forward(high/10)
        tle.left(90)
    tle.pendown()
    tle.begin_fill()
    for square1 in range(4):#四邊
        tle.forward(high/5)   #定義邊長
        tle.left(90)        #左轉角度
    tle.end_fill()


#查看中心點
tle.penup()
tle.pencolor('blue')
tle.home()
tle.pendown()

tle.mainloop()