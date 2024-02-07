from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import product_list,home, product_create, product_update, product_delete, category_create, category_list
from users.views import list_it
urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/create/', product_create, name='product_create'),
    path('categoty/create/', category_create, name='category_create'),
    path('category/list/', category_list, name='category_lis'),
    path('products/<int:pk>/update/', product_update, name='product_update'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),
    path('list_it/', list_it, name='list_it'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
