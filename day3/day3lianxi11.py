import random
num =random.randint(0,100)
num2=0
coin=0
while True:
    num1 = int(input("请输入您要猜的数:"))
    num2 =num2 + 1
    coin=coin +10
    if  num2<7:

       if num1>num:
           print("大了")
       elif num1<num:
            print("小了")
       else:
           print("恭喜您猜对了","本次中奖号码为:",num,"猜的次数",num2,"花费",coin)
           break
    else:
        print("系统锁定退出",num)
        break