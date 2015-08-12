__author__ = 'FRAMGIA\le.cong.phuc'
from django.db import models


class Subject(models.Model):
    name = models.CharField('Name', max_length=200)
    description = models.CharField('Description', max_length=500)
    created_at = models.DateTimeField('Created at')
    updated_at = models.DateTimeField('Updated at')
    begin_at = models.DateTimeField('Begin at')
    end_at = models.DateTimeField('End at')
    status = models.BooleanField('Status')

    class Meta:
        app_label = 'framgia'