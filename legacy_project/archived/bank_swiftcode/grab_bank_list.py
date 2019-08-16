# python 3 
from bs4 import BeautifulSoup
import pandas as pd 
import urllib 
# help function 
def parse_swift_code(swift_url):
    try:
        opener=urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        page = opener.open(swift_url)
        soup = BeautifulSoup(page,"html.parser")
        for k,j in enumerate(soup.find_all('a',{'href': True})):
            if k == 7:
                print (k,j.text)
                return j.text
            else:
                pass
        #return j.text
    except:
        return None

def clean_df(df):
	# drop any col, row with null value 
	#df_ = df.dropna()
	df_ = df_[(df_.bank_name != 'SWIFT Code Databse') | 
	          (df_.bank_name != 'Countries List') |
	          (df_.bank_name != 'Home') |
	          (df_.bank_name != 'Next') |
	          (df_.bank_name != 'Last') |
	          (df_.bank_name != 'Privacy policy') |
	          (df_.bank_name != 'DMCA Policy') |
	          (df_.bank_name != 'Contact Us') ]
	return df_ 

def main_():

	#url="http://www.swiftcodelist.com/banks/united-kingdom-1.html"

	output = [[] for k in range(3)]

	for x in range(1,43):
		url="http://www.swiftcodelist.com/banks/united-kingdom-{}.html".format(x)
		print (url)

		opener=urllib.request.build_opener()
		opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		page = opener.open(url)
		soup = BeautifulSoup(page,"html.parser")
		anchors = soup.find_all('a', {'href': True})

		for k in anchors:

			if len(k.text) < 3:
				print (k.text)
				output[0].append(None)
				print (k['href'])
				output[1].append(k['href'])
				output[2].append(None)	        
			else:
				output[0].append(k.text)
				print (k.text)
				output[1].append(k['href'])
				print (k['href'])
				output[2].append(parse_swift_code(k['href']))

	df_ = pd.DataFrame(output).T
	cols=['bank_name','url','swift_code']
	df_.columns = [cols]
	print (df_)
	#df_ =clean_df(df_)
	df_.to_csv('UK_bank_swift_code_list.csv')

if __name__ == '__main__':
	main_()