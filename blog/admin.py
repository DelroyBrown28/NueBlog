from django.contrib import admin
from . import models
from .models import Post, Comment


@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author', 'slug')
    prepopulated_fields = {
        "slug" : ("title",),
    }
    
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'publish', 'status')
    list_filter = ('publish', 'status')
    search_fields = ('name', 'email', 'content')
