from selenium import webdriver
from selenium.webdriver import  ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.maximize_window()
driver.find_element_by_id("kw").click()
time.sleep(2)
ac=ActionChains(driver)
ac.key_down("z"),ac.key_up("z").perform()
time.sleep(2)
driver.quit()


