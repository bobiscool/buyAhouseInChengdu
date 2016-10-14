  #coding=utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
import os

def tick():
    print('ehdkn')
    os.system('scrapy crawl kanfang')
   
if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick,'interval',hours=8)

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown() 