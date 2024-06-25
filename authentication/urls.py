from django.urls import path
from . import views

urlpatterns = [
    path('signin', views.singin, name='signin'),
    path('signup', views.singup, name='signup'),
    path('signout', views.signout, name='signout'),
]