

from django.urls import path

from apps.project_management import views

urlpatterns = [
    ############html页面跳转#############
    # 项目介绍
    path('intro/', views.pj_intro.project_intro, name='project_intro'),
    # 项目host
    path('host/', views.pj_host.project_host, name='project_host'),
    # API接口页面
    path('interface/', views.pj_host.project_interface, name='project_interface'),
    # 测试用例
    path('case/', views.pj_host.test_case, name='test_case'),
    # 运行记录
    path('record/', views.pj_host.run_record, name='run_record'),
    # 新增api接口页面
    path('interface/add', views.api.add_api, name='add_api'),

    ############数据库操作#############
    # host保存到数据库
    path('host/insert', views.pj_host.host_insert, name='host_insert'),
    # host更新
    path('host/update', views.pj_host.host_update, name='host_update'),
    # host删除
    path('host/delete', views.pj_host.host_delete, name='host_delete'),
]