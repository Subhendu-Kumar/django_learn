from django.db import models

# Create your models here.


class user(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=10)

    class Meta:
        db_table = "users"
