# python 3 


from selenium import webdriver
import time, re
from bs4 import BeautifulSoup
from urllib.request import urlopen


# grab "steak restaurant "
url = 'http://www.google.com'
# set up selenium driver (via firefox)
driver = webdriver.Firefox()
#driver.get(url)
#element = driver.find_element_by_xpath("//input[@id='lst-ib']")
#element.send_keys('abcde')

keywords = ['sss','jp','usa']
keywords = ['日本']


for keyword in keywords:
	# access to website
	driver.get(url)
	element = driver.find_element_by_xpath("//input[@id='lst-ib']")
	element.send_keys(keyword)
	button = driver.find_element_by_xpath("//div[@class='jsb']/center/input[1]")
	button.click()
	# analyze website elements 
	current_url = driver.current_url
	page = urlopen(current_url)
	#html = driver.page_source
	#soup = BeautifulSoup(html)
	soup = BeautifulSoup(page, 'html.parser')
	for item in soup.find_all('b'):
		print (item.text)
	driver.implicitly_wait(10)
	#driver.get(url)


