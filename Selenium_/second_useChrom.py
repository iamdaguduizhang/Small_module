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


f = open("params.data", "rb")
params = pickle.load(f)
print(params)
driver = myWebDriver(service_url=params["server_url"], session_id=params["session_id"])
driver.get('http://s.weibo.com/weibo/高兴&nodup=1&page=1')
driver.get_screenshot_as_file('second_result.png')
