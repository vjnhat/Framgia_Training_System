from django.conf.urls import include, url
from django.contrib import admin
from . import views
from framgia.views.admin.course  import CourseList, CourseDetail, CourseUpdate, CourseDelete, CourseCreate
from framgia.views.admin.subject import SubjectCreate, SubjectDelete, SubjectDetail, SubjectList, SubjectUpdate

urlpatterns = [

    url(r'^$', views.base.BaseIndexView.as_view(), name='base_index'),

    url(r'^course/(?P<pk>[0-9]+)/$', views.course.CourseDetailView.as_view(), name='course_index'),

    url(r"^user/course-learning/", views.user.user_learning_course, name="user_course_learning"),

    url(r"^admin/", include(admin.site.urls)),

    url(r"^login/", views.user.login_user, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}, name="logout"),
    url(r'^register/$', views.user.register, name="register"),
    url(r'^admin/courses/$',CourseList.as_view(), name = "course_index"),
    url(r'^admin/course/(?P<pk>\d+)/$', CourseDetail.as_view(), name= "course_detail"),
    url(r'^admin/course/(?P<pk>\d+)/edit/$', CourseUpdate.as_view(), name = "course_update"),
    url(r'^admin/course/(?P<pk>\d+)/delete/$', CourseDelete.as_view(), name = "course_delete"),
    url(r'^admin/course/new/$', CourseCreate.as_view(), name = "course_new" ),
    url(r'^admin/subjects/$', SubjectList.as_view(), name = "subject_index"),
    url(r'^admin/subject/(?P<pk>\d+)', SubjectDetail.as_view(),name = "subject_detail"),
    url(r'admin/subject/(?P<pk>\d+)/edit/$', SubjectUpdate.as_view(), name="subject_update"),
    url(r'admin/subject/(?P<pk>\d+)/delete/$', SubjectDelete.as_view(), name="subject_delete"),
    url(r'admin/subject/new/$', SubjectCreate.as_view(), name="subject_new"),
]
