from django.db import models

# Create your models here.


class user1(models.Model):
    Name = models.CharField(max_length=50, default="")
    password = models.IntegerField(max_length=50, default="")


class created1(models.Model):
    Username = models.CharField(max_length=50, default="")
    password1 = models.IntegerField(max_length=20, default="")
    Fname = models.CharField(max_length=50, default="")
    Lname = models.CharField(max_length=50, default="")
    Email = models.CharField(max_length=50, default="")
    pass1 = models.IntegerField(max_length=20, default="")
    mobile = models.IntegerField(max_length=20, default="")
    branch = models.CharField(max_length=50, default="")
