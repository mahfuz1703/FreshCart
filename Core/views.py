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
        'categories': categories,
        'vendors': vendors,
    }
    return render(request, "home/all_products.html", context)

def all_categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, "home/all_category.html", context)

def product_category_wise(request, category_id):
    category = Category.objects.get(category_id=category_id)
    products = Product.objects.filter(product_status="published", category=category)

    context = {
        'category': category,
        'products': products,
    }
    return render(request, "home/product_category_wise.html", context)

def all_vendors(request):
    vendors = Vendor.objects.all()
    context = {
        'vendors': vendors,
    }
    return render(request, "home/all_vendors.html", context)

def vendor_details(request, vendor_id):
    vendor = Vendor.objects.get(vendor_id=vendor_id)
    products = Product.objects.filter(product_status="published", vendor=vendor)

    context = {
        'vendor': vendor,
        'products': products,
    }
    return render(request, "home/vendor_details.html", context)
