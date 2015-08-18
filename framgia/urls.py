from django.conf.urls import include, url
from django.contrib import admin
from . import views
from framgia.views.admin.course  import CourseList, CourseDetail, CourseUpdate, CourseDelete, CourseCreate

urlpatterns = [
    url(r"^$", views.base.index, name="base_index"),

    # url(r"^course/(?P<course_id>[0-9]+)/$", views.course.index, name="course_index"),
    url(r"^course/", views.course.index, name="course_index"),

    url(r"^user/course-learning/", views.user.user_learning_course, name="user_course_learning"),

    url(r"^admin/", include(admin.site.urls)),

    url(r"^login/", views.user.login_user, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name="logout"),
    url(r'^register/$', views.user.register, name="register"),
    url(r'^users/(?P<pk>\d+)/profile/$', views.user.ProfileDetail.as_view(), name="profile"),
    url(r'^users/(?P<pk>\d+)/edit/$', views.user.EditProfile.as_view(), name="editprofile"),

    url(r'^admin/courses/$',CourseList.as_view(), name = "course_index"),
    url(r'^admin/course/(?P<pk>\d+)/$', CourseDetail.as_view(), name= "course_detail"),
    url(r'^admin/course/(?P<pk>\d+)/edit/$', CourseUpdate.as_view(), name = "course_update"),
    url(r'^admin/course/(?P<pk>\d+)/delete/$', CourseDelete.as_view(), name = "course_delete"),
    url(r'^admin/course/new/$', CourseCreate.as_view(), name = "course_new" ),
]
