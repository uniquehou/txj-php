from django.conf.urls import url
from . import views

app_name = "SignIn"
urlpatterns = [
    url(r'^$', views.index),
    url(r'index', views.index, name='index'),
    url(r'submit', views.submit, name='submit'),
]
