from  threading import  Thread
import  time
basket=0
num=0
class people(Thread):
    chef=""
    count=0
    def run(self) -> None:
        global basket
        global num
        while num <=300:
         if basket >=300:
          time.sleep(3)
          break
         else:
            count=self.count+1
            basket=basket+1
            print(self.chef,"造了1一个面包","总共造了",count,"个面包")

class  people2(Thread):
    customer=""
    count=0
    money=0
    def run(self) -> None:
        global basket
        global  num
        while num <=300:
            if basket<=0:
                print(self.customer,"没有抢到面包")
            else:
                 count=self.count+1
                 basket=basket-1
                 money=10*count
                 print(self.customer,"抢到一个面包","总共买了",count,"个面包","花了",money,"钱")
class  time11(Thread):
      def run(self) -> None:
          global num
          while True:
              if num<301:
                time.sleep(1)
                num=num+1
p1=people()
p2=people()
p3=people()
p4=people()
p5=people()
p6=people()
p7=people2()
p8=people2()
p9=people2()
p10=people2()
p11=people2()
t=time11()
p1.chef="1"
p2.chef="2"
p3.chef="3"
p4.chef="4"
p5.chef="5"
p6.chef="6"
p7.customer="7"
p8.customer="8"
p9.customer="9"
p10.customer="10"
p11.customer="11"
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()
p7.start()
p8.start()
p9.start()
p10.start()
p11.start()
t.start()
