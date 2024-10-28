from django.urls import path
from .views import OrderCreate, OrderSummary, OrderDetail, my_orders, delivery

urlpatterns = [
    path('create/', OrderCreate.as_view(), name='order_create'),  # Order Creation
    path('order_summary/', OrderSummary.as_view(), name='order_summary'),  # List of Orders
    path('order_detail/<int:pk>/', OrderDetail.as_view(), name='order_detail'),  # Order Tracking
    path('my_orders/', my_orders, name='my_orders'),  # User's orders
    path('delivery/', delivery, name='delivery'),      # Delivery information
]
