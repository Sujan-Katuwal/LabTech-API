# Generated by Django 5.1.3 on 2024-12-07 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_management', '0003_alter_bookingmanagement_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingmanagement',
            name='service',
        ),
    ]