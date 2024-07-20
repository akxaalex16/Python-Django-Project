from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# Create your views here.
# when there is a request to /products --> it needs to call this index function
# mapping URL to function
# Uniform Resource Locator (Address)
def index(request):
    # Product.objects.all() returns all the products we have in the database
    # Product.objects.filter() to filter the products, example we want to get products that cost more than 2 dollars or products that are out of stock
    # Product.objects.get() to get a single product
    # Product.objects.save() for inserting a new product or updating an existing product
    # return HttpResponse('Hello World')
    products = Product.objects.all()

    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New Products')
