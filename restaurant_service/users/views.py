
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .models import MenuItem
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request, 'users/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('menu')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


from django.contrib.auth.decorators import login_required

@login_required
def menu(request):
    return render(request, 'users/menu.html')

import logging

logger = logging.getLogger(__name__)

@login_required
def menu_view(request):
    query = request.GET.get('q')
    if query:
        menu_items = MenuItem.objects.filter(name__icontains=query)
    else:
        menu_items = MenuItem.objects.all()

    logger.debug(f"Menu items: {menu_items}")  # Logging debug statement

    return render(request, 'users/menu.html', {'menu_items': menu_items, 'query': query})




from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        # Logic to add the item to the cart goes here
        # For now, just redirect back to the menu page
        return HttpResponseRedirect(reverse('menu'))
    
# views.py
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, MenuItem

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        menu_item_id = request.POST.get('item_id')
        menu_item = MenuItem.objects.get(id=menu_item_id)
        user = request.user

        cart, created = Cart.objects.get_or_create(user=user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, menu_item=menu_item)

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect('cart')

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    item_count = cart_items.count()
    return render(request, 'users/cart.html', {'cart_items': cart_items, 'item_count': item_count})

