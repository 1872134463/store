from collections import Counter
list1=['小明','小张','小黄','小杨']
list2=['小黄','小李','小王','小杨','小周']
list3=['小杨','小张','小吴','小冯','小周']
list4=[]
list5=[]
a=0
b=0
c=0
d=0
for i in list1:
    list4.append(i)
for i in list2:
    list4.append(i)
for i in list3:
    list4.append(i)
a=set(list4)
print("选课学生总数为:",len(a))
for i  in list1:
    if i not in list2 :
        if i not in list3:
            c=c+1
print("选第一个学科的数量:",c,"名字：",i)
for i  in list1:
    if i not in list2 :
        if i not in list3:
            d=d+1
            print(i)
for i  in list2:
    if i not in list1 :
        if i not in list3:
            d=d+1
            print(i)
for i  in list3:
    if i not in list1 :
        if i not in list2:
            d=d+1
        print(i)
print("只选一门学科学生数量:",d)