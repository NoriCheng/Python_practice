import turtle as tle
import random
tle.colormode(255)
tle.speed(0)
tle.tracer(0) #取消繪製動畫
#固定視窗
# def square():
#     tle.pendown()
#     tle.begin_fill()
#     return

high=650
long=650
tle.setup(high,long)
allsquare=[]
#建立25個座標加入串列
for x in range(-2,3):
     for y in range(-2,3):         #建立25個元組
        t=(x*high/5,y*long/5) #定義所有方形中心的座標
        allsquare.append(t)     #將25個座標加進串列
print(allsquare)
#繪製特殊顏色
tle.pencolor(50,50,0)
tle.fillcolor(50,50,0)
tle.penup()
tle.goto(allsquare.pop(random.randint(0,25))) #隨機選擇串列其中一個座標並取出
tle.seth(0) #設定箭頭指向0度
for pos in range(2): #前進位置至頂點
    tle.forward(50)
    tle.left(90)
tle.pendown()
tle.begin_fill()
for square0 in range(4):#四邊
    tle.forward(100)       #定義邊長
    tle.left(90)            #左轉角度
tle.end_fill()
#繪製剩餘顏色
tle.pencolor(50,100,0)
tle.fillcolor(50,100,0)

for square in range(24):
        tle.penup()
        tle.goto(allsquare[square]) #畫筆移至方形左下座標
        tle.seth(0)                 #設定箭頭指向0度
        for pos in range(2):        #前進位置至頂點
            tle.forward(50)
            tle.left(90)
        tle.pendown()
        tle.begin_fill()
        for square1 in range(4):#四邊
                tle.forward(100)   #定義邊長
                tle.left(90)        #左轉角度
        tle.end_fill()


#查看中心點
tle.penup()
tle.pencolor('blue')
tle.home()
tle.pendown()

tle.mainloop()
