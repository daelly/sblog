#coding:utf-8
'''
Created on 2016年2月19日

@author: daelly
'''
from django.conf.urls import url

from . import views

app_name = 'sblog'

urlpatterns = [
    url(r'^index$', views.blog_home),
    url(r'^$', views.blog_home, name='home'),
    url(r'^category/(?P<category_slug>\w+)$', views.blog_category, name='category'),
    url(r'^about$', views.blog_about, name='about'),
    url(r'^learn$', views.blog_learn, name='learn'),
    url(r'^diary$', views.blog_diary, name='diary'),
    url(r'^shuo$', views.blog_shuo, name='shuo'),
    url(r'^album$', views.blog_album, name='album'),
    url(r'^board$', views.blog_board, name='board'),
    url(r'^article/(?P<blog_id>[0-9]+)$', views.blog_detail, name='detail'),
]