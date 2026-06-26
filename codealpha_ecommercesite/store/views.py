import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import JsonResponse
from .models import Product, Order, OrderItem
from django.template.loader import render_to_string

def product_list(request):
    query = request.GET.get('q', '').strip()
    
    if query:
        # Filter products whose name contains the search query (case-insensitive)
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    # If the request comes from JavaScript (AJAX Fetch)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Render only the product cards into an HTML string
        html = render_to_string('store/product_modules.html', {'products': products}, request=request)
        return JsonResponse({'html': html})

    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('product_list')

def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prod_id = str(data.get('product_id'))
        cart = request.session.get('cart', {})
        cart[prod_id] = cart.get(prod_id, 0) + 1
        request.session['cart'] = cart
        return JsonResponse({'total_items': sum(cart.values())})

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    grand_total = 0
    for prod_id, qty in cart.items():
        try:
            product = Product.objects.get(id=prod_id)
            total = product.price * qty
            grand_total += total
            cart_items.append({'product': product, 'quantity': qty, 'total': total})
        except Product.DoesNotExist:
            pass
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'grand_total': grand_total})

def checkout_view(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('product_list')
    if request.method == 'POST':
        address = request.POST.get('address')
        order = Order.objects.create(user=request.user if request.user.is_authenticated else None, shipping_address=address)
        grand_total = 0
        for prod_id, qty in cart.items():
            product = Product.objects.get(id=prod_id)
            grand_total += product.price * qty
            OrderItem.objects.create(order=order, product=product, quantity=qty, price=product.price)
        order.total_price = grand_total
        order.save()
        request.session['cart'] = {}
        return render(request, 'store/checkout.html', {'success': True})
    return render(request, 'store/checkout.html', {'success': False})

# Add this new view function to the bottom of store/views.py
def update_cart_quantity(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prod_id = str(data.get('product_id'))
        action = data.get('action') # 'increase' or 'decrease'
        
        cart = request.session.get('cart', {})
        
        if prod_id in cart:
            if action == 'increase':
                # Check stock limits
                product = get_object_or_404(Product, id=prod_id)
                if cart[prod_id] < product.stock:
                    cart[prod_id] += 1
            elif action == 'decrease':
                cart[prod_id] -= 1
                if cart[prod_id] <= 0:
                    del cart[prod_id] # Remove item if quantity hits zero
                    
            request.session['cart'] = cart
            
        # Re-calculate totals to send back to JavaScript
        item_qty = cart.get(prod_id, 0)
        product = Product.objects.filter(id=prod_id).first()
        item_total = float(product.price) * item_qty if product else 0
        
        grand_total = 0
        for p_id, qty in cart.items():
            p = Product.objects.filter(id=p_id).first()
            if p: grand_total += float(p.price) * qty
            
        return JsonResponse({
            'item_removed': prod_id not in cart,
            'item_qty': item_qty,
            'item_total': item_total,
            'grand_total': grand_total,
            'cart_empty': len(cart) == 0
        })
