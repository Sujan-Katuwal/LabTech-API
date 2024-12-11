from django.db import models

# Create your models here.
class Branch(models.Model):
    branch_name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=10)
    location = models.CharField(max_length=225)
    gps_location = models.CharField(max_length=225)
    branch_type = models.CharField(max_length=50, choices=(('Headquarter', 'Headquarter'), ('Other', 'Other')))

    def __str__(self):
        return self.branch_name
                                   
