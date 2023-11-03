from turtle import Screen, Turtle

def square(size):

    if t1.filling():    # 判斷是否填滿
        t1.pensize(5)
    else:
        t1.pensize(3)
    count = 0
    while count < 4:
        t1.forward(size)
        t1.right(90)
        count += 1

def drawing(number):
    red = 30
    green = 10
    blue = 20

    times = 0

    while times < number:
        t1.color(red % 255, green % 255, blue % 255)    # 定義色碼不大於255
        t1.begin_fill()
        square(size)
        t1.end_fill()

        t1.right(360 / number)

        red, green, blue = red + 20, green + 30, blue + 10
        times += 1  #計數器

size = int(input("How long do you want the side lengths to be? "))
number = int(input("How many squares do you want in the image? "))

s1 = Screen()   # 這行稱為類別建構式，產生類別
s1.colormode(255)

t1 = Turtle()
t1.speed('fastest')  # because I have no patience

drawing(number)

s1.exitonclick()
