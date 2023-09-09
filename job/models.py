from django.db import models

JOB_TYPE = (
            ('Full Time','Full Time'),
            ('Work from home','Work from home'),
            ('Part Time','Part Time'),
            ('Shift based','Shift based'),
)

class Job(models.Model):
    title = models.CharField(max_length=100)
    # location = 
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title