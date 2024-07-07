from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    
    # products
    path('all_products/', views.all_products, name='all_products'),

    # Category
    path('category/', views.all_categories, name='all_categories'),
    path('category/<category_id>/', views.product_category_wise, name='product_category_wise'),

    # Vendor
    path('vendors/', views.all_vendors, name='all_vendors'),
    path('vendors/<vendor_id>/', views.vendor_details, name='vendor_details'),
]