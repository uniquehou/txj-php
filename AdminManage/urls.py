from django.conf.urls import url
from AdminManage import views

app_name = "AdminManage"
urlpatterns = [
    url(r'^$', views.index),
    url(r'^index', views.index, name="index"),
    url(r'^login', views.login, name="login"),
    url(r'^regis', views.regis, name="regis"),
    url(r'^index$', views.index, name="index"),
    url(r'info_manage', views.info_manage, name="info_manage"),
    url(r'password_modify', views.password_modify, name="password_modify"),
    url(r'password_find', views.password_find, name="password_find"),
    url(r'free_course_manage', views.free_course_manage, name='free_course_manage'),
    url(r'free_course_show', views.free_course_show, name='free_course_show'),
    url(r'^download$', views.download, name="download"),
    url(r'^exit', views.exit, name="exit"),
]
