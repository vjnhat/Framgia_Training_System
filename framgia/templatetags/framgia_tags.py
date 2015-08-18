__author__ = 'FRAMGIA\le.cong.phuc'
from django import template
from framgia.models.course import Course
from framgia.models.task import Task
register = template.Library()


@register.inclusion_tag('course/course_list.html')
def get_course_list(takes_context=True):
    course_list = Course.objects.all()
    return {'course_list': course_list}


@register.inclusion_tag('task/task_subject.html')
def get_task_list(subject_id):
    task_list = Task.objects.filter(subject_id=subject_id)
    return {'task_list': task_list}
