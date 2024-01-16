from django.db import models

class Partners(models.Model):
    partner_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/partners/')

    def __str__(self) -> str:
        return self.partner_name
