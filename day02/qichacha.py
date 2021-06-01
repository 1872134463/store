from selenium import webdriver
from  selenium.webdriver import ActionChains
import  time
driver=webdriver.Chrome()
driver.get("http://www.qcc.com")
driver.maximize_window()
time.sleep(6)
driver.find_element_by_xpath("//*[@id='addfavorModal']/div/div/div[1]").click()
driver.find_element_by_link_text("登录 | 注册").click()
time.sleep(3)
ele=driver.find_element_by_xpath("//*[@id='nc_1_n1z']")#获取滑块
ac =ActionChains(driver)
ac.click_and_hold(ele).move_by_offset(348,34).perform()
time.sleep(3)
driver.quit()

