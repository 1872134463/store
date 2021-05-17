class people:
    _name=""
    _age=""
    _sex=""
    def setName(self,name):
        self._name=name
    def getName(self):
        return self._name
    def setAge(self,age):
        self._age=age
    def getAge(self):
        return  self._age
    def setSex(self,sex):
        self._sex=sex
    def getSex(self):
        return  self._sex
class worker(people):
     def aaa(self):
          print("干活")
class student(people):
    __sid = None
    def setSid(self,sid):
        self.__sid = sid
    def getSid(self):
        return self.__sid
    def study(self):
         print("学习")
    def sing(self):
         print("唱歌")