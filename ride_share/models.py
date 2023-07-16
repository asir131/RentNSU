from django.contrib.auth.models import User
from django.db import models


class Vehicle(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    cover = models.FileField(upload_to='vehicles', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    is_available = models.BooleanField(default=True, null=True, blank=True)
    map_link = models.CharField(max_length=40, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    from_location = models.CharField(max_length=40, blank=True, null=True)
    to_location = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=40, blank=True, null=True)
    def __str__(self):
        return self.name


class Ride(models.Model):
    passenger = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, blank=True, null=True)
    is_approved = models.BooleanField(default=False, null=True, blank=True)
    method = models.CharField(max_length=20, null=True, blank=True)
    txn_id = models.CharField(max_length=20, null=True, blank=True)
    account_no = models.CharField(max_length=20, null=True, blank=True)
    request_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

