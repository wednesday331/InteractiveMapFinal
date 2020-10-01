#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contains the main Python Django code for
the Interactive Map of Massachusetts Guide
project.
"""


import markdown2
import secrets

from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db import IntegrityError, models
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from markdown2 import Markdown
from . import util
from .models import CountyListEntry, User

#Index/Main Page
def index(request):
    """Simply displays the map of Massachusetts."""
    return render(request, "county/index.html")

#County Information
def county_information(request, countyname):
    """
    Contains code for when more information
    about the county is requested.
    """
    markdowner = Markdown()
    counties_list = util.list_entries()
    if countyname in counties_list:
        county_page_data = util.get_entry(countyname)
        county= markdowner.convert(county_page_data)
        user=request.user
        if request.user.is_anonymous is False:
            user_list=CountyListEntry.objects.filter(user=user)
            posts=[]
            for post in user_list:
                posts.append(post.countyname)
            if countyname in posts:
                saved_already=True
                return render(request, "county/countyinformation.html", {"county": county,
                                                                         "countyname": countyname,
                                                                         "saved_already":saved_already
                                                                        }
                             )
        saved_already=False
        return render(request, "county/countyinformation.html",
                      {"county": county,
                       "countyname": countyname,
                       "saved_already":saved_already
                      }
                     )
    return render(request, "county/index.html", {"message":"No Such County"})

#Your/My List Code
def your_list(request):
    """
    Contains code for the personalized
    My List functionality.
    ('Your List' and 'My List' are interchangeable).
    """
    counties_list=util.list_entries()
    user=request.user
    if request.user.is_anonymous is False:
        user_list=CountyListEntry.objects.filter(user=user)
        posts=[]
        for post in user_list:
            posts.append(post.countyname)
        pagination = Paginator(posts, 5)
        page_no = request.GET.get('page')
        posts = pagination.get_page(page_no)
        return render (request, "county/yourlist.html", {"user_list": user_list, "posts":posts})
    return render(request, "county/login.html", {
        "message": "Please log in to view your list."
    })

#Save
def save_county(request,countyname):
    """
    Contains code to save a county to a personal
    list (My List).
    """
    markdowner = Markdown()
    if request.user.is_anonymous:
        return render(request, "county/login.html",
                      {"message": "Please log in before saving any counties."
                      }
                     )
    else:
        user=request.user
        content=util.get_entry(countyname)
        county_list_entry=CountyListEntry.objects.create(user=user,
                                                         countyname=countyname,
                                                         content=content
                                                        )
        county_list_entry.save()
        saved_already=bool('Saved')
        return render(request, "county/countyinformation.html", {"county": markdowner.convert(content),
                                                                 'countyname': countyname,
                                                                 "message":"County Saved!",
                                                                 "saved_already":saved_already
                                                                }
                     )
    return render(request, "county/countyinformation.html", {"county": markdowner.convert(content),
                                                             'countyname': countyname,
                                                             "saved_already":saved_already
                                                            }
                 )

#Unsave
def unsave_county(request,countyname):
    """
    Contains code to save a county to a personal
    list (My List).
    """
    user=request.user
    markdowner = Markdown()
    county_page_data = util.get_entry(countyname)
    countyname_entry = CountyListEntry.objects.filter(user=user,
                                                       countyname=countyname
                                                      )
    countyname_entry.delete()
    saved_already=bool(False)
    return render(request, "county/countyinformation.html", {"county": markdowner.convert(county_page_data),
                                                             'countyname': countyname,
                                                             "message":"County Unsaved!",
                                                             "saved_already":saved_already})
#Login
def login_view(request):
    """Contains code to login a user."""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        username_1 = User.objects.filter(username=username, password=password)
        username_length=len(username_1)
        if username_length == 1:
            user_obtained=User.objects.filter(username=username, password=password)[0]
            login(request, user_obtained)
            return render(request, "county/index.html")
        else:
            return render(request, "county/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        if request.user.is_anonymous:
            return render(request, "county/login.html")
        else:
            return render(request, "county/index.html")

#Logout
def logout_view(request):
    """Contains code to logout a user."""
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# Register
def register(request):
    """Contains code to register a user."""
    if request.method == "POST":
        username = request.POST["username"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if not username:
            return render(request, "county/register.html", {
                "message": "Please type in a username."})
        if not password:
            return render(request, "county/register.html", {
                "message": "Please type in a password."})
        if password != confirmation:
            return render(request, "county/register.html", {
                "message": "The passwords need to match."})

        # Attempt to create new user
        try:
            user = User.objects.create(username=username, password=password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "county/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    return render(request,"county/register.html")
