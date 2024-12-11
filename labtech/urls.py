"""
URL configuration for labtech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from account.views import UserViewSet
from category.views import CategoryViewSet
# from category.views import SubCategoryViewSet
from serviceManagement.views import ServiceViewSet
from branch.views import BranchViewSet
from booking_management.views import BookingViewSet
from customer_inquires.views import CustomerInquireViewSet
from branch_detail.views import BranchDetailViewSet
from gallery.views import GalleryViewSet
from social_media.views  import SocialMediaViewSet
from banner.views import BannerViewSet
from FAQ.views import FAQViewSet


from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="test@example.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'category', CategoryViewSet, basename='category')
# router.register(r'sub_category', SubCategoryViewSet, basename='sub_category')
router.register(r'service', ServiceViewSet, basename='service')
# router.register(r'branch', BranchViewSet, basename='branch')
router.register(r'booking', BookingViewSet, basename='booking')
router.register(r'customer_inquire', CustomerInquireViewSet, basename="customer_inquire")
router.register(r'branch_detail', BranchDetailViewSet, basename="branch_detail")
router.register(r'gallery', GalleryViewSet, basename='gallery')
router.register(r'social_media', SocialMediaViewSet, basename='social_media')
router.register(r'banner', BannerViewSet, basename='banner')
router.register(r'FAQ', FAQViewSet, basename='FAQ')




urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   path('api/', include(router.urls)),
   path('api/', include('account.urls')),

   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
