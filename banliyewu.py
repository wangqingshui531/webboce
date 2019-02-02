from selenium import webdriver
import time
import profile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from mylog import log

url = "http://service.js.10086.cn/login.html?url=http://service.js.10086.cn/PERSON_BUSI.html?t=1549068705893"
timeout = 60
sleeptime = 60
phone=""
secret=""
pagename="yewubanli"

#获取用户名和密码
item = profile.yewubanliprofile()
phone = item['phone']
print("banliyewu.py   phone:"+phone)
passwd = item['passwd']
print("banliyewu.py   passwd:" + passwd)
logger=log()

try:
    driver = webdriver.Firefox()
    driver.get(url)
    driver.find_element_by_id("userNumber").send_keys(phone)
    driver.find_element_by_id("userPassword").click()
    driver.find_element_by_id("userPassword").send_keys(passwd)
    start = time.time()
    driver.find_element_by_id("popBox-login-button").click()
    print('start time')
    loc = (By.ID, 'diyBusiMain')
    wait = WebDriverWait(driver, timeout).until(expected_conditions.presence_of_element_located(loc))
    print(driver.title)
    logger.logspendtime(pagename,time.time()-start)
    print("spend time " + str(time.time()-start) + "s")
    time.sleep(5)
    driver.quit()
    driver = None
except Exception as err:
    print(err)
    driver.save_screenshot('F:\screen.png')
    #logger.logspendtime(site, timeout)
    print("err happend. spend time " + str(timeout) + "s")
    if driver != None:
        driver.quit()