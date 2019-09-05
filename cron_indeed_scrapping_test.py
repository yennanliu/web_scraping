# import packages
import requests
import pandas as pd
import time 
import datetime
import os 
from celery_queue.IndeedScrapper.indeed_extract import *


# current date 
current_time, current_date  = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S'), datetime.datetime.now().strftime('%Y-%m-%d')

# limit per sity
max_results_per_city = 200

# db of city 
city_set = ['New+York', 'San+Francisco','Singapore','Tokyo']

# job roles
job_set = ['data+engineer', 'machine+learning+engineer', 'data+scientist']

# output dir 
output_dir='./output'

# file num
file = 1

# from where to skip
SKIPPER = 0

# loop on all cities
for city in city_set:
    
    # for each job role
    for job_qry in job_set:
        
        # count
        cnt = 0
        startTime = time.time()

        # skipper
        if(file > SKIPPER):
        
            # dataframe
            df = pd.DataFrame(columns = ['unique_id', 'city', 'job_qry','job_title', 'company_name', 'location', 'summary', 'salary', 'link', 'date', 'full_text'])
        
            # for results
            for start in range(0, max_results_per_city, 10):

                # get dom 

                # hot fix here for Asia city scrapping (will optimize it then)
                if city=='Singapore':
                    page = requests.get('http://www.indeed.com.sg/jobs?q=' + job_qry +'&l=' + str(city) + '&start=' + str(start))

                elif city=='Tokyo':
                    page = requests.get('https://jp.indeed.com/jobs?q=' + job_qry +'&l=' + str(city) + '&start=' + str(start))

                else:
                    page = requests.get('http://www.indeed.com/jobs?q=' + job_qry +'&l=' + str(city) + '&start=' + str(start))

                #ensuring at least 1 second between page grabs                    
                time.sleep(1)  

                #fetch data
                soup = get_soup(page.text)
                divs = soup.find_all(name="div", attrs={"class":"row"})
                
                # if results exist
                if(len(divs) == 0):
                    break

                # for all jobs on a page
                for div in divs: 

                    #specifying row num for index of job posting in dataframe
                    num = (len(df) + 1) 
                    cnt = cnt + 1

                    #job data after parsing
                    job_post = [] 

                    #append unique id
                    job_post.append(div['id'])

                    #append city name
                    job_post.append(city)

                    #append job qry
                    job_post.append(job_qry)

                    #grabbing job title
                    job_post.append(extract_job_title(div))

                    #grabbing company
                    job_post.append(extract_company(div))

                    #grabbing location name
                    job_post.append(extract_location(div))

                    #grabbing summary text
                    job_post.append(extract_summary(div))

                    #grabbing salary
                    job_post.append(extract_salary(div))

                    #grabbing link
                    link = extract_link(div, city)
                    job_post.append(link)

                    #grabbing date
                    job_post.append(extract_date(div))

                    #grabbing full_text
                    job_post.append(extract_fulltext(link))

                    #appending list of job post info to dataframe at index num
                    df.loc[num] = job_post
                    
                #debug add
                write_logs(('Completed =>') + '\t' + city  + '\t' + job_qry + '\t' + str(cnt) + '\t' + str(start) + '\t' + str(time.time() - startTime) + '\t' + ('file_' + str(file)) + '  ' + str(current_time))

            #saving df as a local csv file  
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)
            df = df.sort_values('date') # sort the df by job post date
            df.to_csv('output/{}_jobs_{}_{}'.format(current_date, str(city).replace('+','_'), str(job_qry).replace('+','_'))  + '.csv', encoding='utf-8')
        
        else:

            #debug add
            write_logs(('Skipped =>') + '\t' + city  + '\t' + job_qry + '\t' + str(-1) + '\t' + str(-1) + '\t' + str(time.time() - startTime) + '\t' + ('file_' + str(file)) + '  ' + str(current_time))
        
        # increment file
        file = file + 1
