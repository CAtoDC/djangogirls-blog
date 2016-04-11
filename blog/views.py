from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here
def post_list(request):
    # "posts" is now the queryset variable name
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
