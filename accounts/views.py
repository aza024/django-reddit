from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def signup(request):
    if request.method == 'POST':
        #check for password matching
        if request.POST['password1'] == request.POST['password2']:
            #try to get a user with name and check to see 
                try:
                    user = User.objects.get(username=request.POST['username'])
                    return render(request,'accounts/signup.html',{'Error': 'Username has already been taken. Please select a different username'})
                    #create user sending data given in request
                except User.DoesNotExist:
                    user = User.objects.create_user(request.POST['username'], email=request.POST['email'], password=request.POST['password1'])
                    #upon account creation, login user and prevent user from viewing admin page
                    login(request,user)
                    return render(request,'accounts/signup.html', {'Success':'Account successfully created'})
        else:
            return render(request,'accounts/signup.html', {'Error':'Passwords didn\'t match'})
    else:
        return render(request,'accounts/signup.html')


def loginview(request):
    if request.method == 'POST':
        #check for password matching
        user = authenticate(username=request.POST['username'], password=request.POST['password1'])
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return render(request,'accounts/login.html', {'Error':'Login Successful'})
        else:
            return render(request,'accounts/login.html', {'Error':'Username/Passwords didn\'t match. Please try again.'})
    else:
        return render(request,'accounts/login.html')

def logoutview(request):
    if request.method == 'POST':
        logout(request)