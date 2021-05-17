class chef:
    _name=""
    _age=""
    def setName(self,name):
        self._name=name
    def getName(self):
        return self._name
    def setAge(self,age):
        self._age=age
    def getAge(self):
        return  self._age
    def abb(self):
        print("蒸饭1")
class cheff(chef):
     def abd(self):
        print("炒菜2")
class chefff(cheff):
     def abb(self):
         print("蒸饭")
     def abd(self):
         print("炒菜")
class test:
 a=chefff()
 a.setName("张三")
 a.setAge("30")
 print(a.getName(),a.getAge())
b=chefff()
b.abb()
b.abd()