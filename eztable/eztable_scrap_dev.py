# python 3 


from selenium import webdriver
import time, re
from bs4 import BeautifulSoup



def enter_text(xpath, text, driver):
    textbox = driver.find_element_by_xpath(xpath)
    textbox.send_keys(text)


# grab "steak restaurant "
url = 'https://tw.eztable.com/'
# set up selenium driver (via firefox)
driver = webdriver.Firefox()
driver.implicitly_wait(3)
driver.get(url)

xpath_ = ".//input[@class='search-input']"
enter_text(xpath_, "japan" , driver)






