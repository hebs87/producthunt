from django.shortcuts import render, redirect
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
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES)

        if product_form.is_valid():
            product_form.instance.hunter = request.user
            if request.POST["url"].startswith("http://") or request.POST["url"].startswith("https://"):
                # Save URL if it starts with the above
                product_form.instance.url = request.POST["url"]
            else:
                # Add http:// if URL doesn't start with it
                product_form.instance.url = "http://" + request.POST["url"]
            product_form.save()
            return redirect('home', {'product_form': product_form})
    else:
        product_form = ProductForm()

    context = {
        "product_form": product_form
    }

    return render(request, 'create.html', context)


@login_required
def detail(request, product_id):
    '''
    Loads full details of the product
    '''
    return render(request, 'detail.html')