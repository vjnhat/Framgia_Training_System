__author__ = 'FRAMGIA\le.cong.phuc'
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from framgia.models.course import Course, CourseSubject
from framgia.models.subject import Subject
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

class CourseList(ListView):
    model = Course
    template_name = "course/index.html"

# display all information about a course such as name, description, subjects.
class CourseDetail(DetailView):
    model = Course
    template_name = 'course/detail.html'


class CourseUpdate(UpdateView):
    model = Course
    fields = ['name', 'description']
    template_name = "course/form/course_update_form.html"
    success_url = reverse_lazy("course_index")


class CourseDelete(DetailView):
    model = Course
    success_url = reverse_lazy('course_index')
    template_name = 'course/course_confirm_delete.html'

class CourseCreate(CreateView):
    model = Course
    fields = ["name", "description"]
    success_url = reverse_lazy("course_index")
    template_name = "course/form/course_form.html"

