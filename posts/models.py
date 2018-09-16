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
    image = models.ImageField(default='')
    

    # def pub_date_pretty(self):
    #     return self.created_at.strftime('%b %e %Y')
