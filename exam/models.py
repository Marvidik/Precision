from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()


class Maths(models.Model):
    Quest=models.TextField()
    op1=models.CharField(max_length=100)
    op2=models.CharField(max_length=100)
    op3=models.CharField(max_length=100)
    op4=models.CharField(max_length=100)
    ans=models.CharField(max_length=100)

    def __str__(self):

        return self.Quest

class  Essay(models.Model):
    essay=models.TextField()

class English(models.Model):
    essay=models.ForeignKey(Essay,on_delete=models.CASCADE)
    Quest=models.TextField()
    op1=models.CharField(max_length=100)
    op2=models.CharField(max_length=100)
    op3=models.CharField(max_length=100)
    op4=models.CharField(max_length=100)
    ans=models.CharField(max_length=100)

    def __str__(self):

        return self.Quest

class Score(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=100)
    score=models.IntegerField()

    def __str__(self):
        return str(self.student)



class Demo(models.Model):
    essay=models.TextField()
    Quest=models.TextField()
    op1=models.CharField(max_length=100)
    op2=models.CharField(max_length=100)
    op3=models.CharField(max_length=100)
    op4=models.CharField(max_length=100)



