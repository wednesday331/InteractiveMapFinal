import markdown2
import secrets
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from . import util
from markdown2 import Markdown
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms
from .models import User, CountyListEntry
from django.db import models


def index(request):
    return render(request, "county/index.html")

def countyinformation(request, countyname):
    markdowner = Markdown()
    countieslist = util.list_entries()
    if countyname in countieslist:
        countypagedata = util.get_entry(countyname)
        county= markdowner.convert(countypagedata)
        user=request.user
        if request.user.is_anonymous is False:
            userlist=CountyListEntry.objects.filter(user=user)
            posts=[]
            for post in userlist:
                posts.append(post.countyname)
            if countyname in posts:
                SavedAlready=True
                return render(request, "county/countyinformation.html", {"county": county, "countyname": countyname, "SavedAlready":SavedAlready})
        SavedAlready=False
        return render(request, "county/countyinformation.html", {"county": county, "countyname": countyname, "SavedAlready":SavedAlready})
    return render(request, "county/index.html", {"message":"No Such County"})


def yourlist(request):
    countieslist=util.list_entries()
    user=request.user
    if request.user.is_anonymous is False:
        userlist=CountyListEntry.objects.filter(user=user)
        posts=[]
        for post in userlist:
            posts.append(post.countyname)
        pagination = Paginator(posts, 5)
        pageno = request.GET.get('page')
        posts = pagination.get_page(pageno)
        return render (request, "county/yourlist.html", {"userlist": userlist, "posts":posts})
    return render(request, "county/login.html", {
        "message": "Please log in to view your list."
    })
def savecounty(request,countyname):
    markdowner = Markdown()
    if request.user.is_anonymous:
        return render(request, "county/login.html",{"message": "Please log in before saving any counties."})
    else:
        user=request.user
        content=util.get_entry(countyname)
        CountyListentry=CountyListEntry.objects.create(user=user, countyname=countyname, content=content)
        CountyListentry.save()
        SavedAlready=bool('Saved')
        return render(request, "county/countyinformation.html", {"county": markdowner.convert(content), 'countyname': countyname, "message":"County Saved!",  "SavedAlready":SavedAlready})
    return render(request, "county/countyinformation.html", {"county": markdowner.convert(content), 'countyname': countyname, "SavedAlready":SavedAlready})

def unsavecounty(request,countyname):
    user=request.user
    markdowner = Markdown()
    countypagedata = util.get_entry(countyname)
    countynameentry = CountyListEntry.objects.filter(user=user, countyname=countyname)
    countynameentry.delete()
    SavedAlready=bool(False)
    return render(request, "county/countyinformation.html", {"county": markdowner.convert(countypagedata), 'countyname': countyname, "message":"County Unsaved!", "SavedAlready":SavedAlready})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usern = User.objects.filter(username=username, password=password)
        userlen=len(usern)
        if userlen == 1:
            userx=User.objects.filter(username=username, password=password)[0]
            login(request, userx)
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

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
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
