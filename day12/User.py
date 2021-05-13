class User:
    __account=None
    __username=None
    __password=None
    __adress=None
    # __money=None
    def setAccount(self,account):
        self.__account=account
    def  getAccount(self):
        return self.__account
    def setUsername(self,username):
        self.__username=username
    def  getUsername(self):
        return self.__username
    def setPassword(self,password):
        self.__password=password

    def getPassword(self):
        return self.__password
    def setAdress(self,adress):
        self.__adress=adress
    def  getAdress(self):
        return self.__adress
    # def setMoney(self,money):
    #     self.__money=money
    # def  getMoney(self):
    #     return self.__money