from turtle import Screen, Turtle
# from random import randint, choice

S1 = Screen()
S1.bgcolor('black')
S1.tracer(0)    # 取消動畫
width = 500
height = 500
manw = 1
manh = 1
start = (width-width/manw + 30, height-height/manh + 30)
S1.screensize(width, height)


def drawhead(pos, color):
    head = Turtle()
    head.color(color)
    head.fillcolor(color)
    head.penup()
    head.goto(pos)
    # 畫頭
    head.seth(0)
    head.begin_fill()
    head.forward(100)
    head.seth(90)
    head.circle(100, 180)
    head.seth(0)
    head.forward(100)
    head.end_fill()
    head.penup()
    # 畫天線
    head.pen(pensize=5)
    head.forward(25)
    head.circle(50, 75)
    head.pendown()
    head.forward(70)
    head.penup()
    head.goto(pos)
    head.seth(180)
    head.forward(25)
    head.circle(-50, 75)
    head.pendown()
    head.forward(70)
    head.penup()
    head.home()
    head.hideturtle()
    return  # 畫頭


def drawbody(pos, color):
    body = Turtle()
    body.color(color)
    body.fillcolor(color)
    body.penup()
    body.goto(pos[0] + 100, pos[1] - 10)
    body.pendown()
    body.begin_fill()
    for r in range(1, 5):
        body.right(90)
        if r % 2 == 1:
            body.forward(170)
        else:
            body.forward(200)
    body.end_fill()
    body.penup()
    body.goto(pos[0] - 100, pos[1] - 10 - 170)
    body.begin_fill()
    body.pendown()
    body.seth(270)
    body.circle(30, 90)
    body.forward(140)
    body.circle(30, 90)
    body.end_fill()
    body.hideturtle()
    return


def drawlimbs(pos, color):
    limbs = Turtle()
    limbs.color(color)
    limbs.fillcolor(color)
    limbs.pensize(50)  # 手多粗
    # 畫手
    long = 100
    limbs.penup()
    limbs.goto(pos[0] + 130, pos[1] - 60)
    limbs.pendown()
    limbs.seth(70)
    limbs.forward(long)
    limbs.penup()
    limbs.goto(pos[0] - 130, pos[1] - 60)
    limbs.pendown()
    limbs.seth(250)
    limbs.forward(long)
    limbs.penup()
    # 畫腳
    limbs.goto(pos[0] + 15, pos[1] - 170)
    limbs.pendown()
    limbs.seth(-60)
    limbs.forward(100)
    limbs.penup()
    limbs.goto(pos[0] - 50, pos[1] - 170)
    limbs.pendown()
    limbs.seth(-90)
    limbs.forward(90)
    limbs.penup()
    return


def draweyes(pos, color):
    eyes = Turtle()
    eyes.color(color)
    eyes.fillcolor(color)
    eyes.begin_fill()
    eyes.penup()
    eyes.goto(pos[0] + 45, pos[1] + 30)
    eyes.pendown()
    eyes.circle(12)
    eyes.end_fill()
    eyes.penup()
    eyes.goto(pos[0] - 45, pos[1] + 30)
    eyes.begin_fill()
    eyes.pendown()
    eyes.circle(12)
    eyes.end_fill()
    eyes.penup()

    return


a = 'green'
b = 'green'
c = 'green'
d = 'white'

drawlimbs(start, a)
drawhead(start, b)
drawbody(start, c)
draweyes(start, d)

S1.mainloop()
