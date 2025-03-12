from datetime import datetime
from django.db import models

# Create your models here.


class Store(models.Model):
    store_id = models.IntegerField(unique=True)
    store_location = models.CharField(max_length=100)
    created_date2 = models.DateTimeField(auto_now_add=True)  # Set once on creation
    updated_date2 = models.DateTimeField(auto_now=True)  # Update on every save
    
    def __str__(self):
        return f"{self.store_id} - {self.store_location} - {self.created_date2} - {self.updated_date2}"


class Products(models.Model):
    product_id = models.IntegerField(unique=True)
    product_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)  # Set once on creation
    updated_date = models.DateTimeField(auto_now=True)  # Update on every save

    def __str__(self):
        return f"{self.product_id} - {self.product_name} - {self.created_date} - {self.updated_date}"