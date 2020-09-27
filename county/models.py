# Register your models here.
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class CountyListEntry(models.Model):
    user=models.ForeignKey('User', on_delete=models.CASCADE, related_name='usernames')
    countyname=models.CharField(max_length=255)
    content = models.CharField(max_length=255)
