"""
Models for the inventory app in our ecommerce project
"""
from django.db import models
import uuid

class Category(models.Model):
    """Category model for our inventory app"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=False)
    parent = models.ForeignKey("self", on_delete=models.CASCADE)

class SeasonalEvents(models.Model):
    """Seasonal events model for our inventory app"""
    name = models.CharField(max_length=100, unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

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

    product_id = models.CharField(max_length=255, )
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    is_digital = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    stock_status = models.CharField(max_length=3, choices=STOCK_STATUS, default=OUT_OF_STOCK)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seasonal_event = models.ForeignKey(SeasonalEvents, on_delete=models.CASCADE)

class ProductLine(models.Model):
    """Product Line model for our inventory app"""
    price = models.DecimalField()
    stock_keeping_unit = models.UUIDField(default=uuid.uuid4)
    stock_quantity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    order = models.IntegerField()
    weight = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class ProductImage(models.Model):
    """Product image model for our inventory app"""
    name = models.CharField(max_length=100)
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField()
    order = models.IntegerField()
    product_line = models.ForeignKey(ProductLine, on_delete=models.CASCADE)

