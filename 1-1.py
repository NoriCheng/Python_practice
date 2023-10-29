from turtle import *
speed(5)

i=0
while i<3:
    up()
    forward(50)
    down()
    left(90)
    forward(100+50*i)
    left(90)
    forward(200+100*i)
    left(90)
    forward(200+100*i)
    left(90)
    forward(200+100*i)
    left(90)
    forward(100+50*i)
    right(90)
    i+=1
mainloop()