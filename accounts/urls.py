

from django.urls import path

from accounts import views

urlpatterns = [
    path('list/', views.test, name='list'),
    # 主页面
    path('home/', views.home, name='home'),
    # 首页页面
    path('home/page', views.home_page, name='home_page'),
    # 项目管理页面

    # 成员管理页面
    path('home/Member', views.Member_management, name='Member_management'),


]