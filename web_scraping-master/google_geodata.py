'''
ref :  https://pypi.python.org/pypi/geocoder
ref :  https://pypi.python.org/pypi/py-translate
ref :  https://developers.google.com/maps/documentation/geocoding/get-api-key
ref :  https://developers.google.com/maps/documentation/geocoding/start
'''



df = pd.read_excel('0701.xlsx')
df.columns
dd=df[['地址.1','區域']]
dd=dd.dropna()

dd.columns=['address','group']
dd.to_csv('test0701.csv',encoding='utf-8')


google_api = 'your_google_api'
address='taipei 101'
url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=25.0330,121.5654&radius=50000&keyword={}&key={}'.format(address,google_api)


def geo(x):
	lon_lat=[[] for k in range(2)]

	for i,v in enumerate(x):
		address=v 
		url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=25.0330,121.5654&radius=50000&keyword={}&key={}'.format(address,google_api)
		r = requests.get(url)
		results = r.json()
		lon_lat[0].append(results['results'][0]['geometry']['location']['lng'])
		lon_lat[1].append(results['results'][0]['geometry']['location']['lat'])
	geo_data=pd.DataFrame(lon_lat).T 
	return geo_data


		
data=geo(dd['address'])
data.columns=['lat','lon']
data=pd.merge(dd,data, left_index=True,right_index=True)
