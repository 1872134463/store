num1 =int(input("请输入第一个数:"))
num2 =int(input("请输入第二个数:"))
num3 =int(input("请输入第三个数:"))
if num1+num2>num3  and  num2+num3>num1 and  num1+num3>num2 and num1>0 and num2>0 and num3>0:
    if  num1 == num2 or num1 ==num3 or num2 ==num3:
        if num1==num2==num3:
           print("三边组成等边三角形")
        else:
           if num1*num1 + num2*num2 ==num3*num3 or num1*num1+ num3*num3==num2*num2 or num2*num2+num3*num3==num1*num1:
               print("三边组成等腰直角三角形")
           else:
               print("三边组成等腰三角形")
    elif num1*num1 + num2*num2 ==num3*num3 or num1*num1+ num3*num3==num2*num2 or num2*num2+num3*num3==num1*num1:
        print("三边组成直角三角形")
    else:
         print("三边组成普通三角形")
else:
    print("三边不能组成三角形")