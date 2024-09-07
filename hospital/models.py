from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms

# Create your models here.
class User(AbstractUser):

    usertype = models.CharField(max_length=100)


class Speciality(models.Model):

    Sp_Name = models.CharField(max_length=100)


class Patient(models.Model):

    sp_id = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Address = models.CharField(max_length=200)
    Phone = models.BigIntegerField()
    Age =  models.PositiveIntegerField()

class Doctor(models.Model):

    sp_id = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Address = models.CharField(max_length=200)
    Phone = models.BigIntegerField()
    Age =  models.PositiveIntegerField()
    Qualification = models.CharField(max_length=100)

class Book(models.Model):
    date = models.DateField()
    time = models.TimeField()
    sp_id = models.ForeignKey(Speciality, default=1,on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)


