# credit : https://ianlondon.github.io/blog/web-scraping-discovering-hidden-apis/


#import library 
from bs4 import BeautifulSoup
import urllib, json
import pandas as pd
import sys ,re,time


url="https://app.bluemove.es/api/public/locations/list?cityId=100&accountId=1"

def extract_data():
	pass 


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



def main_():
	print (url)
	opener=urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	page = opener.open(url)
	soup = BeautifulSoup(page)
	geo_data =  dict(json.loads(soup.text))
	geo_data_ = geo_data['data']['locations']
	print (geo_data_)
	print ('length of data :',len(geo_data_) )

	# transfer to  dataframe 
	output = [[] for k in range(5)]
	for count in range(len(geo_data['data']['locations'])):
		scraped_data = geo_data['data']['locations'][count]
		for k,j in enumerate(scraped_data['Location']['vehicles']):
		    #print (k)
			output[0].append(scraped_data['Location']['vehicles'][k]['id'])
			output[1].append(scraped_data['Location']['vehicles'][k]['gpslat'])
			output[2].append(scraped_data['Location']['vehicles'][k]['gpslong'])
			output[3].append(scraped_data['Location']['vehicles'][k]['gps_timestamp'])
			output[4].append(scraped_data['Location']['vehicles'][k]['status'])
	df_ = pd.DataFrame(output).T
	df_.columns = [['id','gpslat','gpslong','gps_timestamp','status']]
	print (df_) 




if __name__ == '__main__':
	main_()







