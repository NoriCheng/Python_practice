import math
import tkinter as tk
import tkinter.font as tkFont
import pandas as pd


def rgb_to_hsv(r, g, b):
    # R, G, B values are divided by 255
    # to change the range from 0..255 to 0..1:
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    # h, s, v = hue, saturation, value
    cmax = max(r, g, b)  # maximum of r, g, b
    cmin = min(r, g, b)  # minimum of r, g, b
    diff = cmax-cmin   # diff of cmax and cmin.
    # if cmax and cmax are equal then h = 0
    if cmax == cmin:
        h = 0
    # if cmax equal r then compute h
    elif cmax == r:
        h = (60 * ((g - b) / diff) + 360) % 360
    # if cmax equal g then compute h
    elif cmax == g:
        h = (60 * ((b - r) / diff) + 120) % 360
    # if cmax equal b then compute h
    elif cmax == b:
        h = (60 * ((r - g) / diff) + 240) % 360
    # if cmax equal zero
    if cmax == 0:
        s = 0
    else:
        s = (diff / cmax) * 100
    # compute v
    v = cmax * 100
    return h, s, v


def hsv2rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b


# 建立TK 視窗
file = open(r"tkColors.txt", 'r', encoding="utf-8")
item_list = []
while True:
    line = file.readline()        # 'Aaa    100   20.5\n'
    if line == '':
        break         # 讀不到資料時  強迫脫離
    if line == '\n':
        continue    # 讀到空行  中途返回
    item_list.append(line)
# len(item_list)  # 3040

color_dict = {}
for n in range(int(len(item_list)/4)) :
    tuple1 = (int(item_list[n*4+1].strip()),int(item_list[n*4+2].strip()),int(item_list[n*4+3].strip()))
    color_dict[tuple1] = item_list[n*4].strip()
COLORS = tuple(color_dict.values())       # 508 個顏色的名字
RGB = list(color_dict.keys())       # 508 個顏色的RGB tuple
HSV = [rgb_to_hsv(*item)+COLORS[n:n+1] for n, item in enumerate(RGB)]
HSV = sorted(HSV, key=lambda x: (x[0], x[1], x[2]))     # 508  [(0, 0, 0.0, 'grey0'), (0, 0.0, 0.01, 'grey1'),...]


def color_pad():
    def left_mouse(event):
        rgb = []
        widget = event.widget
        顯示顏色label["bg"] = widget.cget("bg")
        顯示顏色label["fg"] = widget.cget("fg")
        顯示顏色label["text"] = widget.cget("text")
        value = var.get()

        if value == "1":
            df = pd.DataFrame([widget.cget("text")],columns=["Copy Name"])
            df.to_clipboard(index=False)
            print(value)
        elif value == "2":
            af = pd.DataFrame([item[0] for item in color_dict.items()\
                               if widget.cget("text") == item[1]], columns=["R", "G", "B"])
            af.to_clipboard(index=False)
            print(value)
        return
    # 建立 調色盤GUI 介面
    ws = tk.Toplevel(mains)
    ws.title("調色盤")
    # font_微軟正黑 = tkFont.Font(family="微軟正黑體", size=5)  # no default root window 不可設定字型
    ws.geometry('1425x850')
    ws.configure(bg="#000000")
    rown = 0
    global button_bg_C
    button_bg_C = [f"C_{nam}" for nam in range(508)]

    for n, item in enumerate(HSV):
        if n % 17 != 0:

            button_bg_C[n] = tk.Button(ws, text=HSV[n][3],
                                       fg=(lambda x: "white" if x[2]<81 or x[1] > 120 else "black")(HSV[n]),
                                       font=("微軟正黑體", 9), width=11, height=1, bg=HSV[n][3])
            button_bg_C[n].bind('<Button-1>',left_mouse)
            button_bg_C[n].grid(row=rown, column=n % 17)
        else:
            rown += 1

    ws.mainloop()

    return


# 主畫面
mains = tk.Tk()
mains.title("主畫面")
mains.geometry('400x300')
var = tk.StringVar()
var.set("1")
font_微軟正黑36 = tkFont.Font(family="微軟正黑體", size=10)
目前複製顏色text = tk.Label(mains,text="目前複製顏色",width=10,height=2)
調色盤按鈕 = tk.Button(mains,text="開啟調色盤",font=("微軟正黑體", 10),width=10,height=2,command=color_pad)
選項_文字 = tk.Radiobutton(mains, text="輸出顏色名稱",variable=var,value=1)
選項_色碼 = tk.Radiobutton(mains, text="輸出顏色RGB",variable=var, value=2)
顯示顏色label = tk.Label(mains, bg="white", width=20, height=2)
text = tk.Text(height=5, width=30, font=("Arial", 14, "bold"))
text.insert('0.0', "複製測試區")

調色盤按鈕.grid(column=0, row=0)
目前複製顏色text.grid(column=0, row=1)
顯示顏色label.grid(column=1, row=1)
選項_文字.grid(column=0, row=2)
選項_色碼.grid(column=1, row=2)
text.grid(column=0, row=3, columnspan=2)
mains.mainloop()
