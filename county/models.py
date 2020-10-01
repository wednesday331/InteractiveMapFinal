#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""List of classes necessary for views.py"""

# Register your models here.
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models

# User Class
class User(AbstractUser):
    pass

# List of Counties for each user
class CountyListEntry(models.Model):
    """The following stores data on the list of counties for each user.

    This class is important for the "My List" functionality of the app.
    """
    user=models.ForeignKey('User',
                           on_delete=models.CASCADE,
                           related_name='usernames')
    countyname=models.CharField(max_length=255)
    content = models.CharField(max_length=255)
