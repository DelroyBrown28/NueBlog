from django.contrib import admin
from . import models
from .models import Post, Comment
from mptt.admin import MPTTModelAdmin


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'large_feature', 'small_feature_1', 'small_feature_2', 'get_likes', 'category', 'id', 'status', 'author')
    list_editable = ('status', 'category', 'large_feature', 'small_feature_1', 'small_feature_2')
    prepopulated_fields = {
        "slug" : ("title",),
    }
    

    
admin.site.register(models.Category)
admin.site.register(models.Comment, MPTTModelAdmin)
