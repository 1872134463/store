name ="root"
password ="admin"
num = 1

while  True:
    name1 =input("请输入用户名:")
    password1 =input("请输入密码:")
    if  name1==name and  password1==password:
        print("登录成功")
        break
    else:
        print("错误！")
        if num < 3:
            num = num + 1
        else:
            print("系统锁定")
            break







