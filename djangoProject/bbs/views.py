from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# 장고에서는 views가 컨트롤러 역할

def start(request) :
    return render(request, 'bbs/index.html')