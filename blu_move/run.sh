#!/bin/sh


echo "scraping via shell ...."
bash blu_scrape_V2.sh 
echo "prepare data python ...."
#/anaconda/envs/g_dash/bin/python blu_scrape_V2.py
source activate zip_dev && python blu_scrape_V2.py
#echo "clean file..."

