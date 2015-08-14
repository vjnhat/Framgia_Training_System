__author__ = 'FRAMGIA\le.cong.phuc'
from django.db import models
from . import subject
from django.utils import timezone
import datetime

class Task(models.Model):
    name = models.CharField('Name', max_length=200)
    subject_id = models.ForeignKey(subject.Subject)
    content = models.CharField('Content', max_length=1000)
    created_at = models.DateTimeField('Created at', auto_now=True)
    begin_at = models.DateTimeField('Begin at', auto_now= True)
    end_at = models.DateTimeField('End at', default= timezone.now()+ datetime.timedelta(days = 90))

    class Meta:
        app_label = 'framgia'