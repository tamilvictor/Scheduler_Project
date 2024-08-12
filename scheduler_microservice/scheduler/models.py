from django.db import models

class Job(models.Model):
    JOB_TYPES = [
        ('email_notification', 'Email Notification'),
        ('number_crunching', 'Number Crunching'),
        ('data_backup', 'Data Backup'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    job_type = models.CharField(max_length=50, choices=JOB_TYPES)
    interval = models.IntegerField()  # Interval in seconds
    last_run = models.DateTimeField(blank=True, null=True)
    next_run = models.DateTimeField(blank=True, null=True)
    parameters = models.JSONField(blank=True, null=True)  # Additional parameters

    def __str__(self):
        return self.name