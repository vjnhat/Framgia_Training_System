from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [

    url(r'^$', views.base.BaseIndexView.as_view(), name='base_index'),

    url(r'^course/(?P<pk>[0-9]+)/$', views.course.CourseDetailView.as_view(), name='course_index'),

    url(r"^user/course-learning/", views.user.user_learning_course, name="user_course_learning"),

    url(r"^admin/", include(admin.site.urls)),

    url(r"^login/", views.user.login_user, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}, name="logout"),
    url(r'^register/$', views.user.register, name="register"),
    url(r'^admin/', include('framgia.views.admin.urls')),
]
