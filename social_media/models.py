from django.db import models


class SocialMedia(models.Model):
    social_media_name = models.CharField(max_length=50) 
    icon = models.ImageField(upload_to='social_media_icons/', blank=True, null=True)  
    personal_profile_url = models.URLField()  

    def __str__(self):
        return self.social_media_name
