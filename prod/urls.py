from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
#product_list,home, product_create,product_detail, product_update, product_delete, category_create, category_list
from users.views import list_it
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('categoty/create/', views.category_create, name='category_create'),
    path('category/list/', views.category_list, name='category_lis'),
    path('products/<int:pk>/update/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('list_it/', list_it, name='list_it'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('view/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
