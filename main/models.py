from django.db import models

# Create your models here.
class Product (models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    category = models.CharField(max_length=100)
    rating = models.IntegerField()