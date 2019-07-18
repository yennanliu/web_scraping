#!/bin/sh


sqlite3  weather.db "select * from weather_data limit 3;" 

echo '---------------------'
echo ''


sqlite3  weather.db "select CET from weather_data limit 3;" 