from django.db import models


# Create your models here.


class Products_category(models.Model):
    # id - default
    title = models.CharField(max_length=100, unique=True)


class Products(models.Model):
    # id - default
    title = models.CharField(max_length=100)
    count = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    category = models.ForeignKey(Products_category, on_delete=models.CASCADE)
