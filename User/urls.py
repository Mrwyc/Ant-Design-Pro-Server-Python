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
    path(r'web_get_centext/', views.web_get_centext),
    path(r'context_update_del/', views.context_update_del),
    path(r'web_get_context/', views.web_get_context),
    path(r'get_web_name/', views.get_web_name),       # 获取系统名称
    path(r'update_web_name/', views.update_web_name),       # 修改网站名称
    path(r'filter_huashu/', views.filter_huashu),       # 筛选话术
    path(r'register_user/', views.register_user),       # 用户注册
    path(r'web_get_user_info/', views.web_get_user_info),       # 获取用户信息
    path(r'web_login_user/', views.web_login_user),       # 用户登陆
    path(r'web_context_list/', views.web_context_list),       # 用户登陆
    path(r'web_get_contextInfo/', views.web_get_contextInfo),       # 用户登陆
    path(r'web_get_setting_info/', views.web_get_setting_info),       # 获取网站会员简介
    path(r'web_get_setting_infotwo/', views.web_get_setting_infotwo),       # 获取客服微信
]