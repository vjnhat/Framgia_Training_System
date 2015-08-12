__author__ = 'FRAMGIA\le.cong.phuc'
from django.db import models
from . import subject


class Task(models.Model):
    name = models.CharField('Name', max_length=200)
    subject_id = models.ForeignKey(subject.Subject)
    content = models.CharField('Content', max_length=1000)
    created_at = models.DateTimeField('Created at')
    begin_at = models.DateTimeField('Begin at')
    end_at = models.DateTimeField('End at')

    class Meta:
        app_label = 'framgia'