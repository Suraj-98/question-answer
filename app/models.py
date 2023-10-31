from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()

    def __str__(self):
        return str(self.question)

class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.TextField()
    like = models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return str(self.answer)