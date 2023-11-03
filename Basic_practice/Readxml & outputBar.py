import 老師模組
import random
import matplotlib.pyplot as plt
import matplotlib


list_2D = []
with open(r"新竹市重要遊憩據點遊客人次統計.csv", 'r', encoding="utf-8") as file:
    for line in file.readlines():
        if line == '\n': continue
        linelist = line.split(",")
        list_2D.append(linelist)
print(list_2D)
欄位名稱 = []
欄位名稱.append(list_2D.pop(0))     # 將項目獨立出來
list_2D_108 = []
mon = 0
for n, item in enumerate(list_2D):
    for tou in range(len(item)):
        list_2D[n][tou] = item[tou].replace('"', '').replace('\n', '')
    # 將item中的 108年度取出來弄成新串列
    if item[2][0:3] == '108':
        mon += 1
        list_2D_108.append([f'{item[2][0:3]}年{mon}月']+item[3:])

print(list_2D_108)
for item in list_2D_108:    # 將人次字串轉成整數
    for n, a in enumerate(item[1:]):
        item[n+1] = int(a)

print(list_2D_108)

分類 = list(zip(*list_2D_108))
print(分類)



matplotlib.rc('font', family='Microsoft JhengHei')
# 方法一
# color_bar = random.sample(老師模組.MPL_COLORS, 12)

# 方法二
import matplotlib.colors as mcolors
color_bar = list(mcolors.TABLEAU_COLORS)

# 方法三 16進制轉換色碼
# color_bar = ['#{0:02x}{1:02x}{2:02x}'.format(random.randint(0,255),
# random.randint(0,255), random.randint(0,255))for n in range(12)]

# 方法四 colormaps調色盤
# cmp = plt.colormaps['tab20c']       # colormaps 選用tab20c 調色盤
# color_bar = cmp([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])     # 取用tab20c調色盤的前12色

# color_bar = ['balck']
fig, ax = plt.subplots()

ax.bar(分類[0], 分類[1], color=color_bar)     # 以日期為 x軸，股價為 y軸畫點

fig.set_size_inches(12,6)   # 設定 w , h 長寬

ax.set(xlabel='日期', ylabel='人次',
       title='108年度新竹遊憩據點人次統計')

plt.show()
