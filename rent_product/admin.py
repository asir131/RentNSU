from django.contrib import admin

# Register your models here.
from rent_product.models import *

admin.site.register(Product)
admin.site.register(Rent)
