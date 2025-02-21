from django.db import models

# Create your models here.


class my_model(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=10)
    age = models.IntegerField()
    dob = models.DateField()