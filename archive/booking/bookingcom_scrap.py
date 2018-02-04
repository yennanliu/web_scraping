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
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)
print ('===========')


# open firefox as browser
browser = webdriver.Firefox()
# set up site url 
#base_url="https://www.booking.com/searchresults.zh-tw.html?aid=304142&label=gen173nr-1FCAEoggJCAlhYSDNiBW5vcmVmaOcBiAEBmAEwuAEHyAEP2AEB6AEB-AEMkgIBeagCAw&sid=fc93df7eb22345d0203784b4d254c349&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.zh-tw.html%3Faid%3D304142%3Blabel%3Dgen173nr-1FCAEoggJCAlhYSDNiBW5vcmVmaOcBiAEBmAEwuAEHyAEP2AEB6AEB-AEMkgIBeagCAw%3Bsid%3Dfc93df7eb22345d0203784b4d254c349%3Bcheckin_month%3D6%3Bcheckin_monthday%3D16%3Bcheckin_year%3D2017%3Bcheckout_month%3D6%3Bcheckout_monthday%3D17%3Bcheckout_year%3D2017%3Bclass_interval%3D1%3Bdest_id%3D17%3Bdest_type%3Dairport%3Bgroup_adults%3D2%3Bgroup_children%3D0%3Blabel_click%3Dundef%3Bmap%3D1%3Bmih%3D0%3Bno_rooms%3D1%3Boffset%3D33%3Braw_dest_type%3Dairport%3Broom1%3DA%252CA%3Brows%3D33%3Bsb_price_type%3Dtotal%3Bsearch_selected%3D1%3Bsrc%3Dindex%3Bsrc_elem%3Dsb%3Bss%3D%25E9%25A6%2599%25E6%25B8%25AF%25E8%25B5%25A4%25E9%25B1%25B2%25E8%25A7%2592%25E5%259C%258B%25E9%259A%259B%25E6%25A9%259F%25E5%25A0%25B4%252C%2520%25E9%25A6%2599%25E6%25B8%25AF%252C%2520%25E9%25A6%2599%25E6%25B8%25AF%3Bss_raw%3Dhk%3Bssb%3Dempty%26%3B&ss=NYC&ssne=%E8%B5%A4%E9%B1%B2%E8%A7%92&ssne_untouched=%E8%B5%A4%E9%B1%B2%E8%A7%92&checkin_year=2017&checkin_month=6&checkin_monthday=16&checkout_year=2017&checkout_month=6&checkout_monthday=17&room1=A%2CA&group_adults=2&group_children=0&no_rooms=1&highlighted_hotels=&dest_id=&dest_type=&search_pageview_id=024242b9a80c0437&search_selected=false"
base_url="https://www.booking.com/searchresults.zh-tw.html?aid=304142&label=gen173nr-1FCAEoggJCAlhYSDNiBW5vcmVmaOcBiAEBmAEwuAEHyAEP2AEB6AEB-AEMkgIBeagCAw&sid=fc93df7eb22345d0203784b4d254c349&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.zh-tw.html%3Faid%3D304142%3Blabel%3Dgen173nr-1FCAEoggJCAlhYSDNiBW5vcmVmaOcBiAEBmAEwuAEHyAEP2AEB6AEB-AEMkgIBeagCAw%3Bsid%3Dfc93df7eb22345d0203784b4d254c349%3Bcheckin_month%3D6%3Bcheckin_monthday%3D16%3Bcheckin_year%3D2017%3Bcheckout_month%3D6%3Bcheckout_monthday%3D17%3Bcheckout_year%3D2017%3Bclass_interval%3D1%3Bdest_id%3D17%3Bdest_type%3Dairport%3Bgroup_adults%3D2%3Bgroup_children%3D0%3Blabel_click%3Dundef%3Bmap%3D1%3Bmih%3D0%3Bno_rooms%3D1%3Boffset%3D33%3Braw_dest_type%3Dairport%3Broom1%3DA%252CA%3Brows%3D33%3Bsb_price_type%3Dtotal%3Bsearch_selected%3D1%3Bsrc%3Dindex%3Bsrc_elem%3Dsb%3Bss%3D%25E9%25A6%2599%25E6%25B8%25AF%25E8%25B5%25A4%25E9%25B1%25B2%25E8%25A7%2592%25E5%259C%258B%25E9%259A%259B%25E6%25A9%259F%25E5%25A0%25B4%252C%2520%25E9%25A6%2599%25E6%25B8%25AF%252C%2520%25E9%25A6%2599%25E6%25B8%25AF%3Bss_raw%3Dhk%3Bssb%3Dempty%26%3B&ss={}&ssne=%E8%B5%A4%E9%B1%B2%E8%A7%92&ssne_untouched=%E8%B5%A4%E9%B1%B2%E8%A7%92&checkin_year=2017&checkin_month=6&checkin_monthday=16&checkout_year=2017&checkout_month=6&checkout_monthday=17&room1=A%2CA&group_adults=2&group_children=0&no_rooms=1&highlighted_hotels=&dest_id=&dest_type=&search_pageview_id=024242b9a80c0437&search_selected=false"
print (base_url)
base_url = base_url.format(args.echo)
browser.get(base_url)


page = 0                              
#while len(soup.select('.paging-start')) > 0:
while page < 2:
	page += 1 
	try: 
		#'======== start parse ========'
		soup = BeautifulSoup(browser.page_source,"html.parser")
		#for ele in soup.find_all('h3'):
		for ele in soup.findAll("span", { "class" : "sr-hotel__name" }):
			print ele.text 
		# next page 
		browser.find_element_by_link_text(u"下一頁").click()
		print 'page =' , page
		time.sleep(1)
	except Exception as e:
		print e, 'something failed'


#browser.close()




