# products/urls.py
from django.urls import path
from .views import ProductList, ProductListByCategory, ProductDetail, ProductSearch

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),  # Product listing
    path('category/<slug:category_slug>/', ProductListByCategory.as_view(), name='product_list_by_category'),  # Filter by category
    path('<int:pk>/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),  # Product detail
    path('product_search/', ProductSearch.as_view(), name='product_search'),  # Product search
]
