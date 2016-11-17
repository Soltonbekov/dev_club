# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list, name = 'post_list'),
    url(r'^create_post/add/$', views.create_post, name = 'create_post'),
    url(r'^edit_post/(?P<post_id>[0-9]+)/$', views.edit_post, name = 'edit_post'),
    url(r'^delete_post/(?P<post_id>[0-9]+)/$', views.delete_post, name = 'delete_post'),
]
