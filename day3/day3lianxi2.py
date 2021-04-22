num=1
num1=0
num3=0
while num<=10:
    num=num+1
    num2=int(input("请输入您要输入的数："))
    if num3>num2:
       num3=num3
    else:
        num3=num2
    num1=num1+num2
print(num3)
print(num1)
num4=num1/10
print(num4)