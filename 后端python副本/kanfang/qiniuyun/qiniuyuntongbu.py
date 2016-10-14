
#sync json
from apscheduler.schedulers.blocking import BlockingScheduler
import os

def tick():
    os.system('python qiniuyun.py')

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick,'interval',minutes=2)

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()