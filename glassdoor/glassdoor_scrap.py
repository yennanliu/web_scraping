# -*- coding: utf-8 -*-


#=======================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
# https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest, time, re
from bs4 import BeautifulSoup
import argparse

# parse parameter from command line to python 
# https://docs.python.org/3/howto/argparse.html


# open firefox as browser
browser = webdriver.Firefox()
# set up site url
#base_url = "https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=data+&sc.keyword=data+&locT=C&locId=2671300&jobType=" 
base_url = "https://www.glassdoor.com/Job/london-data-jobs-SRCH_IL.0,6_IC2671300_KE7,11.htm"
print (base_url)
browser.get(base_url)



