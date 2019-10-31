from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def register(request):
    '''
    Renders register.html and allows user to register
    '''
    register_form = UserRegistrationForm()

    context = {
        'register_form': register_form,
    }

    return render(request, 'register.html', context)


def login(request):
    '''
    Renders login.html and allows user to register
    '''
    return render(request, 'login.html')


def logout(request):
    '''
    Logs user out and redirects to login page
    '''
    return render(request, 'login.html')
