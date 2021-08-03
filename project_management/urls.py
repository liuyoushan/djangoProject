

from django.urls import path

from project_management import views

urlpatterns = [
    # 项目管理页面
    path('project/', views.project, name='project'),
    # 项目介绍
    path('project/intro', views.project_intro, name='project_intro'),
    # 项目host
    path('project/host', views.project_host, name='project_host'),

    # API接口
    path('project/interface', views.project_interface, name='project_interface'),

    # 测试用例
    path('project/case', views.test_case, name='test_case'),
    # 运行记录
    path('project/record', views.run_record, name='run_record'),

    # host保存到数据库
    path('host/insert', views.host_insert, name='host_insert'),

    # host更新
    path('host/update', views.host_update, name='host_update'),

    # host删除
    path('host/delete', views.host_delete, name='host_delete'),
]