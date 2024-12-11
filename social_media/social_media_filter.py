from django_filters import rest_framework as filters
from .models import SocialMedia

class SocalMediaFilter(filters.FilterSet):
    social_media_name = filters.CharFilter(field_name="social_media_name", lookup_expr="icontains")
    

    class Meta:
        model = SocialMedia
        fields = ['social_media_name']
    