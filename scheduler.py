from main import jokes
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(jokes(), 'interval', seconds=10)
