from  selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.suning.com/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("笔记本")
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()
driver.find_element_by_xpath("//*[@id='pop418']/a").click()
driver.find_element_by_xpath("//*[@id='0000000000-12276998611']/div/div/div[3]/a[3]").click()
time.sleep(3)
wins =driver.window_handles
driver.switch_to.window(wins[1])
driver.find_element_by_xpath("//*[@id='addCart']").click()
time.sleep(3)
driver.quit()