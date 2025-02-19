from django.db import models

# Create your models here.


# abstract base class models
class common_info(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    date = models.DateField()

    class Meta:
        abstract = True


class trainer(common_info):
    address = models.CharField(max_length=50)
    date = None


class teacher(common_info):
    salary = models.IntegerField()
    date = models.DateTimeField()


# multi table inheritance
class bank(models.Model):
    b_name = models.CharField(max_length=50)
    b_address = models.CharField(max_length=100)


class b_manager(bank):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


# proxy model inheritance
class university(models.Model):
    uname = models.CharField(max_length=30)
    ulocation = models.CharField(max_length=30)


class college(university):
    class Meta:
        proxy = True
