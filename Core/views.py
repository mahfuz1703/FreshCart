from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from taggit.models import Tag
from django.db.models import Count, Avg
from .forms import ProductReviewForm
from django.contrib import messages

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

def product_details(request, product_id):
    product = Product.objects.get(product_id=product_id)
    products = Product.objects.filter(category=product.category).exclude(product_id=product_id)
    product_images = product.p_images.all()
    avarage_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, "Your review successfully added. Thank you!!")
            return redirect('product_details', product_id=product_id)
    else:
        form = ProductReviewForm()

    reviews = ProductReview.objects.filter(product=product).order_by("-date")

    context = {
        'product': product,
        'products': products,
        'p_images': product_images,
        'reviews': reviews,
        'avarage_rating': avarage_rating,
        'form': form,
    }
    return render(request, "home/product_details.html", context)

def product_tag_wise(request, tag_slug=None):
    products = Product.objects.filter(product_status="published")
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])

    context= {
        'products': products,
        'tag': tag_slug,
    }
    return render(request, "home/product_tag_wise.html", context)
