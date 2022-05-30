from django.shortcuts import render
import sys


from db.mysql import read, read2


def index(req):
    all = read()
    all2 = read2()
    context = {'all': all, 'all2' : all2}
    for one in all:
        print(one)

    return render(req, 'visual/main.html', context)



