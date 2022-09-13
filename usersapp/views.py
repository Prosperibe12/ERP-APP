from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . decorators import *
from django.contrib.auth.decorators import login_required

# Create your views here.
"""
All views for this users section of this app will be defined here
"""
# login function
def sign_in(request):
    
    # process authentication
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # authenticate user and login
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            # filter user's group and redirect appropriately
            if user.groups.filter(name='Vendors').exists():
                messages.success(request, 'Logged in Successfully')
                return redirect('home')
            
            elif user.groups.filter(name='Manager').exists():
                messages.success(request, 'Logged in Successfully')
                return redirect('dashboard')
            
            elif user.groups.filter(name='Staff').exists():
                messages.success(request, 'Logged in Successfully')
                return redirect('dashboard')
            
            elif user.groups.filter(name='General').exists():
                messages.success(request, 'Logged in Successfully')
                return redirect('dashboard')
                
            else:
                messages.warning(request, 'Access Denied')
                return redirect('login')
            
        else:
            messages.warning(request, 'Invalid Username or Password')
            
    context = {
        'Title': 'Login Page'
    }
    return render(request, 'usersapp/login.html', context)

# dashboard view function
@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager', 'Staff', 'General'])
def dashboard_view(request):
    
    context = {
        'Title': 'DashBoard'
    }
    return render(request, 'usersapp/dashboard.html', context)

# logout function
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('login')

# user profile function
# remember to set this up when user profile is created
# the template,view function and url