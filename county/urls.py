#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""List of Django paths for the map guide code."""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("yourlist", views.your_list, name="your_list"),
    path("countyinformation/<str:countyname>", views.county_information, name="county_information"),
    path("unsavecounty/<str:countyname>", views.unsave_county, name="unsave_county"),
    path("savecounty/<str:countyname>", views.save_county, name="save_county"),
]
