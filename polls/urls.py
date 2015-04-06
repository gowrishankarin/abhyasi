#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Gowri Shankar
# @Date:   2015-04-04 17:45:18
# @Last Modified by:   Gowri Shankar
# @Last Modified time: 2015-04-04 18:41:43
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]