# import modules
from tkinter import *
import tkinter.font as tkFont   # 查詢所有字體
# print(list(tkFont.families()))


# configure workspace
ws = Tk()   # 創造物件
ws.title("First Program")   # 設定視窗名稱
ws.geometry('500x500')  # 指定視窗大小
ws.configure(bg="#bbbbbb")     # 指定視窗背景顏色

# function territory
# def welcome():
#     name = nameTf.get()
#     return Label(ws, text=f'200 {name}', pady=15, bg='#567').grid(row=2, columnspan=2)


def searchprice():
    # name = nameTf.get()
    age = int(nameTf1.get())
    std = nameTf2.get()

    if age <= 5:
        readOnlyText.insert(1.0, "0元")
    elif age > 5 and std == 'Y':
        readOnlyText.insert(1.0, "200元")
    elif 5 < age <= 18 and std == 'N':
        readOnlyText.insert(1.0, "250元")
    elif age > 18 and std == 'N':
        readOnlyText.insert(1.0, "350元")
    else:
        readOnlyText.insert(1.0, "沒票")
    return

# label & Entry boxes territory


font_微軟正黑體24 = tkFont.Font(family='微軟正黑體', size=24)
nameLb1 = Label(ws, text="請輸入年齡:", bg='#bbbbbb', fg='black', font=('微軟正黑體', '20', 'normal'))
nameLb1.pack()
nameTf1 = Entry(ws, bg='white', fg='black', font=font_微軟正黑體24)
nameTf1.pack()
nameLb2 = Label(ws, text="請輸入是否為學生(Y/N):", bg='#bbbbbb', fg='black', font=('微軟正黑體', '20', 'normal'))
nameLb2.pack()
nameTf2 = Entry(ws, bg='white', fg='black', font=font_微軟正黑體24)
nameTf2.pack()


# # button territory
welBtn = Button(ws, text="價格查詢...", command=searchprice, font=font_微軟正黑體24, bg='#000000', fg='#FFFFFF')
welBtn.pack()
readOnlyText = Text(ws,font=font_微軟正黑體24)     # 設定記事本
readOnlyText.pack()

# Position Provide territory
# nameLb.grid(row=0, column=0)
# nameTf.grid(row=0, column=1)
# welBtn.grid(row=1, columnspan=2)

# infinite loop
ws.mainloop()
