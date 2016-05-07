import cookielib
import urllib2
import urllib
import time
import ssl

"""
gateway_tools.py
~~~~~~~~~~~~~~~~~~~~~~~
Author: ZhangYunHao
Version:1.3 for windows
Time:2016-5-7 12:16

This module function is provide gateway tools.
Including all the tools needed to be used.
Select function 'login' or 'logout' by change variable 'Choose' at the end of program.
"""

# Ignore SSL certificate for all
ssl._create_default_https_context = ssl._create_unverified_context


def url_read(url, timeout=1, sleep=1):
	"""Read URL content.Also slove delay mistake and print error's reason."""
	request = urllib2.Request(url)

	try:
		response = urllib2.urlopen(request, timeout=timeout)
	except urllib2.URLError, e:
		print time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
		print e.reason
		print 'url_read Error:Please check your network connection !!!'
		time.sleep(sleep)
		url_read(url)
		return 0

	result = response.read()

	return result


def login_gateway_test(userid, password):
	"""" use username and password to login gateway for test."""

	url_login = 'https://ids.cau.edu.cn/amserver/UI/Login?module=LDAP&IDToken1=%s&IDToken2=%s' % (userid, password)

	flag = url_read(url_login).find('Redirecting')

	return flag


def login_gateway(userid, password):
	data = {
		"DDDDD": userid,
		"upass": password,
		"AMKKey": '',
		"v6ip": ''
	}

	headers = {
		'Host': '202.205.80.10',
		'Origin': 'http://202.205.80.154',
		'Referer': 'http://202.205.80.154/',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
	}

	#  Encode post_data to specific format.
	post_data = urllib.urlencode(data)
	#  Login_url.
	login_url = 'http://202.205.80.10/1.htm'
	request = urllib2.Request(login_url, post_data, headers)
	urllib2.urlopen(request)


def logout_gateway():
	url_logout = 'http://202.205.80.10/F.htm'
	request = urllib2.Request(url_logout)
	urllib2.urlopen(request)


def login_gateway_wifi(username, password):
	"""" use username and password to login WIFI gateway."""

	data = {
		"DDDDD": username,
		"upass": password,
		"0MKKey": ""
	}

	headers = {
		'Host': '202.205.80.9',
		'Origin': 'http://202.205.80.9',
		'Referer': 'http://202.205.80.9/0.htm',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
	}

	#  Encode post_data to specific format.
	post_data = urllib.urlencode(data)
	#  Login_url.
	login_url = 'http://202.205.80.9/0.htm'

	# Create cookie processor to save cookie for next url.
	cj = cookielib.LWPCookieJar()
	cookie_support = urllib2.HTTPCookieProcessor(cj)
	opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
	urllib2.install_opener(opener)

	request = urllib2.Request(login_url, post_data, headers)
	urllib2.urlopen(request)

	opener.open('http://202.205.80.9/1.htm')


def logout_gateway_wifi(username, password):
	"""" use username and password to logout WIFI gateway."""

	data = {
		"DDDDD": username,
		"upass": password,
		"0MKKey": ""
	}

	headers = {
		'Host': '202.205.80.9',
		'Origin': 'http://202.205.80.9',
		'Referer': 'http://202.205.80.9/0.htm',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
	}

	#  Encode post_data to specific format
	post_data = urllib.urlencode(data)
	#  Login_url
	login_url = 'http://202.205.80.9/0.htm'

	# Create cookie processor to save cookie for next url.
	cj = cookielib.LWPCookieJar()
	cookie_support = urllib2.HTTPCookieProcessor(cj)
	opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
	urllib2.install_opener(opener)

	request = urllib2.Request(login_url, post_data, headers)
	urllib2.urlopen(request)

	opener.open('http://202.205.80.9/F.htm')


def text_save(content, filename, mode='a'):
	# Try to save a list variable in txt file.
	file = open(filename, mode)
	for i in range(len(content)):
		file.write(str(content[i]) + '\n')
	file.close()


def text_read(filename):
	# Try to read a txt file and return a list.Return [] if there was a mistake.
	try:
		file = open(filename, 'r')
	except IOError:
		error = []
		return error
	content = file.readlines()

	for i in range(len(content)):
		content[i] = content[i][:len(content[i]) - 1]

	file.close()
	return content


def check_set():
	"""Detect if there is a setup file('gateway.setup')."""
	try:
		open('gateway.setup', 'r')
	except IOError:
		return -1
	return 2


def set():
	"""Create a setup file to save user's id and password."""
	print 'Please set up your userid and password.(Press enter to end input)'

	userid = raw_input('Please input your userid:')
	password = raw_input('Please input your password:')

	if login_gateway_test(userid, password) > 1:
		print 'Settings succeeded'
		list_t = [userid, password]
		text_save(list_t, 'gateway.setup', mode='w')
	if login_gateway_test(userid, password) < 1:
		print 'Failed to login,please check your input!'
		print '                           '
		set()
		return 0


def check_wifi():
	"""Test network is cable network or WIFI"""
	url = 'http://202.205.80.9/0.htm'
	request = urllib2.Request(url)
	try:
		urllib2.urlopen(request, timeout=0.3)
	except urllib2.URLError:
		return -1
	return 2


def log():
	if choose == 'login':
		if check_wifi() > 1:
			login_gateway_wifi(userid, password)
			print 'successful login WIFI!'
		else:
			login_gateway(userid, password)
			print 'successful login gateway!'
	if choose == 'logout':
		if check_wifi() > 1:
			logout_gateway_wifi(userid, password)
			print 'successful logout WIFI!'
		else:
			logout_gateway()
			print 'successful logout gateway!'


# Check setup.
if check_set() < 1:
	set()
else:
	print 'Successful read setup......'

# Load setup file.
list_user = text_read('gateway.setup')

# Get user's userid and password.
userid = list_user[0]
password = list_user[1]

# Choose login or logout.
choose = 'login'
while 1:
	time.sleep(1)
	log()
