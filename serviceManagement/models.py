from django.db import models
from category.models import MainCategory

# Create your models here.
class OurService(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # service_tags = models.ManyToManyField('Tag')
    category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name="Services")
    # sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="services")
    
    def __str__(self):
        return self.service_name
