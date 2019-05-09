# -*- coding: utf-8 -*-
import pickle
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument('-headless')
# firefox_options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Firefox(options=firefox_options)

driver.get('https://www.zhihu.com/signup?next=%2F')

#获取cookie，此处的cookies
time.sleep(30)
cookies = driver.get_cookies()
with open('firefox_cookie_result.txt', 'w') as fp:
    fp.write(str(cookies))
time.sleep(2)
driver.quit()

# 将拿到的cookie 添加到浏览器的cookie中去
# with open('firefox_cookie_result.txt', 'r') as fp:
#     cookies = eval(fp.read())
# for x in cookies:
#     print x
#     driver.add_cookie(cookie_dict=x)
# time.sleep(3)
# driver.refresh()

# 下边是将浏览器的特征存起来的，可以再次使用该浏览器对象
# print'=' * 20
# params = {}
# params["session_id"] = driver.session_id
# params["server_url"] = driver.command_executor._url
# f = open("params.data", 'wb')
# pickle.dump(params, f)
# f.close()

driver.get_screenshot_as_file('firefox_result.png')