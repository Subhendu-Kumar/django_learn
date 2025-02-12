from django.db import models

# Create your models here.


class SkModel(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    age = models.IntegerField()
