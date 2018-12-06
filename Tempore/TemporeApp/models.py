from django.db import models
from django import forms
# Create your models here.
class person(models.Model):
    FirstName=models.CharField(max_length=20)
    LastName=models.CharField(max_length=20)
    Location=models.CharField(max_length=50)

    def __str__(self):
        return self.FirstName