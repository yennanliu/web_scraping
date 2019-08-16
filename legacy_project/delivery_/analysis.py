from scrap import *
from data2db import *

def get_values():

	sql0="""
SELECT *
	FROM weather_data
	LIMIT 10 ;
	"""
	sql ="""
SELECT avg(temp_max) AS avg_max_temp,
       avg(temp_min) AS avg_min_temp,

  (SELECT ((avg(temp_max)+avg(temp_min)))/2
   FROM weather_data) AS avg_all_temp
FROM weather_data
WHERE TYPE = 'Actual:'

	"""

	sql2 ="""
SELECT date(CET) AS best_swim_date,
       (temp_min+ temp_min)/2 AS avg_day_temp
FROM weather_data
WHERE avg_day_temp =
    (SELECT max((temp_min+ temp_min)/2) AS max_mean_temp
     FROM weather_data
     WHERE TYPE = 'Actual:')
  AND TYPE = 'Actual:'

	"""
	print (sql0)
	outcome0 = pd.read_sql(sql0, con ='sqlite:///weather.db' )
	print (outcome0)
	print ('-------------------------------')
	print (sql)
	outcome = pd.read_sql(sql, con ='sqlite:///weather.db' )
	print (outcome)
	print ('-------------------------------')
	print (sql2)
	outcome2 = pd.read_sql(sql2, con ='sqlite:///weather.db' )
	print (outcome2)

if __name__ == '__main__':
	get_values()
