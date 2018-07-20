# python 3 


# ops 
import pandas as pd
import datetime
import urllib, json
from bs4 import BeautifulSoup



def main():
	url='https://www.carandclassic.co.uk/'
	opener=urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	page = opener.open(url)
	soup = BeautifulSoup(page)
	soup.find_all('div',attrs={'class': 'item'})[2].find_all('li')
	print (soup)



if __name__ == '__main__':
	main()