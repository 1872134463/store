from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://8.129.91.152:8765/Index/reg.html")
driver.find_element_by_xpath("//*[@id='phone']").send_keys("13111418622")
time.sleep(10)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[3]/a").click()
time.sleep(10)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[4]/input").send_keys("zhangsan123456")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[5]/label/input").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[6]/button").click()
driver.quit()