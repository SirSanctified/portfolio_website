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
    list_display = ['id', 'name', 'email', 'subject', 'timestamp']
    list_filter = ['timestamp', 'subject', 'email']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['timestamp', 'name', 'email', 'subject', 'message']


@admin.register(models.Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'timestamp']
    list_filter = ['timestamp', 'author']
    search_fields = ['title', 'author', 'content']


@admin.register(models.Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'blog', 'timestamp']
    list_filter = ['timestamp', 'name']
    search_fields = ['name', 'blog', 'comment']
