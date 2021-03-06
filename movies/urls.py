# coding: utf-8
from django.conf.urls import patterns, url


urlpatterns = patterns('movies.views',
    url(r'^$', 'home', name='home'),
    url(r'^filme/(?P<slug>[\w-]+)/$', 'detail', name='detail'),
    url(r'^genero/(?P<slug>[\w-]+)/$', 'genre', name='genre'),
    url(r'^ator/(?P<slug>[\w-]+)/$', 'actor', name='actor'),
)