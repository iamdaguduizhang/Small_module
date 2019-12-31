# -*- coding:utf-8 -*-
# @Time    :2019/11/29 2:45 下午
# @Author  :Dg

import requests
import execjs
from scrapy import Selector
s = requests.session()

def spider():
    url = "http://www.landchina.com/default.aspx?tabid=226"
    response = s.get(url)

    text = response.text
    # f_js = re.findall("javascript\">(.*?)</script>", text)[0]
    print(text)
    ctx = execjs.compile("""
        function stringToHex(str) {
        var val = "";
        for (var i = 0; i < str.length; i++) {
            if (val == "") val = str.charCodeAt(i).toString(16);
            else val += str.charCodeAt(i).toString(16);
        }
        return val;
    }

    var width = "1920";
    var height = "1080";
    var screendate = width + "," + height;
    url = "/default.aspx?tabid=226&security_verify_data=" + stringToHex(screendate);
    return url;
    """)
    location = ctx.call("YunSuoAutoJump")
    second_url = "http://www.landchina.com" + location

    _ = s.get(second_url)

    res = s.get(url)
    print(res.text)
    selector = Selector(text=res.text)

    result = selector.css("#TAB_contentTable tr")[1:]
    td_list = result.css("td")
    print(td_list)

spider()