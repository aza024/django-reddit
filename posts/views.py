from django.shortcuts import render
#require user to be logged in
from django.contrib.auth.decorators import login_required

#only access if user is logged in
@login_required
def create(request):
    return render(request,'posts/create.html')