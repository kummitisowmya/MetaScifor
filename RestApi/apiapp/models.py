from django.db import models

# Create your models here.
class Student(models.Model):
    FirstName=models.CharField(max_length=200)
    LastName=models.CharField(max_length=200)



