import 老師模組
import random
import datetime

list_2D = []
with open(r"市府學生資料.txt", 'r') as file:
    for line in file.readlines():
        if line == '\n': continue  # 讀到空行 中途返回
        line_list = line.split()  # \n也會自動消掉
        line_list[3] = int(line_list[3])
        line_list[4] = int(line_list[4])
        line_list[5] = int(line_list[5])
        list_2D.append(line_list)

#
# age_young = []
# list_2D.sort(reverse=True, key=lambda allgrades: int(allgrades[3])+int(allgrades[4])+int(allgrades[5]))
# print(list_2D, "\n總成績最高的是:" + list_2D[0][1] + "，總分是" + str(int(list_2D[0][3])+int(list_2D[0][4])+int(list_2D[0][5])))
#
# list_2D.sort(key=lambda young: young[2])
#
# print(list_2D, "\n最年輕的是:" + list_2D[0][1] + "，出生日期:"+list_2D[0][2])

for item in list_2D:    # 計算成績平均並加入串列
    item.append(round((item[3]+item[4]+item[5])/3,2))   # round 用以四捨五入取指定小數點位數
list_2D.sort(key=lambda x: x[6], reverse=False)

dict = {}
for n, item in enumerate(list_2D, start=1):
    dict[item[6]] = n
dict1 = {key: 31-value for key, value in dict.items()}  # 使用字典去排除重複分數的排名
for item in list_2D:
    item.append(str(dict1[item[6]])+"名")
sorted(list_2D, key=lambda x: x[0], reverse=True)

print(list_2D)
date_Now = datetime.date.today()

for item in list_2D:
    年,月,日 = item[2].split('-')  # 將 2005-04-09 以 - 去切片
    if 月 < str(date_Now.month):
        item.append(str(date_Now.year-int(年)-1)+'歲')
    else:
        item.append(str(date_Now.year-int(年))+'歲')
#     if item[2][5:7] < str(date_Now.month):
#         item.append(str(date_Now.year - int(item[2][:4])+1)+'歲')    # 過月份要+1歲
#     else:
#         item.append(str(date_Now.year - int(item[2][:4])) + '歲')
print(list_2D)
col_name = ['學號', '   姓名', '  生日', '  國文', ' 數學', ' 英文', ' 平均', ' 名次', '年齡']
with open(r"整理市府班學生資料.txt", 'w') as file:
    file.write(' '.join(col_name)+'\n')    # 加上項目名稱
    for item in list_2D:
        for n, value in enumerate(item[3:7], start=3):
            item[n] = str(value)
        # item[3] = str(item[3])
        # item[4] = str(item[4])
        # item[5] = str(item[5])
        # item[6] = str(item[6])
        file.write(' '.join(item)+'\n')
