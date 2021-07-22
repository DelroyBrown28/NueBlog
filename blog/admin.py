from django.contrib import admin
from . import models
from .models import Post, Comment
from mptt.admin import MPTTModelAdmin
from tinymce.widgets import TinyMCE


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'add_to_carousel', 'category', 'id', 'status', 'author')
    list_editable = ('status', 'category', 'add_to_carousel')
    prepopulated_fields = {
        "slug" : ("title",),
    }
    formfield_overrides = {

    models.Post.content: {'widget': TinyMCE()}}
 
@admin.register(models.Vote)    
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'vote')
    # list_editable = ()
    

    
admin.site.register(models.Category)
admin.site.register(models.Comment, MPTTModelAdmin)
