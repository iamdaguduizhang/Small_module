# -*- coding: utf-8
import pickle
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class MyChrom(object):

    def create_driver(self, chrom_kind):
        """
        创建有头或者无头的浏览器
        :param chrom_kind: 1有头 0无头，
        :return:
        """
        chrome_options = Options()
        if chrom_kind:
            chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        else :
            chrome_options.add_argument('--headless')

        # 设置不加载图片
        prefs = {"profile.managed_default_content_settings.images": 2}
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument( 'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
        #                              'like Gecko) Chrome/65.0.3325.146 Safari/537.36"')
        # chrome_options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(chrome_options=chrome_options)
        return driver

    def get_noheadless_cookie(self, url, operation_time, driver_kind=1):
        """
        获得cookie的方法
        :param driver_kind: 浏览器是否有头，此处默认为有头的浏览器
        :param url: 要登陆的网址
        :param operation_time: 给自己预留的操作时间（完成登陆的过程）
        :return: 无返回值，结果将cookie保存在当前目录的cookie_result中去
        """
        driver = self.create_driver(driver_kind)
        driver.get(url)
        time.sleep(int(operation_time))
        # 获取cookie，此处的cookies
        cookies = driver.get_cookies()
        with open('cookie_result.txt', 'w') as fp:
            fp.write(str(cookies))
        time.sleep(2)
        driver.get_screenshot_as_file('result.png')
        driver.quit()
        return '保存cookie成功'

    def use_cookie(self, url, driver_kind=0):
        """
        此处为使用拿到的cookie进行登录
        :param url: 尝试使用cookie登陆的网址
        :param driver_kind: 此处默认无头
        :return:
        """
        driver = self.create_driver(driver_kind)
        driver.get(url)
        with open('cookie_result.txt', 'r') as fp:
            cookies = eval(fp.read())
        for x in cookies:
            print x
            driver.add_cookie(cookie_dict=x)
        time.sleep(3)
        driver.refresh()
        # 查看结果
        driver.get_screenshot_as_file('result2.png')
        driver.quit()
        # self.save_chrom_feature(driver)

    def save_chrom_feature(self, driver):
        """
        次函数用于保存浏览器的特征值,使得打开的浏览器驱动可以再次使用
        :param driver:
        :return:
        """
        print'=' * 20
        params = {}
        params["session_id"] = driver.session_id
        params["server_url"] = driver.command_executor._url
        f = open("params.data", 'wb')
        pickle.dump(params, f)
        f.close()
        print '=================特征值已保存================='

# 这个模块里边要做那些事情呢，
# 有些网站不能无头登陆，那就有头模拟登陆，获得cookie，然后再将cookie加到无头浏览器中去。
# 一：登陆网站，保存cookie  有头
# 二：登陆网站，查看是否成功  无头
