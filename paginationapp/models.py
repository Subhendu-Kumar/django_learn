from django.db import models

# Create your models here.


class book(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=20)
    published = models.DateField()
