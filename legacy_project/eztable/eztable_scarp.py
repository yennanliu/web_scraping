# python 3 


from selenium import webdriver
import time, re
from bs4 import BeautifulSoup

# grab "steak restaurant "
url = 'https://tw.eztable.com/search?q=%E7%89%9B%E6%8E%92'
# set up selenium driver (via firefox)
driver = webdriver.Firefox()
driver.implicitly_wait(3)
driver.get(url)
# set grab 50 pages 
for i in range(1,50):
	driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
	### wait 1 sec tull JS/ajax load the all contents 
	time.sleep(1)

# analysis web page generate by JS via BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html5lib")
for block in soup.find_all('h5'):
	# print restaurant name 
	print (block.text)
