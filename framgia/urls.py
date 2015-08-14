__author__ = 'FRAMGIA\le.cong.phuc'
"""TrainingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from framgia.view.course import CourseList, CourseDetail, CourseUpdate, CourseDelete, CourseCreate
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^courses/$',CourseList.as_view(), name = "course_index"),
    url(r'^course/(?P<pk>\d+)/$', CourseDetail.as_view(), name= "course_detail"),
    url(r'^course/(?P<pk>\d+)/edit/$', CourseUpdate.as_view(), name = "course_update"),
    url(r'^course/(?P<pk>\d+)/delete$', CourseDelete.as_view(), name = "course_delete"),
    url(r'^course/new/$', CourseCreate.as_view(), name = "course_new" ),
]
