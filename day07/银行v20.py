import random
from DBUtils import select
from DBUtils import update


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

    # 判断是否已满
    sql="select count(*) from users"
    data=select(sql,[])
    if data[0][0]>=100:
        return 3
    sql01 = "select * from users where users.account = %s"
    data01=select(sql01,account)
    if len(data01)!=0:
        return  2
    sql02="insert into users values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2=[account,username,password,country,province,street,door,0,bank_name]
    update (sql02,param2)
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

    sql="select * from users where users.account = %s"
    data=select(sql,account)
    if  len(data)!=0:
        sql="update users set money = money + %s where account= %s"
        param=[money,account]
        update(sql,param)

        return 1
    if   len(data)==0:
        return False
def save():
    account =input("请输入您的账号:")
    money =input("请输入您要存的存款金额:")
    sta = bank_save(account,money)
    if sta  == False:
        print("用户不存在")
    if sta == 1:
        print("存款成功")
def bank_wda(account,password,wdamoney):

    sql="select count(*) from users where users.account = %s"
    data=select(sql,account)

    if data[0][0] == 0:
        return 1
    if data[0][0] == 1:
        sql="select count(*) from users where users.account= %s and users.password=%s"
        param = [account,password]
        data = select(sql,param)
        if data[0][0] == 1:
            sql2 = "select * from users where users.account= %s"
            param2 = [account]
            data2 = select(sql2,param2)
            datanum = data2[0][7]
            if datanum >= wdamoney:
                sql="update users set users.money =users.money -%s where users.money>=%s"
                param=(wdamoney,wdamoney)
                update(sql,param)
                return 0
            else:
                return 3
        else:
            return 2




def wda():
    account =input("请输入您的账号:")
    password =input("请输入您的密码:")
    wdamoney =int(input("请输入您要取的取款金额:"))
    stb =bank_wda(account,password,wdamoney)
    if stb == 1:
        print("账号不存在")
    if stb == 2:
        print("密码不对")
    if stb == 3:
        print("钱不够")
def bank_tran(account1,account2,password,money):
    sql="select count(*) from users where users.account= %s or users.account =%s"
    param=[account1,account2]
    data=select(sql,param)
    if data[0][0]==2:
        sql="select count(*) from users where users.account= %s and users.password=%s"
        param=[account1,password]
        data=select(sql,param)
        if data[0][0] == 1:
            sql="select * from users where users.account= %s"
            param=[account1]
            data=select(sql,param)
            num=data[0][7]
            if num>=money:
               sql="update users set users.money =users.money - %s where users.account=%s"
               param1=[money,account1]
               update(sql,param1)
               sql1="update users set users.money =users.money + %s where users.account=%s"
               param2=[money,account2]
               update(sql1,param2)
            else:
                return 3
        if data[0][0]==0:
            return 2
    else :
        return 1



def tran():
    account1 =input("请输入转出的账号:")
    account2 =input("请输入转入的账号:")
    password =input("请输入转出账号密码:")
    money  =int(input("请输入转出金额:"))
    stc =bank_tran(account1,account2,password,money)
    if stc == 1:
        print("正常")
        if stc==2:
            print("账号不对")
        if stc== 3:
            print("钱不够")
def bank_query(account,password):
    sql="select count(*) from users where users.account= %s"
    data=select(sql,account)
    if data[0][0]==1:
        sql="select count(*) from users where users.account= %s and users.password=%s"
        param=[account,password]
        data=select(sql,param)
        if data[0][0]==1:
            return 2
        if data[0][0]==0:
            return 1
    if data[0][0 ]==0:
        return 0

def query():
    account=input("请输入账号:")
    password =input("请输入密码:")
    ste=bank_query(account,password)
    if ste == 0:
        print("该用户不存在")
    if ste == 1:
        print("输入信息错误")
    if ste ==2:
        sql="select * from users where users.account= %s"
        param=[account]
        data=select(sql,param)

        account=data[0][0]
        password=data[0][2]
        money=data[0][7]
        country=data[0][3]
        province=data[0][4]
        street=data[0][5]
        door=data[0][6]
        bank_name=data[0][8]


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







































