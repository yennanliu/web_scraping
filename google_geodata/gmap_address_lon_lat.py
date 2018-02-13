# -*- coding: utf-8 -*-

import urllib.request, json 
import pandas as pd 
import numpy as np 
import requests
import urllib, json
import os 


# ref 
# https://developers.google.com/maps/documentation/geocoding/start


gmap_api = os.environ['gmap_api']
print ('gmap_api : ' , gmap_api)


def gmap_url(address_):
	address_fix = address_.replace(' ','+')
	print (address_fix)
	g_map_url='https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(address_fix,gmap_api)
	print (g_map_url)
	return g_map_url 


def address_2_lonlat(g_map_url):
	with urllib.request.urlopen(g_map_url) as url:
		try:
			data = json.loads(url.read().decode())
			print(data)
			#data['results'][0]['geometry']['location']
			return data
		except Exception as e:
			print (e)
			print ('fail to convert address to lon & lat ') 
		return None 



def get_lon_lat(address_):
	g_map_url = gmap_url(address_)
	try:
		# to do :  fix utf-8 python 3 encodin problem 
		data = address_2_lonlat(g_map_url)
		result = data['results'][0]['geometry']['location']
	except:
		result = None,None
	return result 


# help function 
# ------------- 

def split_lat(x):
    try:
        return str(x['lat'])
    except:
        return None 
    
def split_lon(x):
    try:
        return str(x['lng'])
    except:
        return None 







