from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('cart/update/', views.update_cart_quantity, name='update_cart_quantity'),

]
