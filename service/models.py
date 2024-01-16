from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)

    title_ar = models.CharField(max_length=255, null=True)
    description_ar = models.TextField(null=True)
    image = models.ImageField(upload_to='./images/services/')
    
    def __str__(self):
        return self.title
