from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from framgia.models.course import Course, CourseSubject
from framgia.models.subject import Subject
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse


class CourseList(ListView):
    """ show all courses"""
    model = Course
    template_name = "admin/course/index.html"


class CourseDetail(DetailView):
    """ display all information about a course such as name, description, subjects."""
    model = Course
    template_name = 'admin/course/detail.html'


class CourseUpdate(UpdateView):
    """ Edit a course's information """
    model = Course
    fields = ['name', 'description']
    template_name = "admin/course/form/course_update_form.html"
    success_url = reverse_lazy("course_index")


class CourseDelete(DeleteView):
    """ Delete a course """
    model = Course
    success_url = reverse_lazy('course_index')
    template_name = 'admin/course/course_confirm_delete.html'


class CourseCreate(CreateView):
    """ Create a new course """
    model = Course
    lst_subjects = Subject.objects.all()
    fields = ["name", "description"]
    success_url = reverse_lazy("course_index")
    template_name = "admin/course/form/course_form.html"
