from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def test(request):
    return HttpResponse('test:0001')


def home_page(request, template_name='home_page.html'):
    return render(request, template_name)

def home(request, template_name='home.html'):
    return render(request, template_name)

def Member_management(request, template_name='Member_management.html'):
    return render(request, template_name)