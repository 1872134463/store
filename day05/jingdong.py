from appium import webdriver
import time
server = r'http://localhost:4723/wd/hub'      # Appium Server, 端口默认为4723
desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',          # 需替换成你的driverName
    'platformVersion': '7.1.2',
    'appPackage': 'com.jingdong.app.mall',
    'appActivity': 'com.jingdong.app.mall.main.MainActivity '
}
driver = webdriver.Remote(server, desired_capabilities) # 连接手机和APP
driver.find_element_by_id("bqd").click()
time.sleep(10)# 点击wlan
driver.find_element_by_id("bq").click()
time.sleep(3)
driver.tap(856,108)
driver.find_element_by_id("搜索框笔记本电脑").click()
time.sleep(5)
driver.find_element_by_id("a3g").send_keys("笔记本")
time.sleep(5)
driver.find_element_by_id("com.jingdong.app.mall:id/a9b").click()
time.sleep(5)
driver.find_element_by_xpath("	//android.widget.RelativeLayout[@content-desc='新品']").click()
time.sleep(5)
driver.find_element_by_id("	com.jd.lib.productdetail.feature:id/pd_invite_friend").click()
time.sleep(5)
driver.tap(450,1545)
driver.quit()