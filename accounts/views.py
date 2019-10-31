from django.shortcuts import render


# Create your views here.
def register(request):
    '''
    Renders register.html and allows user to register
    '''
    return(render, 'register.html')


def login(request):
    '''
    Renders login.html and allows user to register
    '''
    return(render, 'login.html')


def logout(request):
    '''
    Logs user out and redirects to login page
    '''
    return(render, 'login.html')
