# get the coporates' name via their phone number since it is hard to know who they are 
# just an initail test here, will do  API like version in the future 



import requests
from bs4 import BeautifulSoup
col1=[]
col2=[]
col3=[]

count = 0
#b = 'http://number.whoscall.com/%E5%8F%B0%E7%81%A3%E5%8F%B0.../'
b = "http://number.whoscall.com/zh-TW/tw/"

def k(tel):
	for x in range(len(tel)):
          if len(tel[x]) < 8 or len(tel[x]) > 20 :
                          continue 
          else:  
		        url = b +str(tel[x]) 
		        r = requests.get(url)
		        soup = BeautifulSoup(r.content)
		        g = soup.find('span' ,{'itemprop':"name"})
                
		        for item in g:
                           col1.append(item )
                           col2.append(tel[x])
                           col3.append(x)



                           
