
from selenium import webdriver
import time
import xml.dom.minidom
import profile

url = "http://service.js.10086.cn/login.html?url=http://service.js.10086.cn/PERSON_BUSI.html?t=1549068705893"
timeout = 60
sleeptime = 60
phone=""
secret=""

#获取用户名和密码
item = profile.yewubanliprofile()
phone = item['phone']
print("banliyewu.py   phone:"+phone)
passwd = item['passwd']
print("banliyewu.py   passwd:" + passwd)

try:
    driver = webdriver.Firefox()
    start = time.time()
    driver.get(url)
    driver.find_element_by_id("userNumber").send_keys(phone)
    driver.find_element_by_id("userPassword").click()
    driver.find_element_by_id("userPassword").send_keys(passwd)
    driver.find_element_by_id("popBox-login-button").click()
    print('start time')
    print(driver.title)
    #logger.logspendtime(site,time.time()-start)
    print("spend time " + str(time.time()-start) + "s")
    driver.quit()
    driver = None
except Exception as err:
    print(err)
    driver.save_screenshot('F:\screen.png')
    #logger.logspendtime(site, timeout)
    print("err happend. spend time " + str(timeout) + "s")
    if driver != None:
        driver.quit()
