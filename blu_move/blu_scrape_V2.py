import json
import pandas as pd
import sys ,re,time


def get_json():
	# read json from shell scraper (blu_scrape_V2.sh)
	with open("blu_.json") as json_file:
	    blu_data = json.load(json_file)
	return blu_data

 

 
def main_():
	blu_data = get_json()
	# prepare data, parese needed columns 
	# for loop
	output = [[] for k in range(11)]

	for loc_index in range(len(blu_data['data']['locations'])):
		for k in range(len(blu_data['data']['locations'][loc_index]['Location']['vehicles'])):
			data_ =blu_data['data']['locations'][loc_index]['Location']['vehicles'][k]['data']
			print (data_['id'])
			# car data 
			# gat car ID, lat, lon, status, gps_timestamp
			output[0].append(data_['id'])
			output[1].append(data_['gpslat'])
			output[2].append(data_['gpslong'])
			output[3].append(data_['gps_timestamp'])
			output[4].append(data_['status'])
			# reservation data 
			# get reservation : end, end_block, end_reservation, start, start_block, start_reservation 
			data_reserve = blu_data['data']['locations'][loc_index]['Location']['vehicles'][k]['occupation']['allReservations']
			if len(data_reserve) == 0:
				output[5].append(None)
				output[6].append(None)
				output[7].append(None)
				output[8].append(None)
				output[9].append(None)
				output[10].append(None)

			else:
				#pd.to_datetime(data_reserve[0]['end'], format='%d/%m/%y %H:%M:%S')
				output[5].append(pd.to_datetime(data_reserve[0]['end'], format='%d/%m/%Y %H:%M:%S'))   
				output[6].append(pd.to_datetime(data_reserve[0]['end_block'], format='%d/%m/%Y %H:%M:%S'))
				output[7].append(pd.to_datetime(data_reserve[0]['end_reservation'], format='%d/%m/%y %H:%M:%S'))
				output[8].append(pd.to_datetime(data_reserve[0]['start'], format='%d/%m/%Y %H:%M:%S'))
				output[9].append(pd.to_datetime(data_reserve[0]['start_block'], format='%d/%m/%Y %H:%M:%S'))
				output[10].append(pd.to_datetime(data_reserve[0]['start_reservation'], format='%d/%m/%y %H:%M:%S'))
				#print (data_reserve)
		        #print ('=====')
		    	    
	df_ = pd.DataFrame(output).T
	df_.columns = [['id','gpslat','gpslong','gps_timestamp','status',
	                'end','end_block','end_reservation',
	                'start','start_block','start_reservation']]
	df_.to_csv('blu_.csv')
	print (df_) 
	return df_


if __name__ == '__main__':
	main_()




