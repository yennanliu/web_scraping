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
import sys ,re, lxml,time

# transform chinese into web url in python 3 
# https://stackoverflow.com/questions/1695183/how-to-percent-encode-url-parameters-in-python/13625238#13625238
from urllib.parse import quote

# parse parameter from command line to python 
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)
print (quote(args.echo))
area = quote(args.echo)
print ('===========')



# help function 

def url_fix(x):
    return 'http://www.ipeen.com.tw' + x

def parse_area(x):
    return x[3:6]



def grab_raw(area):
    output = [[] for k in range(4)]
    for page in range(1,2):
	    #url_='http://www.ipeen.com.tw/search/all/000/0-100-0-0/?adkw=%E5%A4%A7%E5%AE%89%E5%8D%80&p={}'
	    url_='http://www.ipeen.com.tw/search/all/000/0-100-0-0/?adkw={}&p={}'
	    url_=url_.format(area,page)
	    print (url_)
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
	    time.sleep(1)
    print (output)
    return output

def grab_df():

	output = grab_raw(area)
	df = pd.DataFrame(output).T
	df.columns = ['name', 'address', 'url','style']
	df.url = df.url.apply(lambda x :url_fix(x) )
	df['area'] = df['address'].apply(lambda x :parse_area(x) )
	print (df.head())
	df.to_csv('ipeen_restaurant_0617.csv')
	return df 

if __name__ == '__main__':
	grab_df()




