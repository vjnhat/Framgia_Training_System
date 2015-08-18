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

    """ get courses """

    def get_course(self):
        from framgia.models.course import Course
        list_other = Course.objects.exclude(subjects = self)
        list_course = []
        for course in Course.objects.all():
            if course not in list_other:
                list_course.append(course)
        return list_course



    class Meta:
        app_label = 'framgia'
        

