from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        # return the name of the category as string
        return self.name

    def categoryproviders(self):
        # Return all providers of the category.
        return self.providers.all()

class Provider(models.Model):
    LOCALITY_CHOICES = [
        (1, 'National'),
        (0, 'International'),
    ]

    name = models.CharField(max_length=255, unique=True)
    price = models.PositiveIntegerField()
    quality = models.PositiveIntegerField()
    deliveryDelay = models.PositiveIntegerField()  
    locality = models.IntegerField(max_length=15, choices=LOCALITY_CHOICES)
    address = models.CharField(max_length=500, blank=True)
    category = models.ForeignKey(Category, related_name='providers', on_delete=models.CASCADE)

    def __str__(self):
        # return the name of the provider as string
        return self.name