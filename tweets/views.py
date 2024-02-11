# tweets/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Tweet
from prod.models import Product


    

def create_tweet(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        tweet = Tweet.objects.create(user=request.user, content=content)
        tweet.save()
        return redirect('home')
    return render(request, 'tweets/create_tweets.html')
from django.shortcuts import render, get_object_or_404, redirect
from prod.models import Product
from prod.forms import ProductForm

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


# views.py

from django.shortcuts import render, redirect, get_object_or_404
from prod.models import Cart, CartItem, Product
from django.contrib.auth.decorators import login_required

@login_required
def view_cart(request):
    # Retrieve the user's cart
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Get cart items
    cart_items = cart.items.all()

    total_price = sum(item.product.cost_price * item.quantity for item in cart_items)

    return render(request, 'tweets/view_cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Retrieve the user's cart
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    # Increment the quantity if the item is already in the cart
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')

@login_required
def update_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    quantity = int(request.POST.get('quantity'))

    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('view_cart')

# views.py
from django.shortcuts import render
from django.http import HttpResponse

def make_payment(request):
    if request.method == 'POST':
        # Process payment using M-Pesa API
        phone_number = request.POST.get('phone_number')
        amount = request.POST.get('amount')
        
        # Call M-Pesa API to initiate payment
        # Example: mpesa_processor.process_payment(phone_number, amount)
        
        # For demonstration purposes, return a success message
        return HttpResponse("Payment successful!")
    
    return render(request, 'tweets/payment_form.html')
