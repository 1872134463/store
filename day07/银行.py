import random
import pymysql
bank_name = "中国工商银行的昌平支行"
# 打印欢迎页面
def welcome():
    print("---------------------------------")
    print("-     中国工商银行账户管理系统V1.0     -")
    print("---------------------------------")
    print("-   1.开户                       -")
    print("-   2.存钱                       -")
    print("-   3.取钱                       -")
    print("-   4.转账                       -")
    print("-   5.查询                       -")
    print("-   6.Bye!                       -")
    print("----------------------------------")

# 银行的开户逻辑
def bank_addUser(account,username,password,country,province,street,door):
    con=pymysql.connect(host="localhost",user="root",password="root",database="bank")
    cursor=con.cursor()
    # 判断是否已满
    sql="select account from users"
    num1=cursor.execute(sql)
    data=cursor.fetchall()
    con.commit()
    cursor.close()
    con.close()
#提交数据
#关闭资源
    if num1 > 100:
               return 3
    con=pymysql.connect(host="localhost",user="root",password="root",database="bank")
    cursor=con.cursor()
    sql01 = "select account from users where users.account = %s"
    param01 = [account]
    cursor.execute(sql01,param01)
    if param01  in data:
               return  2
    con.commit()
    cursor.close()
    con.close()
    con=pymysql.connect(host="localhost",user="root",password="root",database="bank")
    cursor=con.cursor()
    sql="insert into users values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param=[account,username,password,country,province,street,door,0,bank_name]
    cursor.execute(sql,param)
    con.commit()
    cursor.close()
    con.close()
    return  1
# 用户开户方法
def addUser():
    # 随机获取账号
    li = ["1","2","3","4","5","6","7","8","9","0","a","b","c","e","f"]
    account = ""
    for i in range(8):
        index = random.randint(0, len(li) - 1)
        account = account + li[index]
    username = input("请输入用户名：")
    password = input("请输入您的密码（6位数字）：")
    print("接下来要输入您的地址信息：")
    country = input("\t输入国家：")
    province = input("\t输入省份：")
    street =  input("\t输入街道：")
    door = input("\t输入门牌号：")
    # 余额不允许第一次输入，需要存钱
    status = bank_addUser(account,username,password,country,province,street,door)
    if status == 1:
        print("恭喜开户成功！")
        info = '''
            ------------个人信息----------------
            账号：%s,
            用户名：%s,
            取款密码：%s,
            地址信息：
                国家：%s,
                省份：%s,
                街道：%s,
                门牌号：%s,
            余额：%s,
            开户行：%s
            -----------------------------------
        '''
        print(info % (account,username,password,country,province,street,door,0,bank_name))
    elif status == 2:
         print("对不起，该用户已存在！请稍后重试！！！")
    elif status == 3:
        print("对不起，该银行库已满，请携带证件到其他银行办理！！！")

def bank_save(account,money):
    con=pymysql.connect(host="localhost",user="root",password="root",database="bank")
    cursor=con.cursor()
    sql="select account from users where users.account= %s"
    param=[account]
    cursor.execute(sql,param)
    data=cursor.fetchall()
    num=len(data)
    con.commit()
    cursor.close()
    con.close()
    if  num==1:
        con=pymysql.connect(host="localhost",user="root",password="root",database="bank")
        cursor=con.cursor()
        sql="update users set money = money + %s where account= %s"
        param=[money,account]
        cursor.execute(sql,param)
        con.commit()
        return 1
    if   num==0:
        return False
    cursor.close()
    con.close()

def save():
    account =input("请输入您的账号:")
    money =input("请输入您要存的存款金额:")
    sta = bank_save(account,money)
    if sta  == False:
        print("用户不存在")
    if sta == 1:
        print("存款成功")
def bank_wda(account,password,wdamoney):
    con=pymysql.connect(host="localhost",user="root",password="root",database="bank")
    cursor=con.cursor()
    sql="select account from users where users.account= %s"
    param=[account]
    cursor.execute(sql,param)
    data=cursor.fetchall()
    num=len(data)
    if num==0:
        return 1
    if num==1:
       sql="select password from users where users.account= %s and users.password=%s"
       param=[account,password]
       num=cursor.execute(sql,param)
       if num ==1:
          sql="update users set users.money =users.money -%s where users.money>=%s"
          param=[wdamoney,wdamoney]
          num=cursor.execute(sql,param)
          con.commit()
          if num==1:
              return 0
          if num==0:
              return 3
       if num==0:
           return 2
       cursor.close()
       con.close()




def wda():
    account =input("请输入您的账号:")
    password =input("请输入您的密码:")
    wdamoney =input("请输入您要取的取款金额:")
    stb =bank_wda(account,password,wdamoney)
    if stb == 1:
          print("账号不存在")
    if stb == 2:
        print("密码不对")
    if stb == 3:
        print("钱不够")
def bank_tran(account1,account2,password,money):
    con=pymysql.connect(host="localhost",user="root",password="root",database="bank")
    cursor=con.cursor()
    sql="select account from users where users.account= %s or users.account =%s"
    param=[account1,account2]
    num=cursor.execute(sql,param)
    if num==2:
        sql="select password from users where users.account= %s and users.password=%s"
        param=[account1,password]
        num=cursor.execute(sql,param)
        if num == 1:
            sql="update users set users.money =users.money - %s where users.account=%s"
            param=[money,account1]
            num=cursor.execute(sql,param)
            sql1="update users set users.money =users.money + %s where users.account=%s"
            param1=[money,account2]
            num1=cursor.execute(sql1,param1)
            con.commit()
            if num == 1 and num1== 1:
                return 0
            else:
                return 3
        if num==0:
            return 2
    else :
        return 1
    cursor.close()
    con.close()



def tran():
   account1 =input("请输入转出的账号:")
   account2 =input("请输入转入的账号:")
   password =input("请输入转出账号密码:")
   money  =input("请输入转出金额:")
   stc =bank_tran(account1,account2,password,money)
   if stc == 1:
    print("正常")
    if stc==2:
        print("账号不对")
    if stc== 3:
          print("钱不够")
def bank_query(account,password):
    con=pymysql.connect(host="localhost",user="root",password="root",database="bank")
    cursor=con.cursor()
    sql="select account from users where users.account= %s"
    param=[account]
    num=cursor.execute(sql,param)
    con.commit()
    if num==1:
        sql="select password from users where users.account= %s and users.password=%s"
        param=[account,password]
        num=cursor.execute(sql,param)
        con.commit()
        if num==1:
            return 2
        if num==0:
            return 1
    if num==0:
        return 0
    cursor.close()
    con.close()

def query():
    account=input("请输入账号:")
    password =input("请输入密码:")
    ste=bank_query(account,password)
    if ste == 0:
        print("该用户不存在")
    if ste == 1:
        print("输入信息错误")
    if ste ==2:
        con=pymysql.connect(host="localhost",user="root",password="root",database="bank")
        cursor=con.cursor()
        sql="select * from users where users.account= %s"
        param=[account]
        cursor.execute(sql,param)
        date =cursor.fetchall()
        con.commit()
        for i in date:
            account=date[0][0]
            password=date[0][2]
            money=date[0][7]
            country=date[0][3]
            province=date[0][4]
            street=date[0][5]
            door=date[0][6]
            bank_name=date[0][8]


            info = '''
                ------------个人信息----------------
                账号：%s,
                密码：%s,
                余额：%s,
                地址信息：
                    国家：%s,
                    省份：%s,
                    街道：%s,
                    门牌号：%s,
                
                开户行：%s
                -----------------------------------
            '''
            print(info % (account,password,money,country,province,street,door,bank_name))
        cursor.close()
        con.close()
while True:
    welcome()
    num = input("请输入您的业务编号：")
    if num.isdigit():
        num = int(num)
        if num == 1:
            addUser()
        elif num == 2:
            save()
        elif num == 3:
            wda()
        elif num == 4:
            tran()
        elif num == 5:
           query()
        elif num == 6:
            print("拜拜了您嘞，欢迎下次光临！！！")
            break
        else:
            print("输入非法！请重新输入！！！别瞎弄！！！")
    else:
        print("您输入非法！请重新输入！！！")







































