from crontab import CronTab

#This function will help you to set up your CRON job.
def setCronJob(run_type, hours, minutes, dow, dom, month):
    my_cron = CronTab(user='henriterrasse')

    #the path must be the right one here.
    cmd = 'python ~/Code/job_offers_monitoring/wrapper.py'
    job = my_cron.new(command=cmd)
    if run_type.lower() == "daily":
        job.minute.on(minutes)
        job.hour.on(hours)
    elif run_type.lower() == "weekly":
        job.dow.on(dow)
        job.minute.on(minutes)
        job.hour.on(hours)
    elif run_type.lower() == "monthly":
        job.dom.on(dom)
        job.minute.on(minutes)
        job.hour.on(hours)
    elif run_type.lower() == "yearly":
        job.dom.on(dom)
        job.month.on(month)
        job.minute.on(minutes)
        job.hour.on(hours)
    my_cron.write()
    print(my_cron.render())

setCronJob("daily", 12, 00, "","","")