import  xlrd
import xlwt
a=[]
b=0
c=0
d=0
e=0
e1=0
f=0
g=0
g1=0
aa=0
bb=0
bb1=0
cc=0
dd=0
dd1=0
ee=0
ff=0
ff1=0
gg=0
aaa=0
aaa1=0
bbb=0
ccc=1
aaaa1=0
bbbb1=0
cccc1=0
dddd1=0
eeee1=0
ffff1=0
gggg1=0
mmmm1=0
wb =xlrd.open_workbook(filename="E:\\2021培训\Python\\12月份衣服销售数据.xlsx",encoding_override=True)
sheet=wb.sheet_by_name("12月份各种服饰销售情况")
rows =sheet.nrows
cols =sheet.ncols
for i in range(rows):
    sheet.row_values(i)
    a.append(sheet.row_values(i))
del a[0]
for i in a:

   b=b+ i[2]*i[4]
print("总销售额:", b)
aaaa1=("总销售额:", str(b))
for i in a:
    c=c+i[4]
d=c/len(a)
print("平均日销售量:", d)
bbbb1=("平均日销售量:",str(d))
for i in a:
    if i[1]=="羽绒服":
        e=e+i[4]
        e1=i[3]
f=e/e1
print("羽绒服本月销售占比为:",f)
cccc1=("羽绒服本月销售占比为:",str(f))
for i in a:
    if i[1]=="牛仔裤":
        g=g+i[4]
        g1=i[3]
aa=g/g1
print("牛仔裤本月销售占比为:",aa)
dddd1=("牛仔裤本月销售占比为:",str(aa))
for i in a:
    if i[1]=="风衣":
        bb=bb+i[4]
        bb1=i[3]
cc=bb/bb1
print("风衣本月销售占比为:",cc)
eeee1=("风衣本月销售占比为:",str(cc))
for i in a:
    if i[1]=="皮草":
        dd=dd+i[4]
        dd1=i[3]
ee=dd/dd1
print("皮草本月销售占比为:",ee)
ffff1=("皮草本月销售占比为:",str(ee))
for i in a:
    if i[1]=="T血":
        ff=ff+i[4]
        ff1=i[3]
gg=ff/ff1
print("T血本月销售占比为:",gg)
gggg1=("T血本月销售占比为:",str(gg))
for i in a:
    if i[1]=="衬衫":
        aaa=aaa+i[4]
        aaa1=i[3]
bbb=aaa/aaa1
print("衬衫本月销售占比为:",bbb)
mmmm1=("衬衫本月销售占比为:",str(bbb))
hb =xlwt.Workbook()
sheet=hb.add_sheet("12月份各种服饰销售情况")
sheet.write(0,0,"日期")
sheet.write(0,1,"服装名称")
sheet.write(0,2,"价格/件")
sheet.write(0,3,"库存数量")
sheet.write(0,4,"销售量/每日")
sheet.write(33,0,aaaa1)
sheet.write(33,3,bbbb1)
sheet.write(33,4,cccc1)
sheet.write(34,4,dddd1)
sheet.write(35,4,eeee1)
sheet.write(36,4,ffff1)
sheet.write(37,4,gggg1)
sheet.write(38,4,mmmm1)
for i in a:

    sheet.write(ccc,len(i)-5,i[0])
    sheet.write(ccc,len(i)-4,i[1])
    sheet.write(ccc,len(i)-3,i[2])
    sheet.write(ccc,len(i)-2,i[3])
    sheet.write(ccc,len(i)-1,i[4])
    ccc=ccc+1
sheet=hb.add_sheet("羽绒服")
sheet.write(0,0,"名称")
sheet.write(0,1,"本月销售量")
sheet.write(1,0,"羽绒服")
sheet.write(1,1,f*a[0][3])
sheet=hb.add_sheet("牛仔裤")
sheet.write(0,0,"名称")
sheet.write(0,1,"本月销售量")
sheet.write(1,0,"牛仔裤")
sheet.write(1,1,f*a[1][3])
sheet=hb.add_sheet("风衣")
sheet.write(0,0,"名称")
sheet.write(0,1,"本月销售量")
sheet.write(1,0,"风衣")
sheet.write(1,1,f*a[2][3])
sheet=hb.add_sheet("皮草")
sheet.write(0,0,"名称")
sheet.write(0,1,"本月销售量")
sheet.write(1,0,"皮草")
sheet.write(1,1,f*a[3][3])
sheet=hb.add_sheet("T血")
sheet.write(0,0,"名称")
sheet.write(0,1,"本月销售量")
sheet.write(1,0,"T血")
sheet.write(1,1,f*a[4][3])
sheet=hb.add_sheet("衬衫")
sheet.write(0,0,"名称")
sheet.write(0,1,"本月销售量")
sheet.write(1,0,"衬衫")
sheet.write(1,1,f*a[5][3])
hb.save("总数据.xls")