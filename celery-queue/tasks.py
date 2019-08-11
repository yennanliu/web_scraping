import os
import time
import urllib.request as request
from bs4 import BeautifulSoup
from celery import Celery
import sys
sys.path.append("..")
from IndeedScrapper.indeed_scrapper import Scrape_Runner

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')
celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery.task(name='tasks.scrap_task')
def scrape():
	url = 'https://github.com/apache/spark'
	opener=request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	page = opener.open(url)
	soup = BeautifulSoup(page)
	print (soup.text)
	return soup.text

@celery.task(name='tasks.indeed_scrap_task')
def indeed_scrape():
	Scrape_Runner()
	