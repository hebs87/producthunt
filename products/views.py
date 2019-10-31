from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProductForm


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
    product_form = ProductForm()

    context = {
        "product_form": product_form
    }

    return render(request, 'create.html', context)
