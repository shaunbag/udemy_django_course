from django.db import models

# Create your models here.
class Blog(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255) 
    entry = models.TextField()
    created_at = models.DateField(auto_now=True)
    image = models.CharField(max_length=255, default="https://via.placeholder.com/150", null=True, blank=True)
    