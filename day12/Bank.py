import random
from DBUtils import DBUtils
DB=DBUtils()

class Bank:
    DBUtils =DBUtils()


    __money = 0
    def setMoney(self,money):
        self.__money=money
    def  getMoney(self):
        return self.__money


    __bank_name="中国工商银行昌平支行"
    def getBank_name(self):
        return self.__bank_name


    def bank_addUser(self,account,username,password,country,province,street,door):

        # 判断是否已满
        sql="select count(*) from users"
        data=DB.select(sql,[])
        if len(data)>=100:
            return 3
        sql01 = "select * from users where users.account = %s"
        param1 = [account]
        data01=DB.select(sql01,param1)
        if len(data01)!=0:
            return  2
        sql02="insert into users values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param2=[account,username,password,country,province,street,door,0,self.__bank_name]
        DB.update(sql02,param2)
        return  1
    def bank_save(self,account,money):

        sql="select * from users where users.account = %s"
        param = [account]
        data=DB.select(sql,param)
        if  len(data)!=0:
            sql="update users set money = money + %s where account= %s"
            param=[money,account]
            DB.update(sql,param)

            return 1
        if   len(data)==0:
            return False
    def bank_wda(self,account,password,wdamoney):

        sql="select count(*) from users where users.account = %s"
        param = [account]
        data=DB.select(sql,param)

        if data[0][0] == 0:
            return 1
        if data[0][0] == 1:
            sql="select count(*) from users where users.account= %s and users.password=%s"
            param = [account,password]
            data = DB.select(sql,param)
            if data[0][0] == 1:
                sql2 = "select * from users where users.account= %s"
                param2 = [account]
                data2 = DB.select(sql2,param2)
                datanum =(str(data2[0][7]) )
                if datanum >= wdamoney:
                    sql="update users set users.money =users.money -%s where users.money>=%s"
                    param=(wdamoney,wdamoney)
                    DB.update(sql,param)
                    return 0
                else:
                    return 3
            else:
                return 2
    def bank_tran(self,account1,account2,password,money):
        sql="select count(*) from users where users.account= %s or users.account =%s"
        param=[account1,account2]
        data=DB.select(sql,param)
        if data[0][0]==2:
            sql="select count(*) from users where users.account= %s and users.password=%s"
            param=[account1,password]
            data=DB.select(sql,param)
            if data[0][0] == 1:
                sql="select * from users where users.account= %s"
                param=[account1]
                data=DB.select(sql,param)
                num=(str(data[0][7]))
                if num>=money:
                    sql="update users set users.money =users.money - %s where users.account=%s"
                    param1=[money,account1]
                    DB.update(sql,param1)
                    sql1="update users set users.money =users.money + %s where users.account=%s"
                    param2=[money,account2]
                    DB.update(sql1,param2)
                else:
                    return 3
            if data[0][0]==0:
                return 2
        else :
            return 1
    def bank_query(self,account,password):
        sql="select count(*) from users where users.account= %s"
        param = [account]
        data=DB.select(sql,param)
        if data[0][0]==1:
            sql="select count(*) from users where users.account= %s and users.password=%s"
            param=[account,password]
            data=DB.select(sql,param)
            if data[0][0]==1:
                return 2
            if data[0][0]==0:
                return 1
        if data[0][0 ]==0:
            return 0

