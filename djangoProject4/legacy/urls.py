from django.urls import path
from . import views

app_name = 'legacy'
urlpatterns = [
    path('visual/', views.index, name='customers'),
]
