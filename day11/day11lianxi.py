class cup:
    __height=0
    __volume=0
    __color=""
    __tom=""
    def setheight(self,height):
        self.__height=height
    def getheight(self):
        return self.__height
    def setvolume(self,volume):
        self.__volume=volume
    def getvolume(self):
        return self.__volume
    def setcolor(self,color):
        self.__color=color
    def getcolor(self):
        return self.__color
    def settom(self,tom):
        self.__tom=tom
    def gettom(self):
        return self.__tom
    def gongneng(self):
        print("属性为:",  self.__height,self.__volume,self.__color,self.__tom,"能装水")
a=cup()
a.setheight("20cm")
a.setvolume("1l")
a.setcolor("蓝色")
a.settom("塑料")
a.gongneng()