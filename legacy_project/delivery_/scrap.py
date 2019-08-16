import pandas as pd
import numpy as np 
import datetime
import urllib, json
from bs4 import BeautifulSoup

def get_weather_data(year,month):
	#url_ = "https://www.wunderground.com/history/airport/EDDT/2014/12/01/MonthlyCalendar.html?req_city=Werftpfuhl&req_statename=Germany&reqdb.zip=00000&reqdb.magic=46&reqdb.wmo=10389#calendar"
	url_ = "https://www.wunderground.com/history/airport/EDDT/{}/{}/01/MonthlyCalendar.html?req_city=Werftpfuhl&req_statename=Germany&reqdb.zip=00000&reqdb.magic=46&reqdb.wmo=10389#calendar".format(year,month)
	print (url_)
	# query the page 
	opener=urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	page = opener.open(url_)
	soup = BeautifulSoup(page)
	# set up output and filter data by attrs 
	output = [[] for k in range(3)]
	for k in soup.find_all('td', attrs={'class': 'value-header'}):
	    output[0].append(k.text)
	    
	for k in soup.find_all('span', attrs={'class': 'high'}):
	    output[1].append(k.text)
	    
	for k in soup.find_all('span', attrs={'class': 'low'}):
	    output[2].append(k.text)

	output_ =pd.DataFrame(output).T
	output_.columns = ['type','temp_max','temp_min']
	# get day list in 2014 
	sample_dates = pd.date_range(start='2014-01-01',end='2014-12-31', freq='d')
	datetimelist = []
	# get day list in specific month 
	for x in sample_dates:
		# '1'.zfill(2) = 01 , '11'.zfill(2) = 11 
		month_ = str(month).zfill(2)
		if str(x)[:7] == '{}-{}'.format(year,month_):
	        #print (str(x))
			datetimelist.append(pd.to_datetime(x))
		else:
			pass
	datetime_ = pd.DataFrame(datetimelist)
	datetime_.columns=['CET']
	# duplicate datetime data, since there are Actual, and Average  weather data 
	datetime_ = pd.concat([datetime_]*2).sort_values('CET').reset_index()
	#datetime_.head()
	output_['CET'] = np.array(datetime_.CET)
	print (output_)
	return output_