from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    products = Product.objects.filter(product_status="published").order_by('-id')
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, "home/index.html", context)

def all_products(request):
    products = Product.objects.filter(product_status="published").order_by('-id')
    categories = Category.objects.all()
    vendors = Vendor.objects.all()
    context = {
        'products': products,
        'product_count': len(products),

        'categories': categories,
        'vendors': vendors,
    }
    return render(request, "home/all_products.html", context)

def all_categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, "partials/base.html", context)

