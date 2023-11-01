import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

file = r"銷售業績.xlsx"
df = pd.read_excel(file)
df['年'] = df['日期'].dt.year
df['月'] = df['日期'].dt.month
df['日'] = df['日期'].dt.day
df1 = df.pivot_table(index="月",columns='店名',values='小計',aggfunc='sum')
print(df1.loc[1,:].values)
# draw map
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#4C2A85", "#BE96FF", "#957DAD", "#5E366E", "#A98CCC"])
matplotlib.rc('font', family='Microsoft JhengHei')
fig1,ax1 = plt.subplots(figsize=(20,12))
cmap = plt.colormaps["cool"]
color_bar = cmap(np.linspace(0,1,15))


ax1.bar(df1.index-0.25, df1[' 南吉'],color=color_bar[0],width=0.1)
ax1.bar(df1.index-0.15, df1[' 四維'],color=color_bar[1],width=0.1)
ax1.bar(df1.index-0.05, df1[' 崇德'],color=color_bar[2],width=0.1)
ax1.bar(df1.index+0.05, df1[' 新創'],color=color_bar[3],width=0.1)
ax1.bar(df1.index+0.15, df1[' 科鈺'],color=color_bar[4],width=0.1)
ax1.bar(df1.index+0.25, df1[' 陽明'],color=color_bar[5],width=0.1)

ax1.set_title("年度各店銷售額")
ax1.set_xlabel("月份")
ax1.set_ylabel("金額")
plt.legend(df1,fontsize="x-large")
plt.show()
