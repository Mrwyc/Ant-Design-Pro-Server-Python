# -*- coding: utf-8 -*-
__author__ = 'YongCong Wu'
# @Time    : 2019/7/29 10:22
# @Email   :  : 1922878025@qq.com




from django.urls import path, include
from User import views


urlpatterns = [
    path(r'login/', views.StudentsView.as_view()),
    path(r'user_login/', views.user_login),
    path(r'routers/', views.RoutersData.as_view()),
    path(r'userinfo/', views.UserInfo.as_view()),
    path(r'userdata/', views.user_date_list),
    path(r'updateinfo/', views.UserdataView.as_view()),
    path(r'delete_user/', views.del_user_info),
    path(r'add_user/', views.add_user_info),
    path(r'add_aritive/', views.add_aritive_data),
    path(r'get_ariticle/', views.get_ariticle_list),
    path(r'add_one_mulu/', views.add_mulu),
    path(r'get_one_mulu/', views.get_one_mulu),
    path(r'add_two_mulu/', views.add_two_mulu),
    path(r'get_mulu/', views.get_mulu),
    path(r'get_one_mulu_data/', views.get_one_mulu_data),
    path(r'get_two_mulu_data/', views.get_two_mulu_data),
    path(r'create_content/', views.create_content),
    path(r'get_context/', views.get_context),
]