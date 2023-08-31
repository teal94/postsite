from django.urls import path
from .views import CustomTokenObtainView, CustomTokenRefreshView

urlpatterns = [
    path('token/', CustomTokenObtainView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]