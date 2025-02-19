from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class new_book(models.Model):
    book_name = models.CharField(max_length=20)
    book_author = models.CharField(max_length=15)
    book_published_date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class post(models.Model):
    post_title = models.CharField(max_length=30)
    post_category = models.CharField(max_length=10)
    post_published_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class dance(models.Model):
    dance_name = models.CharField(max_length=10)
    dance_type = models.CharField(max_length=10)
    user = models.ManyToManyField(User)

    def dance_by(self):
        return ",".join([str(d) for d in self.user.all()])
