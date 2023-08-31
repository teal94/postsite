from rest_framework import routers
from django.urls import path, include

from .views import PostViewSet

router = routers.DefaultRouter()
router.register(r'', PostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]
