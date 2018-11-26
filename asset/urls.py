#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf.urls import url
from asset import views
from django.urls import path

app_name = 'asset'

urlpatterns = [
    path('report/', views.report, name='report'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    path('detail/<int:asset_id>', views.detail, name="detail"),
    path('', views.dashboard),
]


