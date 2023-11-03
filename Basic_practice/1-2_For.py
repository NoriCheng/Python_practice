from turtle import *
speed(10)
for i in range(3):  # 控制方形數
     penup()    #起筆
     goto(100+i*50,-100-i*50)    #直接加上位址
     seth(90)   #轉角度
     pendown()  #落筆
     for x in range(4): #控制邊長數
        forward(200+100*i)
        left(90)

mainloop()