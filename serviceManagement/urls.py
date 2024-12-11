from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ServiceViewSet

# Create the router and register the ViewSet
router = DefaultRouter()
router.register(r'service', ServiceViewSet, basename='service')

urlpatterns = [
    path('', include(router.urls)),
#    path('api-auth/', include("rest_framework.urls")),
]
