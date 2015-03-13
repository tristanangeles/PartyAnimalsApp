from django.contrib import admin

from .models import Trait,Name,Job
# Register your models here.
admin.site.register(Trait)
admin.site.register(Name)
admin.site.register(Job)