from django.db import models

# Create your models here.
# 장고는 sql문을 몰라도 테이블을 생성할 수 있도록
# 제공하고 있음.
# ORM을 models.py에 정의해주세요.
# 테이블하나당 클래스하나로 정의
class Member(models.Model):
    #멤버변수를 생성해주면,
    #1.vo의 변수의 역할
    #2.table의 항목을 생성
    user_id = models.CharField(max_length=255)
    user_pw = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_tel = models.CharField(max_length=255)

#java vo에서의 toString()역할
    def __str__(self):
        return self.user_id + ", " + \
                self.user_pw + ", " + \
                self.user_name + ", " + \
                self.user_tel