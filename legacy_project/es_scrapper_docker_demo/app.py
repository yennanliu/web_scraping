import re
import time
import requests
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch

# change to local host default ip 
#es_client = Elasticsearch(['http://localhost:9200'])
es_client = Elasticsearch(['http://127.0.0.1:9200'])

drop_index = es_client.indices.create(index='blog-sysadmins', ignore=400)
create_index = es_client.indices.delete(index='blog-sysadmins', ignore=[400, 404])

def urlparser(title, url):
    # scrape title
    p = {}
    post = title
    page = requests.get(post).content
    soup = BeautifulSoup(page, 'lxml')
    title_name = soup.title.string

    # scrape tags
    tag_names = []
    desc = soup.findAll(attrs={"property":"article:tag"})
    for x in range(len(desc)):
        tag_names.append(desc[x-1]['content'].encode('utf-8'))

    # payload for elasticsearch
    doc = {
        'date': time.strftime("%Y-%m-%d"),
        'title': title_name,
        'tags': tag_names,
        'url': url
    }
    # ingest payload into elasticsearch
    res = es_client.index(index="blog-sysadmins", doc_type="docs", body=doc)
    time.sleep(0.5)

sitemap_feed = 'https://sysadmins.co.za/sitemap-posts.xml'
page = requests.get(sitemap_feed)
sitemap_index = BeautifulSoup(page.content, 'html.parser')
urls = [element.text for element in sitemap_index.findAll('loc')]

for i in range(3):
    for x in urls:
        print ('x :', x )
        urlparser(x, x)
    time.sleep(5)
