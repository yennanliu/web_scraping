import os
import time
import urllib.request as request
from bs4 import BeautifulSoup
from celery import Celery
import sys

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')
celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery.task(name="task.add")
def add(x, y):
    return x+y

@celery.task(name="task.multiply")
def multiply(x, y):
    return x*y

@celery.task(name='task.scrape_task')
def scrape():
    url = 'https://github.com/apache/spark'
    opener=request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    page = opener.open(url)
    soup = BeautifulSoup(page)
    print (soup.text)
    return soup.text

@celery.task(name='task.scrape_task_api')
def scrape_github_api(account, repo_name):
    url = 'https://github.com/{}/{}'.format(account, repo_name)
    print ("*** url", url)
    opener=request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    page = opener.open(url)
    soup = BeautifulSoup(page)
    print (soup.text)
    return soup.text

@celery.task(name='task.indeed_scrap_task')
def indeed_scrape():
    sys.path.append(".")
    from IndeedScrapper.indeed_scrapper import Scrape_Runner
    Scrape_Runner()

@celery.task(name='task.indeed_scrap_api_V1')
def indeed_scrape_api(city_set):
    sys.path.append(".")
    from IndeedScrapper.indeed_scrapper import Scrape_Runner
    Scrape_Runner(city_set)
    