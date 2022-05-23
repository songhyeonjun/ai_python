from django.http import HttpResponse
from django.shortcuts import render

# member 메뉴와 관련된 컨트롤러 역할.
# urls.py에 요청된 주소별로 함수가 지정되어있어야 함.
# 요청된 주소 하나당 함수 하나!!!
# 요청된 주소에 따른 함수를 views.py를 정의
def index(request):
    print('홈페이지 시작화면입니다.')
    #return HttpResponse('내가 시작하는 첫페이지..')
    # return HttpResponse(
    #     "<body bgcolor=yellow>" +
    #     "<h3>장고 프로젝트1</h3><hr color=red>" +
    #     "-<a href=member/>start page로</a><br>" +
    #     "-<a href=member/index1>index1 page로</a><br>" +
    #     "-<a href=member/index2>index2 page로</a><br>" +
    #     "-<a href=member/index3>index3 page로</a><br>" +
    #     "-<a href=admin/>admin page로</a><br>" +
    #     "-<a href=http://www.naver.com>naver로</a><br>" +
    #     "-<a href=http://www.daum.net>daum로</a><br>" +
    #     "</body>"
    # )
    return render(request, 'member/index.html')

def index1(request):
    return HttpResponse(
        "<body bgcolor=blue>" +
        "<h3>index1 페이지입니다.</h3><hr color=red>" +
        "<h3>장고 홈페이지 index1입니다.</h3>" +
        "<a href=/member/>member page로</a><br>" +
        "<a href='/'>index page로</a><br>" +
        "</body>"
    )

def index3(request):
    return render(request, 'member/index3.html')


def index2(request):
    return HttpResponse(
        "<body bgcolor=lime>" +
        "<h3>index2 페이지입니다.</h3><hr color=red>" +
        "<h3>장고 홈페이지 index2입니다.</h3>" +
        "<a href=/member/>member page로</a><br>" +
        "<a href='/'>index page로</a><br>" +
        "</body>"
    )


def start(request):
    print('시작페이지 호출됨.')
    return HttpResponse('내가 리턴되는 내용임.')