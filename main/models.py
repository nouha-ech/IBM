from django.db import models

# Create your models here.


class Provider(models.Model):
    name = models.CharField(max_length=255)
    locality = models.CharField(max_length=50, choices=[('National', 'National'), ('International', 'International')])
    address = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    contact_info = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    provider = models.ForeignKey(Provider, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    stock_quantity = models.IntegerField()
    release_date = models.DateField(null=True, blank=True)
    rating = models.FloatField()
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name




class Preference(models.Model):
    price = models.PositiveIntegerField(default=0)
    delivery = models.PositiveIntegerField(default=0)
    quality = models.PositiveIntegerField(default=0)
    locality = models.CharField(max_length=50, choices=[('National', 'National'), ('International', 'International')])

    def __str__(self):
        return f"Preference: Price={self.price}, Delivery={self.delivery}, Quality={self.quality}"