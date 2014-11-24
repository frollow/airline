# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

import blog
from blog.views import PostDetailView


urlpatterns = patterns('',
    url(r'^$', blog.views.news),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
)