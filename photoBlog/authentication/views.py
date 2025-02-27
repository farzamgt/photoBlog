from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from posts.models import Category
from django.core.exceptions import ValidationError


def homepage(request):
    categories = Category.objects.all()  
    return render(request, 'homepage.html', {
        'user': request.user,
        'categories': categories, 
    })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next', 'homepage')
            if not next_url or next_url == request.path:
                next_url = 'homepage'
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('homepage')  

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('homepage')
        else:
            errors = []
            if 'username' in form.errors:
                errors.append('Username is already taken. Please choose a different one.')
            if 'password2' in form.errors:
                errors.append('Password must be at least 8 characters long and include numbers and special characters.')
            return render(request, 'authentication/registration.html', {
                'form': form,
                'errors': errors
            })
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/registration.html', {'form': form})