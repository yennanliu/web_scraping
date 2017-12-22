# credit : https://ianlondon.github.io/blog/web-scraping-discovering-hidden-apis/


#import library 
from bs4 import BeautifulSoup
import urllib, json
import pandas as pd
import sys ,re,time


url="https://app.bluemove.es/api/public/locations/list?cityId=100&accountId=1"

def main():
	print (url)
	opener=urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	page = opener.open(url)
	soup = BeautifulSoup(page)
	geo_data =  dict(json.loads(soup.text))
	geo_data_ = geo_data['data']['locations']
	print (geo_data_)
	print ('length of data :',len(geo_data_) )





if __name__ == '__main__':
	main()







