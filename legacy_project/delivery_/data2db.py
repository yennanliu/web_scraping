

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


#==============================


class db_manipulation:
	def __init__(self, *args, **kwargs):
		self.df = get_data()
		self.con  = 'sqlite:///weather.db'
	def test(self):
		print (self.con)

	def dumb2db(self):
		try:
			self.df.to_sql('weather_data',if_exists='fail',con=self.con)
			print ('dump to DB ok')
		except:
			print ('dump DB failed')

	def update2db(self):
		try:
			df = self.df 
			df.to_sql('weather_data',if_exists='append',con=self.con)
			print ('update to DB ok')
		except:
			print ('dump DB failed')




if __name__ == '__main__':
	db_job = db_manipulation()
	db_job.dumb2db()
	#dump_db()







