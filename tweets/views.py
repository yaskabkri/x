# tweets/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Tweet
from prod.models import Product

def home(request):
    prode = Product.objects.all()
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweets/home.html', {'prode':prode,'tweets': tweets})
    
    

def create_tweet(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        tweet = Tweet.objects.create(user=request.user, content=content)
        tweet.save()
        return redirect('home')
    return render(request, 'tweets/create_tweets.html')
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'prod/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_create.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_update.html', {'form': form, 'product': product})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_delete_confirm.html', {'product': product})
