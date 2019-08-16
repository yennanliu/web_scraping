import psycopg2
from sqlalchemy import create_engine
from pytz import timezone
import datetime
import os

european = timezone('Europe/Madrid')
now_tz = datetime.datetime.now(tz = european)
now = now_tz.replace(tzinfo = None)
now = now.replace(microsecond = 0)
db_url = os.environ['db_url']
print ('db_url : ' , db_url)

def write_data_to_db(df, table_name,db_url):
    try:
        # add insert time 
        df["date_of_insert"] = now
        print ('=============')
        print (df.head())
        print (table_name)
        print ('=============')
        engine = create_engine(db_url)
        conn = engine.connect()
        df.to_sql(name= table_name, con= engine, schema= 'rw', if_exists = "append", index = False)
        # close the connection after imput data 
        conn.close()
        print("insert to DB ok")
    except Exception as e:
        print (e)
        print ('fail to write to db')
        