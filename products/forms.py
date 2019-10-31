from django import forms
from datetime import datetime
from .models import Product


class ProductForm(forms.ModelForm):
    '''
    Form that allows users to create new product
    '''
    title = forms.CharField(
        label="Product Title",
        min_length=5,
        max_length=100,
        widget=forms.TextInput(),
        required=True)
    url = forms.CharField(
        label="Product Link",
        min_length=10,
        max_length=2000,
        widget=forms.TextInput(),
        required=True)
    image = forms.ImageField(
        label="Image",
        widget=forms.FileInput())
    icon = forms.ImageField(
        label="Icon",
        widget=forms.FileInput())
    body = forms.CharField(
        label="Product Details",
        min_length=10,
        max_length=2000,
        widget=forms.Textarea(),
        required=True)

    class Meta:
        model = Product
        fields = ["title", "url", "image", "icon", "body"]
