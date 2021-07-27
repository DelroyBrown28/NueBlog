import uuid
from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from mptt.models import MPTTModel, TreeForeignKey
from djrichtextfield.models import RichTextField




def user_directory_path(instance, filename):
    return 'posts/{0}/{1}'.format(instance.title, filename)


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
        
    

class Post(models.Model):
    
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    
    OPTIONS = {
        ('draft', 'Draft'),
        ('published', 'Published'),
    }
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='published', help_text='URL deirecting to this post')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    excerpt = models.TextField(null=True)
    image = models.ImageField(upload_to='posts/%Y/%m/%d/', default='posts/default.jpg')
    # image_caption = models.CharField(max_length=100, default='Image caption.')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = RichTextField()
    status = models.CharField(max_length=10, choices=OPTIONS, default='published')
    favorites = models.ManyToManyField(User, related_name='favorite', default=None, blank=True)
    likes = models.ManyToManyField(User, related_name='like', default=None, blank=True)
    thumbsup = models.IntegerField(default='0')
    thumbsdown = models.IntegerField(default='0')
    thumbs = models.ManyToManyField(User, related_name='thumbs', default=None, blank=True)
    add_to_carousel = models.BooleanField(default=False)
    published = models.DateTimeField(default=timezone.now)
    objects = models.Manager() # DEFAULT MANAGER
    newmanager = NewManager() # CUSTOM MANAGER
    
    
 
    def __unicode__(self):
        return "{0}".format(self.title)
    
  
    def get_absolute_url(self):
        return reverse("blog:post_single", args=[self.slug])
    
    def get_cat_list(self):
        k = self.category # for now ignore this instance method
        
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]
    
    
    class Meta:
        ordering = ('-published', )
    
    def __str__(self):
        return self.title


class Comment(MPTTModel):
    author = models.ForeignKey(User, related_name='author',
                               on_delete=models.CASCADE, default=None, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True,
                            blank=True,
                            related_name='children')
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    class MPTTMeta:
        order_insertion_by = ['-publish']
        
    
    
    
class Vote(models.Model):
    post = models.ForeignKey(Post, related_name='postid',
                             on_delete=models.CASCADE, default=None, blank=True)
    user = models.ForeignKey(User, related_name='userid',
                             on_delete=models.CASCADE, default=None, blank=True)
    vote = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Vote from {self.user} on post {self.post}"
    
    