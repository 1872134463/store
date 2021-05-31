from selenium import  webdriver
import time
driver=webdriver.Chrome()
driver.get(r"file:///C:/Users/18721/AppData/Local/Temp/Rar$EXa2612.28402/%E8%B5%84%E6%96%99/%E7%BB%83%E4%B9%A0%E7%9A%84html/%E7%BB%83%E4%B9%A0%E7%9A%84html/main.html")
driver.switch_to.frame("frame")
driver.find_element_by_id("input1").send_keys("45455")
time.sleep(2)
driver.quit()
