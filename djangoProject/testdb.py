# -*- coding: utf-8 -*-

from django.http import HttpResponse

from project_management import models




def host_test(request):
    # 获取表单数据

    # 插入数据
    inserte = models.Host(name='测试环境',host='127.0.0.1',description='描述看看.....')
    inserte.save()
    return HttpResponse('添加成功')
