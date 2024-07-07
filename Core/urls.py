from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all_products/', views.all_products, name='all_products'),
    path('category/', views.all_categories, name='all_categories'),
    path('category/<category_id>/', views.product_category_wise, name='product_category_wise'),
]