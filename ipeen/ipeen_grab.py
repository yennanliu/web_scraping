# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
import urllib 
#import simplejson 
from urllib.request import urlopen
from urllib.parse   import quote
import requests
from bs4 import BeautifulSoup
import urllib, json
import pandas as pd, numpy as np
import sys ,re, lxml



# help function 

def url_fix(x):
    return 'http://www.ipeen.com.tw' + x



def grab_raw():
    output = [[] for k in range(4)]
    for page in range(1,20):
	    #url ='http://www.ipeen.com.tw/search/all/000/0-100-0-0/%E4%B8%AD%E5%BC%8F/?p={}&adkw=%E5%8F%B0%E5%8C%97'.format(page)
	    #print (url)
	    url_='http://www.ipeen.com.tw/search/all/000/0-100-0-0/?adkw=%E5%A4%A7%E5%AE%89%E5%8D%80&p={}'
	    url_=url_.format(page)
	    opener=urllib.request.build_opener()
	    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	    page = opener.open(url_)
	    soup = BeautifulSoup(page)
	    for k in soup.find_all('a', attrs={'data-label': '店名'}):
	        output[0].append(k.text)

	    for k in soup.findAll('span',{"style":"padding-left:3em;"}):
	        output[1].append(k.get_text())
	    
	    for k in soup.find_all('a', {'class':"a37 ga_tracking"}):
	        if "/shop/" in str(k['href']):
	            output[2].append((k['href']))
	    for k in soup.find_all('a', attrs={'class': 'ga_tracking'}):
	        if "大分類" in str(k):
	            #print (k.text)
	            output[3].append((k.text))
	        
	        else:
	            pass
    print (output)
    return output

def grab_df():

	output = grab_raw()
	df = pd.DataFrame(output).T
	df.columns = ['name', 'address', 'url','style']
	df.url = df.url.apply(lambda x :url_fix(x) )
	print (df.head())
	df.to_csv('ipeen_restaurant_0617.csv')
	return df 


grab_df()




