# Django
from django.contrib import admin

# local Django
from . models import Category, Member, HouseMember

# Register your models here.

admin.site.register(Category)
admin.site.register(Member)
admin.site.register(HouseMember)
