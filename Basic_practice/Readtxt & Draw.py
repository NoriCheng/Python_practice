import turtle
import MyModule_1

file = open(r"tkColors.txt", 'r', encoding="utf-8")
item_list = []
while True :
    line = file.readline()    # 'Aaa    100   20.5\n'
    if line == '' : break         # 讀不到資料時  強迫脫離
    if line == '\n' : continue    # 讀到空行  中途返回
    item_list.append(line)
# len(item_list)  # 3040

color_dict = {}
for n in range(int(len(item_list)/4)):
    color_dict[item_list[n*4].strip()] = (int(item_list[n*4+1].strip()),
                                            int(item_list[n*4+2].strip()),
                                            int(item_list[n*4+3].strip()))


COLORS = MyModule_1.COLORS  # 479 個顏色     486 個矩形

# for n,color in enumerate(COLORS) :
#     print(n,color_dict[color])  #  全部對得上

w, h  = 1620 , 810
s1 = turtle.Screen()
s1.setup(w, h)
s1.bgcolor('black')
s1.colormode(255)
s1.tracer(0)
suyu1 = turtle.Turtle()
no = 0
for row in range(27):  # 橫的 27 列
    y = 390 - row * 30
    for col in range(18):  # 每一列要畫 18 個方形
        x = -765 + col * 90
        if no > 478 :
            break
        else :
            MyModule_1.畫矩形(suyu1,x, y, 90, 30, COLORS[no])
            if (color_dict[ COLORS[no] ][0]+color_dict[ COLORS[no] ][1]+color_dict[ COLORS[no] ][2])/3 > 180 :
                suyu1.pencolor('black')
                suyu1.fillcolor('black')
            else :
                suyu1.pencolor('white')
                suyu1.fillcolor('white')
            suyu1.penup()
            suyu1.goto(x,y-5)
            suyu1.pendown()
            suyu1.write(COLORS[no], move=False, align='center', font=('Arial', 8, 'normal'))
            no += 1
s1.mainloop()