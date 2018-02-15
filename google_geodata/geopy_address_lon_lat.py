# -*- coding: utf-8 -*-

# ref 
# https://pypi.python.org/pypi/geopy


import numpy as np 
import requests
import os 
from geopy.geocoders import Nominatim



def address_2_lonlat(x):
    print (x)
    try:
        geolocator = Nominatim()
        location = geolocator.geocode(x)
        print(location.latitude, location.longitude)
        return [location.latitude, location.longitude]
    except Exception as e:
        print (e)
        print ('fail to convert address to lon & lat ') 
        return [None,None]



def split_lat(x):
    try:
        return x[0]
    except:
        return None 
    
def split_lon(x):
    try:
        return x[1]
    except:
        return None 



        