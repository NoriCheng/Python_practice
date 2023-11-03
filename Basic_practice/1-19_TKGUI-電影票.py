# import modules
from tkinter import *
import tkinter.font as tkFont   # 查詢所有字體
# print(list(tkFont.families()))


# configure workspace
ws = Tk()   # 創造物件
ws.title("First Program")   # 設定視窗名稱
ws.geometry('500x150')  # 指定視窗大小
ws.configure(bg="#bbbbbb")     # 指定視窗背景顏色

# function territory
# def welcome():
#     name = nameTf.get()
#     return Label(ws, text=f'200 {name}', pady=15, bg='#567').grid(row=2, columnspan=2)


def searchprice():
    # name = nameTf.get()
    age = int(nameTf1.get())
    std = nameTf2.get()
    price5 = '0'
    if age <= 5:
        price = price5
    elif age > 5 and std == 'Y':
        price = '學生票:' + '250'
    elif 5 < age <= 18 and std == 'N':
        price = '一般成人票:' + '300'
    elif age > 18 and std == 'N':
        price = '成人票:' + '350'
    else:
        price = '沒票'
    return (Label(ws, text=f"{age}歲 {'是'if std=='Y' else '不是'}學生 {price}元", bg='#bbbbbb', font=font_微軟正黑體14)
            .grid(row=3, column=1))

# label & Entry boxes territory


font_微軟正黑體14 = tkFont.Font(family='微軟正黑體', size=14)
nameLb1 = Label(ws, text="請輸入年齡:", bg='#bbbbbb', fg='black', font=font_微軟正黑體14)
nameLb1.grid(row=0, column=0)
nameTf1 = Entry(ws, bg='white', fg='black', font=font_微軟正黑體14)
nameTf1.grid(row=0, column=1, ipadx=10)
nameLb2 = Label(ws, text="請輸入是否為學生(Y/N):", bg='#bbbbbb', fg='black', font=font_微軟正黑體14)
nameLb2.grid(row=1, column=0)
nameTf2 = Entry(ws, bg='white', fg='black', font=font_微軟正黑體14)
nameTf2.grid(row=1, column=1, ipadx=10)


# # button territory
welBtn = Button(ws, text="價格查詢...", command=searchprice, font=font_微軟正黑體14, bg='#000000', fg='#FFFFFF')
welBtn.grid(row=3, column=0)


# Position Provide territory
# nameLb.grid(row=0, column=0)
# nameTf.grid(row=0, column=1)
# welBtn.grid(row=1, columnspan=2)

# infinite loop
ws.mainloop()
