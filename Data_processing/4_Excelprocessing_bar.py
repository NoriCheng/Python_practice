import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

file = r"銷售業績.xlsx"
df = pd.read_excel(file)
df['年'] = df['日期'].dt.year
df['月'] = df['日期'].dt.month
df['日'] = df['日期'].dt.day
df1 = df.pivot_table(index="月", columns='店名', values='小計', aggfunc='sum')
print(df1.iloc[:, 0])
# draw map
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#4C2A85", "#BE96FF", "#957DAD", "#5E366E", "#A98CCC"])
matplotlib.rc('font', family='Microsoft JhengHei')
fig1, ax1 = plt.subplots(figsize=(20, 12))
cmap = plt.colormaps["cool"]
color_bar = cmap(np.linspace(0, 1, 15))
bottom = 0
for n in range(6):
    p = ax1.bar(df1.index, df1.iloc[:, n], color=color_bar[n * 2], width=0.5, bottom=bottom)
    bottom += df1.iloc[:, n]
    ax1.bar_label(p, label_type='center')

ax1.set_title("年度各店銷售額")
ax1.set_xlabel("月份")
ax1.set_ylabel("金額")
plt.legend(df1, fontsize="xx-large")
plt.show()
