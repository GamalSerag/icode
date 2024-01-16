from django.db import models

class Contacts(models.Model):
    facebook = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    whatsapp = models.URLField(max_length=200)
    def __str__(self) -> str:
        return 'Social Links'

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return self.first_name +" "+ self.last_name
