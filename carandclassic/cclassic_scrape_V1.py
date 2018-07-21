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
	output={'a':[],'b':[],'c':[],'d':[],'e':[]}
	content=soup.find_all('div',attrs={'class': 'item'})
	for i in range(len(soup.find_all('div',attrs={'class': 'item'}))):
		#print (content[i].find_all('li')[1].text)
		output['a'].append(content[i].find_all('li')[0].text)
		output['b'].append(content[i].find_all('li')[1].text)
		output['c'].append(content[i].find_all('li')[2].text)
		output['d'].append(content[i].find_all('li')[3].text)
		output['e'].append(content[i].find_all('a')[1].text)
	df=pd.DataFrame.from_dict(output)
	print (df)


def main_():
	url='https://www.carandclassic.co.uk/'
	opener=urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	page = opener.open(url)
	soup = BeautifulSoup(page)
	content=soup.find_all('div',attrs={'class': 'item'})
	car_list = []
	for i in range(len(soup.find_all('div',attrs={'class': 'item'}))):
		car_id = content[i].find('a').attrs['href']
		car_list.append(car_id)
	print (car_list)
	car_list = ['/car/C1017959', '/car/C1017957','/car/C1017957']
	output=[[] for i in range(len(car_list))]
	for i,car in enumerate(car_list):	
		url_ = 'https://www.carandclassic.co.uk' + str(car) 
		print ('url_ : ', url_)
		#url_='https://www.carandclassic.co.uk/car/C1017938' 
		opener=urllib.request.build_opener()
		opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		page = opener.open(url_)
		soup = BeautifulSoup(page)
		# Make, Model, Date, Ref, Telephone
		k_list = ['Price','Category','Make','Model','Year','Country','Telephone','Date','Ref']
		conetent=soup.find_all('td',attrs={'class':'caption'})
		for k in conetent:
			if k.text in k_list:
				print ('k_next' , k.find_next_siblings("td")[0].text)
				output[i].append(k.find_next_siblings("td")[0].text)
			else:
				pass
	print (output)
	data = pd.DataFrame(output,columns =k_list )
	print (data)
    


if __name__ == '__main__':
	main_()





