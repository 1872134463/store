from selenium import  webdriver
import time
driver =webdriver.Chrome()#创建浏览器对象
driver.get(r"file:///C:/Users/18721/AppData/Local/Temp/Rar$EXa2612.49688/%E8%B5%84%E6%96%99/%E7%BB%83%E4%B9%A0%E7%9A%84html/%E7%BB%83%E4%B9%A0%E7%9A%84html/%E5%BC%B9%E6%A1%86%E7%9A%84%E9%AA%8C%E8%AF%81/dialogs.html") #输入网址
driver.find_element_by_id("alert").click()
time.sleep(3)
driver.switch_to.alert.accept()#accept点击确定
time.sleep(3)
driver.quit()#退出浏览器
