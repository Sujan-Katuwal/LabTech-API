from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BannerViewSet

# Create the router and register the ViewSet
router = DefaultRouter()
router.register(r'banner', BannerViewSet, basename='banner')


urlpatterns = [
    path('', include(router.urls)),

    # path('api-auth/', include('rest_framework.urls')),
]
