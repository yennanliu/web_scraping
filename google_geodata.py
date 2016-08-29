'''
ref :  https://pypi.python.org/pypi/geocoder
ref :  https://pypi.python.org/pypi/py-translate
ref :  https://developers.google.com/maps/documentation/geocoding/get-api-key
ref :  https://developers.google.com/maps/documentation/geocoding/start
'''

from IPython.display import display, HTML
import pandas as pd, numpy as np 
%pylab inline 
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import seaborn as sns
import time
import datetime as dt   
import os
from pandas import ExcelWriter
#import goslate
import requests





df = pd.read_excel('0701.xlsx')
df.columns
dd=df[['地址.1','區域']]
dd=dd.dropna()

# save as chinese 
dd.columns=['address','group']
dd.to_csv('test0701.csv',encoding='utf-8')



# google API part 

google_api = your_google_api_key
address='taipei 101'
url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(address,google_api)

r = requests.get(url)
results = r.json()
results['results'][0]['geometry']['bounds']['northeast']



def geo(x):
	for i,v in enumerate(x):
		address=v
		url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(address,google_api)
		print (i,v)
		results = r.json()
		#return results['results'][0]['geometry']['bounds']['northeast']





dd['lon_lat'] =dd['address'].apply(lambda x : geo(x))
