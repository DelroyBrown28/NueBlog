from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post
from .forms import NewCommentForm
from django.views.generic import ListView


def home(request):
    
    all_posts = Post.newmanager.all()
    
    return render(request, 'index.html', {'posts' : all_posts})

def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    comments = post.comments.filter(status=True)
    user_comment = None
    
    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('/' + post.slug)
    else:
        comment_form = NewCommentForm()
    return render(request, 'single.html', {
        'post' : post, 
        'comments' : user_comment, 
        'comments' : comments, 
        'comment_form' : comment_form
        })
            

class CategoryListView(ListView):
    template_name = 'category.html'
    context_object_name = 'categorylist'
    
    def get_queryset(self):
        content = {
            'cat' : self.kwargs['category'],
            'posts' : Post.objects.filter(category__name=self.kwargs['category']).filter
            (status='published')
        }
        return content
    
    
                
