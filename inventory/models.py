from django.db import models

# Create your models here.
"""
Models for the inventory app in our ecommerce project
"""
class Product(models.Model):
    """Product table for our inventory app"""
    product_id = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
