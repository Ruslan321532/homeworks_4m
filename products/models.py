from django.db import models


# Create your models here.

class Product(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=256)
    description = models.TextField()
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
