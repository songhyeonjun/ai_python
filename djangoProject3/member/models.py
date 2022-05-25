from django.db import models

# Create your models here.
class Question(models.Model) :
    question_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('')

    def __str__(self):
        return str(self.id) + ", " + \
               self. question_text + ", " + \
               str(self.pub_date)

class Test(models.Model) :
    ## id는 default로 만들어진다.
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    addr = models.CharField(max_length=200)

    # python override
    def __str__(self):
        return str(self.id) + ", " + self.name + ", " + \
            self.tel + ", " + self.addr


