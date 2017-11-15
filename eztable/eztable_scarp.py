# python 3 


from selenium import webdriver
import time, re
from bs4 import BeautifulSoup


url = 'https://tw.eztable.com/search?q=%E6%97%A5%E6%9C%AC%E6%96%99%E7%90%86'

driver = webdriver.Firefox()
driver.implicitly_wait(3)
driver.get(url)

for i in range(1,10):
	driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
	time.sleep(1)


soup = BeautifulSoup(driver.page_source, "html5lib")
for block in soup.find_all('h5'):
	print (block.text)
