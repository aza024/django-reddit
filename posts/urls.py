from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings 
from django.conf.urls.static import static



app_name = 'posts'

urlpatterns = [
    path('create/', views.create, name='create'),
    url(r'^(?P<pk>[0-9]+)/upvote', views.upvote, name='upvote'),
    url(r'^(?P<pk>[0-9]+)/downvote', views.downvote, name='downvote'),
    url(r'^user/(?P<fk>[0-9]+)', views.userposts, name='userposts'),
    path('comment/', views.comment, name='comment'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)