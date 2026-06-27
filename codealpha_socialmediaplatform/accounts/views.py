from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from .models import Profile
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def follow_unfollow_view(request, username):
    target_user = get_object_or_404(User, username=username)
    
    # Safely get or create profiles to prevent the crash
    target_profile, _ = Profile.objects.get_or_create(user=target_user)
    current_profile, _ = Profile.objects.get_or_create(user=request.user)

    if target_profile != current_profile:
        if current_profile.following.filter(id=target_profile.id).exists():
            current_profile.following.remove(target_profile)
        else:
            current_profile.following.add(target_profile)
            
    return redirect('profile', username=username)

@login_required
def edit_profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})


