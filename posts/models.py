from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model): 
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ('name',)

    def __str__(self): 
        return self.name


class Post(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='posts',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User, 
        related_name='posts',
        on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='posts',
        blank=True
    )
    title = models.CharField(max_length=255)
    # image_header = models.ImageField(null=True)
    # image_container = models.ImageField(null=True)
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ('-updated_at',)

    def __str__(self):
        return self.title

