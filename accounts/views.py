from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def register(request):
    '''
    Renders register.html and allows user to register
    '''
    if request.method == "POST":
        register_form = UserRegistrationForm(request.POST)

        if request.POST["password1"] == request.POST["password2"]:
            try:
                # Check to see if username already exists
                user = User.objects.get(username=request.POST["username"])
                return render(request, 'register.html',
                    {'register_form': register_form})
            except User.DoesNotExist:
                # If username doesn't exist, create user
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password2"]
                )
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'register.html',
                    {'register_form': register_form})
    else:
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
