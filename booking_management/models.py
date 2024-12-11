from django.db import models
from serviceManagement.models import OurService
from account.models import CustomUser
from category.models import MainCategory

# Create your models here.
class BookingManagement(models.Model):
    APPOINTMENT_TYPE_CHOICES = [
        ('Online', 'Online'),
        ('Offline', 'Offline'),
    ]
    PAYMENT_OPTION_CHOICES = [
        ('Online', 'Online'),
        ('On Cilnic', 'On Cilnic'),
    ]
    # service = models.ForeignKey(OurService, on_delete=models.CASCADE, related_name="bookings")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="bookings")
    booked_date = models.DateTimeField()
    select_service = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name="bookings")
    # select_test = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="bookings")
    payment_option = models.CharField(max_length=50, choices=PAYMENT_OPTION_CHOICES)
    message = models.TextField()
    appointment_type = models.CharField(max_length=50, choices=APPOINTMENT_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return f"Booking by {self.user.username} for {self.select_service.name}"



