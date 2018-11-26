#!/usr/bin/env python
# encoding: utf-8
'''
@author: zh
@file: urls.py
@time: 2018/10/26 13:52
@desc:
'''
from django.urls import path

from login import views

app_name = 'login'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('user_Confirm/', views.user_confirm, name='user_Confirm')
]
