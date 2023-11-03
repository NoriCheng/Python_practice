# print(len(COLORS))
# list[...]
# tuple(...)
# dict{k:v,k:v,...}
# str '...' or"..."
# 是可迭代物件即可跑迴圈
# 裡面這些元素怎麼拿來用
# print(type(COLORS))
# print(dir(list()))
from turtle import *
import random as rn
colormode(255)
喜歡的顏色=[]

for a in range(10):
        t=(rn.randint(0,255),rn.randint(0,255),rn.randint(0,255),)
        喜歡的顏色.append(t)

print(喜歡的顏色)

for n,item in enumerate(喜歡的顏色):
        len(喜歡的顏色)-n
        penup()
        goto(10+(len(喜歡的顏色)-n)*10,0)
        seth(90)
        pendown()
        pencolor(item)
        fillcolor(item)
        begin_fill()
        circle(10+(len(喜歡的顏色)-n)*10)
        end_fill()
mainloop()
