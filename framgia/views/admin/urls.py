from django.conf.urls import include, url
from framgia.views.admin.course  import CourseList, CourseDetail, CourseUpdate, CourseDelete, CourseCreate
from framgia.views.admin.subject import SubjectCreate, SubjectDelete, SubjectDetail, SubjectList, SubjectUpdate

urlpatterns = [
    url(r'^courses/$',CourseList.as_view(), name = "course_index"),
    url(r'^course/(?P<pk>\d+)/$', CourseDetail.as_view(), name= "course_detail"),
    url(r'^course/(?P<pk>\d+)/edit/$', CourseUpdate.as_view(), name = "course_update"),
    url(r'^course/(?P<pk>\d+)/delete/$', CourseDelete.as_view(), name = "course_delete"),
    url(r'^course/new/$', CourseCreate.as_view(), name = "course_new" ),
    url(r'^subjects/$', SubjectList.as_view(), name = "subject_index"),
    url(r'^subject/(?P<pk>\d+)', SubjectDetail.as_view(),name = "subject_detail"),
    url(r'subject/(?P<pk>\d+)/edit/$', SubjectUpdate.as_view(), name="subject_update"),
    url(r'subject/(?P<pk>\d+)/delete/$', SubjectDelete.as_view(), name="subject_delete"),
    url(r'subject/new/$', SubjectCreate.as_view(), name="subject_new"),
 ]
