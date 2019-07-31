# -*- coding: utf-8 -*-
__author__ = 'YongCong Wu'
# @Time    : 2019/7/29 10:22
# @Email   :  : 1922878025@qq.com




from django.urls import path, include
from User import views


urlpatterns = [
    path(r'login/', views.StudentsView.as_view()),
    path(r'routers/', views.RoutersData.as_view()),
    path(r'userinfo/', views.UserInfo.as_view()),
    path(r'userdata/', views.user_date_list),
    path(r'updateinfo/', views.UserdataView.as_view()),
    path(r'delete_user/', views.del_user_info),
    path(r'add_user/', views.add_user_info),
]