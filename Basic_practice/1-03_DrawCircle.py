from turtle import *
pen()
for i in range(3,0,-1):
     penup()
     goto(150+i*50,0)
     seth(90)
     pendown()
     circle(150+i*50)



mainloop()
