# python 3 

# grab weather data via https://www.wunderground.com/

# ops 
import pandas as pd
import numpy as np 
import datetime
import urllib, json
from bs4 import BeautifulSoup


# UDF 
from script.utility_data_IO import * 
#from script.utility_operation import * 
#import utility_data_IO

cols = ['Mean Temperature', 'Max Temperature', 'Min Temperature',
        'Heating Degree Days', 'Dew Point', 'Average Humidity',
        'Maximum Humidity', 'Minimum Humidity', 'Precipitation',
        'Sea Level Pressure', 'Wind Speed', 'Max Wind Speed', 'Max Gust Speed',
        'Visibility', 'Events', 'timestamp']


# -----------------
# help function

def col_fix(df):
    for col in cols:
        if col in df.columns:
            pass
        else:
            df[col]  = None  
    return df 

# -----------------



def main_(start_date,end_date):
    output=pd.DataFrame([])
    # -------------
    print ('-----------------')
    print ('start_date : ',start_date )
    print ('end_date : ',end_date )
    print ('-----------------')
    for day in pd.date_range(start=start_date, end=end_date, freq='D'):
    #for day in pd.date_range(start_date='3/1/2017', end_date='3/5/2017', freq='D'):
        print ((day))
        date_ = str(day).split(' ')[0] 
        year_ = date_.split('-')[0]
        month_ = date_.split('-')[1]
        day_ = date_.split('-')[2]
   # -------------
        url_new = 'https://www.wunderground.com/history/airport/EBFS/{}/{}/{}/DailyHistory.html?req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo='.format(year_,month_,day_)
        print (url_new)
        
        # query the page 
        opener=urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        page = opener.open(url_new)
        soup = BeautifulSoup(page)
        trs = soup.find_all('td', attrs={'class': 'indent'})
        col=[]
        val=[]
        for tr in trs:
            if tr.text in cols:
                tds = tr.find_next_siblings("td") # you get list
                print (tr.text )
                col.append(tr.text)
                print (tds[0].text)
                val.append(tds[0].text.strip('\n')
                    .replace('\xa0','')
                    .replace('°C','')
                    .replace('mm','')
                    .replace('hPa','')
                    .replace('km/h\n ()','')
                    .replace('km/h','')
                    .replace('kilometers','')
                    .replace('\n\t', '')
                    .replace('\t', '')
                    .replace('\n', '')
                    .replace('- ()', ''))
                    #.replace('-', ''))
            else:
                col.append(tr.text) 
                val.append(None) 

        df = pd.DataFrame({'col':col,'val':val}).set_index('col').T.reset_index()
        df['timestamp'] = day 
        del df['index']
        df = col_fix(df)
        print ('df.columns : ' , df.columns )
        print ('cols : ' , cols  )
        #df.columns = cols 
        df = df[cols] 
        ### update output dataframe 
        output = output.append(df)
    output = output.reset_index()
    print (output)
    del output['index']
    output.columns = ['mean_temperature','max_temperature', 'min_temperature',
                     'heating_degree_days', 'dew_point', 'avg_humidity',
                     'max_humidity', 'min_humidity', 'precipitation',
                     'sea_level_pressure', 'wind_speed', 'max_wind_speed', 'max_gust_speed',
                     'visibility', 'events', 'timestamp']

    output = output[['timestamp','mean_temperature','max_temperature', 'min_temperature',
                     'heating_degree_days', 'dew_point', 'avg_humidity','max_humidity', 'min_humidity', 'precipitation',
                     'sea_level_pressure', 'wind_speed', 'max_wind_speed', 'max_gust_speed',
                     'visibility','events']]
    # clean data 
    output=output.replace('  -', np.nan)
    """
    # modify data type 
    output['mean_temperature']=output['mean_temperature'].astype('float')
    output['max_temperature']=output['max_temperature'].astype('float')
    output['min_temperature']=output['min_temperature'].astype('float')
    output['heating_degree_days']=output['heating_degree_days'].astype('float')
    output['dew_point']=output['dew_point'].astype('float')
    output['avg_humidity']=output['avg_humidity'].astype('float')
    output['max_humidity']=output['max_humidity'].astype('float')
    output['min_humidity']=output['min_humidity'].astype('float')
    output['precipitation']=output['precipitation'].astype('float')
    output['sea_level_pressure']=output['sea_level_pressure'].astype('float')
    output['wind_speed']=output['wind_speed'].astype('float')
    output['max_wind_speed']=output['max_wind_speed'].astype('float')
    output['max_gust_speed']=output['max_gust_speed'].astype('float')
    output['events']=output['events'].astype('str')

    print (output.info())
    """
    print (output.head())
    return output 



if __name__ == '__main__': 
    df_ = main_('1/1/2018', '1/31/2018')
    #df_ = main_('2/1/2016', '2/10/2016')
    print (df_)
    # dump to DB 
    write_data_to_db(df_, 'weather_brussels',db_url)






