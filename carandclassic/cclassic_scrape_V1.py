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
	output={'a':[],'b':[],'c':[],'d':[]}
	content=soup.find_all('div',attrs={'class': 'item'})
	for i in range(len(soup.find_all('div',attrs={'class': 'item'}))):
		#print (content[i].find_all('li')[1].text)
		output['a'].append(content[i].find_all('li')[0].text)
		output['b'].append(content[i].find_all('li')[1].text)
		output['c'].append(content[i].find_all('li')[2].text)
		output['d'].append(content[i].find_all('li')[3].text)
	df=pd.DataFrame.from_dict(output)
	print (df)



if __name__ == '__main__':
	main()