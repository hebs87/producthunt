from django.shortcuts import render


# Create your views here.
def home(request):
    '''
    Returns home page
    '''
    return render(request, 'index.html')
