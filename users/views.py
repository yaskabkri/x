# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
#from .models import Profile


#def profile(request):
 #   user = request.user
  #  pro = Profile.objects.filter(user=user)
   # return render(request, 'tweets/profile.html', {'pro': pro})

# users/views.py


# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, UserLoginForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Redirect to home page after registration
    else:
        form = SignUpForm()
    return render(request, 'tweets/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after login
    else:
        form = UserLoginForm()
    return render(request, 'tweets/login.html', {'form': form})



from prod.models import Product

def list_it(request):
    prode = Product.objects.all()
    return render(request, 'tweets/list.html', {'prode':prode})

# views.py
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the homepage after logout


# views.py

from django.shortcuts import render
from .models import UserProfile
from prod.models import Product

def profile(request):
    # Retrieve the current user's profile
    user_profile = UserProfile.objects.get(user=request.user)

    # Retrieve the products associated with the current user
    user_products = Product.objects.filter(user=request.user)

    context = {
        'user_profile': user_profile,
        'user_products': user_products
    }

    return render(request, 'tweets/profile.html', context)
# views.py

from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm

def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page after update
    else:
        form = ProfileUpdateForm(instance=request.user.userprofile)
    return render(request, 'tweets/profile_update.html', {'form': form})
