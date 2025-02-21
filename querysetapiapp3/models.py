from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=20)
    branch = models.CharField(max_length=5)
    email = models.EmailField()
    address = models.CharField(max_length=30)
    marks = models.IntegerField()
    age = models.IntegerField()
    date_admited = models.DateField()
    date_passed = models.DateField()
