# -*- coding: utf-8 -*-

import time
import redis
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle
r = redis.Redis(host='116.255.163.127', port=6379, password='BDVxnhaTmYl0w42o')  # redis 服务器
# r = redis.Redis('127.0.0.1', port=6379, password='08200redis')
while 1:
	time.sleep(1)
	print '正在执行'
	pc_login_flag = r.get('pc_flag')
	if pc_login_flag == '2':
		print '循环外'
		for x in range(1):
			try:
				time.sleep(2)
				print '循环内'
				cookies_nums = r.llen('cookie_pool')
				# if cookies_nums > 15:
				# 	continue
				with open('params' + str(x) + '.data', 'w') as fp:
					fp.write('')

				# 创建浏览器对象
				chrome_options = Options()
				chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
				driver = webdriver.Chrome(chrome_options=chrome_options)
				# driver.get('https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d9xdMSnC&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F')

				# 32-61,
				if x < 9:
					print '第%s次打开浏览器登录淘宝' % str(x + 1)
					driver.get('https://login.taobao.com/member/login.jhtml')
					driver.find_element_by_xpath('//*[@class="forget-pwd J_Quick2Static"]').click()
					driver.get_screenshot_as_file('test.png')
					time.sleep(1)
					driver.find_element_by_xpath('//*[@class="weibo-login"]').click()
					time.sleep(2)

					# 随机选取一组用户密码，通过微博登录淘宝
					a = [['15313296291', 'qishi123456'],['15137728278', 'daodou12345'], ['movie_protection@rightknights.com','Qishi123456'],['2335084018@qq.com', 'fuxiaolei123'],['13675148457','qishi6666']]
					# user_password = a[random.randint(0, len(a)-1)]
					user_password = a[0]
					user = user_password[0]
					password = user_password[1]
					driver.find_element_by_name('username').send_keys(user)
					time.sleep(3)
					driver.find_element_by_name('password').send_keys(password)
					time.sleep(2)
					driver.find_element_by_xpath('//*[@class="btn_tip"]/a/span').click()
					time.sleep(5)

					# 当访问的频率过高的时候要随意点击一个商品才能拿到cookie
					# if r.get('click_flag') == '1':
					driver.find_element_by_xpath('//*[@class="search-hots-lines"]/div[1]/a[2]').click()
					time.sleep(5)
					#
					# 移动鼠标到个人，退出当前登录状态
					# user = driver.find_element_by_xpath('//*[@class="site-nav-login-info-nick "]')
					# webdriver.ActionChains(driver).move_to_element(user).perform()
					# time.sleep(5)
					# driver.find_element_by_xpathth('//*[@class="site-nav-user-operate"]/a[2]').click()

				# 转储对象至文件
				time.sleep(5)
				handles = driver.window_handles
				one_handles = driver.current_window_handle
				two_handles = None
				for handle in handles:
					if handle != one_handles:
						two_handles = handle
				driver.switch_to.window(two_handles)

				# 获取cookie，此处的cookies
				cookies = driver.get_cookies()
				with open('cookie_result.txt', 'w') as fp:
					print('pppp')
					fp.write(str(cookies))
				time.sleep(2)


				print driver.current_url, '==>>>'
				print'=' * 20
				params = {}
				params["session_id"] = driver.session_id
				params["server_url"] = driver.command_executor._url
				f = open("params" + str(x) +".data", 'wb')
				pickle.dump(params, f)
				f.close()
				time.sleep(3)

			except Exception, e:
				print '浏览器执行过程中出现异常,结束此次循环', e
				# driver.quit()
				continue

			else:
				print '此次循环没问题'

		print '循环%s次结束，设置h5_flag为1' % str(x+1)
		time.sleep(20)
		r.set('h5_flag', '2')
		r.set('pc_flag', '1')





















# 之前的问题是拿到的cookie可能是不能用的，
# 现在可以拿到确定是可以用的cookie，问题在于更换cookie这里，旧的cookie不能用了，
# 现在不能让淘宝开着了，
	# 如果拿到的cookie不能用了，就把这个cookie给删了，然后继续拿cookie继续判断，直到拿到的cookie是可以用的
	# 才继续向下走代码，

# 问题，是让每两小时获得一批cookie呢，还是说当知道cookie失效了后删除的时候去获得呢。？那第二种的话，如何保证运行的实时性呢、？

# 一直循环，表示为0，不去操作浏览器，失效的时候，表示为1，此时打开五次浏览器，然后修改h5标识,h5执行，然后获得cookie，
# 我靠，，像淘宝这样，你爬取它，他肯定是会知道的，然后它先不管你，它查看你是怎么爬的它，然后在你的爬虫的某些关键的地方进行
# 进行一些反爬，那你的爬虫就没得搞了，
# 获取cookie池里的cookie，失效的话就将cookie删除，并去添加新的cookie
	# 任务死循环，获取到有效的cookie才会退出，
		# 为防止任务一直不退出，一个任务如果执行三分钟还没获取到有效cookie则退出。
		# 哪一个任务如果执行的时间大于三分钟呢（大于三分钟的判断在没有获取到cookie的时候进行）
