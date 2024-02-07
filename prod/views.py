from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
def home(request):
    products = Product.objects.all()
    return render(request, 'tweets/home.html', {'products': products})
def product_list(request):
    products = Product.objects.all()
    return render(request, 'prod/product_list.html', {'products': products})
#@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'prod/product_form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'prod/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'prod/product_confirm_delete.html', {'product': product})



from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, product_id):
    # Fetch the product details
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'tweets/product_detail.html', {'product': product})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'prod/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'prod/category_form.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'prod/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})


# views.py

from django.shortcuts import render, redirect
from .models import Cart, CartItem
from .forms import CartItemForm

def view_cart(request):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    cart_items = cart.items.all()
    return render(request, 'tweets/view_cart.html', {'cart_items': cart_items, 'cart': cart})

def add_to_cart(request, product_id):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    product = Product.objects.get(pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')
