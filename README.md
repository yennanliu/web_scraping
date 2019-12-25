# web_scraping

Collection of scrapper pipelines build for different purposes 

[![Build Status](https://travis-ci.org/yennanliu/web_scraping.svg?branch=master)](https://travis-ci.org/yennanliu/web_scraping)
[![PRs](https://img.shields.io/badge/PRs-welcome-6574cd.svg)](https://github.com/yennanliu/web_scraping/pulls)


### Quick Start
<details>
<summary>Quick start via docker</summary>

```bash
# Run via docker 
$ cd ~ && git clone https://github.com/yennanliu/web_scraping
$ cd ~ && cd web_scraping &&  docker-compose -f  docker-compose.yml up 
```
- visit the services via 
	- flower UI : http://localhost:5555/
	- Run "add" task : http://localhost:5001/add/1/2
	- Run "web scrape" task : http://localhost:5001/scrap_task
	- Run "indeed scrape" task : http://localhost:5001/indeed_scrap_task

</details>

<details>
<summary>Quick start manually</summary>

```bash
# Run manually 
# dev 

```
</details>


### File structure 

``` 
├── Dockerfile
├── README.md
├── api.                  : Celery api (broker, job accepter(flask))
│   ├── Dockerfile        : Dockerfile build celery api 
│   ├── app.py            : Flask server accept job request(api)
│   ├── requirements.txt
│   └── worker.py         : Celery broker, celery backend(redis)
├── celery-queue          : Run main web scrapping jobs (via celery)
│   ├── Dockerfile        : Dockerfile build celery-queue
│   ├── IndeedScrapper    : Scrapper scrape Indeed.com 
│   ├── requirements.txt
│   └── tasks.py          : Celery run scrapping tasks 
├── cron_indeed_scrapping_test.py
├── cron_test.py
├── docker-compose.yml    : docker-compose build whole system : api, celery-queue, redis, and flower(celery job monitor)
├── legacy_project        
├── logs                  : Save running logs 
├── output                : Save scraped data 
├── requirements.txt
└── travis_push_github.sh : Script auto push output to github via Travis 

```

### Tech
* [Celery](http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html) : parallel/single thread python tasks management tool (celery broker/worker)
* [Redis](https://redis.io/)  : key-value DB save task data 
* [Flower](https://flower.readthedocs.io/en/latest/) : UI monitor celery tasks 
* [Flask](http://flask.palletsprojects.com/en/1.1.x/) : python light web framework, as project backend server here  
* [Docker](https://www.docker.com/get-started) : build the app environment 


### Todo 
<details>
<summary>TODO</summary>

```
### Project level

0. Deploy to Heroku cloud and make the scrapper as an API service 
1. Dockerize the project 
2. Run the scrapping (cron/paralel)jobs via Celery 
4. Add test (unit/integration test) 
5. Design DB model that save scrapping data systematically 

### Programming level 

1. Add utility scripts that can get XPATH of all objects in html
2. Workflow that automate whole processes
3. Job management 
	- Multiprocessing
	- Asynchronous
	- Queue 
4. Scrapping tutorial 
5. Scrapy, Phantomjs 

### Others 

1. Web scrapping 101 tutorial 

```
</details>

### Ref 
<details>
<summary>Ref</summary>
- Scraping via Celery
	- https://www.pythoncircle.com/post/518/scraping-10000-tweets-in-60-seconds-using-celery-rabbitmq-and-docker-cluster-with-rotating-proxy/

- Travis push to github 
	- https://stackoverflow.com/questions/51925941/travis-ci-how-to-push-to-master-branch
	- https://medium.com/@preslavrachev/using-travis-for-secure-building-and-deployment-to-github-5a97afcac113
	- https://gist.github.com/willprice/e07efd73fb7f13f917ea
	- https://www.vinaygopinath.me/blog/tech/commit-to-master-branch-on-github-using-travis-ci/
	- https://www.hidennis.tech/2015/07/07/deploy-blog-using-travis/

- Indeed scrapping 
	- https://medium.com/@msalmon00/web-scraping-job-postings-from-indeed-96bd588dcb4b
	- https://github.com/tarunsinghal92/indeedscrapperlatest

- Distributed scrapping
	- https://github.com/tikazyq/crawlab


- Unit test Celery
	- https://docs.celeryproject.org/en/latest/userguide/testing.html
</details>