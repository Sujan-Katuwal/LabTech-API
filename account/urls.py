from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet

# Create the router and register the ViewSet
router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include("rest_framework.urls")),
]
