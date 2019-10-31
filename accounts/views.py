from django.shortcuts import render


# Create your views here.
def register(request):
    '''
    Renders register.htm and allows user to register
    '''
    return(render, 'register.html')
