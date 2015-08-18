__author__ = 'FRAMGIA\le.cong.phuc'
from framgia.models.course import Course
from django.views.generic import DetailView


class CourseDetailView(DetailView):
    queryset = Course.objects.all()
    template_name = 'course/course_detail.html'
