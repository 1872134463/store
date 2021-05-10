class computer:
    __size=0
    __price=0
    __model=""
    __memorysize=0
    __standbytime=0
    def setsize(self,size):
        self.__size=size
    def  getsize(self):
        return self.__size
    def setprice(self,price):
        self.__price=price
    def getprice(self):
        return self.__price
    def setmodel(self,model):
        self.__model=model
    def getmodel(self):
        return self.__model
    def setmemorysize(self,memorysize):
        self.__memorysize=memorysize
    def getmemorysize(self):
        return self.__memorysize
    def setstandbytime(self,standbytime):
        self.__standbytime=standbytime
    def getstandbytime(self):
        return self.__standbytime
    def word(self):
        print(self.__model,"打字")
    def game(self):
        print(self.__model,"打游戏")
    def shipin(self):
        print(self.__model,"看视频")
    def  cc(self):
        print(self.__size,self.__price,self.__model,self.__memorysize,self.__standbytime)
a=computer()
a.setsize(16)
a.setprice(4000)
a.setmodel("惠普")
a.setmemorysize("8GB")
a.setstandbytime("4h")
a.word()
a.game()
a.shipin()
a.cc()