from django.conf.urls import include, url
from django.contrib import admin
from framgia.view import user, base
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', user.login_user, name="login"),
    url(r"^$", base.Home.as_view(), name="home"),
]
