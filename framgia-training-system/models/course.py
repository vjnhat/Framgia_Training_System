__author__ = 'FRAMGIA\le.cong.phuc'
from django.db import models
from . import subject


class Course(models.Model):
    name = models.CharField('Name', max_length=200)
    description = models.CharField('Description', max_length=500)
    created_at = models.DateTimeField('Created at')
    updated_at = models.DateTimeField('Updated at')
    begin_at = models.DateTimeField('Begin at')
    end_at = models.DateTimeField('End at')

    class Meta:
        app_label = 'framgia'


class CourseSubject(models.Model):
    course_id = models.ForeignKey(Course)
    subject_id = models.ForeignKey(subject.Subject)

    class Meta:
        app_label = 'framgia'