from apscheduler.schedulers.background import BackgroundScheduler
from .models import Job
from django.utils import timezone

scheduler = BackgroundScheduler()

def execute_job(job: Job):
    # Implement job execution logic based on job type
    print(f"Executing job: {job.name}")
    job.last_run = timezone.now()
    job.next_run = job.last_run + timezone.timedelta(seconds=job.interval)
    job.save()

def schedule_job(job: Job):
    scheduler.add_job(
        execute_job,
        'interval',
        seconds=job.interval,
        args=[job],
        id=str(job.id),
        replace_existing=True
    )
    scheduler.start()