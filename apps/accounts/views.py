from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def Member_management(request, template_name='Member_management.html'):
    return render(request, template_name)