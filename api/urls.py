from django.urls import path
from .views import (
    ProductListCreateAPIView,
    ProductDetailAPIView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,    # View to get the access and refresh tokens
    TokenRefreshView,       # View to refresh the access token
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token

    path('products/', ProductListCreateAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),
]
