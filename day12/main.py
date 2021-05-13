from User import User
from Address import Address
from Bank import Bank
from welcome import Welcome
from Utils import Utils
from DBUtils import DBUtils

welcome = Welcome()
utils = Utils()
address = Address()
user = User()
bank = Bank()
dBUtils=DBUtils()

def addUser():
    account = utils.random()
    user.setUsername(input("请输入用户名"))
    user.setPassword(input("请输入您的密码（6位数字）："))
    print("接下来要输入您的地址信息：")
    address.setCountry(input("请输入国家"))
    address.setProvince(input("请输入省份"))
    address.setStreet(input("请输入街道"))
    address.setDoor(input("请输入门牌号"))
    # 余额不允许第一次输入，需要存钱
    status = bank.bank_addUser(account,user.getUsername(),user.getPassword(),address.getCountry(),address.getProvince(),address.getStreet(),address.getDoor())
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
        print(info % (account,user.getUsername(),user.getPassword(),address.getCountry(),address.getProvince(),address.getStreet(),address.getDoor(),0,bank.getBank_name()))
    if status == 2:
        print("对不起，该用户已存在！请稍后重试！！！")
    if status == 3:
        print("对不起，该银行库已满，请携带证件到其他银行办理！！！")
def save():
    account =input("请输入您的账号:")
    bank.setMoney(input("请输入您要存的存款金额:"))
    sta = bank.bank_save(account,bank.getMoney())
    if sta  == False:
        print("用户不存在")
    if sta == 1:
        print("存款成功")
def wda():
    account =input("请输入您的账号:")
    user.setPassword(input("请输入您的密码:"))
    bank.setMoney(input("请输入您要取的取款金额:"))
    stb =bank.bank_wda(account,user.getPassword(),bank.getMoney())
    if stb == 1:
        print("账号不存在")
    if stb == 2:
        print("密码不对")
    if stb == 3:
        print("钱不够")
def tran():
    account1 =input("请输入转出的账号:")
    account2 =input("请输入转入的账号:")
    password =input("请输入转出账号密码:")
    bank.setMoney(input("请输入转出金额:"))
    stc =bank.bank_tran(account1,account2,password,bank.getMoney())
    if stc == 1:
        print("正常")
        if stc==2:
            print("账号不对")
        if stc== 3:
            print("钱不够")
def query():
    account=input("请输入账号:")
    password =input("请输入密码:")
    ste=bank.bank_query(account,password)
    if ste == 0:
        print("该用户不存在")
    if ste == 1:
        print("输入信息错误")
    if ste ==2:
        sql="select * from users where users.account= %s"
        param=[account]
        data=dBUtils.select(sql,param)

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

    welcome.welcome()
    num = input("请输入您的业务编号：")
    if num.isdigit():
        num = int(num)
        if num == 1:
            addUser()
        elif num == 2:
            save()
            pass
        elif num == 3:
            wda()
            pass
        elif num == 4:
            tran()
            pass
        elif num == 5:
            query()
            pass
        elif num == 6:
            print("拜拜了您嘞，欢迎下次光临！！！")
            break
        else:
            print("输入非法！请重新输入！！！别瞎弄！！！")
    else:
        print("您输入非法！请重新输入！！！")
