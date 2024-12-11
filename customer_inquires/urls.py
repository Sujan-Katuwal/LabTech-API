from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CustomerInquireViewSet

# Create the router and register the ViewSet
router = DefaultRouter()
router.register(r'customer_inquire', CustomerInquireViewSet, basename='customer_inquire')


urlpatterns = [
    path('', include(router.urls)),

    # path('api-auth/', include('rest_framework.urls')),
]
