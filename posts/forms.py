from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ('title','content') 


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title','content','picture','vote_total','')