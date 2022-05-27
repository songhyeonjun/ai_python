from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Visual

def index(request):
    customers = Visual.objects.all()[:5]
    output = '<br>'.join([c.place_info for c in customers])
    return HttpResponse(output)