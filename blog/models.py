from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey



def user_directory_path(instance, filename):
    return 'posts/{0}/{1}'.format(instance.title, filename)


class Category(models.Model):
    name = models.CharField(max_length=100)
    
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
    FEATURED = {
        ('featured_large', 'Large Feature'),
        ('featured_small_1', 'Small Feature 1'),
        ('not-featured', '--'),
    }
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    excerpt = models.TextField(null=True)
    image = models.ImageField(upload_to=user_directory_path, default='posts/default.jpg')
    image_caption = models.CharField(max_length=100, default='Image caption.')
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=OPTIONS, default='draft')
    favorites = models.ManyToManyField(User, related_name='favorite', default=None, blank=True)
    likes = models.ManyToManyField(User, related_name='like', default=None, blank=True)
    like_count = models.BigIntegerField(default='0')
    # large_feature = models.CharField(max_length=20, choices=FEATURED, default='not-featured')
    large_feature = models.BooleanField(default=False)
    small_feature_1 = models.BooleanField(default=False)
    small_feature_2 = models.BooleanField(default=False)
    publish = models.DateTimeField(default=timezone.now)
    objects = models.Manager() # DEFAULT MANAGER
    newmanager = NewManager() # CUSTOM MANAGER
    
    def get_likes(self):
        return ", ".join([str(p) for p in self.likes.all()])

    def __unicode__(self):
        return "{0}".format(self.title)
    
    def get_absolute_url(self):
        return reverse("blog:post_single", args=[self.slug])
    
    
    class Meta:
        ordering = ('-publish', )
    
    def __str__(self):
        return self.title


class Comment(MPTTModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True,
                            blank=True,
                            related_name='children')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    class MPTTMeta:
        order_insertion_by = ['-publish']
        
    def __str__(self):
        return f"Comment by {self.name} on {self.post}"