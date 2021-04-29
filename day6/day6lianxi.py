import random
shop =[
    ["鬼王机甲",2000],
    ["未来坦克",3000],
    ["钢铁浪人",1500],
    ["欧米茄百合子",1500],
    ["基洛夫空艇",2000],
    ["娜塔莎",1500]
]
city ={
    "北京":{
        "昌平区":{
                 "回龙观":["永辉","永旺"],
                 "龙泽":["海底捞","呷脯呷脯"]},
        "海淀区":{
                 "公主坟":["军事博物馆","五道口切糕"],
                 "香山":["香山","植物园"],
                 "高校":["清华","北大"]
                        },
        "朝阳区":{
                "朝阳南北塔":["世纪公园","玉渊潭公园"],
                "双塔":["双塔白醋"]

        },
        "顺义":{
                "龙庆峡":["龙庆峡"]
        }

    },
    "天津":{}
}
def  print_place(date):
    for i  in date:
        print(i)
while True:
    print_place(city)
    num1 =input("请输入您要去的城市:")
    if num1 in city:
        print_place(city[num1])
        num2 =input("请输入您要去的二级城市:")
        if num2 in city[num1]:
            print_place(city[num1][num2])
            num3 =input("请输入您要去的三级城市:")
            if num3 in city[num1][num2]:
                print_place(city[num1][num2][num3])
                num4 = int(input("您是否要进入超市:是,1,否,2:"))
                if num4 ==1:
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

                    print("祝您旅途愉快")
                elif num4 == 2:
                    print("欢迎下次光临")
                else:
                    print("输入非法，请重新输入")





            elif num3 == "q"  or num3 == "Q":
                print("欢迎下次光临")
            else:
                print("输入非法，请重新输入")
        elif num2 =="q"  or num2 =="Q":
            print("欢迎下次光临")
        else:
            print("输入非法,请重新输入")
    elif num1 =="q"  or num1 =="Q":
         print("欢迎下次光临")
         break
    else:
         print("输入非法")






