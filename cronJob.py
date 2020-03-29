import os
import Util

from crontab import CronTab

cron = CronTab(user="hyobinyou")

exists = False
for job in cron:
    if job.comment == Util.cronJobName():
        exists = True

if not exists:
    command = "/usr/local/bin/python3 " + Util.workspace() +'/' + "updateData.py >> " + Util.workspace() #+ "/" + "test.out 2>&1"
    job = cron.new(command=command, comment=Util.cronJobName())
    job.hour.every(1)

    cron.write()
