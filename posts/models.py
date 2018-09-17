from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, default='')
    site_url = models.TextField(default='')
    content = models.TextField(default="")
    created_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    votes_total = models.IntegerField(default=1)
    image = models.FileField(upload_to='images', blank=True)
    

    def created_at_formatted(self):
        return self.created_at.strftime('%b %e %Y')

class Comment(models.Model):
    title = models.CharField(max_length=200, default='')
    content = models.TextField(default="")
    created_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    posts = models.ForeignKey(Post, on_delete= models.CASCADE, null=True)
    votes_total = models.IntegerField(default=1)


    def created_at_formatted(self):
        return self.created_at.strftime('%b %e %Y')


