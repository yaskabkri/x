# tweets/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tweet/', views.create_tweet, name='create_tweet'),
    path('products/', views.product_list, name='product_list'),
]
    

