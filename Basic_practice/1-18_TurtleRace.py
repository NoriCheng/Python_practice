from turtle import Screen, Turtle
from random import randint, choice

def allturtle(Tname, Tcolor,road):
    Tname=Turtle()
    Color=['red', 'blue', 'orange', 'yellow', 'purple', 'purple']
    Tname.goto=(road)

screen = Screen()

drawT = Turtle()
drawT.hideturtle()
drawT.speed('fastest')
drawT.penup()

drawT.goto(-300,140)

for step in range(15):
    drawT.write(step, align='center', font=('Arial', 8, 'normal'))
    drawT.right(90)    # 轉向跑線
    drawT.forward(10)  # 離開數字10格
    drawT.pendown()
    drawT.forward(400)     # 劃出400的線
    drawT.penup()
    drawT.backward(410)
    drawT.left(90)
    drawT.forward(50)  # 每隔間距


turtle_h, turtle_l = 3, 3   #烏龜大小
roy = Turtle()
roy.color('red')
roy.shape('turtle')
roy.turtlesize(turtle_h, turtle_l)

roy.penup()
roy.goto(-350, 100)
roy.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')
bob.turtlesize(turtle_h, turtle_l)

bob.penup()
bob.goto(-350, 40)
bob.pendown()

oreo = Turtle()
oreo.color('orange')
oreo.shape('turtle')
oreo.turtlesize(turtle_h, turtle_l)

oreo.penup()
oreo.goto(-350, -20)
oreo.pendown()

yay = Turtle()
yay.color('yellow')
yay.shape('turtle')
yay.turtlesize(turtle_h, turtle_l)

yay.penup()
yay.goto(-350, -80)
yay.pendown()

go = Turtle()
go.color('green')
go.shape('turtle')
go.turtlesize(turtle_h, turtle_l)

go.penup()
go.goto(-350, -140)
go.pendown()

lis = Turtle()
lis.color('purple')
lis.shape('turtle')
lis.turtlesize(turtle_h, turtle_l)

lis.penup()
lis.goto(-350, -200)
lis.pendown()


while True:
    racer = choice([roy, bob, oreo, yay, go, lis])
    racer.forward(randint(10, 50))

    if racer.xcor() > 410:  # 回傳X座標
        racer.setheading(180)
    elif racer.xcor() < -350:
        break  # we have a winner!


screen.mainloop()
