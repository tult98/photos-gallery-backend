from django.db import models

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=400, blank=True)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url
