from django.shortcuts import render


# Create your views here.
def register(request):
    '''
    Renders register.html and allows user to register
    '''
    return render(request, 'register.html')


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
