# Generated by Django 5.1.3 on 2024-12-08 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviceManagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourservice',
            name='sub_category',
        ),
    ]
