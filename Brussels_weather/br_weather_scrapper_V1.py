import pandas as pd
import datetime
import urllib, json
from bs4 import BeautifulSoup


def main():
	url_new = 'https://www.wunderground.com/history/airport/EDDT/2017/1/18/DailyHistory.html'
	print (url_new)


	# query the page 
	opener=urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	page = opener.open(url_new)
	soup = BeautifulSoup(page)
	trs = soup.find_all('td', attrs={'class': 'indent'})
	for tr in trs:
		tds = tr.find_next_siblings("td") # you get list
		print (tr.text )
		print (tds[0].text)
	#eturn tds 




if __name__ == '__main__':
	main()





