from  selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.jd.com/")
driver.maximize_window()
driver.find_element_by_link_text("你好，请登录").click()
time.sleep(10)
driver.find_element_by_xpath("//*[@id='key']").send_keys("华为手机")
driver.find_element_by_xpath("//*[@id='search']/div/div[2]/button").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[4]/a/em").click()
wins=driver.window_handles
driver.switch_to.window(wins[1])
driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()
time.sleep(3)
driver.quit()

