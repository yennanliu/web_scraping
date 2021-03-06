import os
import time
import sys
from datetime import timedelta
import urllib.request as request
from bs4 import BeautifulSoup
from celery import Celery
from celery.schedules import crontab
from celery.task.base import periodic_task

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')
celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery.task(name="tasks.add")
def add(x, y):
    return x+y

@celery.task(name="tasks.multiply")
def multiply(x, y):
    return x*y

@periodic_task(run_every=(crontab(minute='*')),name="run_every_minute",ignore_result=True)
def push_heart_beat():
    print ("this is heart beat")
    return "this is heart beat"

@celery.task(name='tasks.scrape_task')
def scrape():
    url = 'https://github.com/apache/spark'
    opener=request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    page = opener.open(url)
    soup = BeautifulSoup(page)
    print (soup.text)
    return soup.text

@celery.task(name='tasks.scrape_task_api')
def scrape_github_api(account, repo_name):
    url = 'https://github.com/{}/{}'.format(account, repo_name)
    print ("*** url", url)
    opener=request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    page = opener.open(url)
    soup = BeautifulSoup(page)
    print (soup.text)
    return soup.text

@celery.task(name='tasks.indeed_scrap_task')
def indeed_scrape():
    sys.path.append(".")
    from IndeedScrapper.indeed_scrapper import Scrape_Runner
    Scrape_Runner()

@celery.task(name='tasks.indeed_scrap_api_V1')
def indeed_scrape_api(city_set):
    sys.path.append(".")
    from IndeedScrapper.indeed_scrapper import Scrape_Runner
    Scrape_Runner(city_set)
    