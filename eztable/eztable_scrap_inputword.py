# python 3 


from selenium import webdriver
import time, re
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

# grab "steak restaurant "
url = 'https://tw.eztable.com/search?q='
# set up selenium driver (via firefox)
driver = webdriver.Firefox()

keywords = ['港式','牛排','中餐']

for keyword in keywords:
	# access to website
	driver.get(url)
	# xpath for input word 
	element = driver.find_element_by_xpath("//input[@class='search-input']")
	element.send_keys(keyword)
	# xpath for search button 
	button = driver.find_element_by_class_name("search-btn")
	button.click()
	# get current url 
	print ('current_url : ', driver.current_url)
	driver.get(driver.current_url)
	# analyze html 
	soup = BeautifulSoup(driver.page_source, "html5lib")
	for block in soup.find_all('h5'):
		print (block.text)
	time.sleep(3)


