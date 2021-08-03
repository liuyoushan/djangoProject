from django.http import HttpResponse
from django.shortcuts import render

from .models import Host
# Create your views here.

# 项目主页
def project(request, template_name='project_management.html'):
    return render(request, template_name)

# 项目介绍
def project_intro(request, template_name='project_intro.html'):
    return render(request, template_name)

# 项目host模块的html页面，包括host列表展示
def project_host(request, template_name='project_host.html'):
    # 查询host列表进行显示
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Host.objects.all()
    # 查询输出所有数据
    hostlist = {}
    for var in list:
        hostlist[var.id]=[var.name, var.host, var.description]
    # print(hostlist)
    return render(request, template_name, {
        'hostlist':hostlist,
    })

# api接口
def project_interface(request, template_name='API_interface.html'):
    return render(request, template_name)

# 测试用例
def test_case(request, template_name='test_case.html'):
    return render(request, template_name)

# 运行记录
def run_record(request, template_name='run_record.html'):
    return render(request, template_name)

# host保存到数据库
def host_insert(request):
    request.encoding='utf-8'
    # 获取表单数据
    name=request.GET.get('name', ' ')
    host = request.GET.get('host', ' ')
    description = request.GET.get('description')
    # print('--------------------',name,host,description)
    # 插入数据
    if name and host:
        inserte = Host(name=name,host=host,description=description)
        inserte.save()
        return HttpResponse('添加成功')
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
    Host.objects.filter(id=ids).update(name=name,host=host,description=description)
    return HttpResponse('pass')

# host删除
def host_delete(request):
    # 从前端获取id
    ids = request.GET.get('id', 'null')
    try:
        # 删除指定id的数据
        Host.objects.filter(id=ids).delete()
        return HttpResponse('pass')
    except Exception as e:
        return HttpResponse(e)