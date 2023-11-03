import random
from turtle import Screen, Turtle
# from random import randint, choice

S1 = Screen()
S1.bgcolor('black')
S1.colormode(255)

row = 600
col = 600
turtle_row = int(input("長要幾隻烏龜:"))
turtle_col = int(input("寬要幾隻烏龜:"))
time = int(input("烏龜要轉幾圈:"))
turtle_all = turtle_row * turtle_col
S1.setup(row, col)
count_turtle_num = []
# 建立所有烏龜座標進串列
for col_num in range(turtle_col):
    for row_num in range(turtle_row):
        t = (-row*0.5+row/turtle_row*0.5+row/turtle_row*row_num, col*0.5-col/turtle_col*0.5-col/turtle_col*col_num)
        count_turtle_num.append(t)

print(count_turtle_num)
print(len(count_turtle_num))

# 畫出所有烏龜
Allturtle = []
for n in range(len(count_turtle_num)):
    Allturtle.append(Turtle())
for n in range(len(count_turtle_num)):
    Allturtle[n].color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    Allturtle[n].shape('turtle')
    Allturtle[n].turtlesize(col/turtle_col/50, row/turtle_row/50)
    Allturtle[n].penup()
    Allturtle[n].goto(count_turtle_num[n])
    Allturtle[n].pendown()
n = 0
while True:
    if n < time:
        for spin in range(12):
            for n in range(len(count_turtle_num)):
                Allturtle[n].right(30)
        n += 1
        print('count' + str(time))
    else:
        break

S1.mainloop()
