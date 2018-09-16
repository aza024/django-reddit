from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url'] and request.POST['content']:
            post = Post()
            post.title = request.POST['title']
            post.url = request.POST['url']
            post.created_at = timezone.datetime.now()
            post.user = request.user
            post.save()
            return redirect('home')
        else:
            return render(request,'posts/create.html',{'error':'Please fill out required fields marked with * to create a post.'})
    else:
        return render(request, 'posts/create.html')

def home(request):
    post = Post.objects.order_by('votes_total')
    return render(request, 'posts/home.html', {'posts':post})