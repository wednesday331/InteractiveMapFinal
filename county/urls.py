from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("yourlist", views.yourlist, name="yourlist"),
    path("countyinformation/<str:countyname>", views.countyinformation, name="countyinformation"),
    path("unsavecounty/<str:countyname>", views.unsavecounty, name="unsavecounty"),
    path("savecounty/<str:countyname>", views.savecounty, name="savecounty"),
]
