from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User


@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url'] and request.POST['content']:
            post = Post()
            post.title = request.POST['title']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                post.url = request.POST['url']
            else:
                post.url = 'http://' + request.POST['url']
            post.created_at = timezone.datetime.now()
            post.user = request.user
            post.save()
            return redirect('home')
        else:
            return render(request,'posts/create.html',{'error':'Please fill out required fields marked with * to create a post.'})
    else:
        return render(request, 'posts/create.html')

def home(request):
    post = Post.objects.order_by('-votes_total')
    return render(request, 'posts/home.html', {'posts':post})

def upvote(request, pk):
    #only for get requests
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes_total += 1
        post.save()
        return redirect('home')

def downvote(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes_total -= 1 
        post.save()
        return redirect('home')

def userposts(request, fk):
    posts = Post.objects.filter(user__id=fk).order_by('-votes_total')
    print(fk)
    user = User.objects.get(pk=fk)
    return render(request,'posts/userposts.html', {'posts':posts,'user':user})
  