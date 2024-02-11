# tweets/urls.py
from django.urls import path
from . import views

urlpatterns = [
    
    path('tweet/', views.create_tweet, name='create_tweet'),
    path('products/', views.product_list, name='product_list'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:cart_item_id>/', views.update_cart, name='update_cart'),
    path('make-payment/', views.make_payment, name='make_payment'),
]
    




