from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=500)
    question_writer = models.CharField(default='blank', max_length=500)

    def __str__(self):
        return str(self.id) + ", " + \
               self. question_text + ", " + \
               str(self.question_writer)