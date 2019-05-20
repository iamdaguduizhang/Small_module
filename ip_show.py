# -*- coding: utf-8 -*-

import time
import requests
from lxml import etree
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
}
url = 'http://2019.ip138.com/ic.asp'


def ip_show():

    response = requests.get(url=url, headers=header)
    content = etree.HTML(response.content)
    IP = content.xpath('//center/text()')[0]
    print IP
    time.sleep(5)


if __name__ == '__main__':
    ip_show()
