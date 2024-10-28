from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),  # Cart detail
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),  # Add product to cart
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),  # Remove product from cart
]
