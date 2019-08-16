import pandas as pd
import datetime
import urllib, json
from bs4 import BeautifulSoup

def get_html_data(url):
	opener=urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	page = opener.open(url)
	soup = BeautifulSoup(page)
	return soup

def fix_price(x):
    return x.split(' ')[0]

def main_():
	# -----------  collect classic car ID  -----------
	url='https://www.carandclassic.co.uk/cat/3/'
	soup = get_html_data(url)
	content=soup.find_all('div',attrs={'class': 'item'})
	car_list = []
	for i in range(len(soup.find_all('div',attrs={'class': 'item'}))):
		# -----------  only get car ID with not null price -----------
		if len(content[i].find('li',attrs={'class':'price'}).text.replace('£','')) > 0:
			car_id = content[i].find('a').attrs['href']
			car_list.append(car_id)
		else:
			pass 
	print (car_list)
	#car_list = ['/car/C1017959', '/car/C1017957','/car/C1017957']
	# ----------- go through every car page, grab the car profile information  -----------
	output=[[] for i in range(len(car_list))]
	for i,car in enumerate(car_list):	
		url_ = 'https://www.carandclassic.co.uk' + str(car) 
		print ('url_ : ', url_)
		soup = get_html_data(url_)
		# ----------- collect needed columns -----------
		# Make, Model, Date, Ref, Telephone
		k_list = ['Price','Category','Make','Model','Year','Country','Telephone','Date','Ref']
		content=soup.find_all('td',attrs={'class':'caption'})
		for k in content:
			if k.text in k_list:
				print ('k_next' , k.find_next_siblings("td")[0].text)
				output[i].append(k.find_next_siblings("td")[0].text)
			else:
				pass
	print (output)
	# ----------- output scrape data as dataframe and fix column value -----------
	data = pd.DataFrame(output,columns =k_list )
	data['Price'] = data['Price'].apply(lambda x :  fix_price(x))
	print (data)
	return data
    
if __name__ == '__main__':
	main_()
