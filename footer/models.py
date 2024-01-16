from django.db import models

class Footer(models.Model):
    title = models.CharField(max_length=25)
    url1 = models.URLField(null=True, blank=True)
    url2 = models.URLField(null=True, blank=True)
    url3 = models.URLField(null=True, blank=True)
    url4 = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

