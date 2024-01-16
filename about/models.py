from django.db import models

class About(models.Model):

    description = models.TextField()
    logo1 = models.ImageField(upload_to='images/logo', null=True)
    logo2 = models.ImageField(upload_to='images/logo', null=True)

    def __str__(self) -> str:
        return 'About and Logos'
    
    