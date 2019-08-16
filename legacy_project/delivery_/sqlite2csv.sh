#!/bin/sh
#sqlite3 -header -csv  weather.db "select * from weather_data;" > weather.csv

# enter db name 
echo 'db list : '
echo '---------------'
ls *.db 
echo '---------------'
echo 'plz enter db file name ?'
read dbname 

# enter csv name 
echo 'plz enter csv file name ?'
read csvname 

# enter table name 
echo 'table list : '
echo '---------------'
sqlite3 $dbname.db ".table"
echo '---------------'

echo 'plz enter table name ?'
read tablename 

echo 'extract' $dbname  with  $tablename 'to' $csvname

sqlite3 -header -csv  $dbname.db "select * from $tablename ;" > $csvname.csv
