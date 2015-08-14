from django.db import models
from django.utils import timezone
import datetime


class Subject(models.Model):
    name = models.CharField('Name', max_length=200)
    description = models.CharField('Description', max_length=500)
    created_at = models.DateTimeField('Created at', auto_now=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
    begin_at = models.DateTimeField('Begin at', auto_now=True)
    end_at = models.DateTimeField('End at', default= timezone.now()+ datetime.timedelta(days = 90))
    status = models.BooleanField('Status', default= True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'framgia'