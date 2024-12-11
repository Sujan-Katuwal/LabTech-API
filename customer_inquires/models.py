from django.db import models

# Create your models here.
class CustomerInquiry(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f"Inquiry from {self.full_name}"