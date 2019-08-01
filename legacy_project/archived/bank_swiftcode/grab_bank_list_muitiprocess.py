# python 3 


# credit 
# https://morvanzhou.github.io/tutorials/python-basic/multiprocessing/2-add/
# https://morvanzhou.github.io/tutorials/python-basic/multiprocessing/3-queue/

from bs4 import BeautifulSoup
import pandas as pd 
import urllib 
# multiprocessing
import multiprocessing as mp

import sys
sys.setrecursionlimit(10000) # 10000 is an example, try with different values
#====================

# help function 
def parse_swift_code(swift_url):
    try:
        opener=urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        page = opener.open(swift_url)
        soup = BeautifulSoup(page,"html.parser")
        # need to fix here ( find -> find_all)
        for k,j in enumerate(soup.find('a',{'href': True})):
            if k == 7:
                print (k,j.text)
                return j.text
            else:
                pass
        #return j.text
    except:
        return None

#====================

# main scrape function 

# url list 
url="http://www.swiftcodelist.com/banks/united-kingdom-{}.html"
url_ = [url.format(x) for x in range(1,2)]


def crawl(url):
	print ('-------------')
	print (url)
	print ('-------------')
	#url="http://www.swiftcodelist.com/banks/united-kingdom-1.html"
	#output = [[] for k in range(3)]
	#for x in range(1,43):
	#	url="http://www.swiftcodelist.com/banks/united-kingdom-{}.html".format(x)
	#	print (url)
	opener=urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	page = opener.open(url)
	soup = BeautifulSoup(page,"html.parser")
	# need to fix here ( find -> find_all)
	anchors = soup.find('a', {'href': True})
	return anchors


def parse(anchors):
	for k in anchors:
		if len(k.text) < 3:
			print (k.text)
			#output[0].append(None)
			print (k['href'])
			#output[1].append(k['href'])
			#output[2].append(None)	        
		else:
			#output[0].append(k.text)
			print (k.text)
			#output[1].append(k['href'])
			print (k['href'])
			#output[2].append(parse_swift_code(k['href']))



def main_(url):
	print ('-------------')
	print (url)
	print ('-------------')
	#url="http://www.swiftcodelist.com/banks/united-kingdom-1.html"
	output = [[] for k in range(3)]
	#for x in range(1,43):
	#	url="http://www.swiftcodelist.com/banks/united-kingdom-{}.html".format(x)
	#	print (url)
	opener=urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	page = opener.open(url)
	soup = BeautifulSoup(page,"html.parser")
	# need to fix here ( find -> find_all)
	anchors = soup.find('a', {'href': True})

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
	return df_ 




#====================

# parse job

def multi_scrap():
	#count =0
	pool = mp.Pool(2)
	while True:
		# htmls = [crawl(url) for url in unseen]
		# --->
		crawl_jobs = [pool.apply_async(main_, args=(url,)) for url in url_]
		output = [j.get() for j in crawl_jobs]
		print (output)
		# results = [parse(html) for html in htmls]
		# --->
		#parse_jobs = [pool.apply_async(parse, args=(html,)) for html in htmls]
		#results = [j.get() for j in parse_jobs]


def multi_scrap_():
	#count =0
	pool = mp.Pool(2)
	while True:
		# htmls = [crawl(url) for url in unseen]
		# --->
		crawl_jobs = [pool.apply_async(crawl, args=(url,)) for url in url_]
		data = [j.get() for j in crawl_jobs]
		print (data)
		#results = [parse(html) for html in htmls]
		# --->
		parse_jobs = [pool.apply_async(parse, args=(data,)) for a in data]
		results = [j.get() for j in parse_jobs]


#====================



if __name__ == '__main__':
	multi_scrap_()








