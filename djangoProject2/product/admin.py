from django.contrib import admin

# Register your models here.
import product.models

admin.site.register(product.models.Product)