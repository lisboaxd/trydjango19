from django.conf.urls import url
from django.contrib import admin
from .views import (posts_list,posts_create,posts_detail,posts_delete,posts_update,)

urlpatterns = [
    url(r'^$', posts_list, name='list'),
    url(r'^create/$', posts_create, name='create'),
    url(r'^(?P<id>\d+)/detail/$', posts_detail,name='detail'),
    url(r'^(?P<id>\d+)/delete/$', posts_delete, name='delete'),
    url(r'^(?P<id>\d+)/edit/$', posts_update, name='update'),
]
