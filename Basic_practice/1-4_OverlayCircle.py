from turtle import *
colormode(255) # 此種模式須寫入模式
# pencolor('red')
# fillcolor('green')
# pencolor('#ff0000')
# fillcolor('#00ff00')
for i in range(10,1,-1):
        penup()
        goto(150+i*30,0)
        seth(90)

        pendown()
        pencolor(200+i * -20, 200+i*-10, 0)
        fillcolor(0, 200+i * -20, 200+i*-10)
        begin_fill()
        circle(150+i*30)
        end_fill()
mainloop()