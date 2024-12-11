from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BranchViewSet

# Create the router and register the ViewSet
router = DefaultRouter()
router.register(r'branch', BranchViewSet, basename='branch')

urlpatterns = [
    path('', include(router.urls)),
#    path('api-auth/', include("rest_framework.urls")),
]
