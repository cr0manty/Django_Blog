from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=32)
    text = models.TextField(blank=True)
    img = models.ImageField(blank=True)
