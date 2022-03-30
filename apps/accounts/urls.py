

from django.urls import path

from apps.accounts import views

urlpatterns = [


    # 成员管理页面
    path('member/', views.Member_management, name='Member_management'),


]