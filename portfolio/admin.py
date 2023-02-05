from django.contrib import admin
from . import models


@admin.register(models.UserProfile)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


@admin.register(models.Technology)
class TechnologyModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'technology_name']


@admin.register(models.Project)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'project_name', 'project_url']


@admin.register(models.Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'timestamp']
    list_filter = ['timestamp', 'email']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['timestamp', 'name', 'email', 'message']


@admin.register(models.Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',]
    


@admin.register(models.SoftSkill)
class SoftSkillModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']