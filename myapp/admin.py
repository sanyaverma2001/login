from django.contrib import admin
from django.db import models
from . models import user_register

# Register your models here.

class useradmin(admin.ModelAdmin):
    list_display=('username','email','password')
admin.site.register(user_register,useradmin)


