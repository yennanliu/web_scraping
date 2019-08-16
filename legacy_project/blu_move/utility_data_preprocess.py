import pandas as pd 

def data_prepare():
	df = pd.read_csv('blu.csv')
	#df = df 
	#print (df.head())
	cols = ['start', 'start_block','start_reservation','end','end_block','end_reservation']
	for col in cols:
		df[col] = pd.to_datetime(df[col])
		# maybe need to modify time form 
		# 04/01/2018  17:45:00 -> 2018-01-04 17:45:00 for example 
		# df.col = df.col.timestrip("%Y-%M-%D hr:mm:ss")
		# end_date_relative = now.date().strftime("%d/%m/%Y")

	df['reservation_time'] = df['end_reservation'] - df['start_reservation']
	print (df.head(3))
	return df 
	
if __name__ == '__main__':
	data_prepare()
