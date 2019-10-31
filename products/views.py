from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    '''
    Returns home page
    '''
    return render(request, 'index.html')


@login_required
def create(request):
    '''
    Allows user to add a product
    '''
    return render(request, 'create.html')
