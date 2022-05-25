from django.contrib import admin
from django.urls import path

import member.views
import question.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', member.views.start),
    path('member/', member.views.index),
    path('member/insert', member.views.insert),
    path('member/insert2', member.views.insert2),
    path('member/del', member.views.delete),
    path('member/del2', member.views.delete2),
    path('member/one', member.views.one),
    path('member/one2', member.views.one2),
    path('member/one22/<id>', member.views.one22),
    path('member/up/<id>', member.views.up),
    path('member/up2', member.views.up2),
    path('member/all', member.views.all),
    path('member/login', member.views.login),
    path('member/login2', member.views.login2),

    path('question/', question.views.start)
    path('question/insert', question.views.start)
    path('question/', question.views.start)
]