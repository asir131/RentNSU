from django import forms
from django.forms import ModelForm

from rent_product.models import *
from ride_share.models import Vehicle, Ride


# Add and update product
class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        exclude = ('owner',)


METHOD = (
    ('', 'Select any'),
    ('bkash', 'Bkash'),
    ('rocket', 'Rocket'),
    ('nagad', 'Nagad'),
    ('upay', 'Upay'),
    ('sure_cash', 'Sure Cash'),
)


# Rent product
class RideRequestForm(ModelForm):
    method = forms.ChoiceField(choices=METHOD)

    class Meta:
        model = Ride
        exclude = ('owner', 'passenger', 'vehicle', 'is_approved')
