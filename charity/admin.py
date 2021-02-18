# Django
from django.contrib import admin

# local Django
from . models import Category, Member, HouseMember, Requirement

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    list_display_links = ('category',)


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'house_name', 'locality',)
    list_display_links = ('name',)


class HouseMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'member', 'relationship',)
    list_display_links = ('name',)


class RequirementAdmin(admin.ModelAdmin):
    list_display = ('member',)
    list_display_links = ('member',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(HouseMember, HouseMemberAdmin)
admin.site.register(Requirement, RequirementAdmin)


