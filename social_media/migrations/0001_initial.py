# Generated by Django 5.1.3 on 2024-12-06 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_media_name', models.CharField(max_length=50)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='social_media_icons/')),
                ('personal_profile_url', models.URLField()),
            ],
        ),
    ]