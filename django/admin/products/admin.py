from django.contrib import admin

from .models import Product, User

admin.register(Product, User)
