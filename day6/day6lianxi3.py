students = [
    {'name':'张三','age':23,'score':88,'tel':'23423532','gender':'男'},
    {'name':'李四','age':26,'score':80,'tel':'12533453','gender':'女'},
    {'name':'王五','age':15,'score':58,'tel':'56453453','gender':'男'},
    {'name':'赵六','age':16,'score':57,'tel':'86786785','gender':'保密'},
    {'name':'小明','age':18,'score':98,'tel':'23434656','gender':'女'},
    {'name':'小红','age':23,'score':72,'tel':'67867868','gender':'女'},
]
a=0
b=0
c=0
max_sco=0
max_name=0
for item in students:
   if  item['score']<60:
       a=a+1

print("不及格学生个数:",a)
for item in students:
    if item['age']<=18:
        b=b+1
print("未成年个数:",b)
#endswith
for item in students:
    if item['tel'].endswith("8"):
        c=c+1
print("手机尾号是8:",c)
max_sc0 =item["score"]
for item in students:
    if item['score']>=max_sco:
        max_sco=item['score']
        max__name=item['name']
print(max_sc0)
print(max__name)
#排序
students.sort(key=lambda stu:stu["score"])
students.reverse()
for item in students:
  print(item)
# 删除
for item in students:
   if item['gender']=="保密":
    students.remove(item)
for item in students:
     print(item)
