from django.conf.urls import include, url
from django.contrib import admin
from . import views

from framgia.view.course import CourseList, CourseDetail, CourseUpdate, CourseDelete, CourseCreate
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r"^user/course-learning/", views.user.user_learning_course, name="user_course_learning"),

    url(r"^admin/", include(admin.site.urls)),

    url(r"^login/", views.user.login_user, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}, name="logout"),
    url(r'^courses/$',CourseList.as_view(), name = "course_index"),
    url(r'^course/(?P<pk>\d+)/$', CourseDetail.as_view(), name= "course_detail"),
    url(r'^course/(?P<pk>\d+)/edit/$', CourseUpdate.as_view(), name = "course_update"),
    url(r'^course/(?P<pk>\d+)/delete$', CourseDelete.as_view(), name = "course_delete"),
    url(r'^course/new/$', CourseCreate.as_view(), name = "course_new" ),
]