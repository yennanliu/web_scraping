

## Tech 

Python 3.4.5, Pandas 0.20.3, numpy , BeautifulSoup, urllib, sqlite3


## File Structure 

```
├── README.md
├── analysis.py : calcluate average temperature, best to swim day  
├── data2db.py  : dump needed data to sqlite 
├── scrap.py    : scrap weather data from wunderground.com
└── weather.db  : sqlite db save whole daily weather data  in 2014 
```


## QUICK START


```Bash
cd web_scraping
# scrap and dump data to db 
python data2db.py
# get needed analysis output 
python analysis.py

```

```Bash
# output 

BeautifulSoup([your markup], "html5lib")

  markup_type=markup_type))
        type temp_max temp_min        CET
0    Actual:       4°      -1° 2014-01-01
1   Average:       2°      -2° 2014-01-01
2    Actual:       7°       1° 2014-01-02
3   Average:       3°      -2° 2014-01-02
.....

-------------------------------

SELECT avg(temp_max) AS avg_max_temp,
       avg(temp_min) AS avg_min_temp,

  (SELECT ((avg(temp_max)+avg(temp_min)))/2
   FROM weather_data) AS avg_all_temp
FROM weather_data
WHERE TYPE = 'Actual:'

	
   avg_max_temp  avg_min_temp  avg_all_temp
0     15.260274      7.312329     10.304795
-------------------------------

SELECT date(CET) AS best_swim_date,
       (temp_min+ temp_min)/2 AS avg_day_temp
FROM weather_data
WHERE avg_day_temp =
    (SELECT max((temp_min+ temp_min)/2) AS max_mean_temp
     FROM weather_data
     WHERE TYPE = 'Actual:')
  AND TYPE = 'Actual:'

	
  best_swim_date  avg_day_temp
0     2014-07-05            21
1     2014-07-21            21
```













