"""
Models for the inventory app in our ecommerce project
"""
from django.db import models
import uuid

class Product(models.Model):
    """Product model for our inventory app"""

    IN_STOCK = "IS"
    OUT_OF_STOCK = "OOS"
    BACKORDERED = "BO"

    STOCK_STATUS = {
        IN_STOCK:"In Stock",
        OUT_OF_STOCK:"Out of Stock",
        BACKORDERED:"Backordered",
    }

    product_id = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    is_digital = models.BooleanField(default=False, null=False, blank=False)
    is_active = models.BooleanField(default=False, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    stock_status = models.CharField(max_length=3 , choices=STOCK_STATUS, default=OUT_OF_STOCK, null=False, blank=False)

class ProductLine(models.Model):
    """Product Line model for our inventory app"""
    price = models.DecimalField(null=False, blank=False)
    stock_keeping_unit = models.UUIDField(default=uuid.uuid4, null=False, blank=False)
    stock_quantity = models.IntegerField(default=0, null=False, blank=False)
    is_active = models.BooleanField(default=False, null=False, blank=False)
    order = models.IntegerField(null=False, blank=False)
    weight = models.FloatField(null=False, blank=False)

class ProductImage(models.Model):
    """Product image model for our inventory app"""
    name = models.CharField(max_length=100, null=False, blank=False)
    alternative_text = models.CharField(max_length=100, null=False, blank=False)
    url = models.ImageField(null=False, blank=False)
    order = models.IntegerField(null=False, blank=False)

class Category(models.Model):
    """Category model for our inventory app"""
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(null=False, blank=False)
    is_active = models.BooleanField(default=False, null=False, blank=False)

class SeasonalEvents(models.Model):
    """Seasonal events model for our inventory app"""
    name = models.CharField(max_length=100, null=False, blank=False)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
