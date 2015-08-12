__author__ = 'FRAMGIA\le.cong.phuc'
from django.db import models
from . import course, subject, task


class User(models.Model):
    name = models.CharField('Name',max_length=100)
    email = models.CharField('Email', max_length=100)
    password = models.CharField('Password', max_length=100)
    remember = models.BooleanField('Remember')
    supervision = models.BooleanField('Supervision')
    study_status = models.BooleanField('Study Status')
    created_at = models.DateTimeField('Created at')
    updated_at = models.DateTimeField('Updated at')

    class Meta:
        app_label = 'framgia'


class UserCourse(models.Model):
    user_id = models.ForeignKey(User)
    course_id = models.ForeignKey(course.Course)
    status = models.BooleanField('Status')

    class Meta:
        app_label = 'framgia'


class UserSubjects(models.Model):
    user_id = models.ForeignKey(User)
    subject_id = models.ForeignKey(subject.Subject)
    status = models.BooleanField('Status')

    class Meta:
        app_label = 'framgia'


class UserTask(models.Model):
    user_id = models.ForeignKey(User)
    task_id = models.ForeignKey(task.Task)
    status = models.BooleanField('Status')

    class Meta:
        app_label = 'framgia'
