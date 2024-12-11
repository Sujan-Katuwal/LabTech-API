from django.db import models


class Banner(models.Model):
    image = models.ImageField(upload_to='banners/images/', blank=True, null=True) 
    image_url = models.URLField(blank=True, null=True) 
    video = models.FileField(upload_to='banners/videos/', blank=True, null=True) 
    video_url = models.URLField(blank=True, null=True)  
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.image_url
