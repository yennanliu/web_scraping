import requests
import pandas as pd
import random
import time
from fake_useragent import UserAgent

# 將 JSON 資料轉換為結構化字典
def convert_job_data(original_dict):
    data = original_dict['data']

    # 將 jobType 轉換為描述文字
    job_type_mapping = {
        0: '全部',
        1: '全職',
        2: '兼職',
        3: '高薪',
        4: '派遣'
    }
    
    # 將 remoteWork 轉換為描述文字
    remote_work_mapping = {
        1: '完全遠端',
        2: '部分遠端'
    }
    
    # 建立包含工作資訊的字典
    job_info = {
        '職缺名稱': data['header']['jobName'],
        '公司名稱': data['header']['custName'],
        '公司網址': data['header']['custUrl'],
        '發佈日期': data['header']['appearDate'],
        '職缺分析網址': 'https:' + data['header']['analysisUrl'],
        '上班地區': data['jobDetail']['addressRegion'],
        '上班地點': data['jobDetail']['addressDetail'],
        '工作待遇': data['jobDetail']['salary'],
        '最低薪資': data['jobDetail']['salaryMin'],
        '最高薪資': data['jobDetail']['salaryMax'],
        '工作性質': job_type_mapping.get(data['jobDetail']['jobType'], '未知'),
        '上班時段': data['jobDetail']['workPeriod'],
        '假期政策': data['jobDetail']['vacationPolicy'],
        '工作經歷': data['condition']['workExp'],
        '學歷要求': data['condition']['edu'],
        '擅長工具': [specialty['description'] for specialty in data['condition']['specialty']],
        '工作技能': [skill['description'] for skill in data['condition']['skill']],
        '產業類別': data['industry'],
        '職務類別': [category['description'] for category in data.get('jobDetail', {}).get('jobCategory', [])],
        '出差外派': data['jobDetail']['businessTrip'],
        '遠端工作': remote_work_mapping.get((data['jobDetail'].get('remoteWork') or {}).get('type', 0), '無'),
        '公司人數': '' if data.get('employees') == '暫不提供' else data.get('employees', '').replace('人', ''),
        '管理責任': data['jobDetail']['manageResp']
    }
    return job_info

# 單獨抓取某一職缺的詳細資料
def fetch_job_detail(job_id):
    
    try:
        ua = UserAgent(platforms='pc')
        
        url = f'https://www.104.com.tw/job/ajax/content/{job_id}'
        headers = {
            'User-Agent': ua.random,
            'Referer': f'https://www.104.com.tw/job/{job_id}'
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 檢查 HTTP 回應狀態

        data = response.json()
        job_info = convert_job_data(data)
        job_info['連結'] = f'https://www.104.com.tw/job/{job_id}'
        
        return job_info

    except Exception as e:
        print(f"處理職缺 {job_id} 時出錯: {e}")
        return None
