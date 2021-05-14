import random
import xlwt
shop =[
    ["鬼王机甲",2000],
    ["未来坦克",3000],
    ["钢铁浪人",1500],
    ["欧米茄百合子",1500],
    ["基洛夫空艇",2000],
    ["娜塔莎",1500]
]
hb =xlwt.Workbook()
sheet=hb.add_sheet("商城系统")
sheet.write(0,0,"商品")
sheet.write(0,1,"价格")
sheet.write(1,0,"鬼王机甲")
sheet.write(1,1,2000)
sheet.write(2,0,"未来坦克")
sheet.write(2,1,3000)
sheet.write(3,0,"钢铁浪人")
sheet.write(3,1,1500)
sheet.write(4,0,"欧米茄百合子")
sheet.write(4,1,1500)
sheet.write(5,0,"基洛夫空艇")
sheet.write(5,1,2000)
sheet.write(6,0,"娜塔莎")
sheet.write(6,1,1500)
hb.save("商城改造.xls")


salary =input("请输入您的资金:")
salary =int(salary)
mycart =[]

a =0
a1 =random.randint(1,30)
if a1 >=1 and  a1 <=10:
    a = a +1
    print("恭喜您获得1张鬼王机甲优惠券:满600减300","a=",a)
else:
    a=a +2
    print("恭喜你获得1张未来坦克优惠券：半折甩卖","a=",a)
a2 =0
while True:
    for index,value in enumerate(shop):
        print(index,"  ",value)
    num=input("请输入您要买的编号:")
    if num.isdigit():
        num=int(num)
        if num>= len(shop):
            print("商品不存在,请重新输入")
        else:

            if a==1:
                if  num == 0:
                    # shop[0][1]=1700
                    if salary>=shop[num][1]:
                        shop[0][1]=1700
                        mycart.append(["鬼王机甲",1700])
                        salary =salary -shop[num][1]
                        a2 =a2+shop[num][1]/10
                        print("成功添加到购物车，您的资金余额为:",salary,"您的积分余额为:",a2)
                        a= 0
                        shop[0][1]=2000
                    else:
                        print("资金不足，无法购买")
                elif num>0 and  num<len(shop):
                    if salary>=shop[num][1]:
                        mycart.append(shop[num])
                    salary =salary -shop[num][1]
                    a2 =a2+shop[num][1]/10
                    print("成功添加到购物车，您的资金余额为:",salary,"您的积分余额为:",a2)
                else:
                    print("资金不足，无法购买")
            elif  a==2:
                if  num == 1:
                    # shop[1][1]=1500
                    if salary>=shop[num][1]:
                        shop[1][1]=1500
                        mycart.append(["未来坦克",1500])
                        salary =salary -shop[num][1]
                        a2 =a2+shop[num][1]/10
                        print("成功添加到购物车，您的资金余额为:",salary,"您的积分余额为:",a2)
                        a= 0
                        shop[1][1]=3000
                    else:
                        print("资金不足，无法购买")
                elif   (num==0) or (num>1 and num <len(shop)):
                    if salary>=shop[num][1]:
                        mycart.append(shop[num])
                        salary =salary -shop[num][1]
                        a2 =a2+shop[num][1]/10
                        print("成功添加到购物车，您的资金余额为:",salary,"您的积分余额为:",a2)
                    else:
                        print("资金不足，无法购买")
            else:
                if salary>=shop[num][1]:
                    mycart.append(shop[num])
                    salary =salary -shop[num][1]
                    a2 =a2+shop[num][1]/10
                    print("成功添加到购物车，您的资金余额为:",salary,"您的积分余额为:",a2)
                else:
                    print("资金不足，无法购买")

    elif num=="q" or num == "Q":
        print("欢迎老板下次光临:")
        break
    else :
        print("输入非法,请重新输入")

print("您本次购买的商品如下:")
for index,value in enumerate(mycart):
    print(index,"  ",value)
print("您的余额为:",salary)

