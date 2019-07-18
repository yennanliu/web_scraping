# web_scraping

Collection of scrappers for different applications 

### File structure 

``` 
├── README.md
├── archive
└── legacy_project
```

### Quick start

```bash
# get repo and install packages 
$ git clone https://github.com/yennanliu/web_scraping
$ cd web_scraping 
# install library
$ source setup.sh
# run demo script 
$ python weather_scrapper/br_weather_scrapper_V1.py 

```


### Todo 
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



