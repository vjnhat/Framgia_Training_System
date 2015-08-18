__author__ = 'nhat'
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from framgia.models.course import Course, CourseSubject
from framgia.models.subject import Subject
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse


class SubjectList(ListView):
    """ show all subjects"""
    model = Subject
    template_name = "admin/subject/index.html"


class SubjectDetail(DetailView):
    """ display all information about a subject such as name, description, courses."""
    model = Subject
    template_name = 'admin/subject/detail.html'



class SubjectUpdate(UpdateView):
    """ Edit a subject's information """
    model = Subject
    fields = ['name', 'description']
    template_name = "admin/subject/subject_update_form.html"
    success_url = reverse_lazy("subject_index")


class SubjectDelete(DeleteView):
    """ Delete a subject """
    model = Subject
    success_url = reverse_lazy('subject_index')
    template_name = 'admin/subject/subject_confirm_delete.html'


class SubjectCreate(CreateView):
    """ Create a new subject """
    model = Subject
    fields = ["name", "description"]
    success_url = reverse_lazy("subject_index")
    template_name = "admin/subject/subject_form.html"
