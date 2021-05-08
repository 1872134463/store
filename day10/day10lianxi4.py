a=[]
b=[]
c=0
d=[]
e=[]
o=0
f= open(file="scores.txt",mode="r+",encoding="utf-8")
f1= open(file="总分.txt",mode="w+",encoding="utf-8")
data=f.readlines()
for i in data:
    da=i.replace("\n","").split(",")
    a.append(da)
for i in a:
    e.append(i[0])
    del i[0]
    b.append(i)

for i in b:
    for im in i:
        c=c+(int(im))
    d.append(c)
for i in d:
    f1.write(e[o]+str(i)+"\n")
    o=o+1
