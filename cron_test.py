import datetime

def main():
    current_time, current_date  = datetime.datetime.now(), datetime.datetime.now().strftime('%Y-%m-%d')
    print('current time : ', current_time)
    with open('output/{}.txt'.format('output-'+str(current_date)), "w") as file:
        file.write('* this is cron test program \n')
        file.write(str(current_time) + '\n')
        file.write('hello world')
        file.close()
        print ('write to file OK')

if __name__ == '__main__':
    main()