from scrap import *
from data2db import *




def get_values():
	sql ="""select 
	avg(temp_max) as avg_max_temp,
	avg(temp_min) as avg_min_temp,
	(select ((avg(temp_max)+avg(temp_min)))/2 from weather_data ) as avg_all_temp
	from weather_data

	"""

	sql2 ="""
	select 
	date(CET) as best_swim_date,
	(temp_min+ temp_min)/2 as avg_day_temp
	from 
	weather_data
	where avg_day_temp  = ( 
	select 
	max((temp_min+ temp_min)/2) as max_mean_temp
	from weather_data ) 


	"""
	print (sql)
	outcome = pd.read_sql(sql, con ='sqlite:///weather.db' )
	print (outcome)
	print ('-------------------------------')
	print (sql2)
	outcome2 = pd.read_sql(sql2, con ='sqlite:///weather.db' )
	print (outcome2)


get_values()







