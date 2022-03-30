

from django.urls import path

from . import views

urlpatterns = [
    # 主页面
    path('', views.home, name='home'),
    # 首页页面
    path('page/', views.home_page, name='home_page'),
    # 成员管理页面
    path('Member/', views.Member_management, name='Member_management'),


]