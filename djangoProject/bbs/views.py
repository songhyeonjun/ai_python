from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# 장고에서는 views가 컨트롤러 역할
import bbs.models


def start(request) :
    return render(request, 'bbs/index.html')

def insert(request) :
    return render(request, 'bbs/insert.html')

def insert2(request) :
    # post 방식으로 서버로 전달된 데이터를 받아야 한다.
    data = request.POST
    print(data)
    # 객체 생성해서 save()호출
    one = bbs.models.Bbs(no=data['no'],
                         title=data['title'],
                         content=data['content'],
                         writer=data['writer'])
    one.save()
    return HttpResponse('ok')
