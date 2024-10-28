from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from products.models import Product
from .models import CartItem
from .serializers import CartItemSerializer

# View to show cart details
@api_view(['GET'])
def cart_detail(request):
    cart_items = CartItem.objects.all()
    serializer = CartItemSerializer(cart_items, many=True)
    return Response(serializer.data)

# View to add a product to the cart
@api_view(['POST'])
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(product=product)

    if not created:
        cart_item.quantity += 1  # Increase quantity if it already exists
    cart_item.save()  # Save the cart item

    serializer = CartItemSerializer(cart_item)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# View to remove a product from the cart
@api_view(['DELETE'])
def cart_remove(request, product_id):
    cart_item = get_object_or_404(CartItem, product_id=product_id)
    cart_item.delete()  # Remove the cart item from the database

    return Response({'message': f'Product {cart_item.product.name} removed from cart.'}, status=status.HTTP_204_NO_CONTENT)
