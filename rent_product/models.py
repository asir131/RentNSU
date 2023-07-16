from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    cover = models.FileField(upload_to='rent_products', blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="owner")
    is_available = models.BooleanField(default=True, null=True, blank=True)
    category = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.name


class Rent(models.Model):
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="tenant")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    is_approved = models.BooleanField(default=False, null=True, blank=True)
    method = models.CharField(max_length=20, null=True, blank=True)
    txn_id = models.CharField(max_length=20, null=True, blank=True)
    account_no = models.CharField(max_length=20, null=True, blank=True)
