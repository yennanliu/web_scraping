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
	col=[]
	val=[]
	for tr in trs:
		tds = tr.find_next_siblings("td") # you get list
		print (tr.text )
		col.append(tr.text)
		print (tds[0].text)
		val.append(tds[0].text.strip('\n')
			.replace('\xa0','')
			.replace('°C','')
			.replace('mm','')
			.replace('hPa','')
			.replace('km/h\n ()','')
			.replace('km/h','')
			.replace('kilometers',''))

	df = pd.DataFrame({'col':col,'val':val}).set_index('col').T.reset_index()
	del df['index']
	print (df)
	return df 




if __name__ == '__main__':
	main()





