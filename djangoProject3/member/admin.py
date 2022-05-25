from django.contrib import admin

# Register your models here.
from member.models import Question, Test

admin.site.register(Question)
admin.site.register(Test)
