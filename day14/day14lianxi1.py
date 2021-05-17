import time
class Oldphone:
    _brand=""

    def setBrand(self,brand):
        self._brand=brand
    def getBrand(self):
        return self._brand
    def call(self,number):
        print("正在给",number,"打电话")
class Newphone(Oldphone):
    def call(self,number):
        print("语音拨号中")
        for i in range(3):
            time.sleep(1)
            print(".",end="")
        super().call(number)
    def ab(self):
        print("品牌为:", self.getBrand(),"的手机很好用")
a=Newphone()
a.setBrand("华为")
a.call("1352000045")
a.ab()

