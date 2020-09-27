from django.contrib import admin
from .models import User, CountyListEntry

# Register your models here.
admin.site.register(User)
admin.site.register(CountyListEntry)
