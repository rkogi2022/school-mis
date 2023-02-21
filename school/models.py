from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class attendance(models.Model):
    studentname=models.CharField(max_length=200,null=True)
    studentid=models.CharField(max_length=50,null=True)
    lecturesattended=models.IntegerField(null=True)
    totallectures=models.IntegerField(null=True)

    def __str__(self):
        return self.studentname

class marks(models.Model):
    studentname=models.CharField(max_length=200,null=True)
    studentid=models.CharField(max_length=50,null=True)
    physics=models.IntegerField(null=True)
    mathematics=models.IntegerField(null=True)
    english=models.IntegerField(null=True)
    kiswahili=models.IntegerField(null=True)
    chemistry=models.IntegerField(null=True)
    biology=models.IntegerField(null=True)
    agriculture=models.IntegerField(null=True)
    def __str__(self):
        return self.studentname

class notice(models.Model):
    message = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message
 