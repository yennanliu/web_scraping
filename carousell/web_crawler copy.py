from bs4 import BeautifulSoup
import requests, re
import pandas as pd 
import urllib 
import random
import os
import sys
import subprocess
import json



# Chat 
# ipeen 
# Carousell 
# ptt 
# airbnb
# spotify


# ====================================================

def regular_chat():
	sample_response = ['HI THERE', 'WAZZA UP','R U KIDDING ME', '..?']
	response = sample_response[random.randint(0,3)]
	print (response)
	return response

def general_intro():
	sample_response = """
######## 

for Carousell product survey, please type "!caro prosuctname" \n
for asking, please type "ask" \n
for main application, please type anything \n
have fun :) \n

########

	"""
	print (sample_response)
	return sample_response


# ====================================================

# Spotify 



def spotify_album(artist):
	# make sure artist name feat spotify API query form 
	artist = artist.replace (" ", "+")
	print (artist)
	url="https://api.spotify.com/v1/search?q=${}&type=artist".format(artist)

	command = """ 

	API_ARTIST_URL=$(curl -s "{}" | jq -r '.artists.items[0].href') 
	curl -s "$API_ARTIST_URL/top-tracks?country=US" > spotify_data.json

	""".format(url)
	print (command)
	os.system(command)
	album = ''
	try:
		data_spotify = json.loads(open('spotify_data.json').read())
		for k in range(0,len(data_spotify['tracks'])): 
		    print (data_spotify['tracks'][k]['name'])
		    album += data_spotify['tracks'][k]['name'] + "\n\n"
	except:
		album = 'no feat artist, return null data'
		print (album)
	# remove intermediate json 	
	os.system('rm spotify_data.json')
	return album
	



# ====================================================

# Carousell


def Caro_grab_(query):
	url = 'https://tw.carousell.com/search/products/?query={}'
	url=url.format(query)
	opener=urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	page = opener.open(url)
	soup = BeautifulSoup(page,"html.parser")
	anchors = soup.find_all('a', {'class': 'pdt-card-thumbnail', 'href': True})
	content='' 
	url_refix = 'https://tw.carousell.com/p/'
	for anchor in anchors:
		for k in re.findall('\d+', anchor['href']):
			if len(k) > 3:
				url = url_refix + k 
				content += anchor.find('img')['alt'] + "\n" + str(url) + "\n\n"

	print (content)
	return content[:600]


def Caro_grab():
	url = 'https://tw.carousell.com/?hl=en'
	opener=urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	page = opener.open(url)
	soup = BeautifulSoup(page,"html.parser")
	anchors = soup.find_all('a', {'class': 'pdt-card-thumbnail', 'href': True})
	content='' 
	url_refix = 'https://tw.carousell.com/p/'
	for anchor in anchors:
		for k in re.findall('\d+', anchor['href']):
			if len(k) > 3:
				url = url_refix + k 
				content += anchor.find('img')['alt'] + "\n" + str(url) + "\n\n"

	print (content)
	return content[:600]





# ====================================================

### ipeen


def ipeen_grab():
	output = [[] for k in range(2)]
	for page in range(1,5):
	    url ='http://www.ipeen.com.tw/search/all/000/0-100-0-0/%E4%B8%AD%E5%BC%8F/?p={}&adkw=%E5%8F%B0%E5%8C%97'.format(page)
	    print (url)
	    opener=urllib.request.build_opener()
	    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	    page = opener.open(url)
	    soup = BeautifulSoup(page)
	    for k in soup.find_all('a', attrs={'data-label': '店名'}):
	        output[0].append(k.text)

	    for k in soup.findAll('span',{"style":"padding-left:3em;"}):
	        output[1].append(k.get_text())
	data = ''
	for k, m in zip(output[0],output[1]):
	    data += str(k) + str(m)
	# limit number of query response here, since there may be limit in msg length 
	return data[:600]


# ==================================================== 

### ptt beauty 


def ptt_beauty():
	url = 'https://www.ptt.cc/bbs/Beauty/index.html'
	rs = requests.session()
	res = rs.get('https://www.ptt.cc/bbs/Beauty/index.html', verify=False)
	soup = BeautifulSoup(res.text, 'html.parser')
	#ALLpageURL = soup.select('.btn.wide')[1]['href']
	content=''
	# limit number of query response here, since there may be limit in msg length 
	for k in soup.find_all('a',href=True)[:15]:

	    try:
	    	if len(k['href']) < 30:
	    		pass
	    	else:
	            print ("https://www.ptt.cc/"+ k['href'], k.text)
	            content +=  k.text + "\n" + 'https://www.ptt.cc%s'%(k['href']) + "\n\n"
	    except:
	        pass

	print ('==================')
	print (content)
	return content



# ====================================================

if __name__ == "__main__":
	spotify_album('pete rock')
	#Caro_grab()
	#regular_chat()
	#ptt_beauty()
	#pttBeauty()






