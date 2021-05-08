from DBUtils import select
from DBUtils import update
c=[]
num=0
f=open(file="用户.txt",mode="r+",encoding="utf-8")
data=f.readlines()
for i in data:
    da=i.replace("\n","").split(",")
    c.append(da)
for i in c:
   sql01 = "select * from users2 where users2.姓名 = %s"
   data01=select(sql01,i[0])
   if len(data01)==0:
      sql="insert into users2 values(%s,%s,%s)"
      param=[i[0],i[1],i[2]]
      update(sql,param)
   else:
       break

for i in c:
   num=num+int(i[2])
print("资产总和为:",num)