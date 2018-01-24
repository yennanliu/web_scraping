# python 3 
from bs4 import BeautifulSoup
import pandas as pd 
import urllib 


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





def main():
	
	url="http://www.swiftcodelist.com/banks/united-kingdom-1.html"
	print (url)

	opener=urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	page = opener.open(url)
	soup = BeautifulSoup(page,"html.parser")

	anchors = soup.find_all('a', {'href': True})
	output = [[] for k in range(2)]

	for k in anchors:
	    if len(k.text) < 3:
	        print (k.text)
	        output[0].append(None)
	        print (k['href'])
	        output[1].append(k['href'])
	        
	    else:
	        output[0].append(k.text)
	        print (k.text)
	        output[1].append(k['href'])
	        print (k['href'])

	df_ = pd.DataFrame(output).T
	cols=['bank_name','url']
	df_.columns = [cols]
	print (df_)


if __name__ == '__main__':
	main()








