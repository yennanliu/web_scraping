# web_scraping

Collection of scrapper pipelines build for different purposes 

### File structure 

``` 
├── Dockerfile
├── README.md
├── api.                 : run celery monitor web server (via flask) 
├── celery-queue         : define main web scrapping jobs (via celery)
├── docker-compose.yml
├── legacy_project       : save legacy projects 
├── output
├── requirements.txt
└── travis_push_github.sh
```

### Quick start
```bash
$ cd ~ && git clone https://github.com/yennanliu/web_scraping
$ cd ~ && cd web_scraping &&  docker-compose -f  docker-compose.yml up 
# visit the services via 
# flower UI : http://localhost:5555/
# Run a "add" task : http://localhost:5001/add/1/2
# Run a "web scrape" task : http://localhost:5001/scrap_task
```

### Todo 
<details>
<summary>TODO</summary>

```
### Project level
1. Dockerize the project 
2. Run the scrapping (cron/paralel)jobs via Celery 
3. Deploy to Heroku cloud 
4. Add test 

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
</details>
