# 取得所有職缺詳細信息並存入 DataFrame
def fetch_all_job_details(job_urls):
    
    job_details = []

    for index, original_url in enumerate(job_urls):
        job_id = original_url.split('/job/')[1].split('?')[0]
        job_info = fetch_job_detail(job_id)

        if job_info:
            job_details.append(job_info)
            print(f"已完成 {index + 1} / {len(job_urls)} : {job_info['職缺名稱']}")

        sleep_time = random.uniform(3, 8)
        time.sleep(sleep_time)
    
    df = pd.DataFrame(job_details)
    return df

# 取得職缺詳細信息並存入 DataFrame
df = fetch_all_job_details(job_urls)
df.to_excel('104_jobs.xlsx')
