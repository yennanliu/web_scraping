import pandas as pd
import datetime
import urllib, json
from bs4 import BeautifulSoup




def main():
    output=pd.DataFrame([])
    # -------------

    for day in pd.date_range(start='3/1/2017', end='3/5/2017', freq='D'):
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
                .replace('\n', ''))

        df = pd.DataFrame({'col':col,'val':val}).set_index('col').T.reset_index()
        df['timestamp'] = day 
        del df['index']
        ### update output dataframe 
        output = output.append(df)
    output = output.reset_index()
    del output['index']
    output.columns = ['mean_temperature','max_temperature', 'min_temperature',
                     'heating_degree_days', 'dew_point', 'avg_humidity',
                     'max_humidity', 'min_umidity', 'precipitation',
                     'see_level_pressure', 'wind_speed', 'max_wind_speed', 'max_gust_speed',
                     'visibility', 'cvents', 'timestamp']
    print (output)
    return output 



if __name__ == '__main__':
	main()





