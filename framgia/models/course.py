__author__ = 'FRAMGIA\le.cong.phuc'
from django.db import models
from . import subject
from django.utils import timezone
import  datetime


class Course(models.Model):
    name = models.CharField('Name', max_length=200)
    description = models.CharField('Description', max_length=500)
    created_at = models.DateTimeField('Created at', auto_now=True)
    updated_at = models.DateTimeField('Updated at',auto_now=True)
    begin_at = models.DateTimeField('Begin at', auto_now=True)
    end_at = models.DateTimeField('End at', default= timezone.now()+ datetime.timedelta(days = 90))
    subjects = models.ManyToManyField(subject.Subject, through=u'CourseSubject', related_name='course')

    def __str__(self):
        return  self.name

    def get_subjects_list(self):
        return self.subjects.all()

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('CourseDetail.as_view()' , args=[str(self.id)])

    class Meta:
        app_label = 'framgia'


class CourseSubject(models.Model):
    course = models.ForeignKey(Course)
    subject = models.ForeignKey(subject.Subject)
    class Meta:
        app_label = 'framgia'