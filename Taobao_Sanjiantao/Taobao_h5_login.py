# -*- coding: utf-8 -*-
import time
import redis
import pickle


try:
    import http.client as http_client
except ImportError:
    import httplib as http_client
import socket
from selenium.webdriver.chrome.webdriver import WebDriver as  Chrome
from selenium.webdriver.chrome.remote_connection import ChromeRemoteConnection
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.remote.errorhandler import ErrorHandler
from selenium.webdriver.remote.switch_to import SwitchTo
from selenium.webdriver.remote.mobile import Mobile
from selenium.webdriver.remote.file_detector import FileDetector, LocalFileDetector
from selenium.webdriver.remote.command import Command


class myWebDriver(Chrome):
    def __init__(self, capabilities=None, service_url=None, session_id=None):
        if service_url is None and session_id is None:
            raise NameError

        if capabilities is None:
            capabilities = DesiredCapabilities.FIREFOX.copy()

        self.capabilities = dict(capabilities)
        self.w3c = True
        executor = ChromeRemoteConnection(remote_server_addr=service_url)
        self.session_id = session_id
        self.command_executor = executor
        self.command_executor.w3c = self.w3c
        if type(self.command_executor) is bytes or isinstance(self.command_executor, str):
            self.command_executor = RemoteConnection(self.command_executor, keep_alive=True)
        self._is_remote = True
        self.error_handler = ErrorHandler()
        self._switch_to = SwitchTo(self)
        self._mobile = Mobile(self)
        self.file_detector = LocalFileDetector()


    def quit(self):
        """Quits the driver and close every associated window."""
        try:
            self.execute(Command.QUIT)
        except (http_client.BadStatusLine, socket.error):
            # Happens if Firefox shutsdown before we've read the response from
            # the socket.
            pass


r = redis.Redis('127.0.0.1', port=6379, password='08200redis')
while 1:

    time.sleep(1) 
    print '等待'
    h5_flag = r.get('h5_flag')
    if h5_flag == '2':
            for x in range(1):
                try:
                    time.sleep(5)
                    f = open("params"+ str(x) + ".data", 'rb')
                    params = pickle.load(f)
                    print(params)

                    browser = myWebDriver(service_url=params["server_url"],session_id=params["session_id"])

                    print '第%s次打开浏览器登录h5' %(x + 1)
                    time.sleep(5)
                    browser.get('https://s.m.taobao.com/h5?q=%E4%B8%83%E5%8C%B9%E7%8B%BC&sst=1&n=20&buying=buyitnow')
                    time.sleep(5)

                    #获得cookie和token
                    cookies_begin = browser.get_cookies()
                    cookies = ""
                    token = ""
                    for cookie in cookies_begin:
                        cookies += cookie.get('name') + '=' + cookie.get('value') + ';'
                        if cookie.get('name') == '_m_h5_tk':
                            token = cookie.get('value').split('_')[0]
                            print (token)
                            r.set('token', token)
                    time.sleep(10)
                    r.set('cookies', cookies)
                    r.lpush('cookie_pool',  str({'token':token, 'cookie':cookies}))
                    print ('cookies保存成功')
                    print(cookies)
                    a = input('p:')

                    if 'https://login.m.taobao.com/login.htm?' in browser.page_source:
                        r.set('click_flag', '1')
                    browser.quit()

                except Exception, e:
                    print '此次循环出错'
                    continue

                else:
                    print '此次循环没问题'

            r.set('h5_flag', '1')



