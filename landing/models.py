from django.db import models

class LandingPage(models.Model):
    title_ar = models.CharField(max_length=255, null=True)
    title_en = models.CharField(max_length=255, null=True)
    description_ar = models.TextField( null=True)
    description_en = models.TextField(null=True)
    image = models.ImageField(upload_to='landing_page_images/')

    def __str__(self):
        return self.title_en
    


    
