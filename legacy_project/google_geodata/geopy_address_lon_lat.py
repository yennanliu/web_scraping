# -*- coding: utf-8 -*-
# ref 
# https://pypi.python.org/pypi/geopy
# todo : deal with geopy request limit 
# https://stackoverflow.com/questions/30108786/how-to-deal-with-geopys-query-limit
# install Nominatim on server 
# https://wiki.openstreetmap.org/wiki/Nominatim/Installation
# work around 
# https://www.shanelynn.ie/batch-geocoding-in-python-with-google-geocoding-api/
import numpy as np 
import time
import requests
import os 
from geopy.geocoders import Nominatim

def address_2_lonlat(x):
    print (x)
    time.sleep(1)  # let's see if sleep 1 per epoch is OK for limitation 
    try:
        geolocator = Nominatim()
        location = geolocator.geocode(x)
        print(location.latitude, location.longitude)
        return [location.latitude, location.longitude]
    except Exception as e:
        print (e)
        print ('fail to convert address to lon & lat ') 
        return [None,None]

def address_2_lonlat_hack(x):
    """
    in case frequent request would make script get block
    here is a mini hack : make script sleep until the API is able to response 
    then do the run again 
    """
    print (x)
    time.sleep(1)  # let's see if sleep 1 per epoch is OK for limitation 
    try:
        geolocator = Nominatim()
        location = geolocator.geocode(x)
        print(location.latitude, location.longitude)
        return [location.latitude, location.longitude]
    except Exception as e:
        print (e)
        if str(e) == '[Errno 61] Connection refused':
            print ('meet API request limit, try again...')
            print ('sleep 1 min  ...')
            time.sleep(60)
            address_2_lonlat_hack(x)
        else:
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

def run_hack(df):
    """
    df :
    id, address zipcode , lat lon 
    """
    pass         