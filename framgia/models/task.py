__author__ = 'FRAMGIA\le.cong.phuc'
from django.db import models
from framgia.models.subject import Subject


class Task(models.Model):
    name = models.CharField('Name', max_length=200)
    subject = models.ForeignKey(Subject)
    answer_a = models.CharField('Answer A', max_length=500)
    answer_b = models.CharField('Answer B', max_length=500)
    answer_c = models.CharField('Answer C', max_length=500)
    answer_true = models.CharField('Answer true', max_length=1)
    created_at = models.DateTimeField('Created at', auto_now=True)
    begin_at = models.DateTimeField('Begin at', auto_now=True)
    end_at = models.DateTimeField('End at', auto_now=True)

    class Meta:
        app_label = 'framgia'
