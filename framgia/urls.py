from django.conf.urls import include, url
from django.contrib import admin
<<<<<<< HEAD
from framgia.view import user, base
=======
from . import views

>>>>>>> [UPDATE] code
urlpatterns = [
    url(r'^$', views.base.index, name='base_index'),

    # url(r'^course/(?P<course_id>[0-9]+)/$', views.course.index, name='course_index'),
    url(r'^course/', views.course.index, name='course_index'),

    url(r'^user/course-learning/', views.user.user_learning_course, name='user_course_learning'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', user.login_user, name="login"),
    url(r"^$", base.Home.as_view(), name="home"),
]
