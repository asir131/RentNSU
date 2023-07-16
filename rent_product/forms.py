from django import forms
from django.forms import ModelForm

from rent_product.models import *

CATEGORY = (
    ('', 'Select any'),
    ('Electronic Accessories', 'Electronic Accessories'),
    ('Electronic device', 'Electronic device'),
    ('Fashion', 'Fashion'),
    ('Daily Accessories', 'Daily Accessories'),
    ('Sports Items', 'Sports Items'),
    ('other', 'Other'),
)


# Add and update product
class ProductForm(ModelForm):
    category = forms.ChoiceField(choices=CATEGORY)

    class Meta:
        model = Product
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
class RentRequestForm(ModelForm):
    method = forms.ChoiceField(choices=METHOD)
    from_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=False)
    to_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = Rent
        exclude = ('owner', 'tenant', 'product', 'is_approved')
