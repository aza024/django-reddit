from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'posts'

urlpatterns = [
    path('create/', views.create, name='create'),
    url(r'^(?P<pk>[0-9]+)/upvote', views.upvote, name='upvote'),
    url(r'^(?P<pk>[0-9]+)/downvote', views.downvote, name='downvote'),
]
