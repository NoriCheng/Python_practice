import MyModule_1
import random
import datetime

birthday = []
for n in range(30):     # 新增隨機生日進串列
    d = datetime.datetime(random.randint(1990, 2006), random.randint(1, 12), random.randint(1, 28))
    birthday.append('{:%Y-%m-%d}'.format(d))

grades = [str(random.randint(10, 100)) for n in range(90)]   # 新增隨機分數進串列

list_2D = []
grn = 0
for n, stu in enumerate(MyModule_1.STUDENTS, start=1):   # 將學生名稱加上生日以及成績
    學號 = '112'+format(n, '03')
    list_2D.append([學號, stu, birthday[grn], grades[0+grn], grades[1+grn], grades[2+grn]])
    grn += 1

with open(r"市府學生資料.txt", 'w') as file:
    for item in list_2D:
        file.write(' '.join(item)+'\n')

age_young = []
list_2D.sort(reverse=True, key=lambda allgrades: int(allgrades[3])+int(allgrades[4])+int(allgrades[5]))
print(list_2D, "\n總成績最高的是:" + list_2D[0][1] + "，總分是" + str(int(list_2D[0][3])+int(list_2D[0][4])+int(list_2D[0][5])))

list_2D.sort(key=lambda young: young[2])

print(list_2D, "\n最年輕的是:" + list_2D[0][1] + "，出生日期:"+list_2D[0][2])
