# products/views.py
from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Q

class ProductSearch(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', None)  # Get the search query parameter
        if query:
            return Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))  # Search by name or description
        return Product.objects.none()  # Return an empty queryset if no query is provided

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListByCategory(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = get_object_or_404(Category, slug=category_slug)
        return Product.objects.filter(category=category)

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
