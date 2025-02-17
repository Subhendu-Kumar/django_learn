from django.db import models

# Create your models here.


class SubhenduModel(models.Model):
    name = models.CharField(max_length=40)
    branch = models.CharField(max_length=20)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    age = models.IntegerField()
