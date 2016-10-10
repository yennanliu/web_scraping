import urllib 
import simplejson 
import sys
from urllib.request import urlopen
import csv
import requests
from bs4 import BeautifulSoup
import lxml
import urllib, json
import pandas as pd, numpy as np
import pprint
import datetime as dt 
from urllib.parse   import quote
#from BeautifulSoup import BeautifulSoup




def scrap():
	output = [[] for k in range(2)]
	q_ = '永和'
	url = 'http://www.google.com/search?q={}&start='.format(quote(q_)) +'&as_sitesearch=facebook.com' 
	sys.path.append("./BeautifulSoup")
	#opener = urllib2.build_opener()
	opener=urllib.request.build_opener()
	print (opener)
	print ('++++++++++++++++++')
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	
	for start in range(0,2):
		url = 'http://www.google.com/search?q={}&start={}'.format(quote(q_),str(start*10)) +'&as_sitesearch=facebook.com' 
		print  (url)
		page = opener.open(url)
		soup = BeautifulSoup(page)
		for k in soup.findAll('h3'):
			if "<b>" in str(k.find('a').contents[0]):
				output[0].append(k.find('a').contents[1])
			else:
				output[0].append(k.find('a').contents[0])
		for k in soup.findAll('cite'):
			output[1].append(k.contents[0])
		#print (output)
	output_ = pd.DataFrame(output).T
	output_.columns = ['name', 'url']
	print (output_)
	return output_
