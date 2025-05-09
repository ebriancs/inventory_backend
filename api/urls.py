from django.urls import path
from .views import (
    ProductListCreateAPIView,
    ProductDetailAPIView,
    login,
)

urlpatterns = [
    path('login/', login),
    path('products/', ProductListCreateAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),
]
