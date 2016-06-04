from django.contrib import admin

from .models import *
# Register your models here.

class GRUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(GRUser, GRUserAdmin)