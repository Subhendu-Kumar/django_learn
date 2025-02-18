from django.db import models

# Create your models here.


class SuModel(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    age = models.IntegerField()
