from django.contrib import admin
from .models import ContactMessage, Contacts

admin.site.register(Contacts)
admin.site.register(ContactMessage)
