import random
import time
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# 初始化 fake_useragent
ua = UserAgent(platforms='pc')

# 設定 base_url 和查詢參數
base_url = "https://www.104.com.tw/jobs/search/"
params = {
    'keyword': 'python',
    'page': 1
}

# 用來儲存所有工作的 URL
job_urls = []

# 爬取前 150 頁
for page in range(1, 151):
    print(f"正在抓取第 {page} 頁...")
    params['page'] = page
    
    # 建立隨機的 User-Agent
    headers = {
        'User-Agent': ua.random
    }
    
    # 發送 GET 請求
    response = requests.get(base_url, headers=headers, params=params)
    soup = BeautifulSoup(response.text, 'lxml')
    
    # 找到所有的工作列表項目
    job_items = soup.find_all('article', class_='js-job-item')
    
    # For Loop 每個工作項目，提取工作 URL
    for job in job_items:
        job_link = job.find('a', class_='js-job-link')
        if job_link:
            job_url = job_link['href']
            # 104 的 URL 需要補全
            full_job_url = "https:" + job_url
            job_urls.append(full_job_url)
    
    # 隨機等待 5 到 10 秒
    sleep_time = random.uniform(5, 10)
    print(f"等待 {sleep_time:.2f} 秒...")
    time.sleep(sleep_time)
