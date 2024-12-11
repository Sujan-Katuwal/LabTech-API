from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import SocialMediaViewSet

# Create the router and register the ViewSet
router = DefaultRouter()
router.register(r'social_media', SocialMediaViewSet, basename='social_media')


urlpatterns = [
    path('', include(router.urls)),

    # path('api-auth/', include('rest_framework.urls')),
]
