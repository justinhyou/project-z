import Util

from crontab import CronTab

cron = CronTab(user="hyobinyou")
changed = False
for job in cron:
    if job.comment == Util.cronJobName():
        cron.remove(job)
        changed = True

if changed:
    cron.write()
