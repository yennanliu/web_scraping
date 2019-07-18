#!/bin/sh


echo "scraping via shell ...."
bash blu_scrape_V2.sh 
echo "prepare data python ...."
# 2 python script run way in case of different local dev envs
source activate zip_dev && python blu_scrape_V2.py ||  /Users/yennanliu/anaconda3/envs/ds_dash/bin/python blu_scrape_V2.py || python /home/ubuntu/yen_dev/blu_move/blu_scrape_V2.py


#echo "clean file..."

