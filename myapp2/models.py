from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    age = models.IntegerField()

    # def __str__(self):
    #     return self.name


class Student(models.Model):
    class Branch(models.TextChoices):
        CSE = "CSE", "Computer Science and Engineering"
        EE = "EE", "Electrical Engineering"
        CE = "CE", "Civil Engineering"
        ME = "ME", "Mechanical Engineering"
        ECE = "ECE", "Electronics and Communication Engineering"

    name = models.CharField(max_length=20)
    branch = models.CharField(
        max_length=3,
        choices=Branch.choices,
        default=Branch.CSE,
    )
    email = models.EmailField()
    address = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        db_table = "student_details"
