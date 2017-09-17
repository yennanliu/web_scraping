

from scrap import *


def get_data():
	output = pd.DataFrame()
	for month in range(1,13):
		df = get_weather_data('2014',month)
		print (df)
		output= output.append(df)
	return output 



def dump_db():
	try:
		df = get_data()
		df.to_sql('weather_data', if_exists='fail',con='sqlite:///weather.db')
		print ('dump to DB ok')
	except:
		print ('dump DB failed')


def update_db():
	try:
		df = get_data()
		df.to_sql('weather_data',if_exists='append',con='sqlite:///weather.db')
		print ('update to DB ok')
	except:
		print ('update DB failed')






#dump_db()





