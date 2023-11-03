import turtle
turtle.color('red')
turtle.fillcolor('yellow')
turtle.begin_fill()

while True:
    turtle.forward(200)
    turtle.left(170)
    print(turtle.pos())
    if abs(turtle.pos()) < 1:   # x的絕對值小於1跳出迴圈
        break

turtle.end_fill()
turtle.mainloop()
