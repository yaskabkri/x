# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('list_it/', views.list_it, name='list_it'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/update/', views.profile_update, name='profile_update'),
]

