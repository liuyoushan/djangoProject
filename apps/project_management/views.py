import json

from django.http import HttpResponse
from django.shortcuts import render

from .models import Host


# Create your views here.


# 项目介绍模块类方法
class pj_intro:
    def project_intro(request, template_name='project_intro.html'):
        return render(request, template_name)


# host模块类方法
class pj_host:
    # ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇HTML页面接口⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇
    # 调用request.GET.get()方法会警告，根据提示在初始化加上self.GET=None
    def __init__(self):
        self.GET = None

    # 项目host模块的html页面，包括host列表展示
    def project_host(request, template_name='project_host.html'):
        # 查询host列表进行显示
        # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
        list = Host.objects.all()
        # 查询输出所有数据
        hostlist = {}
        for var in list:
            hostlist[var.id] = [var.name, var.host, var.description]
        # print(hostlist)
        return render(request, template_name, {
            'hostlist': hostlist,
        })

    # api接口模块
    def project_interface(request, template_name='API_interface.html'):
        return render(request, template_name)

    # 测试用例
    def test_case(request, template_name='test_case.html'):
        return render(request, template_name)

    # 运行记录
    def run_record(request, template_name='run_record.html'):
        return render(request, template_name)

    # ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇接口相关⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇
    # 新增host
    def host_insert(request):
        request.encoding = 'utf-8'
        # 获取表单数据，name、host、description描述
        name = request.GET.get('name', ' ')
        host = request.GET.get('host', ' ')
        description = request.GET.get('description')
        # print('--------------------',name,host,description)
        # 插入数据
        if name and host:
            inserte = Host(name=name, host=host, description=description)
            inserte.save()
            data = {'data': {'name': name, 'host': host, 'description': description}}
            return HttpResponse(json.dumps(data), content_type='application/json')
            # return Host.objects.all()
        else:
            return HttpResponse('name和host不能为空')

    # host更新
    def host_update(request):
        # 从前端获取id、name、host、decription
        ids = request.GET.get('ids', 'null')
        name = request.GET.get('name', 'null')
        host = request.GET.get('host', 'null')
        description = request.GET.get('description', 'null')
        # 修改
        Host.objects.filter(id=ids).update(name=name, host=host, description=description)
        return HttpResponse('修改成功')


    # host删除
    def host_delete(request):
        # 从前端获取id
        ids = request.GET.get('id', 'null')
        # 按id筛选，从数据库获取到列表所有信息
        dele_data=Host.objects.filter(id=ids).values('name', 'host', 'description')
        # 转换成列表
        data = [str(i) for i in dele_data]
        # 需要先将字符串转换成字典
        data = eval(data[0])
        data = {'data': data}

        try:
            # 删除指定id的数据
            Host.objects.filter(id=ids).delete()
            return HttpResponse(json.dumps(data), content_type='application/json')
        except Exception as e:
            return HttpResponse(e)

# api接口页面
class api:
    # 打开添加接口表单
    def add_api(request, template_name='add_API.html'):
        return render(request, template_name)
